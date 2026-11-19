
# Git & GitHub Troubleshooting

Common Git issues, their causes, practical solutions, and lessons learned.

## 1. Destination Path Already Exists

**Problem**

```text
fatal: destination path already exists and is not an empty directory.
```

**Cause**

The target directory already exists and contains files. Git cannot clone another repository into a non-empty directory with the same name.

**Solution**

Check whether the directory is already a Git repository:

```bash
git remote -v
```

If it is already connected to the correct remote repository, reuse it instead of cloning again.

**Key Takeaway**

Always check the existing local repository before running `git clone`. Avoid creating unnecessary duplicate copies.

---

## 2. Not a Git Repository

**Problem**

```text
fatal: not a git repository (or any of the parent directories): .git
```

**Cause**

The terminal is currently outside the Git repository, or the selected directory has not been initialized as a Git repository.

**Solution**

Navigate to the existing repository directory:

```bash
cd <repository-directory>
```

Then verify the repository connection:

```bash
git status
git remote -v
```

**Key Takeaway**

Git commands must be executed from inside the repository or one of its subdirectories.

---

## 3. Local Branch Is Behind Remote

**Problem**

```text
Your branch is behind 'origin/main' by 1 commit.
```

**Cause**

The remote branch contains commits that are not yet present in the local branch.

**Solution**

If the working tree is clean, update the local branch:

```bash
git fetch origin
git pull --ff-only origin main
```

If local changes exist, review and safely preserve them before synchronizing.

**Key Takeaway**

Synchronize local and remote branches before pushing. `--ff-only` prevents Git from creating an unexpected merge commit.

---

## 4. File Not Under Version Control

**Problem**

```text
fatal: not under version control
```

**Cause**

`git mv` was used on a file that Git does not currently track.

This can happen when a file has been restored from a remote source but has not yet been added to the Git index.

**Solution**

For an untracked file, use normal file operations:

```bash
mv old_path/file.ipynb new_path/file.ipynb
```

On Windows PowerShell:

```powershell
Move-Item old_path/file.ipynb new_path/file.ipynb
```

Then stage the changes:

```bash
git add -A
```

**Key Takeaway**

Use `git mv` for tracked files. For untracked files, use normal file operations followed by `git add`.

---

## 5. Missing Local File but Present on GitHub

**Problem**

A file exists in the remote repository but is missing from the local working directory.

**Cause**

The local working tree may not contain the latest remote version, or the file may not have been restored correctly.

**Solution**

First, retrieve remote information:

```bash
git fetch origin
```

Check whether the file exists in the remote branch:

```bash
git ls-tree -r origin/main
```

Restore the specific file if it exists remotely:

```bash
git restore --source=origin/main --worktree -- path/to/file
```

Verify the restored file before moving or modifying it.

**Key Takeaway**

Use `git fetch` to inspect remote updates without immediately changing local files. Restore only the files needed.

---

## 6. Long Output Blocks Further Terminal Input

**Problem**

A Git command displays a colon (`:`) at the bottom of the terminal and appears to stop accepting input.

**Cause**

Git has opened a pager to display long output page by page.

**Solution**

Press:

```text
q
```

to exit the pager and return to the terminal.

To display output without a pager for a single command:

```bash
git --no-pager log --oneline
```

**Key Takeaway**

A pager is a display interface, not a Git error. Press `q` to exit.

---

## 7. Recommended Diagnostic Commands

When something unexpected happens, start by checking the repository state:

```bash
git status
git remote -v
git branch -vv
git log --oneline -5
```

These commands help identify:

- Current working tree changes
- Remote repository connections
- Local and remote branch tracking
- Recent commit history

## General Principle

Before attempting to fix a Git problem:

1. Check the current repository and branch.
2. Inspect local and remote changes.
3. Identify whether the affected files are tracked or untracked.
4. Preserve existing work before restoring or synchronizing.
5. Verify the result before committing or pushing.

**The goal is not just to resolve errors, but to understand the repository state and avoid losing work.**
