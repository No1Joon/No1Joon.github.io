/* 포스트 본문 후처리 — 코드 블록을 Mac 창 스타일로 감싸고 mermaid 다이어그램을 렌더한다.
 *
 * 부분 네비게이션(post-browser.html)이 본문을 교체한 뒤에도 다시 불러야 하므로
 * window.enhancePostContent 로 노출한다. 이미 처리한 노드는 건너뛰어 재호출이 안전하다.
 */
(function () {
  let mermaidPromise = null;

  // mermaid 모듈은 한 번만 import·initialize 한다 (본문을 여러 번 교체해도 재다운로드 없음)
  function loadMermaid() {
    if (!mermaidPromise) {
      mermaidPromise = import('https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs')
        .then(function (mod) {
          mod.default.initialize({ startOnLoad: false, theme: 'dark', securityLevel: 'loose' });
          return mod.default;
        });
    }
    return mermaidPromise;
  }

  async function enhance(root) {
    const scope = root || document;

    scope.querySelectorAll('.post-content pre > code').forEach(function (code) {
      const pre = code.parentElement;
      if (pre.dataset.enhanced) return;
      pre.dataset.enhanced = '1';

      if (code.classList.contains('language-mermaid')) {
        const graph = document.createElement('div');
        graph.className = 'mermaid';
        graph.textContent = code.textContent;
        pre.replaceWith(graph);
        return;
      }

      const langClass = Array.from(code.classList).find(function (c) {
        return c.startsWith('language-');
      });
      const lang = langClass ? langClass.replace('language-', '') : 'code';

      const wrapper = document.createElement('div');
      wrapper.className = 'code-window';

      const header = document.createElement('div');
      header.className = 'code-header';
      header.innerHTML = '<div class="mac-dots"><span></span><span></span><span></span></div>' +
                         '<div class="code-lang-label"></div>';
      header.querySelector('.code-lang-label').textContent = lang;

      pre.parentNode.insertBefore(wrapper, pre);
      wrapper.appendChild(header);
      wrapper.appendChild(pre);
    });

    const pending = Array.from(scope.querySelectorAll('.mermaid:not([data-processed])'));
    if (pending.length) {
      const mermaid = await loadMermaid();
      await mermaid.run({ nodes: pending });
    }
  }

  window.enhancePostContent = enhance;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { enhance(); });
  } else {
    enhance();
  }
})();
