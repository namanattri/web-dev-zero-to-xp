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

## Git Installation

- Open Terminal (Bottom left, Icon, search terminal)
- Open https://git-scm.com/install/linux
- Run `apt-get install git`
- Run `add-apt-repository ppa:git-core/ppa`
- Run `apt update; apt install git`

## Git Fork & Clone

- Signup on Github
- Clone the repo: `https://github.com/namanattri/web-dev-zero-to-xp`

## Git commands

```
git init
git clone
git status
git pull
git fetch
git checkout
git add
git reset
git commit
git push
git merge
```

### Git commands examples:

#### `git init` initialise a git repo

```
git init
```

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

#### `git reset` unstage all changes

```
git reset
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

#### `git push` 

If we try to push a new branch

```
namanattri@Namans-MacBook-Pro web-dev-zero-to-xp % git push
fatal: The current branch git-cloning has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin git-cloning

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.
```

#### Create upstream branch with tracking `git push --set-upstream origin git-cloning`

```
git push --set-upstream origin git-cloning
```

```
git push -u origin git-cloning
```

`git-cloning` is the branch name here, use your own branch name.

Expected output:

```
namanattri@Namans-MacBook-Pro web-dev-zero-to-xp % git push --set-upstream origin git-cloning
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 10 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 1.26 KiB | 1.26 MiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'git-cloning' on GitHub by visiting:
remote:      https://github.com/namanattri/web-dev-zero-to-xp/pull/new/git-cloning
remote: 
To https://github.com/namanattri/web-dev-zero-to-xp.git
 * [new branch]      git-cloning -> git-cloning
branch 'git-cloning' set up to track 'origin/git-cloning'.
```

#### If remote tracking branch exists them simple push `git push`

```
# stage the changes
git add .
# commit the changes
git commit -m "instructions for pushing new branch"

# push the changes to branch being tracked
git push
```

expected output

```
namanattri@Namans-MacBook-Pro web-dev-zero-to-xp % git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 10 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 1.28 KiB | 1.28 MiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/namanattri/web-dev-zero-to-xp.git
   883b9b1..46671e7  git-cloning -> git-cloning
```

#### Git global configuration

```
git config --global user.name "Chander Sagar"
git config --global user.email "csasagar1@gmail.com"
```

#### Ignoring some files

```
.gitignore
```