from operators import *

def without(nls, *arg):
    ls = nls.copy()
    for i in arg:
        ls.remove(i)
    return ls


class Point24:
    def __init__(self, ls):
        self.nls = ls
        self.opls = [Add(), Sub(), Mul(), Div(), Pow(), Root()]
        self.startTrying()

    def startTrying(self):
        shuffles = [[a, b, c, d]
                    for a in self.nls
                    for b in without(self.nls, a)
                    for c in without(self.nls, a, b)
                    for d in without(self.nls, a, b, c)]
        for nls in shuffles:
            for i in self.opls:
                for j in self.opls:
                    for k in self.opls:
                        {
                            k(j(i(nls[0], nls[1]), nls[2]), nls[3]): lambda: print(f"(({nls[0]} {i} {nls[1]}) {j} {nls[2]}) {k} {nls[3]}"),
                            j(i(nls[0], nls[1]), k(nls[2], nls[3])): lambda: print(f"({nls[0]} {i} {nls[1]}) {j} ({nls[2]} {k} {nls[3]})"),
                            k(i(nls[0], j(nls[1], nls[2])), nls[3]): lambda: print(f"({nls[0]} {i} ({nls[1]} {j} {nls[2]})) {k} {nls[3]}"),
                            i(nls[0], k(j(nls[1], nls[2]), nls[3])): lambda: print(f"{nls[0]} {i} (({nls[1]} {j} {nls[2]}) {k} {nls[3]})"),
                            i(nls[0], j(nls[1], k(nls[2], nls[3]))): lambda: print(f"{nls[0]} {i} ({nls[1]} {j} ({nls[2]} {k} {nls[3]}))"),
                        }.get(24, lambda: None)()


if __name__ == "__main__":
    point24 = Point24([int(i) for i in input("Enter 4 number:\n").split() if i.isdigit()])
