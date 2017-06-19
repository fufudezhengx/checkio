def max(*args, **kwargs):

    def simpleMax(arg1, arg2, key):
        if key:
            if key(arg2) > key(arg1):
                return arg2
            else:
                return arg1
        if key is None:
            if arg2 > arg1:
                return arg2
            else:
                return arg1

    key = kwargs.get('key', None)
    if len(args) == 1:
        args = list(args[0])
    max = args[0]
    for x in range(1, len(args)):
        max = simpleMax(max, args[x], key)
    return max


def min(*args, **kwargs):

    def simpleMin(arg1, arg2, key):
        if key:
            if key(arg2) < key(arg1):
                return arg2
            else:
                return arg1
        if key is None:
            if arg2 < arg1:
                return arg2
            else:
                return arg1

    key = kwargs.get('key', None)
    if len(args) == 1:
        args = list(args[0])

    min = args[0]
    for x in range(1, len(args)):
        min = simpleMin(min, args[x], key)
    return min


if __name__ == '__main__':

    assert max(3, 2) == 3
    assert min(3, 2) == 2
    assert max([1, 2, 0, 3, 4]) == 4
    assert min("hello") == "e"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
