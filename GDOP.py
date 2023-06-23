import numpy as np
from numba import prange
import time
import  CROSS as Cross
import math


class Gdop:
    def __init__(self, canvas, BeaconMas, OvalMas, WallMas, RectMas):

        start_time = time.monotonic()

        canvas.delete('all')

        self.BeaconMas = BeaconMas
        self.OvalMas = OvalMas
        self.WallMas = WallMas
        self.RectMas = RectMas

        self.GDOPmas = np.zeros((canvas.winfo_width(), canvas.winfo_height()))
        self.VisionBeaconPos = []

        self.CrossCheckGDOP(canvas)

        print('Расчеты: ' + str(time.monotonic() - start_time))
        CalculationTime = time.monotonic()
        self.DrawGDOP(canvas)


        print('Рисование: ' + str(time.monotonic() - CalculationTime))
        print('Всего: ' + str(time.monotonic() - start_time))

    def CrossCheckGDOP(self, canvas):

        for i in prange(canvas.winfo_width()):
            if i % 2 == 0:
                for j in prange(canvas.winfo_height()):
                    if j % 2 == 0:

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
                                self.VisionBeaconPos.append(self.BeaconMas[l])

                        self.GDOPcalculation(i, j)
                        self.VisionBeaconPos = []

    def GDOPcalculation(self, x, y):
        InsideBeaconFlag = False
        for k in prange(len(self.VisionBeaconPos)):
            if x == self.VisionBeaconPos[k].x and y == self.VisionBeaconPos[k].y:
                InsideBeaconFlag = True
        if InsideBeaconFlag or len(self.VisionBeaconPos) == 0 or len(self.VisionBeaconPos) == 1:
            self.GDOPmas[x][y] = 0
        else:
            H = np.zeros((len(self.VisionBeaconPos), 2))

            for i in prange(len(self.VisionBeaconPos)):
                H[i][0] = (x - self.VisionBeaconPos[i].x) / math.sqrt(pow(x - self.VisionBeaconPos[i].x, 2) + pow(y - self.VisionBeaconPos[i].y, 2))
                H[i][1] = (y - self.VisionBeaconPos[i].y) / math.sqrt(pow(x - self.VisionBeaconPos[i].x, 2) + pow(y - self.VisionBeaconPos[i].y, 2))
                if isinstance(H[i][0], complex):
                    H[i][0] = int(H[i][0].real)
                if isinstance(H[i][1], complex):
                    H[i][1] = int(H[i][1].real)

            HT = np.transpose(H)
            Hmulti = HT.dot(H)
            if np.linalg.det(Hmulti) == 0:
                self.GDOPmas[x][y] = 0
            else:
                Hinv = np.linalg.inv(Hmulti)
                SumCenterMatrix = pow(Hinv[0][0], 2) + pow(Hinv[1][1], 2)

                self.GDOPmas[x][y] = math.sqrt(SumCenterMatrix)

    def DrawGDOP(self, canvas):
        for i in prange(canvas.winfo_width()):
            if i % 2 == 0:
                for j in prange(canvas.winfo_height()):
                    if j % 2 == 0:

                        """ПОСТРОЕНИЕ ГРАДИЕНТА"""
                        """ПЛОХАЯ ВИДИМОСТЬ - КРАСНЫЙ ЦВЕТ В RGB R=255
                           СРЕДНЯЯ ВИДИМОСТЬ - ЖЕЛТЫЙ ЦВЕТ В RGB R=255, G=255
                           ХОРОШАЯ ВИДИМОСТЬ - ЗЕЛЕНЫЙ ЦВЕТ В RGB G=255"""
                        """ЗДЕСЬ ИСПОЛЬЗУЕТСЯ 240 ВМЕСТО 255, Т.К. УДОБНО ИСПОЛЬЗОВАТЬ ДЛЯ ДИАПОЗОН (ОТ 0.1 ДО 12)"""
                        """ДИАПОЗОН ПОДЕЛЕН НА 2 УЧАТСКА (ДО СЕРЕДИНЫ (ОТ ЗЕЛЕНОГО ДО ЖЕЛТОГО) И ПОСЛЕ СЕРЕДИНЫ (ОТ ЖЕЛТОГО ДО КРАСНОГО)"""
                        """УМНОЖЕНИЕ НА 40 НУЖНО ДЛЯ RGB ПРИВОДА (6*40=240)
                           УМНОЖЕНИЕ НА 2 ДЛЯ РАЗДЕЛЕНИЯ ДО СЕРЕДИНЫ И ПОСЛЕ"""
                        """В УСЛОВИИ > 3 ЗЕЛЕНЫЙ ЦВЕТ РАСТЕТ С УМЕНЬШЕНИЕМ GDOP
                           В УСЛОВИИ <= 3 КРАСНЫЙ ЦВЕТ УМЕНЬШАЕТСЯ С УМЕНЬШЕНИЕМ GDOP"""

                        if self.GDOPmas[i][j] < 0.1:
                            GDOPcolor = '#%02x%02x%02x' % (240, 0, 0)
                        elif self.GDOPmas[i][j] > 6:
                            GDOPcolor = '#%02x%02x%02x' % (240, 0, 0)
                        elif self.GDOPmas[i][j] > 3:
                            GDOPcolor = '#%02x%02x%02x' % (240, int(math.fabs((self.GDOPmas[i][j] * 40 - 240) * 2)), 0)
                        else:
                            GDOPcolor = '#%02x%02x%02x' % (int(math.fabs(120 + self.GDOPmas[i][j] * 40)), 240, 0)

                        canvas.create_rectangle(i, j, i, j, outline=GDOPcolor)

        for i in prange(len(self.BeaconMas)):
            self.BeaconMas[i].DrawBeacon(canvas)
        for i in prange(len(self.WallMas)):
            self.WallMas[i].DrawWall(canvas)
        for i in prange(len(self.OvalMas)):
            self.OvalMas[i].DrawOval(canvas)
        for i in prange(len(self.RectMas)):
            self.RectMas[i].DrawRect(canvas)
        canvas.update()


