import random

class GridGame:
    def __init__(self, grid_size=3):
        self.grid_size = grid_size
        
        # Ensure start and goal positions are different
        while True:
            self.start_x = random.randint(0, self.grid_size - 1)
            self.start_y = random.randint(0, self.grid_size - 1)
            self.goal_x = random.randint(0, self.grid_size - 1)
            self.goal_y = random.randint(0, self.grid_size - 1)
            if self.start_x != self.goal_x or self.start_y != self.goal_y:
                break
        
        self.current_x = self.start_x
        self.current_y = self.start_y
    
    def print_grid(self):
        for y in range(self.grid_size):
            row = ""
            for x in range(self.grid_size):
                if x == self.goal_x and y == self.goal_y:
                    row += " G "
                elif x == self.current_x and y == self.current_y:
                    row += " X "
                else:
                    row += " . "
            print(row)
        print("\n")
    
    def startGame(self):
        print("Game started!")
        self.print_grid()
    
    def moveLeft(self):
        if self.current_x > 0:
            self.current_x -= 1
        else:
            print("Out of bounds move!")
        self.print_grid()
    
    def moveRight(self):
        if self.current_x < self.grid_size - 1:
            self.current_x += 1
        else:
            print("Out of bounds move!")
        self.print_grid()
    
    def moveUp(self):
        if self.current_y > 0:
            self.current_y -= 1
        else:
            print("Out of bounds move!")
        self.print_grid()
    
    def moveDown(self):
        if self.current_y < self.grid_size - 1:
            self.current_y += 1
        else:
            print("Out of bounds move!")
        self.print_grid()

# Example usage
game = GridGame(grid_size=5)  # Change the grid size here
game.startGame()
game.moveRight()
game.moveDown()
game.moveLeft()