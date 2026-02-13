# Hints – 2D and 3D Lists

Use if you're stuck. You should be comfortable with 1D lists and loops.

---

## Part 1 – 2D basics

**1.1** matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. print(matrix), print(matrix[0]), print(matrix[1][2]). First index = row, second = column.

**1.2** grid = [[10, 20], [30, 40], [50, 60]]. print(len(grid)), print(len(grid[0])). len(grid) = number of rows; len(grid[0]) = number of columns.

**1.3** data = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]. print(data[0]), print(data[-1]), print(data[0][0]), print(data[-1][-1]).

---

## Part 2 – 2D and loops

**2.1** matrix = [[1, 2], [3, 4], [5, 6]]. for row in matrix: print(row).

**2.2** grid = [[1, 2, 3], [4, 5, 6]]. for row in grid: for cell in row: print(cell, end=" "); print(). (print() after inner loop starts a new line per row.)

**2.3** nums = [[1, 2], [3, 4], [5, 6]], total = 0. for row in nums: for cell in row: total += cell. print(total).

**2.4** matrix = [[10, 20], [30, 40]]. for i in range(len(matrix)): for j in range(len(matrix[i])): print(matrix[i][j]).

---

## Part 3 – 2D and input

**3.1** n = int(input("Number of rows? ")), m = int(input("Number of columns? ")). grid = []. for i in range(n): row = []; for j in range(m): num = int(input("Row " + str(i+1) + " number " + str(j+1) + ": ")); row.append(num). grid.append(row). print(grid).

**3.2** matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. for i in range(len(matrix)): row_sum = 0; for cell in matrix[i]: row_sum += cell. print("Row " + str(i+1) + " sum: " + str(row_sum)).

---

## Part 4 – 3D lists

**4.1** cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]. cube[0] = first layer (2D). cube[0][1][0] = 3. cube[1][0][1] = 6. cube[-1][-1][-1] = 8. print(cube[0]), print(cube[1][0][1]), print(cube[-1][-1][-1]).

**4.2** data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]. print(len(data)), print(len(data[0])), print(len(data[0][0])). Three levels: layers, rows, columns.

**4.3** cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]], total = 0. for layer in cube: for row in layer: for cell in row: total += cell. print(total).

**4.4** main = []. for layer_idx in range(2): layer = []. for row_idx in range(2): row = []. for col_idx in range(2): num = int(input("Layer " + str(layer_idx+1) + " row " + str(row_idx+1) + " col " + str(col_idx+1) + ": ")); row.append(num). layer.append(row). main.append(layer). print(main).

---

## Reminders

- **2D:** grid[i][j] = element in row i, column j. grid[i] is the whole row (a list).
- **3D:** cube[i][j][k] = layer i, row j, column k. cube[i] is a 2D list (one layer).
- **Nested loops:** outer loop = rows (or layers), inner loop = columns (or elements in row). Match the index order to your list structure.

---

## Common errors

| Error | Check |
|-------|--------|
| IndexError | Ensure index is < len(list). For 2D, check both row index and column index. |
| TypeError: list indices must be integers | You used a list as index; use integer i in range(len(grid)) then grid[i]. |
| Wrong order of indices | grid[row][col] not grid[col][row] if you think "row first". |
