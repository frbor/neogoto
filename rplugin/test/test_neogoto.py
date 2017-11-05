import unittest
import os
import re
import neovim
from python3 import neogoto

class TestNeoGotoPlugin(unittest.TestCase):

    def setUp(self):
        self.nvim = neovim.attach('child', argv=["nvim", "-u", "NONE", "--embed"])

        testfile = os.path.join(
            os.path.dirname(__file__),
            'templates/mutt-user-host-1000-25771-8168793478140598733'
        )

        # Populate buffer with content from file
        with open(testfile) as f:
            self.nvim.current.buffer[:] = [re.sub(r'\n$', '', line) for line in f]

        self.nvim.vars['neogoto_patterns'] = [r'^To:\s?', r'^Cc:\s?', r'^Subject:\s?', r'^\s*$']

        self.plugin = neogoto.NeoGotoPlugin(self.nvim)

    def tearDown(self):
        self.nvim.quit()

    def __cursor_pos(self):
        return self.nvim.current.window.api.get_cursor()

    def test_get_tags_file_in_same_folder(self):
        # Initial setup - should be at start
        self.assertEqual(self.__cursor_pos(), [1,0])

        self.plugin.next([])
        # self.nvim.command("NeoGotoNext")
        self.assertEqual(self.__cursor_pos(), [2,3])

        self.plugin.next([])
        self.assertEqual(self.__cursor_pos(), [4,4])
