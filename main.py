def get_number(the_table):
  search_nums = {}
  find_number = []
  best = 0

  for row in the_table:
    for mini_row in row:
      for number in mini_row:
        if number != 0:
          if number not in search_nums:
            search_nums[number] = 1
          else:
            search_nums[number] += 1


  for i in range(len(search_nums)):
    best = 0
    best_num = 0

    for number in search_nums:
      if search_nums[number] > best:
        best = search_nums[number]
        best_num = number

    search_nums[best_num] = 0
    find_number.append(best_num)


  return find_number


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


best_nums = get_number(table)

for num in best_nums:
  # Search in the table for true position