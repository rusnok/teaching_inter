from functools import reduce

items = [1, 2, 3, 4, 5]
items_sum = reduce(lambda x, y: x + y, items)  # 15
print(items_sum)
# [3, 3, 4, 5]
# [6, 4, 5]
# [10, 5]
# 15

items = [1, 2, 3, 4, 5]
items_sum = reduce(lambda x, y: y, items)  # 15
(print(items_sum))

# [2, 3, 4, 5]
# [3, 4, 5]
# [4, 5]
# [5]