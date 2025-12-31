# Windows Users: Setting up WSL (Recommended)

**WSL (Windows Subsystem for Linux)** provides a complete Linux environment on Windows. This is the **recommended setup for Windows developers** because:

- ✅ Better compatibility with development tools
- ✅ Native Linux commands and utilities
- ✅ Easier to follow Unix-based tutorials
- ✅ Consistent with macOS/Linux development workflows
- ✅ No dual-boot or virtual machine needed
- ✅ Seamless integration with Windows

## Step 1: Install WSL

**Requirements:**
- Windows 10 version 2004+ (Build 19041+) or Windows 11
- Administrator access

**Install WSL (Recommended Method):**

1. **Open PowerShell or Command Prompt as Administrator:**
   - Press `Win + X`
   - Select "Windows PowerShell (Admin)" or "Terminal (Admin)"

2. **Install WSL with Ubuntu:**
   ```powershell
   wsl --install
   ```

   This single command will:
   - Enable WSL feature
   - Install WSL 2
   - Install Ubuntu (default Linux distribution)
   - Set up everything automatically

3. **Restart your computer** when prompted

4. **Set up Ubuntu:**
   - After restart, Ubuntu will launch automatically
   - Create a UNIX username (can be different from Windows username)
   - Create a password (you won't see it as you type - this is normal)
   - Remember this password - you'll need it for `sudo` commands

**Verify WSL Installation:**
```bash
wsl --version
wsl --list --verbose
```

## Step 2: Install a Different Linux Distribution (Optional)

If you want a different distribution:

```powershell
# List available distributions
wsl --list --online

# Install a specific distribution
wsl --install -d Debian
wsl --install -d Ubuntu-22.04
```

## Step 3: Set Up VS Code with WSL

1. **Install VS Code on Windows** (if not already installed)
   - Download from [code.visualstudio.com](https://code.visualstudio.com/)

2. **Install WSL Extension:**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "WSL"
   - Install "WSL" by Microsoft

3. **Open Project in WSL:**
   - Open VS Code
   - Press `Ctrl+Shift+P`
   - Type "WSL: Connect to WSL"
   - Or click the green icon in bottom-left corner → "Connect to WSL"

4. **Access Your Windows Files from WSL:**
   ```bash
   # Windows C: drive is mounted at /mnt/c
   cd /mnt/c/Users/YourUsername/Projects
   ```

5. **Access WSL Files from Windows:**
   - In Windows Explorer, type: `\\wsl$\Ubuntu\home\yourusername`
   - Or: Open WSL terminal and type `explorer.exe .`

## Step 4: Install Development Tools in WSL

Once WSL is set up, open WSL terminal and install tools:

**Update package manager:**
```bash
sudo apt update && sudo apt upgrade -y
```

**Install essential build tools:**
```bash
sudo apt install -y \
  build-essential curl wget git unzip zip \
  ca-certificates gnupg lsb-release \
  jq ripgrep fzf tree htop
```

Now you can follow the **Linux instructions** for installing Python, NVM, and other tools throughout this guide!

## WSL Basic Commands

```bash
# Start WSL (from Windows PowerShell/CMD)
wsl

# Start specific distribution
wsl -d Ubuntu

# Shut down WSL
wsl --shutdown

# Check WSL status
wsl --list --verbose

# Set default distribution
wsl --set-default Ubuntu

# Run a Linux command from Windows
wsl ls -la

# Open current directory in Windows Explorer
explorer.exe .
```

## WSL Tips

1. **File Performance:**
   - Keep project files in Linux filesystem (`~/Projects`) for best performance
   - Accessing Windows files from WSL (`/mnt/c/...`) is slower

2. **VS Code:**
   - Always use "Open Folder in WSL" for best experience
   - Extensions install separately for WSL

3. **Git Configuration:**
   - Configure Git separately in WSL and Windows if using both

4. **Terminal:**
   - Use Windows Terminal for the best WSL experience
   - Install from Microsoft Store (free)

5. **Paste in WSL Terminal:**
   - Right-click to paste
   - Or use `Ctrl+Shift+V` in Windows Terminal

## Troubleshooting WSL

**WSL command not found:**
```powershell
# Enable WSL feature manually
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

**Set WSL 2 as default:**
```powershell
wsl --set-default-version 2
```

**Check WSL status:**
```bash
wsl --status
```

Expected output:
```
Default Distribution: Ubuntu
Default Version: 2
```

**WSL won't start:**
- Ensure virtualization is enabled in BIOS
- Check Windows version: `winver`
- Update Windows to latest version

**Reset Ubuntu (if corrupted):**
```powershell
wsl --unregister Ubuntu
wsl --install -d Ubuntu
```

## Resources

- **Official WSL Docs:** [docs.microsoft.com/windows/wsl](https://docs.microsoft.com/windows/wsl)
- **WSL GitHub:** [github.com/microsoft/WSL](https://github.com/microsoft/WSL)
- **VS Code WSL:** [code.visualstudio.com/docs/remote/wsl](https://code.visualstudio.com/docs/remote/wsl)

---

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
