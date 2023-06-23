import PARAMETERS as Parameters
import  CROSS as Cross
import time
from numba import prange
import  numpy as np

class Coverage:
    def __init__(self, canvas, BeaconMas, OvalMas, WallMas,RectMas):

        start_time = time.monotonic()

        canvas.delete('all')

        self.CountVisibleBeaconsMas = np.zeros((canvas.winfo_width(), canvas.winfo_height()))

        self.BeaconMas = BeaconMas
        self.OvalMas = OvalMas
        self.WallMas = WallMas
        self.RectMas = RectMas

        self.CheckCross(canvas)

        print('Расчеты: ' + str(time.monotonic() - start_time))

        CalculationTime = time.monotonic()

        self.DrawCoverage(canvas)

        print('Рисование: ' + str(time.monotonic() - CalculationTime))
        print('Всего: ' + str(time.monotonic() - start_time))

    def CheckCross(self, canvas):

        for i in prange(canvas.winfo_width()):
            if i % 2 == 0:
                for j in prange(canvas.winfo_height()):
                    if j % 2 == 0:

                        CountVisibleBeacons = 0
                        for l in prange(len(self.BeaconMas)):
                            CrossFlag = False
                            if len(self.WallMas) != 0:
                                for k in prange(len(self.WallMas)):
                                    if Cross.LineCross(i, self.BeaconMas[l].x, j, self.BeaconMas[l].y,
                                                       self.WallMas[k].x1, self.WallMas[k].x2, self.WallMas[k].y1, self.WallMas[k].y2):
                                        CrossFlag = True
                                        break
                            if not CrossFlag:
                                if len(self.RectMas) != 0:
                                    for k in prange(len(self.RectMas)):
                                        if Cross.LineCross(i, self.BeaconMas[l].x, j, self.BeaconMas[l].y,
                                                           self.RectMas[k].x1, self.RectMas[k].x2, self.RectMas[k].y1, self.RectMas[k].y1) or \
                                                Cross.LineCross(i, self.BeaconMas[l].x, j, self.BeaconMas[l].y,
                                                                self.RectMas[k].x2, self.RectMas[k].x2, self.RectMas[k].y1, self.RectMas[k].y2) or \
                                                Cross.LineCross(i, self.BeaconMas[l].x, j, self.BeaconMas[l].y,
                                                                self.RectMas[k].x2, self.RectMas[k].x1, self.RectMas[k].y2, self.RectMas[k].y2) or \
                                                Cross.LineCross(i, self.BeaconMas[l].x, j, self.BeaconMas[l].y,
                                                                self.RectMas[k].x1, self.RectMas[k].x1, self.RectMas[k].y2, self.RectMas[k].y1):
                                            CrossFlag = True
                                            break
                            if not CrossFlag:
                                if len(self.OvalMas) != 0:
                                    for k in prange(len(self.OvalMas)):
                                        if Cross.OvalCross(i, self.BeaconMas[l].x, j, self.BeaconMas[l].y,
                                                           self.OvalMas[k].x1, self.OvalMas[k].x2, self.OvalMas[k].y1, self.OvalMas[k].y2):
                                            CrossFlag = True
                                            break
                            if not CrossFlag:
                                CountVisibleBeacons += 1

                        self.CountVisibleBeaconsMas[i][j] = CountVisibleBeacons

    def DrawCoverage(self, canvas):
        for i in prange(canvas.winfo_width()):
            if i % 2 == 0:
                for j in prange(canvas.winfo_height()):
                    if j % 2 == 0:
                        # if self.CountVisibleBeaconsMas[i][j] == 0:
                        #     canvas.create_rectangle(i - 1, j - 1, i + 1, j + 1, outline=Parameters.VisibleBeaconColor0, tag='Cover')
                        # elif self.CountVisibleBeaconsMas[i][j] == 1:
                        #     canvas.create_rectangle(i - 1, j - 1, i + 1, j + 1, outline=Parameters.VisibleBeaconColor1, tag='Cover')
                        # elif self.CountVisibleBeaconsMas[i][j] == 2:
                        #     canvas.create_rectangle(i - 1, j - 1, i + 1, j + 1, outline=Parameters.VisibleBeaconColor2, tag='Cover')
                        # elif self.CountVisibleBeaconsMas[i][j] == 3:
                        #     canvas.create_rectangle(i - 1, j - 1, i + 1, j + 1, outline=Parameters.VisibleBeaconColor3, tag='Cover')
                        # elif self.CountVisibleBeaconsMas[i][j] >= 4:
                        #     canvas.create_rectangle(i - 1, j - 1, i + 1, j + 1, outline=Parameters.VisibleBeaconColor4andMore, tag='Cover')

                        if self.CountVisibleBeaconsMas[i][j] == 0:
                            canvas.create_rectangle(i, j, i, j, outline=Parameters.VisibleBeaconColor0, tag='Cover')
                        elif self.CountVisibleBeaconsMas[i][j] == 1:
                            canvas.create_rectangle(i, j, i, j, outline=Parameters.VisibleBeaconColor1, tag='Cover')
                        elif self.CountVisibleBeaconsMas[i][j] == 2:
                            canvas.create_rectangle(i, j, i, j, outline=Parameters.VisibleBeaconColor2, tag='Cover')
                        elif self.CountVisibleBeaconsMas[i][j] == 3:
                            canvas.create_rectangle(i, j, i, j, outline=Parameters.VisibleBeaconColor3, tag='Cover')
                        elif self.CountVisibleBeaconsMas[i][j] >= 4:
                            canvas.create_rectangle(i, j, i, j, outline=Parameters.VisibleBeaconColor4andMore, tag='Cover')
        for i in prange(len(self.BeaconMas)):
            self.BeaconMas[i].DrawBeacon(canvas)
        for i in prange(len(self.WallMas)):
            self.WallMas[i].DrawWall(canvas)
        for i in prange(len(self.OvalMas)):
            self.OvalMas[i].DrawOval(canvas)
        for i in prange(len(self.RectMas)):
            self.RectMas[i].DrawRect(canvas)
        canvas.update()