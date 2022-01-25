# sum odd and even
# https://edabit.com/challenge/5XXXppAdfcGaootD9

def sum_odd_and_even(lst):
    return [sum(i for i in lst if not i % 2), sum(i for i in lst if i % 2)]


def sum_odd_and_even(lst):
    odd, even = 0, 0
    for i in lst:
        if i % 2:
            odd += i
        else:
            even += i
    return [even, odd]


# switch key value of dict

# https://edabit.com/challenge/Axim3Ld5zu9RFLZKr

def invert(d):
    return {v: k for k, v in d.items()}


def invert(dct):
    dct2 = {}
    for i, k in dct.items():
        dct2[k] = i
    return dct2


# https://edabit.com/challenge/LR98GCwLGYPSv8Afb

def pluralize(lst):
    nl = []
    for i in lst:
        if lst.count(i) > 1:
            i += 's'
            nl.append(i)
        else:
            nl.append(i)
    return set(nl)


def pluralize(lst):
    return {i+'s' if lst.count(i) > 1 else i for i in lst}
