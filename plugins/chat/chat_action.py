# Smarton AI for Kicad - Analying help documentation paragraphs and invoke plugins intelligently
# Copyright (C) 2023 Beijing Smarton Empower
# Contact: yidong.tian@smartonep.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import pcbnew
import os
import wx
import threading
import atexit

from .frontend import ChatWindow
# from .op import basicop_helpers


class ChatPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Chat Plugin"
        self.category = "General"
        self.description = "Open the chat window"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')
        self.dark_icon_file_name = self.icon_file_name
        self.chat_window = None

    def Run(self):
        # board = pcbnew.GetBoard()
        # basicop_helpers.rotate_by_selected(board=board)

        app = wx.GetApp()
        top_windows = wx.GetTopLevelWindows()

        # Find the top-level window that is an instance of wx.Frame
        frame = None
        for window in top_windows:
            if isinstance(window, wx.Frame):
                frame = window
                break

        if frame is not None:
            if self.chat_window is None or not isinstance(self.chat_window, ChatWindow):
                self.chat_window = ChatWindow(frame)
                userInputThread = threading.Thread(target=self.chat_window.handle_user_input)
                userInputThread.start()
                atexit.register(userInputThread.join)

                monitorThread = threading.Thread(target=self.monitor_kicad)
                monitorThread.start()

                self.chat_window.Bind(wx.EVT_CLOSE, self.on_close_chat_window)
            if self.chat_window.IsIconized():
                self.chat_window.Iconize(False)
            self.chat_window.Raise()
            self.chat_window.Show()

    def on_close_chat_window(self, event):
        self.chat_window = None
        event.Skip()

    def monitor_kicad(self):
        while True:
            if pcbnew.GetBoard() is None:
                if self.chat_window is not None:
                    wx.CallAfter(self.chat_window.Close)
                break

