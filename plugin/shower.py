#=============================================================================
# File: shower.py
# Author: Aleksandr Batsuev (alex@batsuev.com)
# WebPage: https://github.com/batsuev/shower-vim
# License: MIT

from string import Template
import vim

PLUGIN_DIR = vim.eval('fnameescape(fnamemodify(expand("<sfile>"), ":h"))')
TMPL_INDEX = Template(open(os.path.join(PLUGIN_DIR,"shower_templates/index.html"), "r").read())
TMPL_SLIDE = Template(open(os.path.join(PLUGIN_DIR,"shower_templates/slide.html"), "r").read())

shower_slides_counter = 0

def shower_create_index():
    b = vim.current.buffer
    del b[0:]
    # TODO: params for template
    content = TMPL_INDEX.substitute()
    b.append(content.split("\n"), 0)
    # TODO: move cursor to position based on regexp
    vim.current.window.cursor = (16, 8)

def shower_create_slide():
    global shower_slides_counter
    b = vim.current.buffer
    # TODO: params for template
    content = TMPL_SLIDE.substitute(id = 'id_%d' % shower_slides_counter)
    line = vim.current.window.cursor[0] - 1
    b.append(content.split("\n"), line)
    # TODO: move cursor to position based on regexp
    vim.current.window.cursor = (line + 1, 31)
    shower_slides_counter += 1
