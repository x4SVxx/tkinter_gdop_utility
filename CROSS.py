import math
from numba import njit


@njit(fastmath=True)
def LineCross(ConnectX1, ConnectX2, ConnectY1, ConnectY2, WallX1, WallX2, WallY1, WallY2):

    v1 = (WallX2 - WallX1) * (ConnectY1 - WallY1) - (WallY2 - WallY1) * (ConnectX1 - WallX1)
    v2 = (WallX2 - WallX1) * (ConnectY2 - WallY1) - (WallY2 - WallY1) * (ConnectX2 - WallX1)
    v3 = (ConnectX2 - ConnectX1) * (WallY1 - ConnectY1) - (ConnectY2 - ConnectY1) * (WallX1 - ConnectX1)
    v4 = (ConnectX2 - ConnectX1) * (WallY2 - ConnectY1) - (ConnectY2 - ConnectY1) * (WallX2 - ConnectX1)

    if v1 * v2 <= 0 and v3 * v4 <= 0:
        return  True
    else:
        return  False

@njit(fastmath=True)
def OvalCross(ConnectX1, ConnectX2, ConnectY1, ConnectY2, OvalX1, OvalX2, OvalY1, OvalY2):

    OvalX0 = (OvalX2 + OvalX1) / 2
    OvalY0 = (OvalY2 + OvalY1) / 2
    OvalA = (OvalX2 - OvalX1) / 2
    OvalB = (OvalY2 - OvalY1) / 2

    PointCenterX1 = ConnectX1 - OvalX0
    PointCenterX2 = ConnectX2 - OvalX0
    PointCenterY1 = ConnectY1 - OvalY0
    PointCenterY2 = ConnectY2 - OvalY0

    if pow(OvalA, 2) != 0 and pow(OvalB, 2) != 0:

        A = pow(PointCenterX2 - PointCenterX1, 2) / pow(OvalA, 2) + \
            pow(PointCenterY2 - PointCenterY1, 2) / pow(OvalB, 2)
        B = (2 * PointCenterX1 * (PointCenterX2 - PointCenterX1)) / pow(OvalA, 2) + \
            (2 * PointCenterY1 * (PointCenterY2 - PointCenterY1)) / pow(OvalB, 2)
        C = pow(PointCenterX1, 2) / pow(OvalA, 2) + \
            pow(PointCenterY1, 2) / pow(OvalB, 2) - 1

        if A != 0:
            D = pow(B, 2) - 4 * A * C
            if D > 0:
                k1 = (-B + math.sqrt(D)) / (2 * A)
                k2 = (-B - math.sqrt(D)) / (2 * A)
                if k1 >= 0 and k1 <=1 or k2 >= 0 and k2 <= 1:
                    return True
                else:
                    return False
            if D == 0:
                k = -B / (2 * A)
                if k >= 0 and k <= 1:
                    return  True
                else:
                    return  False
            else:
                return False
        else:
            return True
    else:
        return False
