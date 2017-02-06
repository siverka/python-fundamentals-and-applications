def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    print(res)
    return res


s(21)
s(11, 10, 10)
#s(b=31)
print('error')
s(5, 5, 5, 5, 1)
s(11, b=20)
s(0, 0, 31)
s(11, 10)
#s(b=31, 0)
print('error')
s(11, 10, b=10)


