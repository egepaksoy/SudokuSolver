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

def divide(the_table):
  row = []
  column = []

  x = 0
  while x < len(the_table):
    row.append([])
    for row_block in the_table[x]:
      for number in row_block:
        row[x].append(number)
    x += 1

  buyuk = 0
  x = 0
  while buyuk < 3:
    kucuk = 0
    while kucuk < 3:
      column.append([])
      for row in the_table:
        column[x].append(row[buyuk][kucuk])
      kucuk += 1
      x += 1
    buyuk += 1


  return row, column


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
divided = divide(table)