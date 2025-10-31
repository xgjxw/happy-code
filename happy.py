import tkinter as tk
import random

class BlessingWindow:
    def __init__(self, tips, bg_colors):
        self.tips = tips
        self.bg_colors = bg_colors
        self.windows = []  # 存储所有创建的窗口
        self.root = None   # 主root窗口
        self.selected_window = None  # 被选中的窗口
        
    def set_root(self, root):
        """设置主窗口"""
        self.root = root
        
    def create_blessing_windows(self, count=10):
        """
        创建多个祝福窗口
        :param count: 窗口数量
        """
        for _ in range(count):
            self._create_single_window()
            
    def _create_single_window(self):
        """创建单个祝福窗口"""
        # 创建窗口
        window = tk.Toplevel()
        self.windows.append(window)
        
        # 获取屏幕尺寸
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        # 设置窗口尺寸
        window_width = 300
        window_height = 100
        
        # 计算中心区域范围
        center_x = screen_width // 2
        center_y = screen_height // 2
        
        # 将窗口限制在屏幕中心区域 (屏幕中央50%的区域)
        cluster_width = screen_width // 2
        cluster_height = screen_height // 2
        
        # 在中心区域内随机生成位置
        x = random.randrange(
            center_x - cluster_width // 2, 
            center_x + cluster_width // 2 - window_width
        )
        y = random.randrange(
            center_y - cluster_height // 2, 
            center_y + cluster_height // 2 - window_height
        )
        
        # 设置窗口标题和位置
        window.title('温馨祝福')
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # 随机选择祝福语和背景色
        tip = random.choice(self.tips)
        bg = random.choice(self.bg_colors)
        
        # 创建标签
        label = tk.Label(
            window,
            text=tip,
            bg=bg,
            font=('微软雅黑', 10),
            width=40,
            height=4,
            wraplength=280
        )
        label.pack(padx=10, pady=10)
        
        # 绑定点击事件
        window.bind("<Button-1>", self._on_window_click)
        label.bind("<Button-1>", self._on_window_click)
        
        # 设置窗口属性，使其置于顶层
        window.attributes('-topmost', True)
        
    def _on_window_click(self, event):
        """
        点击窗口事件处理
        关闭除当前窗口外的所有窗口
        """
        clicked_window = event.widget
        # 如果点击的是label，需要获取其所在的窗口
        if isinstance(clicked_window, tk.Label):
            clicked_window = clicked_window.master
            
        # 保存被选中的窗口
        self.selected_window = clicked_window
            
        # 隐藏其他所有窗口
        for win in self.windows:
            if win != clicked_window:
                win.withdraw()  # 隐藏窗口
                
        # 3秒后退出程序
        self.root.after(3000, self._exit_program)
        
    def _exit_program(self):
        """退出程序"""
        if self.root:
            self.root.quit()
            self.root.destroy()
                
def create_window():
    # 长句祝福语列表
    tips = [
        '多喝水哦~', '保持微笑呀', '每天都要元气满满', '记得吃早饭！', '记得吃水果', '保持好心情', '好好爱自己',
        '我想你了', '祝你考研成功', '金榜提名', '保持好心情', '好好爱自己', '顺顺利利', '早点休息',
        '愿所有烦恼都消失', '别熬夜', '今天过的开心吗', '天冷了多穿衣服。', '照顾好自己', '万事如意', '要天天开心吖',
        '压力大时深呼吸', '小进步也值得庆祝', '保持好心情', '天气好就多出去走走', '喜欢的事就去做，别在意别人的看法',
        '你就是你没人能代替', '天大地大自己最大', '始终坚信自己', '人生就是用来潇洒的', '你值得所有美好',
        '偶尔放空是充电', '不要给自己太大压力，你已经够好了', '路是自己走出来的', '愿烦恼都消失'
    ]
    
    # 背景颜色选择
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender', 'lightyellow',
        'plum', 'coral', 'bisque', 'aquamarine', 'mistyrose', 'honeydew',
        'peachpuff', 'paleturquoise', 'lavenderblush', 'oldlace', 'lemonchiffon'
    ]
    
    # 创建主窗口（隐藏）
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 创建祝福窗口管理器
    blessing_manager = BlessingWindow(tips, bg_colors)
    blessing_manager.set_root(root)  # 设置主窗口
    
    # 创建多个祝福窗口
    blessing_manager.create_blessing_windows(15)  # 创建15个窗口
    
    # 运行主循环
    root.mainloop()

# 执行函数
if __name__ == "__main__":
    create_window()