def cal_prime_nums(m, n):
    prime_nums = []
    not_prime_nums = []

    for i in range(m, n):
        lst = []
        for j in range(2, i):
            if j not in lst:
                if i % j == 0:
                    lst.append(i)
                    x = int(i / j)
                    if x not in lst:
                        lst.append(x)
                    print('{} = {} * {}'.format(i, j, x))

        if len(lst) == 0:
            print('{} 是一个质数'.format(i))
            prime_nums.append(i)
        else:
            not_prime_nums.append(i)

    print("质数有({})".format(", ".join(str(e) for e in prime_nums)))
    print("非质数({})".format(", ".join(str(e) for e in not_prime_nums)))


if __name__ == "__main__":
    cal_prime_nums(1, 200)
