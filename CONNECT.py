import PARAMETERS as Parameters
import  CROSS as Cross
import time
from numba import prange


def Connect(canvas, BeaconMas, OvalMas, WallMas, RectMas):

    VisionBeacons = []
    NoVisionBeacons = []

    canvas.delete('Connect')

    for i in prange(len(BeaconMas)):
        for j in prange(len(BeaconMas)):
            CrossFlag = False
            if j > i:
                for k in prange(len(WallMas)):
                    if Cross.LineCross(BeaconMas[i].x, BeaconMas[j].x, BeaconMas[i].y, BeaconMas[j].y,
                                       WallMas[k].x1, WallMas[k].x2, WallMas[k].y1, WallMas[k].y2):
                        CrossFlag = True
                        break
                if not CrossFlag:
                    for k in prange(len(RectMas)):
                        if Cross.LineCross(BeaconMas[i].x, BeaconMas[j].x, BeaconMas[i].y, BeaconMas[j].y,
                                           RectMas[k].x1, RectMas[k].x2, RectMas[k].y1, RectMas[k].y1) or \
                                Cross.LineCross(BeaconMas[i].x, BeaconMas[j].x, BeaconMas[i].y, BeaconMas[j].y,
                                                RectMas[k].x2, RectMas[k].x2, RectMas[k].y1, RectMas[k].y2) or \
                                Cross.LineCross(BeaconMas[i].x, BeaconMas[j].x, BeaconMas[i].y, BeaconMas[j].y,
                                                RectMas[k].x2, RectMas[k].x1, RectMas[k].y2, RectMas[k].y2) or \
                                Cross.LineCross(BeaconMas[i].x, BeaconMas[j].x, BeaconMas[i].y, BeaconMas[j].y,
                                                RectMas[k].x1, RectMas[k].x1, RectMas[k].y2, RectMas[k].y1):
                            CrossFlag = True
                            break
                if not CrossFlag:
                    for k in prange(len(OvalMas)):
                        if Cross.OvalCross(BeaconMas[i].x, BeaconMas[j].x, BeaconMas[i].y, BeaconMas[j].y,
                                           OvalMas[k].x1, OvalMas[k].x2, OvalMas[k].y1, OvalMas[k].y2):
                            CrossFlag = True
                            break
                if CrossFlag:
                    NoVisionBeacons.append(BeaconMas[j])
                elif not CrossFlag:
                    VisionBeacons.append(BeaconMas[j])

        ConnectDraw(i, canvas, BeaconMas, VisionBeacons, NoVisionBeacons)

        VisionBeacons.clear()
        NoVisionBeacons.clear()

def ConnectDraw(i, canvas, BeaconMas, VisionBeacons, NoVisionBeacons):

    for j in prange(len(NoVisionBeacons)):
        canvas.create_line(NoVisionBeacons[j].x, NoVisionBeacons[j].y, BeaconMas[i].x, BeaconMas[i].y,
                           fill='green', width=Parameters.FlashConnectWidth, tag='ConnectFlash')
        canvas.update()
        time.sleep(Parameters.ConnectPause)
        canvas.create_line(NoVisionBeacons[j].x, NoVisionBeacons[j].y, BeaconMas[i].x, BeaconMas[i].y,
                           fill='yellow', width=Parameters.FlashConnectWidth, tag='ConnectFlash')
        canvas.update()
        time.sleep(Parameters.ConnectPause)
        canvas.create_line(NoVisionBeacons[j].x, NoVisionBeacons[j].y, BeaconMas[i].x, BeaconMas[i].y,
                           fill='orange', width=Parameters.FlashConnectWidth, tag='ConnectFlash')
        canvas.update()
        time.sleep(Parameters.ConnectPause)
        canvas.delete('ConnectFlash')
        canvas.create_line(NoVisionBeacons[j].x, NoVisionBeacons[j].y, BeaconMas[i].x, BeaconMas[i].y,
                           fill='red', width=Parameters.NoConnectWidth, tag='Connect')
        canvas.update()
        time.sleep(Parameters.ConnectPause)

    for j in prange(len(VisionBeacons)):

        canvas.create_line(VisionBeacons[j].x, VisionBeacons[j].y, BeaconMas[i].x, BeaconMas[i].y,
                           fill='green', width=Parameters.ConnectWidth, tag='Connect')
        canvas.update()
        time.sleep(Parameters.ConnectPause)
