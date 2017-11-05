# neogoto

A plugin for to goto predifned match rules. Usefull for instance when switching between
headers and body in a mail message.

## Installation

Currently only tested with NeoVim and Python3 client.

Install this plugin with your favourite plugin manager. With dein you can do this:

```
call dein#add('frbor/neogoto', {'on_ft': "mail"})
```

## Configuration (for mail)
```
let g:neogoto_patterns = ['^To:\s?', '^Cc:\s?', '^Subject:\s?', '^\s*$']
nnoremap <silent> <C-w> :NeoGotoNext<cr>
```

