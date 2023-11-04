import tkinter
import random

def randomize(col, row):
    global grid_model
    for i in range(row):
        for j in range(col):
            grid_model[i][j] = random.randint(0, 1)


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

def start_handler(event):
    global run
    global var
    run = True
    # 如果没有下面这一条条件判断语句，程序会按照GameOfLife_2中已经存在的grid_model运行
    if var.get() == "Choose the mode":
        var.set("Random")
        randomize(width, height)
    update()
    
def stop_handler(event):
    global run
    run = False

def show():
    for i in range(height):
        for j in range(width):
            if grid_model[i][j] == 1:
                grid_view.create_rectangle(j * cell_size, i * cell_size,
                                           (j + 1) * cell_size, (i + 1) * cell_size,
                                           fill="black", outline='white')
            elif grid_model[i][j] == 2:
                grid_view.create_rectangle(j * cell_size, i * cell_size,
                                           (j + 1) * cell_size, (i + 1) * cell_size,
                                           fill="lightgreen", outline = 'white')

def choose_mode(event):
    if var.get() == "Random":
        grid_view.delete("all")
        randomize(width, height)
    elif var.get() == "Click the pos":
        global run
        run = False
        

def clear_handler(event):
    global run
    global grid_model
    run = False
    grid_view.delete("all")
    grid_model = [0] * height
    for i in range(height):
        grid_model[i] = [0] * width

        
def update():
    if run:
        grid_view.delete("all")
        next_gen()
        show()
        root.after(100, update)

def click_pos(event):
    if not run:
        x,y=int(event.x/cell_size), int(event.y/cell_size)
        if (x < width) & (y < height):
            global grid_model
            global var
            grid_model[y][x] = 1
            var.set("Click the pos")
            show()
            
if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("康威生命游戏")

    height = 50
    width = 110

    grid_model = [0] * height
    next_grid = [0] * height
    for i in range(height):
        grid_model[i] = [0] * width
        next_grid[i] = [0] * width

    cell_size = 10
    layer = 1
    run = False
    options = ["Random", "Click the pos"]
    button_dict = {}

    grid_view = tkinter.Canvas(root, width=width * cell_size,
                               height=height * cell_size, bg="white")
    grid_view.grid(row=0, columnspan=4)

    start_button = tkinter.Button(root, text='Start', width=12)
    start_button.bind('<Button-1>', start_handler)
    start_button.grid(row=height+1, column=0, padx=20, pady=20)

    stop_button = tkinter.Button(root, text='Stop', width=12)
    stop_button.bind('<Button-1>', stop_handler)
    stop_button.grid(row=height+1, column=1, padx=20, pady=20)

    var = tkinter.StringVar(root)
    var.set("Choose the mode")
    # 加上*号有解包功能，不加的话就会把整个列表作为选项显示
    set_button = tkinter.OptionMenu(root, var, *options, command=choose_mode)
    set_button.grid(row=height+1, column=2, padx=20, pady=20)

    clear_button = tkinter.Button(root, text='Clear', width=12)
    clear_button.bind('<Button-1>', clear_handler)
    clear_button.grid(row=height+1, column=3, padx=20, pady=20)

    grid_view.bind('<Button-1>', click_pos)
    root.mainloop()