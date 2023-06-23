from tkinter import *
from tkinter import PhotoImage
import PARAMETERS as Parameters
from COVERAGE import Coverage
from CONNECT import Connect
from GDOP import Gdop


class Window_Functions:

    def __init__(self):

        """СОЗДАНИЕ ГЛАВНОГО ОКНА"""

        self.tk = Tk()
        self.WIDTHSCREEN = self.tk.winfo_screenwidth()
        self.HEIGHTSCREEN = self.tk.winfo_screenheight()
        self.tk.overrideredirect(True)
        self.web_message_buffer = []
        self.tk.minsize(width=int(self.WIDTHSCREEN / 3 * 2), height=int(self.HEIGHTSCREEN / 5 * 4))
        self.tk.maxsize(width=int(self.WIDTHSCREEN / 3 * 2), height=int(self.HEIGHTSCREEN / 5 * 4))
        self.tk.wm_geometry("+%d+%d" % (int(self.WIDTHSCREEN / 2 - self.WIDTHSCREEN / 3 * 2 / 2),
                                        int(self.HEIGHTSCREEN / 2 - self.HEIGHTSCREEN / 5 * 4 / 2)))
        self.tk["bg"] = Parameters.TkColor

        self.canvas = Canvas(self.tk, bg=Parameters.CanvasColor, relief='flat', highlightthickness=0)
        self.canvas.pack()
        self.canvas.place(x=5, y=50, width=int(self.WIDTHSCREEN / 3 * 2) - 10, height=int(self.HEIGHTSCREEN / 5 * 4) - 55)
        self.canvas.update()

        """ФОТОГРАФИИ ДЛЯ КНОПОК"""

        self.Image_Beacon = PhotoImage(file="BeaconImage_v1.png")
        self.Image_Oval = PhotoImage(file="OvalImage_v1.png")
        self.Image_Rectangle = PhotoImage(file="RectangleImage_v1.png")
        self.Image_Wall = PhotoImage(file="WallImage_v1.png")
        self.Image_Polywall = PhotoImage(file="PolywallImage_v1.png")
        self.Image_Connect = PhotoImage(file="ConnectImage_v1.png")
        self.Image_Close = PhotoImage(file="CloseImage_v1.png")
        self.Image_Coverage = PhotoImage(file="CoverageImage_v1.png")
        self.Image_GDOP = PhotoImage(file="GDOPImage_v1.png")
        self.Image_DeleteBeacon = PhotoImage(file="DeleteBeaconImage_v1.png")
        self.Image_DeleteOval = PhotoImage(file="DeleteOvalImage_v1.png")
        self.Image_DeleteWall = PhotoImage(file="DeleteWallImage_v1.png")
        self.Image_DeletePolyWall = PhotoImage(file="DeletePolyWallImage_v1.png")
        self.Image_DeleteRectangle = PhotoImage(file="DeleteRectangleImage_v1.png")
        self.Image_DeleteAll = PhotoImage(file="DeleteAllImage_v1.png")
        self.Image_PressBeacon = PhotoImage(file="PressBeaconImage_v1.png")
        self.Image_PressOval = PhotoImage(file="PressOvalImage_v1.png")
        self.Image_PressRectangle = PhotoImage(file="PressRectangleImage_v1.png")
        self.Image_PressWall = PhotoImage(file="PressWallImage_v1.png")
        self.Image_PressPolywall = PhotoImage(file="PressPolywallImage_v1.png")
        self.Image_PressConnect = PhotoImage(file="PressConnectImage_v1.png")

        """КНОПКИ"""

        self.ButClose = Button(image=self.Image_Close, command=self.CloseButton, relief='flat')
        self.ButClose.pack()
        self.ButClose.place(x=int(self.WIDTHSCREEN / 3 * 2 - 26), y=1, width=25, height=25)

        self.ButBeacon = Button(image=self.Image_Beacon, command=self.BeaconButton, relief='flat')
        self.ButBeacon.pack()
        self.ButBeacon.place(x=5, y=5, width=40, height=40)

        self.ButOval = Button(image=self.Image_Oval, command=self.OvalButton, relief='flat')
        self.ButOval.pack()
        self.ButOval.place(x=100, y=5, width=40, height=40)

        self.ButRect = Button(image=self.Image_Rectangle, command=self.RectButton, relief='flat')
        self.ButRect.pack()
        self.ButRect.place(x=150, y=5, width=40, height=40)

        self.ButWall = Button(image=self.Image_Wall, command=self.WallButton, relief='flat')
        self.ButWall.pack()
        self.ButWall.place(x=200, y=5, width=40, height=40)

        self.ButPolywall = Button(image=self.Image_Polywall, command=self.PolywallButton, relief='flat')
        self.ButPolywall.pack()
        self.ButPolywall.place(x=250, y=5, width=40, height=40)

        self.ButConnect = Button(image=self.Image_Connect, command=self.ConnectButton, relief='flat')
        self.ButConnect.pack()
        self.ButConnect.place(x=400, y=5, width=40, height=40)

        self.ButCoverage = Button(image=self.Image_Coverage, command=self.CoverageButton, relief='flat')
        self.ButCoverage.pack()
        self.ButCoverage.place(x=450, y=5, width=40, height=40)

        self.ButGDOP = Button(image=self.Image_GDOP, command=self.GDOPButton, relief='flat')
        self.ButGDOP.pack()
        self.ButGDOP.place(x=500, y=5, width=40, height=40)

        self.ButDeleteBeacons = Button(image=self.Image_DeleteBeacon, command=self.DeleteBeaconButton, relief='flat')
        self.ButDeleteBeacons.pack()
        self.ButDeleteBeacons.place(x=700, y=5, width=40, height=40)

        self.ButDeleteOval = Button(image=self.Image_DeleteOval, command=self.DeleteOvalButton, relief='flat')
        self.ButDeleteOval.pack()
        self.ButDeleteOval.place(x=750, y=5, width=40, height=40)

        self.ButDeleteWall = Button(image=self.Image_DeleteWall, command=self.DeleteWallButton, relief='flat')
        self.ButDeleteWall.pack()
        self.ButDeleteWall.place(x=800, y=5, width=40, height=40)

        self.ButDeleteRect = Button(image=self.Image_DeleteRectangle, command=self.DeleteRectButton, relief='flat')
        self.ButDeleteRect.pack()
        self.ButDeleteRect.place(x=850, y=5, width=40, height=40)

        self.ButDeletePolyWall = Button(image=self.Image_DeletePolyWall, command=self.DeletePolyWallButton, relief='flat')
        self.ButDeletePolyWall.pack()
        self.ButDeletePolyWall.place(x=900, y=5, width=40, height=40)

        self.ButDeleteAll = Button(image=self.Image_DeleteAll, command=self.DeleteAllButton, relief='flat')
        self.ButDeleteAll.pack()
        self.ButDeleteAll.place(x=1000, y=5, width=40, height=40)

        """ПЕРЕМЕННЫЕ И ФЛАГИ"""

        self.BeaconFlag = False
        self.OvalFlag = False
        self.WallFlag = False
        self.RectFlag = False
        self.PolyWallFlag = False

        self.BeaconCount = 0
        self.OvalCount = 0
        self.WallCount = 0
        self.RectCount = 0

        self.BeaconMas = []
        self.OvalMas = []
        self.WallMas = []
        self.RectMas = []

        self.OvalMotionFlag = False
        self.WallMotionFlag = False
        self.PolyWallMotionFlag = False
        self.RectMotionFlag = False

        self.ReplaceBeaconFlag = False
        self.ReplaceBeacon = []
        self.ReplaceOvalFlag = False
        self.ReplaceOval = []
        self.ReplaceCorner1Flag = False
        self.ReplaceCorner2Flag = False
        self.ReplaceWall = []
        self.ReplaceRectFlag = False
        self.ReplaceRect = []

        self.OvalPosSTART = []
        self.WallPosSTART = []
        self.PolyWallPosSTART = []
        self.RectPosSTART = []
        self.OvalPosFINISH = []
        self.WallPosFINISH = []
        self.PolyWallPosFINISH = []
        self.RectPosFINISH = []

        self.DeltaBeaconWidth = 0
        self.DeltaBeaconHeight = 0
        self.OvalWidth = 0
        self.OvalHeight = 0
        self.DeltaOvalWidth = 0
        self.DeltaOvalHeight = 0
        self.RectWidth = 0
        self.RectHeight = 0
        self.DeltaRectWidth = 0
        self.DeltaRectHeight = 0

    def CloseButton(self):
        self.tk.destroy()

    def BeaconButton(self):
        if self.BeaconFlag:
            self.BeaconFlag = False
            self.ButBeacon["image"] = self.Image_Beacon
        else:
            self.BeaconFlag = True
            self.ButBeacon["image"] = self.Image_PressBeacon
            self.OvalFlag = False
            self.ButOval["image"] = self.Image_Oval
            self.RectFlag = False
            self.ButRect["image"] = self.Image_Rectangle
            self.WallFlag = False
            self.ButWall["image"] = self.Image_Wall
            self.PolyWallFlag = False
            self.ButPolywall["image"] = self.Image_Polywall

            self.PolyWallMotionFlag = False
            self.canvas.delete('Line')

    def OvalButton(self):
        if self.OvalFlag:
            self.OvalFlag = False
            self.ButOval["image"] = self.Image_Oval
        else:
            self.OvalFlag = True
            self.ButOval["image"] = self.Image_PressOval
            self.BeaconFlag = False
            self.ButBeacon["image"] = self.Image_Beacon
            self.RectFlag = False
            self.ButRect["image"] = self.Image_Rectangle
            self.WallFlag = False
            self.ButWall["image"] = self.Image_Wall
            self.PolyWallFlag = False
            self.ButPolywall["image"] = self.Image_Polywall

            self.PolyWallMotionFlag = False
            self.canvas.delete('Line')


    def RectButton(self):
        if self.RectFlag:
            self.RectFlag = False
            self.ButRect["image"] = self.Image_Rectangle
        else:
            self.RectFlag = True
            self.ButRect["image"] = self.Image_PressRectangle
            self.BeaconFlag = False
            self.ButBeacon["image"] = self.Image_Beacon
            self.OvalFlag = False
            self.ButOval["image"] = self.Image_Oval
            self.WallFlag = False
            self.ButWall["image"] = self.Image_Wall
            self.PolyWallFlag = False
            self.ButPolywall["image"] = self.Image_Polywall

            self.PolyWallMotionFlag = False
            self.canvas.delete('Line')

    def WallButton(self):
        if self.WallFlag:
            self.WallFlag = False
            self.ButWall["image"] = self.Image_Wall
        else:
            self.WallFlag = True
            self.ButWall["image"] = self.Image_PressWall
            self.BeaconFlag = False
            self.ButBeacon["image"] = self.Image_Beacon
            self.OvalFlag = False
            self.ButOval["image"] = self.Image_Oval
            self.RectFlag = False
            self.ButRect["image"] = self.Image_Rectangle
            self.PolyWallFlag = False
            self.ButPolywall["image"] = self.Image_Polywall

            self.PolyWallMotionFlag = False
            self.canvas.delete('Line')

    def PolywallButton(self):
        if self.PolyWallMotionFlag:
            self.PolyWallMotionFlag = False
            self.ButPolywall["image"] = self.Image_Polywall
            self.canvas.delete('Line')
        else:
            self.PolyWallFlag = True
            self.ButPolywall["image"] = self.Image_PressPolywall
            self.BeaconFlag = False
            self.ButBeacon["image"] = self.Image_Beacon
            self.OvalFlag = False
            self.ButOval["image"] = self.Image_Oval
            self.RectFlag = False
            self.ButRect["image"] = self.Image_Rectangle
            self.WallFlag = False
            self.ButWall["image"] = self.Image_Wall

            self.PolyWallMotionFlag = False
            self.canvas.delete('Line')

    def DeleteBeaconButton(self):
        for i in range(len(self.BeaconMas)):
            self.canvas.delete(self.BeaconMas[i].BeaconTag)
        self.BeaconMas = []
        self.BeaconCount = 0

    def DeleteOvalButton(self):
        for i in range(len(self.OvalMas)):
            self.canvas.delete(self.OvalMas[i].OvalTag)
        self.OvalMas = []
        self.OvalCount = 0

    def DeleteWallButton(self):
        CloneWallMas=[]
        for i in range(len(self.WallMas)):
            if self.WallMas[i].PolyWallCheck:
                CloneWallMas.append(self.WallMas[i])

            else:
                self.canvas.delete(self.WallMas[i].WallTag)
                self.canvas.delete(self.WallMas[i].CornerTag1)
                self.canvas.delete(self.WallMas[i].CornerTag2)
        self.WallMas = []
        for i in range(len(CloneWallMas)):
            self.WallMas.append(CloneWallMas[i])

    def DeletePolyWallButton(self):
        CloneWallMas=[]
        for i in range(len(self.WallMas)):
            if self.WallMas[i].PolyWallCheck:
                self.canvas.delete(self.WallMas[i].WallTag)
                self.canvas.delete(self.WallMas[i].CornerTag1)
                self.canvas.delete(self.WallMas[i].CornerTag2)
            else:
                CloneWallMas.append(self.WallMas[i])
        self.WallMas = []
        for i in range(len(CloneWallMas)):
            self.WallMas.append(CloneWallMas[i])

        self.PolyWallMotionFlag = False
        self.canvas.delete('Line')

    def DeleteRectButton(self):
        for i in range(len(self.RectMas)):
            self.canvas.delete(self.RectMas[i].RectTag)
        self.RectMas = []
        self.RectCount = 0

    def DeleteAllButton(self):
        self.BeaconMas = []
        self.BeaconCount = 0
        self.OvalMas = []
        self.OvalCount = 0
        self.WallMas = []
        self.WallCount = 0
        self.RectMas = []
        self.RectCount = 0
        self.canvas.delete('all')

        self.PolyWallMotionFlag = False

    """СОЕДИНЕНИЕ МАЯКОВ С УЧЕТОМ ВИДИМОСТИ"""
    def ConnectButton(self):
        if len(self.BeaconMas) != 0:
            Connect(self.canvas, self.BeaconMas, self.OvalMas, self.WallMas, self.RectMas)

    """ПОКРЫТИЕ ПОЛЯ С УЧЕТОМ ВИДИМОСТИ"""
    def CoverageButton(self):
        if len(self.BeaconMas) != 0:
            Coverage(self.canvas, self.BeaconMas, self.OvalMas, self.WallMas, self.RectMas)

    """ПОКРЫТИЕ ПОЛЯ С УЧЕТОМ ВИДИМОСТИ И ГЕОМЕТРИЧЕСКОГО ФАКТОРА"""
    def GDOPButton(self):
        if len(self.BeaconMas) != 0:
            Gdop(self.canvas, self.BeaconMas, self.OvalMas, self.WallMas, self.RectMas)




