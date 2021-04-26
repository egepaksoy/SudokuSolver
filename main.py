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


  # divide rows
  x = 0
  while x < len(the_table):
    row.append([])
    for row_block in the_table[x]:
      for r in row_block:
        row[x].append(r)
    x += 1


  # divide columns
  buyuk = 0
  x = 0
  while buyuk < 3:
    kucuk = 0
    while kucuk < 3:
      column.append([])
      for r in the_table:
        column[x].append(r[buyuk][kucuk])
      kucuk += 1
      x += 1
    buyuk += 1


  return row, column

def search(divided, num):
  for x in divided[0]:
    if num not in x:
      print(x)
  print("xxxxxxxxxxxxxxxx")
  for y in divided[1]:
    if num not in y:
      print(y)

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
bolunmus = divide(table)


search(bolunmus, best_nums[0])