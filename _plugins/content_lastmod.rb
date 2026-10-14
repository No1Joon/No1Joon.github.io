# 본문이 실제로 바뀐 글에만 수정 시각을 준다.
#
# 글마다 제목·설명·본문 마크다운으로 지문(SHA-256)을 만들고, 직전 배포본의 지문 목록(라이브 /lastmod.json —
# CI 가 빌드 전에 .lastmod-prev.json 으로 받아 둔다)과 비교한다.
#   - 지문이 같으면 직전 배포본의 수정 시각을 그대로 쓴다
#   - 지문이 다르면 이번 빌드 시각을 수정 시각으로 쓴다
#   - 처음 보는 글은 발행일(date)을 쓴다
# 결과는 page.last_modified_at 이 되어 jekyll-sitemap 의 <lastmod> 와 jekyll-seo-tag 의 dateModified 로 나간다.
# 이번 빌드에서 새로 생기거나 바뀐 URL 목록은 .indexnow-urls.txt 에 남겨 배포 뒤 IndexNow 통지에 쓴다.
# 폴더 이동·OG image 줄 추가처럼 본문이 그대로인 변경은 수정으로 치지 않는다 (git 커밋 시각을 쓰지 않는 이유).
require "digest"
require "json"
require "time"

module ContentLastmod
  PREV_FILE = ".lastmod-prev.json"
  URLS_FILE = ".indexnow-urls.txt"

  def self.fingerprint(doc)
    Digest::SHA256.hexdigest([doc.data["title"], doc.data["description"], doc.content].join("\u0000"))
  end

  def self.load_prev(site)
    path = File.join(site.source, PREV_FILE)
    return nil unless File.exist?(path)
    JSON.parse(File.read(path))["pages"]
  rescue JSON::ParserError
    nil
  end

  Jekyll::Hooks.register :site, :post_read do |site|
    prev = load_prev(site)
    now = Time.now
    manifest = {}
    changed = []
    changed_langs = []
    newest = {}

    docs = site.posts.docs + (site.collections["en_posts"]&.docs || [])
    docs.each do |doc|
      url = doc.url
      hash = fingerprint(doc)
      published = doc.date
      old = prev && prev[url]
      lastmod =
        if doc.data["last_modified_at"]
          doc.data["last_modified_at"]
        elsif old && old["hash"] == hash
          Time.parse(old["lastmod"])
        elsif old
          changed << url
          now
        else
          changed << url if prev
          published
        end
      lastmod = published if lastmod < published
      doc.data["last_modified_at"] = lastmod
      manifest[url] = { "hash" => hash, "lastmod" => lastmod.iso8601 }
      lang = doc.data["lang"] == "en" ? "en" : "ko"
      changed_langs << lang if changed.last == url
      newest[lang] = lastmod if newest[lang].nil? || lastmod > newest[lang]
    end

    # 홈·영문 홈은 글 목록이라 해당 언어의 가장 최근 수정 시각을 따른다
    site.pages.each do |page|
      lang = { "/" => "ko", "/en/" => "en" }[page.url]
      next unless lang && newest[lang]
      page.data["last_modified_at"] = newest[lang]
    end
    changed << "/" if changed_langs.include?("ko")
    changed << "/en/" if changed_langs.include?("en")

    site.config["content_lastmod_manifest"] = manifest
    File.write(File.join(site.source, URLS_FILE),
               changed.uniq.map { |u| site.config["url"] + u }.join("\n") + (changed.empty? ? "" : "\n"))
  end

  # 다음 빌드의 비교 기준 — 라이브 /lastmod.json 으로 나간다
  Jekyll::Hooks.register :site, :post_write do |site|
    manifest = site.config["content_lastmod_manifest"] or next
    File.write(File.join(site.dest, "lastmod.json"),
               JSON.generate({ "generated" => Time.now.iso8601, "pages" => manifest }))
  end
end
