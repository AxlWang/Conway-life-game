# Conway-life-game

1) Introduction(简介):

EN: This project created a Conway Life game with an operational interface, where users can determine the initial position of the cell by clicking on the interface. In addition, users can clearly see the trajectory of the cell's movement as it is marked with another color.

CN: 该项目实现了著名的康威生命游戏，并设计了可操作界面，玩家可以决定元胞的初始位置。此外，玩家可以清晰地看到元胞的运动轨迹，它被标记成了绿色。

2) Design ideas(设计思路):

EN: The iterative function used to implement the Conway Life game is "next_gen", which uses two two-dimensional lists to record the state of the cell in the current and next generations, respectively. The 'next_gen' function also calls a function called 'count_neighbors' to calculate the number of surviving cells in the neighborhood. The interaction interface design uses the Tkinter library.

CN: 用于实现康威生命游戏的迭代函数是“next_gen”，该函数使用两个二维列表分别记录元胞在当前和下一代中的状态。“next_gen”函数中还调用了一个名为“count_neighbors”的函数，用于计算邻域中存活状态的元胞的数量。交互界面设计使用了Tkinter库。
