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
for _ in range(n):
    add_class(input().split())


m = int(input())
errors = []
for _ in range(m):
    errors.append(input())


m = len(errors)
res = [False for _ in range(m)]


for i in range(m):
    for j in range(i+1, m):
        if is_parent(errors[i], [errors[j]]) == "Yes":
            res[j] = True

for i in range(m):
    if res[i]:
        print(errors[i])
