classes = {}


def add_class(lst: list):
    if len(lst) == 1:
        classes[lst[0]] = []
    else:
        classes[lst[0]] = lst[lst.index(':') + 1:]


def is_parent(parent: str, children: list):
    # классы вообще есть,
    if (parent not in classes.keys()) or (children[0] not in classes.keys()):
        return "No"

    # один и тот же класс
    if parent in children:
        return "Yes"

    # прямой предок
    union_parents = []
    for child in children:
        union_parents.extend(classes[child])
    union_parents = list(set(union_parents))
    if parent in union_parents:
        return "Yes"

    # уходим вглубь
    if len(union_parents) == 0:
        return "No"
    return is_parent(parent, union_parents)


n = int(input())
for i in range(n):
    add_class(input().split())

q = int(input())
for i in range(q):
    p, c = input().split()
    print(is_parent(p, [c]))

# test data
'''classes = dict(G=['F'], A=[], B=['A'], C=['A'], D=['B', 'C'], E=['D'], F=['D'], X=[], Y=['X', 'A'], Z=['X'],
               V=['Z', 'Y'], W=['V'])
lst = [
    'A G',  # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'X W',      # Yes   # X предок W через Y, V
    'A X',      # No    # классы есть, но они нет родства :)
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
    'X QWE'    # No    # нет такого класса QWE
]

for e in lst:
    p, c = e.split()
    print(p, c, end= ' ')
    print(is_parent(p, [c]))

'''
