class Beacon:

    def __init__(self, BeaconCoords, Count, BeaconSize, BeaconOutlineWidth, BeaconColor, BeaconOutlineColor):

        self.x = float(BeaconCoords[0])
        self.y = float(BeaconCoords[1])
        self.BeaconSize = BeaconSize
        self.BeaconOutlineWidth = BeaconOutlineWidth
        self.BeaconColor = BeaconColor
        self.BeaconOutlineColor = BeaconOutlineColor
        self.BeaconTag = 'Beacon' + str(Count)

    def DrawBeacon(self, canvas):

        canvas.create_oval(self.x - self.BeaconSize, self.y + self.BeaconSize, self.x + self.BeaconSize, self.y - self.BeaconSize,
                           outline = self.BeaconOutlineColor, width=self.BeaconOutlineWidth, fill=self.BeaconColor, tag=self.BeaconTag)

        canvas.create_oval(self.x - self.BeaconSize, self.y + self.BeaconSize, self.x + self.BeaconSize, self.y - self.BeaconSize,
                           outline = self.BeaconOutlineColor, width=self.BeaconOutlineWidth, fill=self.BeaconColor, tag=self.BeaconTag)