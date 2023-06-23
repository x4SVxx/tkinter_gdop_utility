from BEACONS import Beacon
from OVALS import Oval
from WALLS import Wall
from RECTANGLES import Rect
import PARAMETERS as Parameters
import keyboard
import time

"""ПЕРЕРИСОВКА ДИНАМИЧЕСКИЙ ОБЪЕКТОВ ПРИ РАССТАНОВКЕ"""
def DrawMotionOval(WindowFunc, x1, y1, x2, y2):
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1
    WindowFunc.canvas.delete('Oval')
    if x2 - x1 > 2 * Parameters.OvalWidth and y2 - y1 > 2 * Parameters.OvalWidth:
        WindowFunc.canvas.create_oval(x1 + Parameters.OvalWidth / 2, y1 + Parameters.OvalWidth / 2,
                                      x2 - Parameters.OvalWidth / 2, y2 - Parameters.OvalWidth / 2,
                                      width = Parameters.OvalWidth, tag='Oval', outline = Parameters.OvalColor)
    else:
        WindowFunc.canvas.create_oval(x1, y1, x2, y2, tag='Oval', fill=Parameters.OvalColor)

def DrawMotionRect(WindowFunc, x1, y1, x2, y2):
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1
    WindowFunc.canvas.delete('Rect')
    if x2 - x1 > 2 * Parameters.RectWidth and y2 - y1 > 2 * Parameters.RectWidth:
        WindowFunc.canvas.create_rectangle(x1 + Parameters.RectWidth / 2, y1 + Parameters.RectWidth / 2,
                                           x2 - Parameters.RectWidth / 2, y2 - Parameters.RectWidth / 2,
                                           width = Parameters.RectWidth, tag='Rect', outline = Parameters.RectColor)
    else:
        WindowFunc.canvas.create_rectangle(x1, y1, x2, y2, tag='Rect', fill=Parameters.RectColor)

def DrawMotionWall(WindowFunc, x1, y1, x2, y2):
    WindowFunc.canvas.create_line(x1, y1, x2, y2, width=Parameters.WallWidth, tag='Line', fill=Parameters.WallColor)

"""ОБРАБОКТА СОБЫТИЙ МЫШИ НА ПОЛЕ"""
def MousePress_Right(x, y, WindowFunc):

    for beacon in WindowFunc.BeaconMas:
        if pow(x - beacon.x, 2) / pow(beacon.BeaconSize, 2) + \
                    pow(y - beacon.y, 2) / pow(beacon.BeaconSize, 2) <= 1:

            WindowFunc.canvas.delete(beacon.BeaconTag)
            WindowFunc.BeaconMas.remove(beacon)

    for oval in WindowFunc.OvalMas:
        if pow(x - (oval.x2 + oval.x1) / 2, 2) / pow((oval.x2 - oval.x1) / 2, 2) + \
                    pow(y - (oval.y2 + oval.y1) / 2, 2) / pow((oval.y2 - oval.y1) / 2, 2) <= 1:

            WindowFunc.canvas.delete(oval.OvalTag)
            WindowFunc.OvalMas.remove(oval)

    for wall in WindowFunc.WallMas:
        if x <= wall.x1 + wall.CornerSize and x >= wall.x1 - wall.CornerSize and \
                y <= wall.y1 + wall.CornerSize and y >= wall.y1 - wall.CornerSize:

            WindowFunc.canvas.delete(wall.WallTag)
            WindowFunc.canvas.delete(wall.CornerTag1)
            WindowFunc.canvas.delete(wall.CornerTag2)
            WindowFunc.WallMas.remove(wall)

    for wall in WindowFunc.WallMas:
        if x <= wall.x2 + wall.CornerSize and x >= wall.x2 - wall.CornerSize and \
                y <= wall.y2 + wall.CornerSize and y >= wall.y2 - wall.CornerSize:

            WindowFunc.canvas.delete(wall.WallTag)
            WindowFunc.canvas.delete(wall.CornerTag1)
            WindowFunc.canvas.delete(wall.CornerTag2)
            WindowFunc.WallMas.remove(wall)

    for rect in WindowFunc.RectMas:
        if x >= rect.x1 and x <= rect.x2 and y >= rect.y1 and y <= rect.y2:

            WindowFunc.canvas.delete(rect.RectTag)
            WindowFunc.RectMas.remove(rect)

def MousePress_Left(x, y, WindowFunc):

    if x >= 3 and y >= 3 and \
            x <= WindowFunc.canvas.winfo_width() - 3 and y <= WindowFunc.canvas.winfo_height() - 3:

        WindowFunc.canvas.delete('Cover')
        WindowFunc.canvas.delete('BeaconShadow')
        WindowFunc.canvas.delete('Connect')

        for beacon in WindowFunc.BeaconMas:
            if pow(x - beacon.x, 2) / pow(beacon.BeaconSize, 2) + \
                    pow(y - beacon.y, 2) / pow(beacon.BeaconSize, 2) <= 1:
                WindowFunc.canvas.delete('BeaconShadow')
                WindowFunc.ReplaceBeaconFlag = True
                WindowFunc.ReplaceBeacon.append(beacon)
                WindowFunc.DeltaBeaconWidth = x - beacon.x
                WindowFunc.DeltaBeaconHeight = y - beacon.y

        if WindowFunc.BeaconFlag == False and WindowFunc.OvalFlag == False and \
                WindowFunc.WallFlag == False and WindowFunc.RectFlag == False and WindowFunc.PolyWallFlag == False and \
                WindowFunc.PolyWallMotionFlag == False:
            for oval in WindowFunc.OvalMas:
                if pow(x - (oval.x2 + oval.x1) / 2, 2) / pow((oval.x2 - oval.x1) / 2, 2) + \
                        pow(y - (oval.y2 + oval.y1) / 2, 2) / pow((oval.y2 - oval.y1) / 2, 2) <= 1:
                    WindowFunc.ReplaceOvalFlag = True
                    WindowFunc.ReplaceOval.append(oval)
                    WindowFunc.OvalWidth = oval.x2 - oval.x1
                    WindowFunc.OvalHeight = oval.y2 - oval.y1
                    WindowFunc.DeltaOvalWidth = x - oval.x1
                    WindowFunc.DeltaOvalHeight = y - oval.y1

        for wall in WindowFunc.WallMas:
            if x <= wall.x1 + wall.CornerSize and x >= wall.x1 - wall.CornerSize and \
                    y <= wall.y1 + wall.CornerSize and y >= wall.y1 - wall.CornerSize:
                WindowFunc.ReplaceCorner1Flag = True
                WindowFunc.ReplaceWall.append(wall)

        for wall in WindowFunc.WallMas:
            if x <= wall.x2 + wall.CornerSize and x >= wall.x2 - wall.CornerSize and \
                    y <= wall.y2 + wall.CornerSize and y >= wall.y2 - wall.CornerSize:
                WindowFunc.ReplaceCorner2Flag = True
                WindowFunc.ReplaceWall.append(wall)

        if WindowFunc.BeaconFlag == False and WindowFunc.OvalFlag == False and \
                WindowFunc.WallFlag == False and WindowFunc.RectFlag == False and WindowFunc.PolyWallFlag == False and \
                WindowFunc.PolyWallMotionFlag == False:
            for rect in WindowFunc.RectMas:
                if x >= rect.x1 and x <= rect.x2 and y >= rect.y1 and y <= rect.y2:
                    WindowFunc.ReplaceRectFlag = True
                    WindowFunc.ReplaceRect.append(rect)
                    WindowFunc.RectWidth = rect.x2 - rect.x1
                    WindowFunc.RectHeight = rect.y2 - rect.y1
                    WindowFunc.DeltaRectWidth = x - rect.x1
                    WindowFunc.DeltaRectHeight = y - rect.y1

        if not WindowFunc.ReplaceBeaconFlag and \
            not WindowFunc.ReplaceCorner1Flag and not WindowFunc.ReplaceCorner2Flag:

            if WindowFunc.BeaconFlag:

                # if x < Parameters.BeaconSize + 3 and \
                #         y < Parameters.BeaconSize + 3:
                #     x = 3 + Parameters.BeaconSize
                #     y = 3 + Parameters.BeaconSize
                # elif x > WindowFunc.canvas.winfo_width() - Parameters.BeaconSize - 3 and \
                #         y < Parameters.BeaconSize + 3:
                #     x = WindowFunc.canvas.winfo_width() - Parameters.BeaconSize - 3
                #     y = 3 + Parameters.BeaconSize
                # elif x < Parameters.BeaconSize + 3 and \
                #         y > WindowFunc.canvas.winfo_height() - Parameters.BeaconSize - 3:
                #     x = 3 + Parameters.BeaconSize
                #     y = WindowFunc.canvas.winfo_height() - Parameters.BeaconSize - 3
                # elif x > WindowFunc.canvas.winfo_width() - Parameters.BeaconSize - 3 and \
                #         y > WindowFunc.canvas.winfo_height() - Parameters.BeaconSize - 3:
                #     x = WindowFunc.canvas.winfo_width() - Parameters.BeaconSize - 3
                #     y = WindowFunc.canvas.winfo_height() - Parameters.BeaconSize - 3
                # elif x < Parameters.BeaconSize + 3:
                #     x = 3 + Parameters.BeaconSize
                # elif x > WindowFunc.canvas.winfo_width() - Parameters.BeaconSize - 3:
                #     x = WindowFunc.canvas.winfo_width() - Parameters.BeaconSize - 3
                # elif y < Parameters.BeaconSize + 3:
                #     y = Parameters.BeaconSize + 3
                # elif y > WindowFunc.canvas.winfo_height() - Parameters.BeaconSize - 3:
                #     y = WindowFunc.canvas.winfo_height() - Parameters.BeaconSize - 3
                if x > Parameters.BeaconSize + 1 and y > Parameters.BeaconSize + 1 and \
                        x < WindowFunc.canvas.winfo_width() - Parameters.BeaconSize - 1 and \
                        y < WindowFunc.canvas.winfo_height() - Parameters.BeaconSize - 1:

                    WindowFunc.canvas.delete('BeaconShadow')

                    PointXY = (x, y)
                    BeaconPos = list(PointXY)
                    WindowFunc.BeaconCount += 1
                    NewBeacon = Beacon(BeaconPos, WindowFunc.BeaconCount, Parameters.BeaconSize,
                                       Parameters.BeaconOutlineWidth,
                                       Parameters.BeaconColor, Parameters.BeaconOutlineColor)
                    WindowFunc.BeaconMas.append(NewBeacon)
                    NewBeacon.DrawBeacon(WindowFunc.canvas)

                else:

                    WindowFunc.canvas.create_oval(x - Parameters.BeaconSize, y - Parameters.BeaconSize,
                                                  x + Parameters.BeaconSize, y + Parameters.BeaconSize,
                                                  outline='red', width=3, tag='BeaconShadowFlesh')
                    WindowFunc.canvas.update()
                    time.sleep(0.2)
                    WindowFunc.canvas.delete('BeaconShadowFlesh')
                    WindowFunc.canvas.update()
                    WindowFunc.canvas.create_oval(x - Parameters.BeaconSize, y - Parameters.BeaconSize,
                                                  x + Parameters.BeaconSize, y + Parameters.BeaconSize,
                                                  outline='red', width=2, tag='BeaconShadowFlesh')
                    WindowFunc.canvas.update()
                    time.sleep(0.2)
                    WindowFunc.canvas.delete('BeaconShadowFlesh')
                    WindowFunc.canvas.update()
                    WindowFunc.canvas.create_oval(x - Parameters.BeaconSize, y - Parameters.BeaconSize,
                                                  x + Parameters.BeaconSize, y + Parameters.BeaconSize,
                                                  outline='red', width=1, tag='BeaconShadow')
                    WindowFunc.canvas.update()



            elif WindowFunc.OvalFlag:

                PointXY = (x, y)
                WindowFunc.OvalPosSTART = list(PointXY)
                WindowFunc.OvalMotionFlag = True

            elif WindowFunc.WallFlag:

                PointXY = (x, y)
                WindowFunc.WallPosSTART = list(PointXY)
                WindowFunc.WallMotionFlag = True

            elif WindowFunc.RectFlag:

                PointXY = (x, y)
                WindowFunc.RectPosSTART = list(PointXY)
                WindowFunc.RectMotionFlag = True

            elif WindowFunc.PolyWallFlag:

                PointXY = (x, y)
                WindowFunc.PolyWallPosSTART = list(PointXY)
                WindowFunc.PolyWallMotionFlag = True

