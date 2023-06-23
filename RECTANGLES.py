class Rect:

    def __init__(self, RectCoordsSTART, RectCoordsFINISH, Count, RectWidth, RectColor):

        self.x1 = float(RectCoordsSTART[0])
        self.y1 = float(RectCoordsSTART[1])
        self.x2 = float(RectCoordsFINISH[0])
        self.y2 = float(RectCoordsFINISH[1])
        self.RectWidth = RectWidth
        self.RectColor = RectColor
        self.RectTag = 'Rect' + str(Count)

    def DrawRect(self, canvas):

        if self.x2 - self.x1 > 2 * self.RectWidth and self.y2 - self.y1 > 2 * self.RectWidth:
            canvas.create_rectangle(self.x1 + self.RectWidth / 2, self.y1 + self.RectWidth / 2,
                                    self.x2 - self.RectWidth / 2, self.y2 - self.RectWidth / 2,
                               width=self.RectWidth, tag=self.RectTag, outline=self.RectColor)
        else:
            canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, tag=self.RectTag, fill=self.RectColor)