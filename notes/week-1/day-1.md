# 🧱 Developer Setup: Ubuntu VM + Git + Docker + GitHub

# virtual box
- Download virtual box from [downloads](https://www.virtualbox.org/wiki/Downloads)
- 

# Ubuntu Desktop
- LTS - Intel/amd64 - ISO

# Git

- Version control system.
- Helps manage changes - view, track.
- Commit history of changes.
- Git hard reset - subsequent history deleted
- Git soft reset - not permanenet deleted
- Branches
- Repository

## Git commands

```
git clone
git status
git pull
git fetch
git checkout
git add
git commit
git push
git merge
```

### Git commands examples:

#### `git status` shows the status of the current repo

```
namanattri@Namans-MacBook-Pro web-dev-zero-to-xp % git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        notes/

```

#### `git add` stages the changes

```
git add README.md
git add notes/week-1/day-1.md 

# or

git add .

git status

# output
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
        new file:   notes/week-1/day-1.md
```

#### `git commit` commits the staged changes

```
git commit -m "day 1 notes starter"

# git commit -m "message for the commit"
```

#### `git branch <branch-name>` creates a branch

```
git branch git-commands
```

#### `git branch` list of branches

```
git branch
  git-commands
* main
```

#### `git checkout <branch-name>` checkouts to branch

```
git checkout git-commands
```

#### `git checkout -b <branch-name>` creates and checkouts branch in single command

```
git checkout -b git-commands 
fatal: a branch named 'git-commands' already exists
```