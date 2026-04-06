Generate GitHub Pages blog posts from a tech stack markdown file.

## Usage

```
/tech-blog <path-to-markdown-file>
```

## What this does

Reads the given markdown file and uses the `tech-stack-blog-generator` agent to create one Jekyll blog post per technology category section (`##` headings).

## Steps

1. Confirm the file exists and is readable
2. Use the `tech-stack-blog-generator` agent with the file path
3. The agent will:
   - Parse each `##` category section from the markdown
   - Generate `_posts/YYYY-MM-DD-{category-slug}.md` for each category
   - Include the technology table, rationale, and code examples
   - Use today's date as the post date
4. Report the created files

## Expected markdown structure

The input file should have sections like:

```markdown
## Frontend

| 기술 | 버전 | 용도 |
|------|------|------|
| React | 18.x | UI 렌더링 |
...

### 왜 이 조합인가
...

## Backend
...
```

## Notes

- Posts are placed in `_posts/` relative to the current working directory
- Existing posts with the same slug will be reported before overwriting
- The blog must already have `_layouts/post.html` and `assets/css/style.css` for proper rendering
- To preview locally: `bundle exec jekyll serve`
