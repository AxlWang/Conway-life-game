# Conway-life-game

1) Introduction(简介):

EN: This project created a Conway Life game with an operational interface, where users can determine the initial position of the cell by clicking on the interface. In addition, users can clearly see the trajectory of the cell's movement as it is marked with another color.

CN: 该项目实现了著名的康威生命游戏，并设计了可操作界面，玩家可以通过点击鼠标决定元胞的初始位置。此外，玩家可以清晰地看到元胞的运动轨迹，它被标记成了绿色。

2) Design ideas(设计思路):

EN: The iterative function used to implement the Conway Life game is "next_gen", which uses two two-dimensional lists to record the state of the cell in the current and next generations, respectively. The 'next_gen' function also calls a function called 'count_neighbors' to calculate the number of surviving cells in the neighborhood. The interaction interface design uses the Tkinter library.

CN: 用于实现康威生命游戏的迭代函数是“next_gen”，该函数使用两个二维列表分别记录元胞在当前和下一代中的状态。“next_gen”函数中还调用了一个名为“count_neighbors”的函数，用于计算邻域中存活状态的元胞的数量。交互界面设计使用了Tkinter库。

3) Areas for improvement(有待改进的地方)

EN: Firstly, the rules of the Conway Life game are variable, and I have only demonstrated the most classic one here. In the future, the design can be improved to allow players to choose their own rules; Secondly, this only demonstrates the situation of one life, what would be the situation of multiple lives?

CN: 首先，康威生命游戏的规则是可变的，我在这里仅仅只演示了最经典的一种。后续可以改进设计，让玩家可以自己选择规则；其次，这里仅仅演示了一种生命的情形，那么多种生命的情形会是什么样的呢？
