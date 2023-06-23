from WINDOW_FUNCTIONS import Window_Functions
import MOUSE as Mouse


class Main:

    def __init__(self):

        def MousePress_Right(event):
            Mouse.MousePress_Right(event.x, event.y, self.WindowFunc)
        def MousePress_Left(event):
            Mouse.MousePress_Left(event.x, event.y, self.WindowFunc)
        def MouseRelease_Left(event):
            Mouse.MouseRelease_Left(event.x, event.y, self.WindowFunc)
        def MouseMotion(event):
            Mouse.MouseMotion(event.x, event.y, self.WindowFunc)
        def MouseWheel(event):
            Mouse.MouseWheel(event.x, event.y, event.delta, self.WindowFunc)

        self.WindowFunc = Window_Functions()

        """ПРИКРЕПЛЕНИЕ ОБРАБОТОК СОБЫТИЙ МЫШИ НА ПОЛЕ"""
        self.WindowFunc.canvas.bind('<ButtonPress-1>', MousePress_Left)
        self.WindowFunc.canvas.bind('<ButtonPress-3>', MousePress_Right)
        self.WindowFunc.canvas.bind('<ButtonRelease-1>', MouseRelease_Left)
        self.WindowFunc.canvas.bind('<Motion>', MouseMotion)
        self.WindowFunc.canvas.bind("<MouseWheel>", MouseWheel)


Program = Main()
Program.WindowFunc.tk.mainloop()