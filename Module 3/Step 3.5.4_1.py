# def find_children(line: list):


    # for p in parents:
    #     parents[p] = len(set(parents[p]))
    # print(parents)
    # print(sorted(parents.items(), key=lambda x: x[0] + 1))

line = [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []},
        {"name": "D", "parents": ["C", "F"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": []}]

# find_children(line)
