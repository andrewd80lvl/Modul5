class Point:
    MIN_X = 0
    MIN_Y = 0
    MAX_X = 1920
    MAX_Y = 1080

    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0

        self.set_coord(x, y)

    def set_coord(self, x, y):
        if not self.validate_coord(x, y):
            raise ValueError('Точка задана вне границ:' + str(self.MAX_X) + ',' + str(self.MAX_Y))

        self.__x = x
        self.__y = y

    def get_coord(self):
        return self.__x, self.__y

    def __add__(self, other):
        if not isinstance(other, Point):
            raise ValueError('Скаладывать между собой можно только классы Point')

        x = self.__x + other.__x
        y = self.__y + other.__y

        if not self.validate_coord(x, y):
            raise ValueError('Точка задана вне границ:' + str(self.MAX_X) + ',' + str(self.MAX_Y))

        return Point(x, y)

    @classmethod
    def validate_coord(cls, x, y):
        if not ((isinstance(x, int) and isinstance(y, int))):
            return False
        else:
            return cls.MIN_X <= x <= cls.MAX_X and cls.MIN_Y <= y <= cls.MAX_X


pt1 = Point(20, 40)
print(pt1.get_coord())
pt2 = Point(60, 60)
print(pt2.get_coord())

pt3 = Point()
pt3 = pt1 + pt2
print(pt3.get_coord())

pt4 = Point(1920, 1080)
pt3 = pt3 + pt4
print(pt3.get_coord())

Traceback (most recent call last):
  File "C:\Users\Andrey.Dolgirev\Documents\project\project\modul_5\modul5_part1_level2.py", line 53, in <module>
    pt3 = pt3 + pt4
  File "C:\Users\Andrey.Dolgirev\Documents\project\project\modul_5\modul5_part1_level2.py", line 31, in __add__
    raise ValueError('Точка задана вне границ:' + str(self.MAX_X) + ',' + str(self.MAX_Y))
ValueError: Точка задана вне границ:1920,1080
(20, 40)
(60, 60)
(80, 100)
