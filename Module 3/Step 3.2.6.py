from unittest import TestCase


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

# s, a, b = input(), input(), input()
# print(strings_methods(s, a, b))


class TestStringsMethods(TestCase):
    def test_1(self):
        self.assertEqual(strings_methods('ababa', 'a', 'b'), 1)

    def test_2(self):
        self.assertEqual(strings_methods('ababa', 'b', 'a'), 1)

    def test_3(self):
        self.assertEqual(strings_methods('ababa', 'c', 'c'), 0)

    def test_4(self):
        self.assertEqual(strings_methods('ababac', 'c', 'c'), 'Impossible')

    def test_5(self):
        self.assertEqual(strings_methods('abbbb', 'a', 'ab'), 'Impossible')

    def test_6(self):
        self.assertEqual(strings_methods('abbbb', 'ab', 'a'), 4)

if __name__ == '__main__':
    unittest.main()
