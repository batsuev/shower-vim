"=============================================================================
" File: shower.vim
" Author: Aleksandr Batsuev (alex@batsuev.com)
" WebPage: https://github.com/batsuev/shower-vim
" License: MIT

if !has('python')
    echo "Error: Required vim compiled with +python"
    finish
endif

exec("pyfile ".fnameescape(fnamemodify(expand("<sfile>"), ":h")."/shower.py"))

command! -nargs=0 Spresentation exec "python shower_create_index()"
command! -nargs=0 Sslide exec "python shower_create_slide()"
