class Wall:

    def __init__(self, WallCoordsSTART, WallCoordsFINISH, Count, WallWidth, WallColor, CornerSize, PolyWallCheck):

        self.x1 = float(WallCoordsSTART[0])
        self.y1 = float(WallCoordsSTART[1])
        self.x2 = float(WallCoordsFINISH[0])
        self.y2 = float(WallCoordsFINISH[1])
        self.WallWidth = WallWidth
        self.WallColor = WallColor
        self.CornerSize = CornerSize
        self.WallTag = 'Wall' + str(Count)
        self.CornerTag1 = 'Corner' + '1' + str(Count)
        self.CornerTag2 = 'Corner' + '2' + str(Count)
        self.PolyWallCheck = PolyWallCheck

    def DrawWall(self, canvas):

        canvas.create_line(self.x1, self.y1, self.x2, self.y2,
                           width=self.WallWidth, fill=self.WallColor, tag=self.WallTag)
        canvas.create_rectangle(self.x1 - self.CornerSize, self.y1 - self.CornerSize,self.x1 + self.CornerSize, self.y1 + self.CornerSize,
                                outline=self.WallColor, tag=self.CornerTag1)
        canvas.create_rectangle(self.x2 - self.CornerSize, self.y2 - self.CornerSize,self.x2 + self.CornerSize, self.y2 + self.CornerSize,
                                outline=self.WallColor, tag=self.CornerTag2)