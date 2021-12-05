from abc import abstractmethod

import numpy as np


class Function:
    def __init__(self):
        self.x = []
        self.y = []
        self.step = 0.001
        self.x_min = -10
        self.x_max = 10

    def set_x_range(self, x_min, x_max):
        self.x_min = x_min
        self.x_max = x_max

    def set_step(self, step):
        self.step = step

    @abstractmethod
    def calc(self, x_point):
        pass

    @abstractmethod
    def formula(self):
        pass

    @abstractmethod
    def calc_roots(self):
        pass

    def evaluate(self):
        self.x = list(np.arange(self.x_min, self.x_max, self.step))
        self.y = [self.calc(x_point) for x_point in self.x]


class Quadratic(Function):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.type = 'quadratic'

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b and self.c and other.c:
            return True
        return False

    def formula(self):
        return f'f(x) = {self.a}*x^2 + {self.b}*x + {self.c}'

    def calc(self, x_point):
        return self.a * x_point**2 + self.b * x_point + self.c

    def calc_roots(self):
        delta = self.b**2 - 4*self.a*self.c
        if delta > 0:
            return round((-self.b - pow(delta, 0.5))/(2*self.a), 3), round((-self.b + pow(delta, 0.5))/(2*self.a), 3)
        if delta == 0:
            return round(-self.b/(2*self.a), 3)
        return 'no roots'

    @classmethod
    def create_function(cls, **kwargs):
        if kwargs['a']:
            a = float(kwargs['a'])
            b = float(kwargs['b'])
            c = float(kwargs['c'])
            return Quadratic(a, b, c)
        raise ValueError('You should pass 3 floats')


class Linear(Function):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.type = 'linear'

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return False

    def formula(self):
        return f'f(x) = {self.a}*x + {self.b}'

    def calc(self, x_point):
        return self.a * x_point + self.b

    def calc_roots(self):
        return round(-self.b/self.a, 3)

    @classmethod
    def create_function(cls, **kwargs):
        if kwargs['a']:
            a = int(kwargs['a'])
            b = int(kwargs['b'])
            return Linear(a, b)
        raise ValueError('You should pass 2 floats')


class Constant(Function):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.type = 'constant'

    def __eq__(self, other):
        if self.a == other.a:
            return True
        return False

    def formula(self):
        return f'f(x) = {self.a}'

    def calc(self, x_point):
        return self.a

    def calc_roots(self):
        if self.a == 0:
            return 'all'
        return 'no roots'

    @classmethod
    def create_function(cls, **kwargs):
        return Constant(kwargs['a'])
