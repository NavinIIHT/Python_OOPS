
class FaultyCalc:
    def __init__(self, x):
        self.x = x
 
    def __add__(self, o):
        return self.x - o.x

    def __sub__(self, o):
        return self.x + o.x

class CorrectCalc:
    def __init__(self, x):
        self.x = x


class MainClass:
    def __init__(self, x):
        self.x = x

if __name__=="__main__":
    ob1 = MainClass(8.4)
    ob2 = MainClass(0)
    print(ob1 + ob2)
    print(ob1 - ob2)
    print(ob1 * ob2)
    print(ob1 / ob2)
