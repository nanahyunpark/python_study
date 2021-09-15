class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __str__(self):
        return "(" + str(round(self.x, 1)) + ', ' + str(round(self.y, 1)) + ")"

class Triangle:
    def __init__(self, points):
        self.points = points
    
    def get_centroid(self):
        sum_x = 0
        for point in self.points:
            sum_x += point.x
        sum_y = 0
        for point in self.points:
            sum_y += point.y
        return Point(sum_x/3, sum_y/3)

def main():
    info = input().split()
    point1 = Point(x=info[0], y=info[1])
    point2 = Point(x=info[2], y=info[3])
    point3 = Point(x=info[4], y=info[5])
    triangle1 = Triangle([point1, point2, point3])
    centroid1 = triangle1.get_centroid()
    print(centroid1)

if(__name__ == '__main__'):
    main()
