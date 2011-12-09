# Shower-vim
Vim plugin for https://github.com/pepelsbey/shower (html presentation engine by @pepelsbey)
## Installation
### pathogen:
```
cd ~/.vim/bundle
git clone https://github.com/batsuev/shower-vim.git
```
### vundle:
Add the following line to .vimrc:
```
Bundle 'git://github.com/miripiruni/csscomb-for-vim.git'
```
### manual:
```
git clone https://github.com/batsuev/shower-vim.git
cp shower-vim/plugin/* ~/.vim/plugin
```
## Usage
```
:Spresentation
```
Creates the blank empty presentation (uses ./shower as shower base path)
```
:Sslide
```
Inserts slide into current cursor position
