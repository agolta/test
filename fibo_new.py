import sys


def fibo(arg):
    result = []
    list_arg = list(range(arg))
    for i, x in enumerate(list_arg):
        if i > 2:
            result.append(result[-1] + result[-2])
        else:
            result.append(x)
    return result


if __name__ == "__main__":
    arg = int(sys.argv[1])
    result = fibo(arg)
    print(result)
