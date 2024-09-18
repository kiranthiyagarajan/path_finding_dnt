import tkinter as tk

class MazeBuilder:
    def __init__(self, master, rows, cols, cell_size):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        
        self.start = None
        self.end = None
        
        self.canvas = tk.Canvas(master, width=cols * cell_size, height=rows * cell_size)
        self.canvas.pack()

        # Draw grid lines
        for i in range(rows):
            for j in range(cols):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

        self.canvas.bind("<Button-1>", self.mark_path)
        
        self.done_button = tk.Button(master, text="Done", command=self.finalize_maze)
        self.done_button.pack()

    def mark_path(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if self.grid[row][col] == 0:
            if self.start is None:
                self.start = (row, col)
                self.grid[row][col] = 1
                self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size, 
                                             (col + 1) * self.cell_size, (row + 1) * self.cell_size, 
                                             fill="red")
            else:
                # Set end point (last point before Done button)
                if self.end is not None:
                    # Reset previous end point to green if it's clicked again
                    self.grid[self.end[0]][self.end[1]] = 1
                    self.canvas.create_rectangle(self.end[1] * self.cell_size, self.end[0] * self.cell_size, 
                                                 (self.end[1] + 1) * self.cell_size, (self.end[0] + 1) * self.cell_size, 
                                                 fill="green")
                
                self.end = (row, col)
                self.grid[row][col] = 1
                self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size, 
                                             (col + 1) * self.cell_size, (row + 1) * self.cell_size, 
                                             fill="blue")
        else:
            # Toggle cell back to wall if clicked again
            if (row, col) != self.start:
                self.grid[row][col] = 0
                self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size, 
                                             (col + 1) * self.cell_size, (row + 1) * self.cell_size, 
                                             fill="white")

    def finalize_maze(self):
        print("Final Maze Layout (1 = Path, 0 = Wall):")
        for row in self.grid:
            for i in row:
                print(i, " ", end=" ")
            print()
        
        if self.start:
            print(f"Start: {self.start}")
        if self.end:
            print(f"End: {self.end}")
        
        self.master.quit()

root = tk.Tk()
root.title("Custom Maze Builder")
maze_builder = MazeBuilder(root, 20, 30, 20)  # rows, columns, sizeofcell
root.mainloop()

