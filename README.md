# Conway-life-game

## 1) Introduction(简介):

- EN: This project created a Conway Life game with an operational interface, where users can determine the initial position of the cell by clicking on the interface. In addition, users can clearly see the trajectory of the cell's movement as it is marked with another color.

- CN: 该项目实现了著名的康威生命游戏，并设计了可操作界面，玩家可以通过点击鼠标决定元胞的初始位置。此外，玩家可以清晰地看到元胞的运动轨迹，它被标记成了绿色。

![效果图](D:/JupyterNotebookFile/CMA/Game of life/ezgif.com-video-to-gif.gif)

## 2) Design ideas(设计思路):

- EN: The iterative function used to implement the Conway Life game is "next_gen", which uses two two-dimensional lists to record the state of the cell in the current and next generations. Each cell has three states, with 0 representing pre birth, 1 representing living, and 2 representing death.The 'next_gen' function also calls a function called 'count_neighbors' to calculate the number of surviving cells in the neighborhood.

- CN: 用于实现康威生命游戏的迭代函数是“next_gen”，该函数使用两个二维列表分别记录元胞在当前和下一代中的状态。每个元胞有3种状态，0代表诞生前，1代表活着的，2代表死亡。“next_gen”函数中还调用了一个名为“count_neighbors”的函数，用于计算邻域中存活状态的元胞的数量。交互界面设计使用了Tkinter库。

```python
def next_gen():
    global grid_model, next_grid
    for i in range(height):
        for j in range(width):
            cell = 0
            count = count_neighbors(grid_model, i, j)
            if (grid_model[i][j] == 0):
                if count == 3:
                    cell = 1
            elif grid_model[i][j] == 1:
                if count == 2 or count == 3:
                    cell = 1
                else:
                    cell = 2
            elif (grid_model[i][j] == 2):
                if count == 3:
                    cell = 1
                else:
                    cell = 2
            next_grid[i][j] = cell
    grid_model, next_grid = next_grid, grid_model

def count_neighbors(grid, row, col):
    count = 0
    for i in [row, (row - 1) % height, (row + 1) % height]:
        for j in [col, (col - 1) % width, (col + 1) % width]:
            if grid[i][j] == 1:
                count += 1
    if grid[row][col] == 1:
        count -= 1
    return count

```

- EN: The interaction interface design uses the Tkinter library. The function of generating cells by clicking on the interface with the mouse is mainly implemented by the "click_pos" function. Grid_view "is the canvas, and we bind the" click_pos "function to it, which means that the canvas is treated as a coordinate system, and" event. x "is the abscissa in this coordinate system. 'event. y' is the vertical coordinate in this coordinate system. It should be noted that you need to click on the "Stop" button before clicking on the interface to generate cells.

- CN: 交互界面设计使用了Tkinter库。鼠标点击界面从而产生元胞的功能主要是由“click_pos”函数实现的。鼠标点击界面从而产生元胞的功能主要是由“click_pos”函数实现的。“grid_view”是画布，我们将“click_pos”函数绑定在画布上，这就意味着将画布作为一个坐标系，“event.x”是这个坐标系中的横坐标。“event.y”是这个坐标系中的纵坐标。需要注意的是，你需要先点击“Stop”键，才能点击界面来生成元胞。

```python
def click_pos(event):
    if not run:
        x,y=int(event.x/cell_size), int(event.y/cell_size)
        if (x < width) & (y < height):
            global grid_model
            global var
            grid_model[y][x] = 1
            var.set("Click the pos")
            show()

grid_view.bind('<Button-1>', click_pos)

```

## 3) Areas for improvement(有待改进的地方)

- EN: Firstly, the rules of the Conway Life game are variable, and I have only demonstrated the most classic one here. In the future, the design can be improved to allow players to choose their own rules; Secondly, this only demonstrates the situation of one life, what would be the situation of multiple lives?

- CN: 首先，康威生命游戏的规则是可变的，我在这里仅仅只演示了最经典的一种。后续可以改进设计，让玩家可以自己选择规则；其次，这里仅仅演示了一种生命的情形，那么多种生命的情形会是什么样的呢？
