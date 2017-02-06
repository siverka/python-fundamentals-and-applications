def closest_mod_5(x: int):
    res = [y for y in range(x, x+5) if not y % 5]
    return res[0]

print(closest_mod_5(6))
print(closest_mod_5(10))
print(closest_mod_5(19))
print(closest_mod_5(-9))

