---
name: smart-commit
description: Generates atomic commit messages based on staged changes, extracting issue IDs from the branch name (e.g., NJB-123). Use this skill whenever the user asks to commit, says "commit this", "commit changes", "make a commit", or after completing a task that should be committed.
---

# Smart Commit Workflow

This skill instructs the agent to dynamically generate **atomic** commit messages by analyzing the current git branch name and staged changes. The goal is to create granular, self-contained commits rather than one large commit.

## 0. Project Convention

**Project Prefix**: `NJB`

The project prefix is derived from the project name's initials (2–3 uppercase letters). For example, "Oh My Algorithm" → `OMA`, "Dev Tools Kit" → `DTK`, "Auth Service" → `AS`.

This prefix is used in branch names and issue IDs: `NJB-<number>` (e.g., `NJB-123`).

> **Note**: This blog project rarely uses issue IDs. If the current branch (typically `main`) has no `NJB-<number>` pattern, skip the prefix and write the commit without it — matching the existing commit history.

**Commit Types**:

| Type | When to Use | Example |
|------|-------------|---------|
| `feat` | New feature, new functionality, new endpoint, new UI component | `feat: add user profile page` |
| `fix` | Bug fix, error correction, broken behavior repair | `fix: resolve infinite loop in token refresh` |
| `chore` | Maintenance, config changes, dependency updates, refactoring, cleanup, CI/CD, docs, tests | `chore: update .gitignore to ignore agent skills` |

> **Rule of thumb**: If it changes what the software _does_ for the user → `feat` or `fix`. If it changes how the software is _built, tested, or maintained_ → `chore`.

> **Blog posts**: New/updated blog posts under `_posts/` typically use Korean commit messages in the existing style (e.g., `Observability: Logging 시리즈 3편 추가`, `Azure 시리즈 3편 추가`). Follow the existing commit history style rather than forcing the `feat/fix/chore` prefix for post content.

## 1. Identify Context

1. **Get Current Branch Name**:
   Run `git branch --show-current` to retrieve the active branch name.

2. **Extract Issue Identifier**:
   Parse the branch name to find a project issue ID matching the pattern `NJB-<number>`.
   - Common patterns: `feature/NJB-123-desc`, `NJB-123-fix-bug`, `fix/NJB-456`.
   - If found, extract it (e.g., `NJB-123`).
   - If not found, proceed without an ID.

## 2. Analyze Changes & Plan Atomic Commits

1. **Review All Changes**:
   - Run `git status` and `git diff` (or `git diff --cached`) to see all modified files.
   - **Crucial**: Do not simply commit everything at once unless it is a single, indivisible change.

2. **Group Changes into Atomic Units**:
   - Identify logical groups of files that belong to a single specific task (e.g., "Refactoring date picker", "Updating locale files", "Cleaning up dependencies").
   - **Strategy**: It is better to have 5 small commits than 1 huge commit with a bulleted list.
   - **Blog-specific grouping**: Posts within the same subcategory series (same folder, same topic) are typically committed together as one unit. Separate series = separate commits.

## 3. Generate Commit Message (For Each Atomic Change)

**Format**:

```
[Issue ID] [type]: [Summary]

[Optional Description - Only if necessary]
```

**Rules**:

1. **Prefix**: Always start with the Issue ID (if found).
2. **Subject**: `[type]: [Summary]` (e.g., `feat: replace date picker`).
   - Use imperative mood ("add", "fix", "update" — not "added", "fixed", "updated").
   - Keep under 72 characters (including prefix).
   - No period at the end.
3. **Description**:
   - **OMIT** the description if the subject line sufficiently explains the change.
   - **INCLUDE** a description ONLY if you need to explain _why_ a complex change was made or provide extra context that doesn't fit in the subject.
   - **DO NOT** use the description just to list files changed.

### Examples

**Blog post series (matches existing history)**

```
Observability: Logging 시리즈 3편 추가
```

```
Azure 시리즈 3편 추가
```

**Config / maintenance change**

```
chore: track CLAUDE config and ignore .gemini dir
```

**Simple Feature (No Description needed)**

```
NJB-123 feat: replace external date pickers with Vuetify VDateInput
```

**Configuration Change (No Description needed)**

```
NJB-123 chore: update .gitignore to ignore all agent skills
```

**Complex Logic Change (Description needed)**

```
NJB-123 fix: resolve infinite loop in auth token refresh

The previous implementation caused a race condition when the token expired
simultaneously with a page navigation. Added a mutex lock to prevent this.
```

**No Issue ID found on branch**

```
feat: add dark mode toggle to settings page
```

## 4. Execute Atomic Commits

**Procedure**:

1. **Unstage All**: Run `git restore --staged .` to start fresh.
2. **Loop through identified atomic groups**:
   a. **Stage**: `git add <file1> <file2> ...` (Only files for this specific atomic unit).
   b. **Verify**: Check `git diff --cached --name-only` to ensure only correct files are staged.
   c. **Commit**: Run `git commit -m "..."` using the generated message for this unit.
   d. **Repeat** until all changes are committed.
3. **Push**: After all commits succeed, run `git push` (per project CLAUDE.md: "커밋 후 항상 바로 `git push` 실행").

**Important**:

- If a file has multiple logical changes (e.g., a fix AND a formatting change), you can try to use `git add -p`, but usually it's safer to just commit the file for the primary change.
- For this skill, prioritizing file-level grouping for atomic commits is usually sufficient.
- If there are too many changes to reasonably separate, ask the user which grouping they prefer.
- **NEVER** append `Co-Authored-By`, `Signed-off-by`, or any git trailer referencing Claude or AI. The commit must look like it was written entirely by the developer. (This matches the project CLAUDE.md rule: "커밋 메시지에 `Co-Authored-By` 라인 넣지 않기".)
