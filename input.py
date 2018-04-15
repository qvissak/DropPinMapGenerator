from gmplot import gmplot
import csv
import sys

class Point:
    _x = None
    _y = None
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)
    def display(self):
        print('(' + str(self._x) + ', ' + str(self._y) + ')')
    def getX(self):
        return self._x
    def getY(self):
        return self._y

# Read CSV of points, comma separated per row
def readData(fileName):
    arrayOfPoints = []
    with open(fileName, 'r') as f:
        for line in f:
            row = str(line).rstrip('\n').split(',')
            arrayOfPoints.append(Point(row[0], row[1]))
    return arrayOfPoints

# Generate a html file containing a map of drop pins
def generateMap(arrayOfPoints, outputName):
    # Create map centered, zoomed on the United States
    start = Point(37, 263)
    gmap = gmplot.GoogleMapPlotter(start.getX(), start.getY(), 5)
    count = 0
    # Create markers on map, first half being blue
    for point in arrayOfPoints:
        if (count < len(arrayOfPoints) // 2):
            gmap.marker(point.getX(), point.getY(), "cornflowerblue")
        else:
            gmap.marker(point.getX(), point.getY(), "darkorange")
        count += 1
    gmap.draw(outputName + ".html")

def main():
    if len(sys.argv) < 3:
        raise Exception("Usage: python3 ./input.py <file-name.csv> <output-file-name>")
    fileName = sys.argv[1]
    outputName = sys.argv[2]
    arrayOfPoints = readData(fileName)
    generateMap(arrayOfPoints, outputName)

if __name__ == "__main__":
    main()
