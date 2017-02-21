import unittest

# s = 'ababa'
# a = 'a'
# b = 'b'
# 1

# s = 'ababa'
# a = 'b'
# b = 'a'
# 1

# s = 'ababa'
# a = 'c'
# b = 'c'
# 0

# s = 'ababac'
# a = 'c'
# b = 'c'
# Impossible

# s = 'abbbb'
# a = 'a'
# b = 'ab'
# Impossible

# s = 'abbbb'
# a = 'ab'
# b = 'a'
# 4


def strings_methods(s: str, a: str, b: str):
    before = s.count(a)
    if before == 0:
        return 0
    else:
        s1 = s.replace(a, b)
        after = s1.count(a)
        if before < after or (before == after and len(s1) >= len(s)):
            return 'Impossible'
        else:
            count = 0
            while a in s:
                s = s.replace(a, b)
                count += 1
            return count

s, a, b = input(), input(), input()
print(strings_methods(s, a, b))
