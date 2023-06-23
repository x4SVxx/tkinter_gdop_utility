class Oval:

    def __init__(self, OvalCoordsSTART, OvalCoordsFINISH, Count, OvalWidth, OvalColor):

        self.x1 = float(OvalCoordsSTART[0])
        self.y1 = float(OvalCoordsSTART[1])
        self.x2 = float(OvalCoordsFINISH[0])
        self.y2 = float(OvalCoordsFINISH[1])
        self.OvalWidth = OvalWidth
        self.OvalColor = OvalColor
        self.OvalTag = 'Oval' + str(Count)

    def DrawOval(self, canvas):

        if self.x2 - self.x1 > 2 * self.OvalWidth and self.y2 - self.y1 > 2 * self.OvalWidth:
            canvas.create_oval(self.x1 + self.OvalWidth / 2, self.y1 + self.OvalWidth / 2,
                               self.x2 - self.OvalWidth / 2, self.y2 - self.OvalWidth / 2,
                               width=self.OvalWidth, tag=self.OvalTag, outline=self.OvalColor)
        else:
            canvas.create_oval(self.x1, self.y1, self.x2, self.y2, tag=self.OvalTag, fill=self.OvalColor)