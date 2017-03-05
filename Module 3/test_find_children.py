# from unittest import TestCase
#
#
# class TestFind_children(TestCase):
#     def test_find_children(self):
#         self.fail()
#
#     def test_1(self):
#         line = [{"name": "A", "parents": []},
#                 {"name": "B", "parents": ["A", "C"]},
#                 {"name": "C", "parents": ["A"]}]
#         answer = [('A', 3),
#                   ('B', 1),
#                   ('C', 2)]
#         self.assertEquals(find_children(line), answer)
#
#     def test_2(self):
#         line = [{"name": "B", "parents": ["A", "C"]},
#                 {"name": "C", "parents": ["A"]},
#                 {"name": "A", "parents": []},
#                 {"name": "D", "parents": ["C", "F"]},
#                 {"name": "E", "parents": ["D"]},
#                 {"name": "F", "parents": []}]
#         answer = [('A', 5), ('B', 1), ('C', 4), ('D', 2), ('E', 1), ('F', 3)]
#         self.assertEquals(find_children(line), answer)

# if __name__ == '__main__':
#     unittest.main()

