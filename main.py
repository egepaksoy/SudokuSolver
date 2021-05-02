table = [
  [0, 0, 0, 9, 0, 0, 1, 0, 0],
  [0, 1, 9, 7, 0, 0, 6, 0, 3],
  [3, 0, 0, 4, 0, 1, 0, 0, 5],

  [0, 0, 0, 0, 2, 0, 0, 1, 0],
  [4, 0, 0, 0, 0, 0, 7, 2, 0],
  [0, 7, 6, 0, 0, 0, 0, 0, 8],

  [6, 2, 0, 8, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 3, 5, 0, 0, 0],
  [1, 0, 0, 0, 0, 6, 3, 7, 9]
]

class Scan():
  def __init__(self, table):
    self.table = table

  def row(self):
    return self.table

  def column(self):
    table = self.table
    c = 0
    column = []

    while c < len(table[0]):
      colum = []
      for col in table:
        colum.append(col[c])
      column.append(colum)
      c += 1
    
    return column

s = Scan(table)
column = s.column()
row = s.row()