
# Git & GitHub Workflow

A practical reference for managing project repositories, tracking changes, and maintaining a clean development workflow.

## 0. Basic Workflow

The typical workflow for updating a project:

```text
Clone / Pull
     ↓
Modify files
     ↓
Check status
     ↓
Stage changes
     ↓
Commit changes
     ↓
Push to GitHub
```

## 1. Initial Folder and File Setup

PowerShell commands for creating project folders and files.

### Create a directory

```powershell
New-Item -ItemType Directory -Force -Path (folder)
```

### Create an empty file
```powershell
New-Item -ItemType File -Force -Path (folder)/(file)
```

## 2. Essential Commands

| Command | Purpose |
|---|---|
| `git clone <url>` | Copy a remote repository locally |
| `git remote -v` | Check remote repository connections |
| `git status` | Check working tree and staging status |
| `git branch` | List local branches |
| `git fetch origin` | Retrieve remote updates without changing local files |
| `git pull --ff-only origin main` | Update the current branch using fast-forward only |
| `git add -A` | Stage all changes, including additions and deletions |
| `git add <file>` | Stage a specific file |
| `git mv <old> <new>` | Move or rename a tracked file or directory |
| `git commit -m "message"` | Save staged changes as a commit |
| `git push origin main` | Upload local commits to GitHub |
| `git log --oneline` | View recent commit history |

## 3. Recommended Update Workflow

### Step 1. Check the repository

```bash
git status
git remote -v
```

### Step 2. Synchronize with GitHub

```bash
git pull --ff-only origin main
```

Run this before starting new work when the working tree is clean.

### Step 3. Make changes

Edit code, add files, reorganize folders, or update documentation.

### Step 4. Review changes

```bash
git status
git diff
```

### Step 5. Stage and commit

```bash
git add -A
git status
git commit -m "Describe the changes"
```

### Step 6. Push to GitHub

```bash
git push origin main
```

## 4. File and Folder Management

Use consistent naming conventions:

- Folders: `snake_case`
- Python files: `snake_case.py`
- Python functions and variables: `snake_case`
- Python classes: `PascalCase`
- Git commit messages: short and descriptive

Examples:

```text
hw1_neural_tuning/
hw2_svm/
hw3_cifar10/
data_loader.py
plot_results.py
```

For tracked files and folders, use:

```bash
git mv old_name new_name
```

For untracked files, use normal file operations and then stage them with `git add`.

## 5. Good Practices

- Pull remote updates before starting new work.
- Check `git status` before committing.
- Write meaningful commit messages.
- Keep notebooks, source code, and documentation organized.
- Avoid committing credentials, private information, or unnecessary generated files.
- Document dependencies and execution instructions.
- Keep each commit focused on a logical change.

## Related Documentation

- [Troubleshooting](troubleshooting.md)
