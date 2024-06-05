def find_highest(lst):
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    max_rest = find_highest(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest