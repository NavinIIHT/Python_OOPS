from abc import ABC, abstractmethod

class Operations(ABC):
    '''Operations'''
    @abstractmethod
    def operation():
        pass

class Add(Operations):

    def operation(x, y):
        return x+y 

class Sub():
    pass

class Mul():
    pass

class Div():
    pass

class Mod():
    pass

class Main:
    
    def get_operations(self, x, y):
        results = list()
        for operation in Operations.__subclasses__():
            results.append(operation.operation(x, y))
        return results


if __name__ == "__main__":
    pass