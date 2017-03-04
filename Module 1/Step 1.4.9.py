inheritance = {'global': ''}
namespaces = {'global': []}


def create(namespace, parent):
    inheritance[namespace] = parent
    namespaces[namespace] = []


def add(namespace, var):
    namespaces[namespace].append(var)


def get(namespace, var):
    if var in namespaces[namespace]:
        return namespace
    elif inheritance[namespace] == '':
        return None
    else:
        return get(inheritance[namespace], var)

operations = {'create': create, 'add': add, 'get': get}

n = int(input())
for _ in range(n):
    operation, namespace, obj = input().strip().split()
    if operation == 'get':
        print(operations[operation](namespace, obj))
    else:
        operations[operation](namespace, obj)

# lines = ['add global a',
#          'create foo global',
#          'add foo b',
#          'get foo a',
#          'get foo c',
#          'create bar foo',
#          'add bar a',
#          'get bar a',
#          'get bar b']
#
# n = 9
# for line in lines:
#     operation, namespace, obj = line.split()
#     if operation == 'get':
#         print(operations[operation](namespace, obj))
#     else:
#         operations[operation](namespace, obj)
