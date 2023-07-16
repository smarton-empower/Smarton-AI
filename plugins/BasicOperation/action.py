import pcbnew
import os
import wx
import threading
import atexit

from .frontend import OneCommandLine


class BasicOperations(pcbnew.ActionPlugin):

    def defaults(self):
        self.name = "Basic Operation"
        self.category = "Modify PCB"
        self.description = "Some Basic Operations"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')
        self.dark_icon_file_name = self.icon_file_name
        self.chat_window = None

    def Run(self):
        # load board
        board = pcbnew.GetBoard()
        # basicop_helpers.rotate_by_fp_selected(board=board)

        app = wx.GetApp()
        top_windows = wx.GetTopLevelWindows()

        # Find the top-level window that is an instance of wx.Frame
        frame = None
        for window in top_windows:
            if isinstance(window, wx.Frame):
                frame = window
                break

        if frame is not None:
            if self.chat_window is None or not isinstance(self.chat_window, OneCommandLine):
                self.chat_window = OneCommandLine(frame, board)
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
