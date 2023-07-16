import wx
import threading
import time


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="多线程示例")

        self.panel = wx.Panel(self)

        self.layout = wx.BoxSizer(wx.VERTICAL)

        self.chat_display = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.layout.Add(self.chat_display, 1, wx.EXPAND)

        self.button = wx.Button(self.panel, label="点击询问")
        self.button.Bind(wx.EVT_BUTTON, self.on_button_clicked)

        self.layout.Add(self.button, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        self.panel.SetSizerAndFit(self.layout)

        self.worker_thread = None
        self.timer = None
        self.dot_count = 0
        self.max_dots = 3
        self.dot_timer_interval = 0.5  # 定时器间隔时间（单位：秒）

    def on_button_clicked(self, event):
        self.button.Disable()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_dots, self.timer)
        self.timer.Start(int(self.dot_timer_interval * 1000))  # 将秒转换为毫秒

        # 创建后台线程并启动
        self.worker_thread = threading.Thread(target=self.process_reply)
        self.worker_thread.start()

    def process_reply(self):
        # 模拟耗时操作
        time.sleep(5)

        # 调用OpenAI API获取回复（假设回复是 "这是回复"）
        reply = "这是回复"

        # 在主线程中更新界面
        wx.CallAfter(self.show_reply, reply)

    def show_reply(self, reply):
        self.timer.Stop()

        # 清除 "正在询问" 的文本和动态效果
        self.chat_display.SetValue(reply)

        self.button.Enable()

        self.layout.Layout()

    def update_dots(self, event):
        self.dot_count += 1

        if self.dot_count > self.max_dots:
            self.dot_count = 1

        dots = '.' * self.dot_count
        text = f"正在询问{dots}"

        self.chat_display.SetValue(text)


app = wx.App()
frame = MyFrame(None)
frame.Show()
app.MainLoop()
