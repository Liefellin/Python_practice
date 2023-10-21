class Fib:
    def __init__(self, end, quo=0, spark=1):
        # print("__init__")
        self.__n = end
        self.__i = 0
        self.__p1 = quo
        self.__p2 = spark

    def __iter__(self):
        # print("__iter__")
        return self

    def __next__(self):
        # print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        r = self.__p1
        self.__p1 = self.__p2
        self.__p2 = self.__p1 +r
        return r
