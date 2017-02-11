classes = {}


def add_class(lst: list):
    if len(lst) == 1:
        classes[lst[0]] = []
    else:
        indx = lst.index(':')
        classes[lst[0]] = lst[indx + 1:]


def get_children(parent):
    res = []
    for key, value in classes.items():
        if parent in value:
            res.append(key)
    return res


def is_parent(parent, child):
    # один и тот же класс
    print('Parent %s, child %s' % (parent, child))
    if (parent == child) and (child in classes.keys()):
        print('Equals')
        return "Yes"
    # прямой предок
    if parent in classes[child]:
        print('Straight')
        return "Yes"
    # уходим вглубь
    for subparent in get_children(parent):
        print('Subparent %s, child %s' % (subparent, child))
        if is_parent(subparent, child):
            return "Yes"
    # все остальное
    return "No"


'''n = int(input())
for i in range(n):
    add_class(input().split())
'''
# classes = {'A': [], 'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}
classes = dict(G=['F'], A=[], B=['A'], C=['A'], D=['B', 'C'], E=['D'], F=['D'], X=[], Y=['X', 'A'], Z=['X'],
               V=['Z', 'Y'], W=['V'])

print(classes)

'''q = int(input())
for i in range(q):
    parent, child = input().split()
    print(is_parent(parent, child))
'''

lst = [
    'A G',  # Yes   # A предок G через B/C, D, F
    # 'A Z',      # No    # Y потомок A, но не Y
    # 'A W',      # Yes   # A предок W через Y, V
    # 'X W',      # Yes   # X предок W через Y, V
    # 'A X',      # No    # классы есть, но они нет родства :)
    #    'X X',      # Yes   # родитель он же потомок
    #    '1 1',      # No    # несуществующий класс
    #    'X QWE'    # No    # нет такого класса QWE
]

for e in lst:
    p, c = e.split()
    print(p, c)
    print(is_parent(p, c))
