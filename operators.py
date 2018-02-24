Nan = 100

class Add:
    def __call__(self, arg1, arg2):
        return arg1 + arg2
    def __str__(self):
        return '+'

class Sub:
    def __call__(self, arg1, arg2):
        return arg1 - arg2
    def __str__(self):
        return '-'

class Mul:
    def __call__(self, arg1, arg2):
        return arg1 * arg2
    def __str__(self):
        return '*'

class Div:
    def __call__(self, arg1, arg2):
        try:
            return arg1 / arg2
        except:
            return Nan
    def __str__(self):
        return '/'

class Pow:
    def __call__(self, arg1, arg2):
        try:
            if arg2 < 10 and arg2 > -10:
                return pow(arg1, arg2)
            else:
                return Nan
        except:
            return Nan
    def __str__(self):
        return '**'

class Root:
    def __call__(self, arg1, arg2):
        try:
            if arg2 > 10 and arg2 < -10:
                return pow(arg1, 1/arg2)
            else:
                return Nan
        except:
            return Nan
    def __str__(self):
        return '√'
