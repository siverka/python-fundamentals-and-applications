def c_n_k(n: int, k: int):
    if k == 0:
        return 1
    else:
        return(c_n_k(n-1, k) + c_n_k(n-1, k-1))

print(c_n_k(3, 2))
print(c_n_k(10, 5))
