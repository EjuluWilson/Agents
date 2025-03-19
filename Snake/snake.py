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
        print("----"*self.grid_size)
        for y in range(self.grid_size):
            row = "|"
            for x in range(self.grid_size):
                if x == self.goal_x and y == self.goal_y:
                    row += " G |"
                elif x == self.current_x and y == self.current_y:
                    row += " X |"
                else:
                    row += " . |"
            print(row)
            print("----"*self.grid_size)
        print("\n")
    
    def check_win(self):
        if self.current_x == self.goal_x and self.current_y == self.goal_y:
            print("Congratulations! You reached the goal!")
            return True
        return False
    
    def startGame(self):
        print("Game started!")
        self.print_grid()
        return {
            "current_position": {"x": self.current_x, "y": self.current_y},
            "goal_position": {"x": self.goal_x, "y": self.goal_y},
            "grid_size": self.grid_size
        }
    
    def move(self, direction):
        """Move in the specified direction: U (up), D (down), L (left), or R (right)."""
        direction = direction.upper()  # Convert to uppercase for consistency
        
        # Calculate the new position based on the direction
        new_x, new_y = self.current_x, self.current_y
        movement = ""
        
        if direction == "U":
            new_y -= 1
            movement = "up"
        elif direction == "D":
            new_y += 1
            movement = "down"
        elif direction == "L":
            new_x -= 1
            movement = "left"
        elif direction == "R":
            new_x += 1
            movement = "right"
        else:
            print(f"Invalid direction: {direction}. Use U, D, L, or R.")
            return {
                "success": False,
                "message": f"Invalid direction: {direction}. Use U, D, L, or R.",
                "current_position": {"x": self.current_x, "y": self.current_y},
                "win": False
            }
        
        # Check if the move is valid (within grid boundaries)
        if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size:
            self.current_x, self.current_y = new_x, new_y
            print(f"Moved {movement} to position ({new_x}, {new_y})")
            self.print_grid()
            win = self.check_win()
            
            return {
                "success": True,
                "message": f"Moved {movement} to ({new_x}, {new_y})",
                "current_position": {"x": self.current_x, "y": self.current_y},
                "win": win
            }
        else:
            print(f"Invalid move: out of bounds")
            return {
                "success": False,
                "message": "Invalid move: out of bounds",
                "current_position": {"x": self.current_x, "y": self.current_y},
                "win": False
            }