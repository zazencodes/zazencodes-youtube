# Neovim Lazy IDE 2024

Watch my video to understand what's going on here. And don't skip step #4.

1. Install/upgrade neovim and setup alias in your "rc" file (e.g. `echo "alias vim=nvim" >> ~/.bashrc`) and install/upgrade ripgrep and git
2. Create a python virtual environment for neovim (e.g. LSP autocomplete) in `~/virtualenvs` named `nvim-venv`, i.e.

        mkdir ~/virtualenvs
        cd ~/virtualenvs
        python3 -m venv nvim-venv

3. Copy nvim folder from this repo to your local neovim config directory

        git clone https://github.com/agalea91/zazencodes-youtube
        cd zazencodes-youtube/src/neovim-lazy-ide-2024
        mkdir ~/.config
        cp -r .config/nvim ~/.config/nvim

4. Spend 20+ hours configuring neovim to your exact liking and get completely lost in obscure and outdated threads on LSP

