import wx
import openai
import os
import json
import threading
import queue
import atexit

from .preinput import plugin_preinput, basicop_helpers
from .GPTModels import GPTModel

# Add your openai api key here
openai.api_key = ""


class OneCommandLine(wx.Frame):
    def __init__(self, parent, board):
        super(OneCommandLine, self).__init__(parent, title="OneCommandLine", size=(600, 300))

        self.board = board

        screen_width, screen_height = wx.DisplaySize()
        position_x = screen_width // 50 + 600
        position_y = (screen_height - self.GetSize()[1]) // 2
        self.SetPosition((position_x, position_y))

        # 创建聊天窗口的控件
        self.panel = wx.Panel(self)
        # 聊天记录框
        self.chat_display = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 用户输入框
        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        # 按钮
        self.send_button = wx.Button(self.panel, label="Send")
        self.clear_button = wx.Button(self.panel, label="Clear")
        # 新增：显示/隐藏插件记录框的按钮
        self.toggle_plugin_display_button = wx.Button(self.panel, label="View all plugins")
        # 插件名称记录框
        self.plugin_display = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        self.plugin_display.Hide()  # 默认隐藏插件记录框

        # 布局控件
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.send_button, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        button_sizer.Add(self.clear_button, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        button_sizer.Add(self.toggle_plugin_display_button, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        # 垂直布局
        chat_sizer = wx.BoxSizer(wx.VERTICAL)
        chat_sizer.Add(self.chat_display, proportion=1, flag=wx.EXPAND)
        chat_sizer.Add(self.text_ctrl, proportion=0, flag=wx.EXPAND | wx.ALL)  # 添加边距
        chat_sizer.Add(button_sizer, proportion=0, flag=wx.EXPAND)  # 添加按钮布局

        # 水平布局
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(chat_sizer, proportion=2, flag=wx.EXPAND | wx.RIGHT)  # 添加边距
        sizer.Add(self.plugin_display, proportion=1, flag=wx.EXPAND)

        self.panel.SetSizer(sizer)

        # 设置输入框的最小尺寸
        chat_sizer.SetItemMinSize(self.text_ctrl, (self.text_ctrl.GetMinSize()[0], 50))

        # gpt属性
        self.language = ""
        self.plugin_names, self.plugin_args, self.plugin_description_msg = plugin_preinput.plugin_preinput()

        self.chat_display.AppendText(f"==========  Smarton AI  ==========\n")
        # self.chat_display.AppendText(f"Smarton AI: Board: {self.board}\n")

        self.plugin_display.AppendText("=" * 30 + "\n")
        self.plugin_display.AppendText(f"<< Plugin function names >>\n")
        self.plugin_display.AppendText("="*30+"\n")
        self.plugin_display.AppendText("-" * 30 + "\n")

        self.plugin_ids = []
        for i in range(len(self.plugin_names)):
            plugin = self.plugin_names[i]
            args = self.plugin_args[i]
            self.plugin_ids.append(i)
            self.chat_display.AppendText(f"Plugin {i+1}: {plugin}\n\t{args}\n")
            self.plugin_display.AppendText(f"{plugin}\n")
            self.plugin_display.AppendText("-"*30+"\n")
        self.chat_display.AppendText(
            f"\nSmarton AI: We currently have the above plugins, please choose one plugin to use at a time\n")

        # 绑定事件
        self.send_button.Bind(wx.EVT_BUTTON, self.on_submit)
        self.clear_button.Bind(wx.EVT_BUTTON, self.on_clear_button_clicked)
        self.toggle_plugin_display_button.Bind(wx.EVT_BUTTON, self.view_all_plugins)

        self.model = 'gpt-3.5-turbo-0613'

        self.userInputQueue = queue.Queue()
        self.exitEvent = threading.Event()

    def on_clear_button_clicked(self, event):
        self.chat_display.SetValue("")  # 清空聊天信息

    def view_all_plugins(self, event):
        # 切换插件记录框的显示状态
        self.plugin_display.Show(not self.plugin_display.IsShown())
        # 调整布局
        self.panel.Layout()

    def on_submit(self, event):
        try:
            user_input = self.text_ctrl.GetValue()
            self.chat_display.AppendText(f"==========  User  ==========\n")
            self.chat_display.AppendText(f"User: {user_input}\n")

            self.text_ctrl.Clear()
            self.userInputQueue.put(user_input)

            self.text_ctrl.SetValue("")  # 清空输入框
            self.text_ctrl.SetMinSize((self.text_ctrl.GetMinSize()[0], -1))  # 恢复文本框的最小尺寸
            self.Layout()  # 重新布局窗口

        except Exception as e:
            self.chat_display.AppendText(f"An exception occurred: {e}\n")

    def handle_user_input(self):
        need_recommend = True
        while True:
            pname = None
            try:
                user_input = self.userInputQueue.get()
                if user_input in self.plugin_names:
                    need_recommend = False
                    pname = user_input
                if need_recommend:
                    messages = self.plugin_description_msg
                    messages.append({"role": "user", "content": f"{user_input}\n"})
                    gpt = GPTModel(self.model, messages, self.plugin_names, self.plugin_ids)
                    self.button_Disable()
                    response = gpt.ask_gpt("Plugin", self.chat_display.AppendText)
                    wx.CallAfter(self.button_Enable, response)

                    selected_plugin_names = response['Plugin']
                    wx.CallAfter(self.chat_display.AppendText, f'==========  Smarton AI  ==========\n')
                    wx.CallAfter(self.chat_display.AppendText, f'Recommend Plugin: {selected_plugin_names}\n')
                    pname = self.userInputQueue.get()

                not_valid_plugin = True
                while not_valid_plugin:
                    # plugin 1: rotate_fp_by_fp_name
                    if pname == self.plugin_names[0]:
                        wx.CallAfter(self.chat_display.AppendText, f'==========  Smarton AI  ==========\n')
                        wx.CallAfter(self.chat_display.AppendText, f'=> Please provide some arguments {self.plugin_args[0]} and separated by commas\n')
                        wx.CallAfter(self.chat_display.AppendText, f'eg. P1, 45\n')
                        params = self.userInputQueue.get().split(',')
                        footprint_name = params[0].strip()
                        rotate_angle = int(params[1].strip())

                        wx.CallAfter(basicop_helpers.rotate_fp_by_fp_name,
                            self.board,
                            footprint_name,
                            rotate_angle,
                        )

                        wx.CallAfter(self.chat_display.AppendText, f'=> {self.plugin_names[0]} Done\n')
                        not_valid_plugin = False
                        need_recommend = True

                    # plugin 2: rotate_fp_by_mouse
                    elif pname == self.plugin_names[1]:
                        wx.CallAfter(self.chat_display.AppendText, f'==========  Smarton AI  ==========\n')
                        wx.CallAfter(self.chat_display.AppendText, f'=> Please click the footprints first\n')
                        wx.CallAfter(self.chat_display.AppendText, f'=> Please provide some arguments {self.plugin_args[1]} and separated by commas\n')
                        wx.CallAfter(self.chat_display.AppendText, f'eg. 45\n')
                        params = self.userInputQueue.get().split(',')
                        rotate_angle = int(params[0].strip())

                        wx.CallAfter(basicop_helpers.rotate_fp_by_mouse,
                            self.board,
                            rotate_angle,
                        )

                        wx.CallAfter(self.chat_display.AppendText, f'=> {self.plugin_names[1]} Done\n')
                        not_valid_plugin = False
                        need_recommend = True

                    # plugin 3: move_fp_by_fp_name
                    elif pname == self.plugin_names[2]:
                        wx.CallAfter(self.chat_display.AppendText, f'==========  Smarton AI  ==========\n')
                        wx.CallAfter(self.chat_display.AppendText, f'=> Please provide some arguments {self.plugin_args[2]} and separated by commas\n')
                        wx.CallAfter(self.chat_display.AppendText, f'eg. P1, 1000000, 1000000\n')
                        params = self.userInputQueue.get().split(',')
                        footprint_name = params[0].strip()
                        X_offset = int(params[1].strip())
                        Y_offset = int(params[2].strip())

                        wx.CallAfter(basicop_helpers.move_fp_by_fp_name,
                                     self.board,
                                     footprint_name,
                                     X_offset,
                                     Y_offset,
                                     )

                        wx.CallAfter(self.chat_display.AppendText, f'=> {self.plugin_names[2]} Done\n')
                        not_valid_plugin = False
                        need_recommend = True

                    # plugin 4: move_fp_by_mouse
                    elif pname == self.plugin_names[3]:
                        wx.CallAfter(self.chat_display.AppendText, f'==========  Smarton AI  ==========\n')
                        wx.CallAfter(self.chat_display.AppendText, f'=> Please click the footprints first\n')
                        wx.CallAfter(self.chat_display.AppendText, f'=> Please provide some arguments {self.plugin_args[3]} and separated by commas\n')
                        wx.CallAfter(self.chat_display.AppendText, f'eg. 1000000, 1000000\n')
                        params = self.userInputQueue.get().split(',')
                        X_offset = int(params[0].strip())
                        Y_offset = int(params[1].strip())

                        wx.CallAfter(basicop_helpers.move_fp_by_mouse,
                                     self.board,
                                     X_offset,
                                     Y_offset,
                                     )

                        wx.CallAfter(self.chat_display.AppendText, f'=> {self.plugin_names[3]} Done\n')
                        not_valid_plugin = False
                        need_recommend = True

                    # plugin 5: flip_fp_by_fp_name
                    elif pname == self.plugin_names[4]:
                        wx.CallAfter(self.chat_display.AppendText, f'==========  Smarton AI  ==========\n')
                        wx.CallAfter(self.chat_display.AppendText, f'=> Please provide some arguments {self.plugin_args[4]} and separated by commas\n')
                        wx.CallAfter(self.chat_display.AppendText, f'eg. P1\n')
                        params = self.userInputQueue.get().split(',')
                        footprint_name = params[0].strip()

                        wx.CallAfter(basicop_helpers.flip_fp_by_fp_name,
                                     self.board,
                                     footprint_name,
                                     )

                        wx.CallAfter(self.chat_display.AppendText, f'=> {self.plugin_names[4]} Done\n')
                        not_valid_plugin = False
                        need_recommend = True

                    # plugin 6: flip_fp_by_mouse
                    elif pname == self.plugin_names[5]:
                        wx.CallAfter(self.chat_display.AppendText, f'==========  Smarton AI  ==========\n')
                        wx.CallAfter(self.chat_display.AppendText, f'=> Please click the footprints first\n')

                        wx.CallAfter(basicop_helpers.flip_fp_by_mouse,
                                     self.board,
                                     )

                        wx.CallAfter(self.chat_display.AppendText, f'=> {self.plugin_names[5]} Done\n')
                        not_valid_plugin = False
                        need_recommend = True

                    # invalid plugin name
                    else:
                        wx.CallAfter(self.chat_display.AppendText, f'==========  Smarton AI  ==========\n')
                        wx.CallAfter(self.chat_display.AppendText, f'Not a valid plugin name, please give a valid name from {self.plugin_names}\n')
                        pname = self.userInputQueue.get()

            except Exception as e:
                self.chat_display.AppendText(f"An exception occurred: {e}\n")



    def button_Enable(self, response):
        text = self.chat_display.GetValue()
        new_text = text.replace('Matching the appropriate Plugin, please wait for a minute ...', '')
        self.chat_display.SetValue(new_text)

        self.chat_display.AppendText(f"==========  Smarton AI  ==========\n")
        self.chat_display.AppendText(f"Based on your request, we recommend you these plugins\n")
        self.chat_display.AppendText(f"{response}\n")
        self.send_button.Enable()

    def button_Disable(self):
        wx.CallAfter(self.chat_display.AppendText, f'Matching the appropriate Plugin, please wait for a minute ...')
        self.send_button.Disable()

