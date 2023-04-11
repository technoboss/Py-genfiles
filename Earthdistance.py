class distbtw2points:
    # Radius of earth in kilometers. Use 3956 for miles
    radius = 6371

    def __init__(self, lat1, lat2, lon1, lon2):
        from math import radians
        # Converts degrees to radians
        self.lat1 = radians(lat1)
        self.lat2 = radians(lat2)
        self.lon1 = radians(lon1)
        self.lon2 = radians(lon2)

    def disLon(self):
        difLon = self.lon2 - self.lon1
        return difLon

    def disLat(self):
        difLat = self.lat2 - self.lat1
        return difLat

    def havFormula(self):  # Haversine formula to compute the distance
        from math import cos, sin, asin, sqrt
        a = sin(self.disLat() / 2) ** 2 + cos(self.lat1) * cos(self.lat2) * sin(self.disLon() / 2) ** 2
        c = 2 * asin(sqrt(a))
        return c

    @classmethod  # Class method to call the radius
    def earthRadius(cls):
        return cls.radius

    def earthDist(self):  # Final step to calculate the distance between the 2 points
        result = self.havFormula() * distbtw2points.earthRadius()
        return result


def doSomeComputation():  # Collect some inputs, compute the distance and display the result
    computeDist1 = distbtw2points(float(input('Lat1: ')), float(input('Lat2: ')), float(input('Lon1: ')),
                                  float(input('Lon2: ')))
    print('---------------------------------------------------------------')
    distance = print(f'The distance between the 2 points is: {computeDist1.earthDist()} KM')
    print('---------------------------------------------------------------')
    return distance


doSomeComputation()

# lat1 = 53.32055555555556
# lat2 = 53.31861111111111
# lon1 = -1.7297222222222221
# lon2 = -1.6997222222222223