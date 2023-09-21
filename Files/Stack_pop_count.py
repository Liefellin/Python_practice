class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        self.__pops = 0
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def get_counter(self):
        return self.__pops

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        self.__pops += 1
        return val


stek = CountingStack()
for i in range(100):
    stek.push(i)
    stek.pop()
print(stek.get_counter())