def MouseRelease_Left(x, y, WindowFunc):

    if WindowFunc.ReplaceBeaconFlag:

        WindowFunc.ReplaceBeaconFlag = False
        WindowFunc.canvas.delete(WindowFunc.ReplaceBeacon[0].BeaconTag)

        if x <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconWidth and \
                y <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
        elif x <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconWidth and \
                y >= WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
        elif x >= WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconWidth and \
                y <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
        elif x >= WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconWidth and \
                y >= WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
        elif x <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconWidth:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
            WindowFunc.ReplaceBeacon[0].y = y - WindowFunc.DeltaBeaconHeight
        elif x >= WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconWidth:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
            WindowFunc.ReplaceBeacon[0].y = y - WindowFunc.DeltaBeaconHeight
        elif y <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = x - WindowFunc.DeltaBeaconWidth
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
        elif y >= WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = x - WindowFunc.DeltaBeaconWidth
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
        else:
            WindowFunc.ReplaceBeacon[0].x = x - WindowFunc.DeltaBeaconWidth
            WindowFunc.ReplaceBeacon[0].y = y - WindowFunc.DeltaBeaconHeight

        WindowFunc.ReplaceBeacon[0].DrawBeacon(WindowFunc.canvas)
        WindowFunc.ReplaceBeacon.pop(0)

    if WindowFunc.ReplaceOvalFlag:

        WindowFunc.ReplaceOvalFlag = False
        WindowFunc.canvas.delete(WindowFunc.ReplaceOval[0].OvalTag)

        if x <= WindowFunc.DeltaOvalWidth + 3 and \
                y <= WindowFunc.DeltaOvalHeight + 3:
            WindowFunc.ReplaceOval[0].x1 = 3
            WindowFunc.ReplaceOval[0].x2 = 3 + WindowFunc.OvalWidth
            WindowFunc.ReplaceOval[0].y1 = 3
            WindowFunc.ReplaceOval[0].y2 = 3 + WindowFunc.OvalHeight
        elif x <= WindowFunc.DeltaOvalWidth + 3 and \
                y >= WindowFunc.canvas.winfo_height() - (WindowFunc.OvalHeight - WindowFunc.DeltaOvalHeight) - 3:
            WindowFunc.ReplaceOval[0].x1 = 3
            WindowFunc.ReplaceOval[0].x2 = 3 + WindowFunc.OvalWidth
            WindowFunc.ReplaceOval[0].y1 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.OvalHeight
            WindowFunc.ReplaceOval[0].y2 = WindowFunc.canvas.winfo_height() - 3
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.OvalWidth - WindowFunc.DeltaOvalWidth) - 3 and \
                y <= WindowFunc.DeltaOvalHeight + 3:
            WindowFunc.ReplaceOval[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.OvalWidth - 3
            WindowFunc.ReplaceOval[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceOval[0].y1 = 3
            WindowFunc.ReplaceOval[0].y2 = 3 + WindowFunc.OvalHeight
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.OvalWidth - WindowFunc.DeltaOvalWidth) - 3 and \
                y >= WindowFunc.canvas.winfo_height() - (
                WindowFunc.OvalHeight - WindowFunc.DeltaOvalHeight) - 3:
            WindowFunc.ReplaceOval[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.OvalWidth - 3
            WindowFunc.ReplaceOval[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceOval[0].y1 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.OvalHeight
            WindowFunc.ReplaceOval[0].y2 = WindowFunc.canvas.winfo_height() - 3
        elif x <= WindowFunc.DeltaOvalWidth + 3:
            WindowFunc.ReplaceOval[0].x1 = 3
            WindowFunc.ReplaceOval[0].x2 = 3 + WindowFunc.OvalWidth
            WindowFunc.ReplaceOval[0].y1 = y - WindowFunc.DeltaOvalHeight
            WindowFunc.ReplaceOval[0].y2 = y + (WindowFunc.OvalHeight - WindowFunc.DeltaOvalHeight)
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.OvalWidth - WindowFunc.DeltaOvalWidth) - 3:
            WindowFunc.ReplaceOval[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.OvalWidth - 3
            WindowFunc.ReplaceOval[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceOval[0].y1 = y - WindowFunc.DeltaOvalHeight
            WindowFunc.ReplaceOval[0].y2 = y + (WindowFunc.OvalHeight - WindowFunc.DeltaOvalHeight)
        elif y <= WindowFunc.DeltaOvalHeight + 3:
            WindowFunc.ReplaceOval[0].x1 = x - WindowFunc.DeltaOvalWidth
            WindowFunc.ReplaceOval[0].x2 = x + (WindowFunc.OvalWidth - WindowFunc.DeltaOvalWidth)
            WindowFunc.ReplaceOval[0].y1 = 3
            WindowFunc.ReplaceOval[0].y2 = 3 + WindowFunc.OvalHeight
        elif y >= WindowFunc.canvas.winfo_height() - (WindowFunc.OvalHeight - WindowFunc.DeltaOvalHeight) - 3:
            WindowFunc.ReplaceOval[0].x1 = x - WindowFunc.DeltaOvalWidth
            WindowFunc.ReplaceOval[0].x2 = x + (WindowFunc.OvalWidth - WindowFunc.DeltaOvalWidth)
            WindowFunc.ReplaceOval[0].y1 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.OvalHeight
            WindowFunc.ReplaceOval[0].y2 = WindowFunc.canvas.winfo_height() - 3
        else:
            WindowFunc.ReplaceOval[0].x1 = x - WindowFunc.DeltaOvalWidth
            WindowFunc.ReplaceOval[0].x2 = WindowFunc.ReplaceOval[0].x1 + WindowFunc.OvalWidth
            WindowFunc.ReplaceOval[0].y1 = y - WindowFunc.DeltaOvalHeight
            WindowFunc.ReplaceOval[0].y2 = WindowFunc.ReplaceOval[0].y1 + WindowFunc.OvalHeight

        WindowFunc.ReplaceOval[0].DrawOval(WindowFunc.canvas)
        WindowFunc.ReplaceOval.pop(0)

    if WindowFunc.ReplaceCorner1Flag:

        WindowFunc.ReplaceCorner1Flag = False
        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].CornerTag1)
        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].CornerTag2)
        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].WallTag)

        if x <= Parameters.CornerSize + 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x1 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y1 = Parameters.CornerSize + 3
        elif x <= Parameters.CornerSize + 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x1 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y1 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x1 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y1 = Parameters.CornerSize + 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x1 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y1 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x1 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y1 = y
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x1 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y1 = y
        elif y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x1 = x
            WindowFunc.ReplaceWall[0].y1 = Parameters.CornerSize + 3
        elif y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x1 = x
            WindowFunc.ReplaceWall[0].y1 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        else:
            WindowFunc.ReplaceWall[0].x1 = x
            WindowFunc.ReplaceWall[0].y1 = y

        WindowFunc.ReplaceWall[0].DrawWall(WindowFunc.canvas)
        WindowFunc.ReplaceWall.pop(0)

    if WindowFunc.ReplaceCorner2Flag:

        WindowFunc.ReplaceCorner2Flag = False
        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].CornerTag1)
        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].CornerTag2)
        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].WallTag)

        if x <= Parameters.CornerSize + 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x2 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y2 = Parameters.CornerSize + 3
        elif x <= Parameters.CornerSize + 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x2 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y2 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x2 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y2 = Parameters.CornerSize + 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x2 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y2 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x2 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y2 = y
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x2 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y2 = y
        elif y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x2 = x
            WindowFunc.ReplaceWall[0].y2 = Parameters.CornerSize + 3
        elif y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x2 = x
            WindowFunc.ReplaceWall[0].y2 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        else:
            WindowFunc.ReplaceWall[0].x2 = x
            WindowFunc.ReplaceWall[0].y2 = y

        WindowFunc.ReplaceWall[0].DrawWall(WindowFunc.canvas)
        WindowFunc.ReplaceWall.pop(0)

    if WindowFunc.ReplaceRectFlag:

        WindowFunc.ReplaceRectFlag = False
        WindowFunc.canvas.delete(WindowFunc.ReplaceRect[0].RectTag)

        if x <= WindowFunc.DeltaRectWidth + 3 and \
                y <= WindowFunc.DeltaRectHeight + 3:
            WindowFunc.ReplaceRect[0].x1 = 3
            WindowFunc.ReplaceRect[0].x2 = 3 + WindowFunc.RectWidth
            WindowFunc.ReplaceRect[0].y1 = 3
            WindowFunc.ReplaceRect[0].y2 = 3 + WindowFunc.RectHeight
        elif x <= WindowFunc.DeltaRectWidth + 3 and \
                y >= WindowFunc.canvas.winfo_height() - (WindowFunc.RectHeight - WindowFunc.DeltaRectHeight) - 3:
            WindowFunc.ReplaceRect[0].x1 = 3
            WindowFunc.ReplaceRect[0].x2 = 3 + WindowFunc.RectWidth
            WindowFunc.ReplaceRect[0].y1 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.RectHeight
            WindowFunc.ReplaceRect[0].y2 = WindowFunc.canvas.winfo_height() - 3
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.RectWidth - WindowFunc.DeltaRectWidth) - 3 and \
                y <= WindowFunc.DeltaRectHeight + 3:
            WindowFunc.ReplaceRect[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.RectWidth - 3
            WindowFunc.ReplaceRect[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceRect[0].y1 = 3
            WindowFunc.ReplaceRect[0].y2 = 3 + WindowFunc.RectHeight
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.RectWidth - WindowFunc.DeltaRectWidth) - 3 and \
                y >= WindowFunc.canvas.winfo_height() - (WindowFunc.RectHeight - WindowFunc.DeltaRectHeight) - 3:
            WindowFunc.ReplaceRect[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.RectWidth - 3
            WindowFunc.ReplaceRect[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceRect[0].y1 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.RectHeight
            WindowFunc.ReplaceRect[0].y2 = WindowFunc.canvas.winfo_height() - 3
        elif x <= WindowFunc.DeltaRectWidth + 3:
            WindowFunc.ReplaceRect[0].x1 = 3
            WindowFunc.ReplaceRect[0].x2 = 3 + WindowFunc.RectWidth
            WindowFunc.ReplaceRect[0].y1 = y - WindowFunc.DeltaRectHeight
            WindowFunc.ReplaceRect[0].y2 = y + (WindowFunc.RectHeight - WindowFunc.DeltaRectHeight)
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.RectWidth - WindowFunc.DeltaRectWidth) - 3:
            WindowFunc.ReplaceRect[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.RectWidth - 3
            WindowFunc.ReplaceRect[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceRect[0].y1 = y - WindowFunc.DeltaRectHeight
            WindowFunc.ReplaceRect[0].y2 = y + (WindowFunc.RectHeight - WindowFunc.DeltaRectHeight)
        elif y <= WindowFunc.DeltaRectHeight + 3:
            WindowFunc.ReplaceRect[0].x1 = x - WindowFunc.DeltaRectWidth
            WindowFunc.ReplaceRect[0].x2 = x + (WindowFunc.RectWidth - WindowFunc.DeltaRectWidth)
            WindowFunc.ReplaceRect[0].y1 = 3
            WindowFunc.ReplaceRect[0].y2 = 3 + WindowFunc.RectHeight
        elif y >= WindowFunc.canvas.winfo_height() - (WindowFunc.RectHeight - WindowFunc.DeltaRectHeight) - 3:
            WindowFunc.ReplaceRect[0].x1 = x - WindowFunc.DeltaRectWidth
            WindowFunc.ReplaceRect[0].x2 = x + (WindowFunc.RectWidth - WindowFunc.DeltaRectWidth)
            WindowFunc.ReplaceRect[0].y1 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.RectHeight
            WindowFunc.ReplaceRect[0].y2 = WindowFunc.canvas.winfo_height() - 3
        else:
            WindowFunc.ReplaceRect[0].x1 = x - WindowFunc.DeltaRectWidth
            WindowFunc.ReplaceRect[0].x2 = WindowFunc.ReplaceRect[0].x1 + WindowFunc.RectWidth
            WindowFunc.ReplaceRect[0].y1 = y - WindowFunc.DeltaRectHeight
            WindowFunc.ReplaceRect[0].y2 = WindowFunc.ReplaceRect[0].y1 + WindowFunc.RectHeight

        WindowFunc.ReplaceRect[0].DrawRect(WindowFunc.canvas)
        WindowFunc.ReplaceRect.pop(0)

    if WindowFunc.OvalMotionFlag:

        WindowFunc.OvalMotionFlag = False
        WindowFunc.canvas.delete('Oval')
        PointXY = (x, y)
        WindowFunc.OvalPosFINISH = list(PointXY)

        if x <= + 3 and y <= 3:
            WindowFunc.OvalPosFINISH[0] = 3
            WindowFunc.OvalPosFINISH[1] = 3
        elif x <= 3 and y >= WindowFunc.canvas.winfo_height() - 3:
            WindowFunc.OvalPosFINISH[0] = 3
            WindowFunc.OvalPosFINISH[1] = WindowFunc.canvas.winfo_height() - 3
        elif x >= WindowFunc.canvas.winfo_width() - 3 and y <= 3:
            WindowFunc.OvalPosFINISH[0] = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.OvalPosFINISH[1] = 3
        elif x >= WindowFunc.canvas.winfo_width() - 3 and y >= WindowFunc.canvas.winfo_height() - 3:
            WindowFunc.OvalPosFINISH[0] = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.OvalPosFINISH[1] = WindowFunc.canvas.winfo_height() - 3
        elif x <= 3:
            WindowFunc.OvalPosFINISH[0] = 3
            WindowFunc.OvalPosFINISH[1] = y
        elif x >= WindowFunc.canvas.winfo_width() - 3:
            WindowFunc.OvalPosFINISH[0] = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.OvalPosFINISH[1] = y
        elif y <= 3:
            WindowFunc.OvalPosFINISH[0] = x
            WindowFunc.OvalPosFINISH[1] = 3
        elif y >= WindowFunc.canvas.winfo_height() - 3:
            WindowFunc.OvalPosFINISH[0] = x
            WindowFunc.OvalPosFINISH[1] = WindowFunc.canvas.winfo_height() - 3
        else:
            WindowFunc.OvalPosFINISH[0] = x
            WindowFunc.OvalPosFINISH[1] = y

        if WindowFunc.OvalPosFINISH[0] < WindowFunc.OvalPosSTART[0]:
            WindowFunc.OvalPosFINISH[0], WindowFunc.OvalPosSTART[0] = WindowFunc.OvalPosSTART[0], WindowFunc.OvalPosFINISH[0]
        if WindowFunc.OvalPosFINISH[1] < WindowFunc.OvalPosSTART[1]:
            WindowFunc.OvalPosFINISH[1], WindowFunc.OvalPosSTART[1] = WindowFunc.OvalPosSTART[1], WindowFunc.OvalPosFINISH[1]

        WindowFunc.OvalCount += 1
        NewOval = Oval(WindowFunc.OvalPosSTART, WindowFunc.OvalPosFINISH, WindowFunc.OvalCount,
                       Parameters.OvalWidth, Parameters.OvalColor)
        WindowFunc.OvalMas.append(NewOval)
        NewOval.DrawOval(WindowFunc.canvas)

    if WindowFunc.WallMotionFlag:

        WindowFunc.WallMotionFlag = False
        WindowFunc.canvas.delete('Line')
        PointXY = (x, y)
        WindowFunc.WallPosFINISH = list(PointXY)

        if x <= Parameters.CornerSize + 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.WallPosFINISH[0] = Parameters.CornerSize + 3
            WindowFunc.WallPosFINISH[1] = Parameters.CornerSize + 3
        elif x <= Parameters.CornerSize + 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.WallPosFINISH[0] = Parameters.CornerSize + 3
            WindowFunc.WallPosFINISH[1] = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.WallPosFINISH[0] = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.WallPosFINISH[1] = Parameters.CornerSize + 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.WallPosFINISH[0] = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.WallPosFINISH[1] = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x <= Parameters.CornerSize + 3:
            WindowFunc.WallPosFINISH[0] = Parameters.CornerSize + 3
            WindowFunc.WallPosFINISH[1] = y
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3:
            WindowFunc.WallPosFINISH[0] = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.WallPosFINISH[1] = y
        elif y <= Parameters.CornerSize + 3:
            WindowFunc.WallPosFINISH[0] = x
            WindowFunc.WallPosFINISH[1] = Parameters.CornerSize + 3
        elif y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.WallPosFINISH[0] = x
            WindowFunc.WallPosFINISH[1] = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        else:
            WindowFunc.WallPosFINISH[0] = x
            WindowFunc.WallPosFINISH[1] = y

        WindowFunc.WallCount += 1
        NewWall = Wall(WindowFunc.WallPosSTART, WindowFunc.WallPosFINISH, WindowFunc.WallCount,
                       Parameters.WallWidth, Parameters.WallColor, Parameters.CornerSize, False)
        WindowFunc.WallMas.append(NewWall)
        NewWall.DrawWall(WindowFunc.canvas)

    if WindowFunc.PolyWallMotionFlag:

        WindowFunc.PolyWallFlag = False

        WindowFunc.canvas.delete('Line')
        PointXY = (x, y)
        WindowFunc.PolyWallPosFINISH = list(PointXY)

        if x <= Parameters.CornerSize + 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.PolyWallPosFINISH[0] = Parameters.CornerSize + 3
            WindowFunc.PolyWallPosFINISH[1] = Parameters.CornerSize + 3
        elif x <= Parameters.CornerSize + 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.PolyWallPosFINISH[0] = Parameters.CornerSize + 3
            WindowFunc.PolyWallPosFINISH[1] = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.PolyWallPosFINISH[0] = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.PolyWallPosFINISH[1] = Parameters.CornerSize + 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.PolyWallPosFINISH[0] = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.PolyWallPosFINISH[1] = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x <= Parameters.CornerSize + 3:
            WindowFunc.PolyWallPosFINISH[0] = Parameters.CornerSize + 3
            WindowFunc.PolyWallPosFINISH[1] = y
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3:
            WindowFunc.PolyWallPosFINISH[0] = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.PolyWallPosFINISH[1] = y
        elif y <= Parameters.CornerSize + 3:
            WindowFunc.PolyWallPosFINISH[0] = x
            WindowFunc.PolyWallPosFINISH[1] = Parameters.CornerSize + 3
        elif y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.PolyWallPosFINISH[0] = x
            WindowFunc.PolyWallPosFINISH[1] = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        else:
            WindowFunc.PolyWallPosFINISH[0] = x
            WindowFunc.PolyWallPosFINISH[1] = y

        WindowFunc.WallCount += 1
        NewWall = Wall(WindowFunc.PolyWallPosSTART, WindowFunc.PolyWallPosFINISH, WindowFunc.WallCount,
                       Parameters.WallWidth, Parameters.WallColor, Parameters.CornerSize, True)
        WindowFunc.WallMas.append(NewWall)
        NewWall.DrawWall(WindowFunc.canvas)
        WindowFunc.PolyWallPosSTART = list(PointXY)

    if WindowFunc.RectMotionFlag:

        WindowFunc.RectMotionFlag = False
        WindowFunc.canvas.delete('Rect')
        PointXY = (x, y)
        WindowFunc.RectPosFINISH = list(PointXY)

        if x <= + 3 and y <= 3:
            WindowFunc.RectPosFINISH[0] = 3
            WindowFunc.RectPosFINISH[1] = 3
        elif x <= 3 and y >= WindowFunc.canvas.winfo_height() - 3:
            WindowFunc.RectPosFINISH[0] = 3
            WindowFunc.RectPosFINISH[1] = WindowFunc.canvas.winfo_height() - 3
        elif x >= WindowFunc.canvas.winfo_width() - 3 and y <= 3:
            WindowFunc.RectPosFINISH[0] = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.RectPosFINISH[1] = 3
        elif x >= WindowFunc.canvas.winfo_width() - 3 and y >= WindowFunc.canvas.winfo_height() - 3:
            WindowFunc.RectPosFINISH[0] = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.RectPosFINISH[1] = WindowFunc.canvas.winfo_height() - 3
        elif x <= 3:
            WindowFunc.RectPosFINISH[0] = 3
            WindowFunc.RectPosFINISH[1] = y
        elif x >= WindowFunc.canvas.winfo_width() - 3:
            WindowFunc.RectPosFINISH[0] = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.RectPosFINISH[1] = y
        elif y <= 3:
            WindowFunc.RectPosFINISH[0] = x
            WindowFunc.RectPosFINISH[1] = 3
        elif y >= WindowFunc.canvas.winfo_height() - 3:
            WindowFunc.RectPosFINISH[0] = x
            WindowFunc.RectPosFINISH[1] = WindowFunc.canvas.winfo_height() - 3
        else:
            WindowFunc.RectPosFINISH[0] = x
            WindowFunc.RectPosFINISH[1] = y

        if WindowFunc.RectPosFINISH[0] < WindowFunc.RectPosSTART[0]:
            WindowFunc.RectPosFINISH[0], WindowFunc.RectPosSTART[0] = WindowFunc.RectPosSTART[0], WindowFunc.RectPosFINISH[0]
        if WindowFunc.RectPosFINISH[1] < WindowFunc.RectPosSTART[1]:
            WindowFunc.RectPosFINISH[1], WindowFunc.RectPosSTART[1] = WindowFunc.RectPosSTART[1], WindowFunc.RectPosFINISH[1]

        WindowFunc.RectCount += 1
        NewRect = Rect(WindowFunc.RectPosSTART, WindowFunc.RectPosFINISH, WindowFunc.RectCount,
                       Parameters.RectWidth, Parameters.RectColor)
        WindowFunc.RectMas.append(NewRect)
        NewRect.DrawRect(WindowFunc.canvas)

def MouseMotion(x, y, WindowFunc):

    if WindowFunc.BeaconFlag:

        WindowFunc.canvas.delete('BeaconShadow')

        if x > Parameters.BeaconSize + 1 and y > Parameters.BeaconSize + 1 and \
                x < WindowFunc.canvas.winfo_width() - Parameters.BeaconSize - 2 and \
                y < WindowFunc.canvas.winfo_height() - Parameters.BeaconSize - 2:

            WindowFunc.canvas.create_oval(x - Parameters.BeaconSize, y - Parameters.BeaconSize,
                                          x + Parameters.BeaconSize, y + Parameters.BeaconSize,
                                          outline='black', width=1, tag='BeaconShadow')
        elif x < 3 or y < 3 or x > WindowFunc.canvas.winfo_width() - 4 or y > WindowFunc.canvas.winfo_height() - 4:
            WindowFunc.canvas.delete('BeaconShadow')

        else:
            WindowFunc.canvas.create_oval(x - Parameters.BeaconSize, y - Parameters.BeaconSize,
                                          x + Parameters.BeaconSize, y + Parameters.BeaconSize,
                                          outline='red', width=1, tag='BeaconShadow')


    if WindowFunc.ReplaceBeaconFlag:

        WindowFunc.canvas.delete('BeaconShadow')

        WindowFunc.canvas.delete(WindowFunc.ReplaceBeacon[0].BeaconTag)

        if x <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconWidth and \
                y <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
        elif x <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconWidth and \
                y >= WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
        elif x >= WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconWidth and \
                y <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
        elif x >= WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconWidth and \
                y >= WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
        elif x <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconWidth:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
            WindowFunc.ReplaceBeacon[0].y = y - WindowFunc.DeltaBeaconHeight
        elif x >= WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconWidth:
            WindowFunc.ReplaceBeacon[0].x = WindowFunc.canvas.winfo_width() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
            WindowFunc.ReplaceBeacon[0].y = y - WindowFunc.DeltaBeaconHeight
        elif y <= WindowFunc.ReplaceBeacon[0].BeaconSize + 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = x - WindowFunc.DeltaBeaconWidth
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.ReplaceBeacon[0].BeaconSize + 3
        elif y >= WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3 + WindowFunc.DeltaBeaconHeight:
            WindowFunc.ReplaceBeacon[0].x = x - WindowFunc.DeltaBeaconWidth
            WindowFunc.ReplaceBeacon[0].y = WindowFunc.canvas.winfo_height() - WindowFunc.ReplaceBeacon[0].BeaconSize - 3
        else:
            WindowFunc.ReplaceBeacon[0].x = x - WindowFunc.DeltaBeaconWidth
            WindowFunc.ReplaceBeacon[0].y = y - WindowFunc.DeltaBeaconHeight

        WindowFunc.ReplaceBeacon[0].DrawBeacon(WindowFunc.canvas)

    if WindowFunc.ReplaceOvalFlag:

        WindowFunc.canvas.delete(WindowFunc.ReplaceOval[0].OvalTag)

        if x <= WindowFunc.DeltaOvalWidth + 3 and \
                y <= WindowFunc.DeltaOvalHeight + 3:
            WindowFunc.ReplaceOval[0].x1 = 3
            WindowFunc.ReplaceOval[0].x2 = 3 + WindowFunc.OvalWidth
            WindowFunc.ReplaceOval[0].y1 = 3
            WindowFunc.ReplaceOval[0].y2 = 3 + WindowFunc.OvalHeight
        elif x <= WindowFunc.DeltaOvalWidth + 3 and \
                y >= WindowFunc.canvas.winfo_height() - (WindowFunc.OvalHeight - WindowFunc.DeltaOvalHeight) - 3:
            WindowFunc.ReplaceOval[0].x1 = 3
            WindowFunc.ReplaceOval[0].x2 = 3 + WindowFunc.OvalWidth
            WindowFunc.ReplaceOval[0].y1 = WindowFunc.canvas.winfo_height() - 3
            WindowFunc.ReplaceOval[0].y2 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.OvalHeight
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.OvalWidth - WindowFunc.DeltaOvalWidth) - 3 and \
                y <= WindowFunc.DeltaOvalHeight + 3:
            WindowFunc.ReplaceOval[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.OvalWidth - 3
            WindowFunc.ReplaceOval[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceOval[0].y1 = 3
            WindowFunc.ReplaceOval[0].y2 = 3 + WindowFunc.OvalHeight
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.OvalWidth - WindowFunc.DeltaOvalWidth) - 3 and \
                y >= WindowFunc.canvas.winfo_height() - (WindowFunc.OvalHeight - WindowFunc.DeltaOvalHeight) - 3:
            WindowFunc.ReplaceOval[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.OvalWidth - 3
            WindowFunc.ReplaceOval[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceOval[0].y1 = WindowFunc.canvas.winfo_height() - 3
            WindowFunc.ReplaceOval[0].y2 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.OvalHeight
        elif x <= WindowFunc.DeltaOvalWidth + 3:
            WindowFunc.ReplaceOval[0].x1 = 3
            WindowFunc.ReplaceOval[0].x2 = 3 + WindowFunc.OvalWidth
            WindowFunc.ReplaceOval[0].y1 = y - WindowFunc.DeltaOvalHeight
            WindowFunc.ReplaceOval[0].y2 = y + (WindowFunc.OvalHeight - WindowFunc.DeltaOvalHeight)
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.OvalWidth - WindowFunc.DeltaOvalWidth) - 3:
            WindowFunc.ReplaceOval[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.OvalWidth - 3
            WindowFunc.ReplaceOval[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceOval[0].y1 = y - WindowFunc.DeltaOvalHeight
            WindowFunc.ReplaceOval[0].y2 = y + (WindowFunc.OvalHeight - WindowFunc.DeltaOvalHeight)
        elif y <= WindowFunc.DeltaOvalHeight + 3:
            WindowFunc.ReplaceOval[0].x1 = x - WindowFunc.DeltaOvalWidth
            WindowFunc.ReplaceOval[0].x2 = x + (WindowFunc.OvalWidth - WindowFunc.DeltaOvalWidth)
            WindowFunc.ReplaceOval[0].y1 = 3
            WindowFunc.ReplaceOval[0].y2 = 3 + WindowFunc.OvalHeight
        elif y >= WindowFunc.canvas.winfo_height() - (WindowFunc.OvalHeight - WindowFunc.DeltaOvalHeight) - 3:
            WindowFunc.ReplaceOval[0].x1 = x - WindowFunc.DeltaOvalWidth
            WindowFunc.ReplaceOval[0].x2 = x + (WindowFunc.OvalWidth - WindowFunc.DeltaOvalWidth)
            WindowFunc.ReplaceOval[0].y1 = WindowFunc.canvas.winfo_height() - 3
            WindowFunc.ReplaceOval[0].y2 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.OvalHeight
        else:
            WindowFunc.ReplaceOval[0].x1 = x - WindowFunc.DeltaOvalWidth
            WindowFunc.ReplaceOval[0].x2 = WindowFunc.ReplaceOval[0].x1 + WindowFunc.OvalWidth
            WindowFunc.ReplaceOval[0].y1 = y - WindowFunc.DeltaOvalHeight
            WindowFunc.ReplaceOval[0].y2 = WindowFunc.ReplaceOval[0].y1 + WindowFunc.OvalHeight


        if WindowFunc.ReplaceOval[0].x2 < WindowFunc.ReplaceOval[0].x1:
            WindowFunc.ReplaceOval[0].x2, WindowFunc.ReplaceOval[0].x1 = WindowFunc.ReplaceOval[0].x1, WindowFunc.ReplaceOval[0].x2
        if WindowFunc.ReplaceOval[0].y2 < WindowFunc.ReplaceOval[0].y1:
            WindowFunc.ReplaceOval[0].y2, WindowFunc.ReplaceOval[0].y1 = WindowFunc.ReplaceOval[0].y1, WindowFunc.ReplaceOval[0].y2

        WindowFunc.ReplaceOval[0].DrawOval(WindowFunc.canvas)

    if WindowFunc.ReplaceCorner1Flag:

        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].CornerTag1)
        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].CornerTag2)
        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].WallTag)

        if x <= Parameters.CornerSize + 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x1 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y1 = Parameters.CornerSize + 3
        elif x <= Parameters.CornerSize + 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x1 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y1 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x1 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y1 = Parameters.CornerSize + 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x1 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y1 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x1 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y1 = y
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x1 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y1 = y
        elif y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x1 = x
            WindowFunc.ReplaceWall[0].y1 = Parameters.CornerSize + 3
        elif y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x1 = x
            WindowFunc.ReplaceWall[0].y1 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        else:
            WindowFunc.ReplaceWall[0].x1 = x
            WindowFunc.ReplaceWall[0].y1 = y

        WindowFunc.ReplaceWall[0].DrawWall(WindowFunc.canvas)

    if WindowFunc.ReplaceCorner2Flag:

        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].CornerTag1)
        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].CornerTag2)
        WindowFunc.canvas.delete(WindowFunc.ReplaceWall[0].WallTag)

        if x <= Parameters.CornerSize + 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x2 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y2 = Parameters.CornerSize + 3
        elif x <= Parameters.CornerSize + 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x2 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y2 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x2 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y2 = Parameters.CornerSize + 3
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x2 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y2 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        elif x <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x2 = Parameters.CornerSize + 3
            WindowFunc.ReplaceWall[0].y2 = y
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x2 = WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3
            WindowFunc.ReplaceWall[0].y2 = y
        elif y <= Parameters.CornerSize + 3:
            WindowFunc.ReplaceWall[0].x2 = x
            WindowFunc.ReplaceWall[0].y2 = Parameters.CornerSize + 3
        elif y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            WindowFunc.ReplaceWall[0].x2 = x
            WindowFunc.ReplaceWall[0].y2 = WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3
        else:
            WindowFunc.ReplaceWall[0].x2 = x
            WindowFunc.ReplaceWall[0].y2 = y

        WindowFunc.ReplaceWall[0].DrawWall(WindowFunc.canvas)

    if WindowFunc.ReplaceRectFlag:

        WindowFunc.canvas.delete(WindowFunc.ReplaceRect[0].RectTag)

        if x <= WindowFunc.DeltaRectWidth + 3 and \
                y <= WindowFunc.DeltaRectHeight + 3:
            WindowFunc.ReplaceRect[0].x1 = 3
            WindowFunc.ReplaceRect[0].x2 = 3 + WindowFunc.RectWidth
            WindowFunc.ReplaceRect[0].y1 = 3
            WindowFunc.ReplaceRect[0].y2 = 3 + WindowFunc.RectHeight
        elif x <= WindowFunc.DeltaRectWidth + 3 and \
                y >= WindowFunc.canvas.winfo_height() - (WindowFunc.RectHeight - WindowFunc.DeltaRectHeight) - 3:
            WindowFunc.ReplaceRect[0].x1 = 3
            WindowFunc.ReplaceRect[0].x2 = 3 + WindowFunc.RectWidth
            WindowFunc.ReplaceRect[0].y1 = WindowFunc.canvas.winfo_height() - 3
            WindowFunc.ReplaceRect[0].y2 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.RectHeight
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.RectWidth - WindowFunc.DeltaRectWidth) - 3 and \
                y <= WindowFunc.DeltaRectHeight + 3:
            WindowFunc.ReplaceRect[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.RectWidth - 3
            WindowFunc.ReplaceRect[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceRect[0].y1 = 3
            WindowFunc.ReplaceRect[0].y2 = 3 + WindowFunc.RectHeight
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.RectWidth - WindowFunc.DeltaRectWidth) - 3 and \
                y >= WindowFunc.canvas.winfo_height() - (WindowFunc.RectHeight - WindowFunc.DeltaRectHeight) - 3:
            WindowFunc.ReplaceRect[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.RectWidth - 3
            WindowFunc.ReplaceRect[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceRect[0].y1 = WindowFunc.canvas.winfo_height() - 3
            WindowFunc.ReplaceRect[0].y2 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.RectHeight
        elif x <= WindowFunc.DeltaRectWidth + 3:
            WindowFunc.ReplaceRect[0].x1 = 3
            WindowFunc.ReplaceRect[0].x2 = 3 + WindowFunc.RectWidth
            WindowFunc.ReplaceRect[0].y1 = y - WindowFunc.DeltaRectHeight
            WindowFunc.ReplaceRect[0].y2 = y + (WindowFunc.RectHeight - WindowFunc.DeltaRectHeight)
        elif x >= WindowFunc.canvas.winfo_width() - (WindowFunc.RectWidth - WindowFunc.DeltaRectWidth) - 3:
            WindowFunc.ReplaceRect[0].x1 = WindowFunc.canvas.winfo_width() - WindowFunc.RectWidth - 3
            WindowFunc.ReplaceRect[0].x2 = WindowFunc.canvas.winfo_width() - 3
            WindowFunc.ReplaceRect[0].y1 = y - WindowFunc.DeltaRectHeight
            WindowFunc.ReplaceRect[0].y2 = y + (WindowFunc.RectHeight - WindowFunc.DeltaRectHeight)
        elif y <= WindowFunc.DeltaRectHeight + 3:
            WindowFunc.ReplaceRect[0].x1 = x - WindowFunc.DeltaRectWidth
            WindowFunc.ReplaceRect[0].x2 = x + (WindowFunc.RectWidth - WindowFunc.DeltaRectWidth)
            WindowFunc.ReplaceRect[0].y1 = 3
            WindowFunc.ReplaceRect[0].y2 = 3 + WindowFunc.RectHeight
        elif y >= WindowFunc.canvas.winfo_height() - (WindowFunc.RectHeight - WindowFunc.DeltaRectHeight) - 3:
            WindowFunc.ReplaceRect[0].x1 = x - WindowFunc.DeltaRectWidth
            WindowFunc.ReplaceRect[0].x2 = x + (WindowFunc.RectWidth - WindowFunc.DeltaRectWidth)
            WindowFunc.ReplaceRect[0].y1 = WindowFunc.canvas.winfo_height() - 3
            WindowFunc.ReplaceRect[0].y2 = WindowFunc.canvas.winfo_height() - 3 - WindowFunc.RectHeight
        else:
            WindowFunc.ReplaceRect[0].x1 = x - WindowFunc.DeltaRectWidth
            WindowFunc.ReplaceRect[0].x2 = WindowFunc.ReplaceRect[0].x1 + WindowFunc.RectWidth
            WindowFunc.ReplaceRect[0].y1 = y - WindowFunc.DeltaRectHeight
            WindowFunc.ReplaceRect[0].y2 = WindowFunc.ReplaceRect[0].y1 + WindowFunc.RectHeight

        if WindowFunc.ReplaceRect[0].x2 < WindowFunc.ReplaceRect[0].x1:
            WindowFunc.ReplaceRect[0].x2, WindowFunc.ReplaceRect[0].x1 = WindowFunc.ReplaceRect[0].x1, WindowFunc.ReplaceRect[0].x2
        if WindowFunc.ReplaceRect[0].y2 < WindowFunc.ReplaceRect[0].y1:
            WindowFunc.ReplaceRect[0].y2, WindowFunc.ReplaceRect[0].y1 = WindowFunc.ReplaceRect[0].y1, WindowFunc.ReplaceRect[0].y2

        WindowFunc.ReplaceRect[0].DrawRect(WindowFunc.canvas)

    if WindowFunc.OvalMotionFlag:

        if x <= 3 and y <= 3:
            DrawMotionOval(WindowFunc,WindowFunc.OvalPosSTART[0], WindowFunc.OvalPosSTART[1], 3, 3)
        elif x <= 3 and y >= WindowFunc.canvas.winfo_height() - 3:
            DrawMotionOval(WindowFunc, WindowFunc.OvalPosSTART[0], WindowFunc.OvalPosSTART[1], 3, WindowFunc.canvas.winfo_height() - 3)
        elif x >= WindowFunc.canvas.winfo_width() - 3 and y <= + 3:
            DrawMotionOval(WindowFunc, WindowFunc.OvalPosSTART[0], WindowFunc.OvalPosSTART[1], WindowFunc.canvas.winfo_width() - 3, 3)
        elif x >= WindowFunc.canvas.winfo_width() - 3 and y >= WindowFunc.canvas.winfo_height() - 3:
            DrawMotionOval(WindowFunc, WindowFunc.OvalPosSTART[0], WindowFunc.OvalPosSTART[1],
                           WindowFunc.canvas.winfo_width() - 3, WindowFunc.canvas.winfo_height() - 3)
        elif x <= 3:
            DrawMotionOval(WindowFunc, WindowFunc.OvalPosSTART[0], WindowFunc.OvalPosSTART[1], 3, y)
        elif x >= WindowFunc.canvas.winfo_width() - 3:
            DrawMotionOval(WindowFunc, WindowFunc.OvalPosSTART[0], WindowFunc.OvalPosSTART[1], WindowFunc.canvas.winfo_width() - 3, y)
        elif y <= 3:
            DrawMotionOval(WindowFunc, WindowFunc.OvalPosSTART[0], WindowFunc.OvalPosSTART[1], x, 3)
        elif y >= WindowFunc.canvas.winfo_height() - 3:
            DrawMotionOval(WindowFunc, WindowFunc.OvalPosSTART[0], WindowFunc.OvalPosSTART[1],
                           x, WindowFunc.canvas.winfo_height() - 3)
        else:
            DrawMotionOval(WindowFunc, WindowFunc.OvalPosSTART[0], WindowFunc.OvalPosSTART[1], x, y)

    if WindowFunc.WallMotionFlag:

        WindowFunc.canvas.delete('Line')

        if x <= Parameters.CornerSize + 3 and \
                y <= Parameters.CornerSize + 3:
            DrawMotionWall(WindowFunc, WindowFunc.WallPosSTART[0],
                           WindowFunc.WallPosSTART[1], Parameters.CornerSize + 3,Parameters.CornerSize + 3)
        elif x <= Parameters.CornerSize + 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            DrawMotionWall(WindowFunc, WindowFunc.WallPosSTART[0], WindowFunc.WallPosSTART[1],
                           Parameters.CornerSize + 3, WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3)
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y <= Parameters.CornerSize + 3:
            DrawMotionWall(WindowFunc, WindowFunc.WallPosSTART[0], WindowFunc.WallPosSTART[1],
                           WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3, Parameters.CornerSize + 3)
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            DrawMotionWall(WindowFunc, WindowFunc.WallPosSTART[0], WindowFunc.WallPosSTART[1],
                           WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3,
                           WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3)
        elif x <= Parameters.CornerSize + 3:
            DrawMotionWall(WindowFunc, WindowFunc.WallPosSTART[0], WindowFunc.WallPosSTART[1],
                                          Parameters.CornerSize + 3, y)
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3:
            DrawMotionWall(WindowFunc, WindowFunc.WallPosSTART[0], WindowFunc.WallPosSTART[1],
                                          WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3, y)
        elif y <= Parameters.CornerSize + 3:
            DrawMotionWall(WindowFunc, WindowFunc.WallPosSTART[0], WindowFunc.WallPosSTART[1],
                                          x, Parameters.CornerSize + 3)
        elif y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            DrawMotionWall(WindowFunc, WindowFunc.WallPosSTART[0], WindowFunc.WallPosSTART[1],
                                          x, WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3)
        else:
            DrawMotionWall(WindowFunc, WindowFunc.WallPosSTART[0], WindowFunc.WallPosSTART[1], x, y)

    if WindowFunc.PolyWallMotionFlag:

        WindowFunc.canvas.delete('Line')

        if x <= Parameters.CornerSize + 3 and \
                y <= Parameters.CornerSize + 3:
            DrawMotionWall(WindowFunc, WindowFunc.PolyWallPosSTART[0],
                           WindowFunc.PolyWallPosSTART[1], Parameters.CornerSize + 3,Parameters.CornerSize + 3)
        elif x <= Parameters.CornerSize + 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            DrawMotionWall(WindowFunc, WindowFunc.PolyWallPosSTART[0], WindowFunc.PolyWallPosSTART[1],
                           Parameters.CornerSize + 3, WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3)
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y <= Parameters.CornerSize + 3:
            DrawMotionWall(WindowFunc, WindowFunc.PolyWallPosSTART[0], WindowFunc.PolyWallPosSTART[1],
                           WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3, Parameters.CornerSize + 3)
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3 and \
                y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            DrawMotionWall(WindowFunc, WindowFunc.PolyWallPosSTART[0], WindowFunc.PolyWallPosSTART[1],
                           WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3,
                           WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3)
        elif x <= Parameters.CornerSize + 3:
            DrawMotionWall(WindowFunc, WindowFunc.PolyWallPosSTART[0], WindowFunc.PolyWallPosSTART[1],
                                          Parameters.CornerSize + 3, y)
        elif x >= WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3:
            DrawMotionWall(WindowFunc, WindowFunc.PolyWallPosSTART[0], WindowFunc.PolyWallPosSTART[1],
                                          WindowFunc.canvas.winfo_width() - Parameters.CornerSize - 3, y)
        elif y <= Parameters.CornerSize + 3:
            DrawMotionWall(WindowFunc, WindowFunc.PolyWallPosSTART[0], WindowFunc.PolyWallPosSTART[1],
                                          x, Parameters.CornerSize + 3)
        elif y >= WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3:
            DrawMotionWall(WindowFunc, WindowFunc.PolyWallPosSTART[0], WindowFunc.PolyWallPosSTART[1],
                                          x, WindowFunc.canvas.winfo_height() - Parameters.CornerSize - 3)
        else:
            DrawMotionWall(WindowFunc, WindowFunc.PolyWallPosSTART[0], WindowFunc.PolyWallPosSTART[1], x, y)

    if WindowFunc.RectMotionFlag:

        if x <= 3 and y <= 3:
            DrawMotionRect(WindowFunc, WindowFunc.RectPosSTART[0], WindowFunc.RectPosSTART[1], 3, 3)
        elif x <= 3 and y >= WindowFunc.canvas.winfo_height() - 3:
            DrawMotionRect(WindowFunc, WindowFunc.RectPosSTART[0], WindowFunc.RectPosSTART[1], 3, WindowFunc.canvas.winfo_height() - 3)
        elif x >= WindowFunc.canvas.winfo_width() - 3 and y <= + 3:
            DrawMotionRect(WindowFunc, WindowFunc.RectPosSTART[0], WindowFunc.RectPosSTART[1], WindowFunc.canvas.winfo_width() - 3, 3)
        elif x >= WindowFunc.canvas.winfo_width() - 3 and y >= WindowFunc.canvas.winfo_height() - 3:
            DrawMotionRect(WindowFunc, WindowFunc.RectPosSTART[0], WindowFunc.RectPosSTART[1],
                           WindowFunc.canvas.winfo_width() - 3, WindowFunc.canvas.winfo_height() - 3)
        elif x <= 3:
            DrawMotionRect(WindowFunc, WindowFunc.RectPosSTART[0], WindowFunc.RectPosSTART[1], 3, y)
        elif x >= WindowFunc.canvas.winfo_width() - 3:
            DrawMotionRect(WindowFunc, WindowFunc.RectPosSTART[0], WindowFunc.RectPosSTART[1], WindowFunc.canvas.winfo_width() - 3, y)
        elif y <= 3:
            DrawMotionRect(WindowFunc, WindowFunc.RectPosSTART[0], WindowFunc.RectPosSTART[1], x, 3)
        elif y >= WindowFunc.canvas.winfo_height() - 3:
            DrawMotionRect(WindowFunc, WindowFunc.RectPosSTART[0], WindowFunc.RectPosSTART[1], x, WindowFunc.canvas.winfo_height() - 3)
        else:
            DrawMotionRect(WindowFunc, WindowFunc.RectPosSTART[0], WindowFunc.RectPosSTART[1], x, y)

def MouseWheel(x, y, delta, WindowFunc):

    for oval in WindowFunc.OvalMas:
        if x >= oval.x1 and x <= oval.x2 and y >= oval.y1 and y <= oval.y2:
            WindowFunc.canvas.delete(oval.OvalTag)
            if delta == 120:
                if keyboard.is_pressed('shift') == True and keyboard.is_pressed('alt') == False:
                    if oval.x1 == 3 and oval.y1 == 3:
                        oval.x2 += 1
                    elif oval.x1 == 3 and oval.y2 == WindowFunc.canvas.winfo_height() - 3:
                        oval.x2 += 1
                    elif oval.x2 == WindowFunc.canvas.winfo_width() - 3 and oval.y1 == 3:
                        oval.x1 -= 1
                    elif oval.x2 == WindowFunc.canvas.winfo_width() - 3 and oval.y2 == WindowFunc.canvas.winfo_height() - 3:
                        oval.x1 -= 1
                    elif oval.x1 == 3:
                        oval.x2 += 1
                    elif oval.x2 == WindowFunc.canvas.winfo_width() - 3:
                        oval.x1 -= 1
                    elif oval.y1 == 3:
                        oval.x1 -= 1
                        oval.x2 += 1
                    elif oval.y2 == WindowFunc.canvas.winfo_height() - 3:
                        oval.x1 -= 1
                        oval.x2 += 1
                    else:
                        oval.x1 -= 1
                        oval.x2 += 1
                elif keyboard.is_pressed('alt') == True and keyboard.is_pressed('shift') == False:
                    if oval.x1 == 3 and oval.y1 == 3:
                        oval.y2 += 1
                    elif oval.x1 == 3 and oval.y2 == WindowFunc.canvas.winfo_height() - 3:
                        oval.y1 -= 1
                    elif oval.x2 == WindowFunc.canvas.winfo_width() - 3 and oval.y1 == 3:
                        oval.y2 += 1
                    elif oval.x2 == WindowFunc.canvas.winfo_width() - 3 and oval.y2 == WindowFunc.canvas.winfo_height() - 3:
                        oval.y1 -= 1
                    elif oval.x1 == 3:
                        oval.y1 -= 1
                        oval.y2 += 1
                    elif oval.x2 == WindowFunc.canvas.winfo_width() - 3:
                        oval.y1 -= 1
                        oval.y2 += 1
                    elif oval.y1 == 3:
                        oval.y2 += 1
                    elif oval.y2 == WindowFunc.canvas.winfo_height() - 3:
                        oval.y1 -= 1
                    else:
                        oval.y1 -= 1
                        oval.y2 += 1
                else:
                    if oval.x1 == 3 and oval.y1 == 3:
                        oval.x2 += 1
                        oval.y2 += 1
                    elif oval.x1 == 3 and oval.y2 == WindowFunc.canvas.winfo_height() - 3:
                        oval.x2 += 1
                        oval.y1 -= 1
                    elif oval.x2 == WindowFunc.canvas.winfo_width() - 3 and oval.y1 == 3:
                        oval.x1 -= 1
                        oval.y2 += 1
                    elif oval.x2 == WindowFunc.canvas.winfo_width() - 3 and oval.y2 == WindowFunc.canvas.winfo_height() - 3:
                        oval.x1 -= 1
                        oval.y1 -= 1
                    elif oval.x1 == 3:
                        oval.x2 += 1
                        oval.y1 -= 1
                        oval.y2 += 1
                    elif oval.x2 == WindowFunc.canvas.winfo_width() - 3:
                        oval.x1 -= 1
                        oval.y1 -= 1
                        oval.y2 += 1
                    elif oval.y1 == 3:
                        oval.x1 -= 1
                        oval.x2 += 1
                        oval.y2 += 1
                    elif oval.y2 == WindowFunc.canvas.winfo_height() - 3:
                        oval.x1 -= 1
                        oval.x2 += 1
                        oval.y1 -= 1
                    else:
                        oval.x1 -= 1
                        oval.x2 += 1
                        oval.y1 -= 1
                        oval.y2 += 1
            elif delta == -120:
                if keyboard.is_pressed('shift') == True and keyboard.is_pressed('alt') == False:
                    oval.x1 += 1
                    oval.x2 -= 1
                elif keyboard.is_pressed('alt') == True and keyboard.is_pressed('shift') == False:
                    oval.y1 += 1
                    oval.y2 -= 1
                else:
                    oval.x1 += 1
                    oval.x2 -= 1
                    oval.y1 += 1
                    oval.y2 -= 1
            oval.DrawOval(WindowFunc.canvas)
    for rect in WindowFunc.RectMas:
        if x >= rect.x1 and x <= rect.x2 and y >= rect.y1 and y <= rect.y2:
            WindowFunc.canvas.delete(rect.RectTag)
            if delta == 120:
                if keyboard.is_pressed('shift') == True and keyboard.is_pressed('alt') == False:
                    if rect.x1 == 3 and rect.y1 == 3:
                        rect.x2 += 1
                    elif rect.x1 == 3 and rect.y2 == WindowFunc.canvas.winfo_height() - 3:
                        rect.x2 += 1
                    elif rect.x2 == WindowFunc.canvas.winfo_width() - 3 and rect.y1 == 3:
                        rect.x1 -= 1
                    elif rect.x2 == WindowFunc.canvas.winfo_width() - 3 and rect.y2 == WindowFunc.canvas.winfo_height() - 3:
                        rect.x1 -= 1
                    elif rect.x1 == 3:
                        rect.x2 += 1
                    elif rect.x2 == WindowFunc.canvas.winfo_width() - 3:
                        rect.x1 -= 1
                    elif rect.y1 == 3:
                        rect.x1 -= 1
                        rect.x2 += 1
                    elif rect.y2 == WindowFunc.canvas.winfo_height() - 3:
                        rect.x1 -= 1
                        rect.x2 += 1
                    else:
                        rect.x1 -= 1
                        rect.x2 += 1
                elif keyboard.is_pressed('alt') == True and keyboard.is_pressed('shift') == False:
                    if rect.x1 == 3 and rect.y1 == 3:
                        rect.y2 += 1
                    elif rect.x1 == 3 and rect.y2 == WindowFunc.canvas.winfo_height() - 3:
                        rect.y1 -= 1
                    elif rect.x2 == WindowFunc.canvas.winfo_width() - 3 and rect.y1 == 3:
                        rect.y2 += 1
                    elif rect.x2 == WindowFunc.canvas.winfo_width() - 3 and rect.y2 == WindowFunc.canvas.winfo_height() - 3:
                        rect.y1 -= 1
                    elif rect.x1 == 3:
                        rect.y1 -= 1
                        rect.y2 += 1
                    elif rect.x2 == WindowFunc.canvas.winfo_width() - 3:
                        rect.y1 -= 1
                        rect.y2 += 1
                    elif rect.y1 == 3:
                        rect.y2 += 1
                    elif rect.y2 == WindowFunc.canvas.winfo_height() - 3:
                        rect.y1 -= 1
                    else:
                        rect.y1 -= 1
                        rect.y2 += 1
                else:
                    if rect.x1 == 3 and rect.y1 == 3:
                        rect.x2 += 1
                        rect.y2 += 1
                    elif rect.x1 == 3 and rect.y2 == WindowFunc.canvas.winfo_height() - 3:
                        rect.x2 += 1
                        rect.y1 -= 1
                    elif rect.x2 == WindowFunc.canvas.winfo_width() - 3 and rect.y1 == 3:
                        rect.x1 -= 1
                        rect.y2 += 1
                    elif rect.x2 == WindowFunc.canvas.winfo_width() - 3 and rect.y2 == WindowFunc.canvas.winfo_height() - 3:
                        rect.x1 -= 1
                        rect.y1 -= 1
                    elif rect.x1 == 3:
                        rect.x2 += 1
                        rect.y1 -= 1
                        rect.y2 += 1
                    elif rect.x2 == WindowFunc.canvas.winfo_width() - 3:
                        rect.x1 -= 1
                        rect.y1 -= 1
                        rect.y2 += 1
                    elif rect.y1 == 3:
                        rect.x1 -= 1
                        rect.x2 += 1
                        rect.y2 += 1
                    elif rect.y2 == WindowFunc.canvas.winfo_height() - 3:
                        rect.x1 -= 1
                        rect.x2 += 1
                        rect.y1 -= 1
                    else:
                        rect.x1 -= 1
                        rect.x2 += 1
                        rect.y1 -= 1
                        rect.y2 += 1
            elif delta == -120:
                if keyboard.is_pressed('shift') == True and keyboard.is_pressed('alt') == False:
                    rect.x1 += 1
                    rect.x2 -= 1
                elif keyboard.is_pressed('alt') == True and keyboard.is_pressed('shift') == False:
                    rect.y1 += 1
                    rect.y2 -= 1
                else:
                    rect.x1 += 1
                    rect.x2 -= 1
                    rect.y1 += 1
                    rect.y2 -= 1
            rect.DrawRect(WindowFunc.canvas)