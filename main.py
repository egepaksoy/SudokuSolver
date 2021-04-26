table = [
  [[0, 0, 0], [9, 0, 0], [1, 0, 0]],
  [[0, 1, 9], [7, 0, 0], [6, 0, 3]],
  [[3, 0, 0], [4, 0, 1], [0, 0, 5]],

  [[0, 0, 0], [0, 2, 0], [0, 1, 0]],
  [[4, 0, 0], [0, 0, 0], [7, 2, 0]],
  [[0, 7, 6], [0, 0, 0], [0, 0, 8]],

  [[6, 2, 0], [8, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [1, 3, 5], [0, 0, 0]],
  [[1, 0, 0], [0, 0, 6], [3, 7, 9]]
]

search_nums = {}
find_number = 0
best = 0

for row in table:
  for mini_row in row:
    for number in mini_row:
      if number != 0:
        if number not in search_nums:
          search_nums[number] = 1
        else:
          search_nums[number] += 1

for number in search_nums:
  if search_nums[number] > best:
    best = search_nums[number]
    find_number = number
