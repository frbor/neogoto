import re
import neovim

# https://neovim.io/doc/user/api.html

@neovim.plugin
class NeoGotoPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

        try:
            self.goto_patterns = self.nvim.eval("g:neogoto_patterns")
        except neovim.api.nvim.NvimError as e:
            self.nvim.command('echo "%s"' % e)


    # @neovim.autocmd('BufEnter', pattern='*.py', eval='expand("<afile>")', sync=True)
    # def on_bufenter(self, filename):
        # self.nvim.out_write("testplugin is in " + filename + "\n")

    @neovim.command("NeoGotoNext", nargs='*', sync=True)
    def next(self, args):
        # self.nvim.current.line = ('Command with args: {},' .format(args))

        (cursor_y, _) = self.nvim.current.window.api.get_cursor()

        buf = self.nvim.current.buffer

        search_lines = [i for i in range(cursor_y, len(buf))] + [i for i in range(0, cursor_y + 1)]

        # Search from current line to end, then from start to current line
        for line_i in search_lines:
            line = buf[line_i]
            # print(cursor_y, line_i, line)
            for pattern in self.goto_patterns:
                matcher = re.search(pattern, line)
                # print(pattern, line)
                if matcher:
                    match_text = matcher.group(0)
                    self.nvim.command('echo "%s"' % match_text)
                    self.nvim.current.window.api.set_cursor([
                        line_i + 1,
                        line.index(match_text) + len(match_text)
                    ])
                    self.nvim.feedkeys("a")
                    return
