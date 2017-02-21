s, t = input(), input()
m = len(t)
count = [s[i:i+m] == t for i in range(len(s) - m + 1)]
print(sum(count))
