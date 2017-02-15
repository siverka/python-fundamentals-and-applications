class multifilter:
    def judge_half(pos, neg):
        return pos >= neg


    def judge_any(pos, neg):
        return pos > 0


    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *func, judge=judge_any):
        self.iterable = iterable
        self.functions = func
        self.judge = judge

    def __iter__(self):
        for x in self.iterable:
            res = [f(x) for f in self.functions]
            if self.judge(res.count(True), res.count(False)):
                yield x



def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]
print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))


