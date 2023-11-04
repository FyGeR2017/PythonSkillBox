class DoubleElement:
    def __init__(self, *lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst) - 1:
            res = self.lst[self.i], self.lst[self.i + 1]
            self.i += 2
            return res
        elif self.i < len(self.lst):
            res = self.lst[self.i], None
            self.i += 1
            return res
        else:
            raise StopIteration

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)

for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)

for pair in dL:
    print(pair)
