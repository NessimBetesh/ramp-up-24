def tallest_skyscraper(lst):
    max_height = 0
    for col in range(len(lst[0])):
        height = 0
        for row in range(len(lst)):
            if lst[row][col] == 1:
                height += 1
        max_height = max(max_height, height)
    return max_height