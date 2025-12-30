# WSL Installation

```
wsl --install
wsl --install -d Ubuntu
```

List distros

```
wsl.exe --list --online
```

Setup default version to 2

```
wsl --set-default-version 2
```

expected output:

```
PS C:\windows\system32> wsl --set-default-version 2
For information on key differences with WSL 2 please visit https://aka.ms/wsl2
The operation completed successfully.
```

Check status

```
wsl --status
```

expected output:

```
Default Distribution: Ubuntu
Default Version: 2
WSL1 is not supported with your current machine configuration.
Please enable the "Windows Subsystem for Linux" optional component to use WSL1.
```

## Connect to instance

```
wsl
```

expected output: prompt with the following text

```
PS C:\windows\system32> wsl
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

csasagar@Attri-PC:/mnt/c/windows/system32$
```

## Update & Upgrade Ubuntu + install dev tools

```
sudo apt update && sudo apt upgrade -y

sudo apt install -y \
  build-essential curl wget git unzip zip \
  ca-certificates gnupg lsb-release \
  jq ripgrep fzf tree htop
```

## Paste in wsl

```
Right
```

# Linux Cheatsheet

## Users

- `root` super user
- `user` limited permissions

## Groups

- `root` super user group
- `user` e.g. `csasagar` 
- `sudo` 

## 📁 Files & Directories

```bash
pwd                 # current directory
ls                  # list files
ls -la              # detailed list (hidden + permissions)
cd /path/to/dir     # change directory
cd ..               # go up one level
cd ~                # home directory

mkdir mydir         # create directory
mkdir -p a/b/c      # nested directories
rmdir mydir         # remove empty dir
rm -r mydir         # remove dir recursively (dangerous)
```

---

## 📄 File Operations

```bash
touch file.txt              # create empty file
cp a.txt b.txt               # copy file
cp -r dir1 dir2              # copy directory
mv old.txt new.txt           # rename / move
rm file.txt                  # delete file
```

---

## 👀 View File Content

```bash
cat file.txt                 # print entire file
less file.txt                # scrollable view (q to quit)
head file.txt                # first 10 lines
tail file.txt                # last 10 lines
tail -f log.txt              # live log follow
```

---

## ✍️ Edit Files (CLI)

```bash
nano file.txt                # beginner-friendly editor
vim file.txt                 # powerful editor (advanced)
```

---

## 🔍 Search & Find

```bash
grep "text" file.txt         # search in file
grep -r "text" .             # recursive search
find . -name "*.js"          # find files by name
```

---

## 🔐 Permissions & Ownership

```bash
ls -l                        # view permissions
chmod 755 file.sh            # change permissions
chmod +x file.sh             # make executable
chown user:user file.txt     # change owner (sudo)
```

---

## ⚙️ System & Processes

```bash
uname -a                     # system info
whoami                       # current user
uptime                       # system running time
df -h                        # disk usage
free -h                      # memory usage

ps aux                       # list processes
top                          # live process view
kill PID                     # kill process
```

---

## 📦 Package Management (Ubuntu / WSL)

```bash
sudo apt update
sudo apt upgrade
sudo apt install git curl vim
sudo apt remove package
```

---

## 🌐 Networking

```bash
ip a                         # network interfaces
ping google.com
curl https://example.com
wget https://file.zip
```

---

## 🧵 Archives & Compression

```bash
tar -czf file.tar.gz folder/     # create archive
tar -xzf file.tar.gz             # extract archive
zip -r file.zip folder/
unzip file.zip
```

---

## 🐳 Docker (very common in WSL)

```bash
docker ps
docker ps -a
docker images
docker run hello-world
docker exec -it container bash
docker logs container
docker stop container
```

---

## 🧠 Environment & Shell

```bash
echo $PATH
env
export MY_VAR=value
alias ll="ls -la"
history
```

---

## 📂 WSL-Specific

```bash
explorer.exe .          # open current dir in Windows Explorer
code .                  # open folder in VS Code (must be installed)
```

---

## 🚀 Git (must-know)

```bash
git init
git clone url
git status
git add .
git commit -m "msg"
git pull
git push
git log --oneline
```

---

## 🧪 Redirection & Pipes (IMPORTANT)

```bash
ls > out.txt            # overwrite
ls >> out.txt           # append
cat file | grep error
ps aux | grep node
```

---

## 🎯 Suggested Learning Order (WSL)

1. `ls`, `cd`, `pwd`
2. `cat`, `less`, `nano`
3. `grep`, `find`
4. `chmod`, `chown`
5. `apt`, `git`
6. pipes `|` and redirection `>`
