rows=range(1,4)
cols=range(1,3)
cells=[(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)