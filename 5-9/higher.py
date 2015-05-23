# without higher order function.
def pick_odd_without(seq):
    ret = []
    for item in seq:
        if item % 2 == 1:
            ret.append(item)
    return ret


# with higher order function.
def is_odd(item):
    return item % 2 == 1


def filter(pred, seq):
    ret = []
    for item in seq:
        if pred(item):
            ret.append(item)
    return ret


def pick_odd_with(seq):
    return filter(is_odd, seq)


print(pick_odd_with(range(10)))
