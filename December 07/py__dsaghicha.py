import math


class Main:
    def __init__(self) -> None:
        pass


    def rectangleInCircle(self, rectWidth: int, rectHeight: int, radius: int) -> bool:
        diagonal = math.sqrt((rectWidth ** 2) + (rectHeight ** 2))
        return diagonal <= (radius * 2)

if __name__== '__main__':
    main = Main()
    res = main.rectangleInCircle(8, 6, 5)
    # res = main.rectangleInCircle(5, 9, 5)
    print(res)