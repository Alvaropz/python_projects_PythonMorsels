def tail(iterable, n):
    if n <= 0 or not iterable:
        return []
    else:
        returned_list = [element for element in iterable]
        return returned_list[-n:]
        