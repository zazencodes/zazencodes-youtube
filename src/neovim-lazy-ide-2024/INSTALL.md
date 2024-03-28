# MacOS
```bash
# Install Homebrew if you don't already have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Update Homebrew
brew update

# Install Neovim
brew install neovim
```

# Ubuntu
```bash
# Update package list
sudo apt update

# Install Neovim
sudo apt install neovim
```

# Windows
```bash
# Open PowerShell as an administrator

# Install Chocolatey if you don't already have it
# (I suggest carefully following instructions here: https://chocolatey.org/install)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Neovim
choco install neovim
```
