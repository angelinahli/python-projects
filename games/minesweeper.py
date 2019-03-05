import random

class Minesweeper:
    """
    A game of Minesweeper revolves around an n x n grid-game.
    * At the start of the game, a number of mines are initialized at random
      coordinates on the grid.
    * Each coordinate i, j (representing the cell grid[i][j] such that i < n && 
      j < n) that does not contain a mine, will indicate to the player how many
      mines are contained in the set of cells bordering grid[i][j]:
      { grid[a][b] | a in (i-1, i+1) && b in (j-1, j+1) }
    * Each turn, the player gets to indicate which co-ordinate they would like to
      play.
        * If the co-ordinate they chose contains a mine, the player loses.
        * If the co-ordinate they chose borders at least 1 mine, the value of
          that cell is revealed to the player.
        * If the co-ordinate they chose borders 0 mines, the entire area of cells
          up until the line of cells with a non 0 value are revealed to the player.
    """

    DEFAULT_NUM_MINES = 10
    DEFAULT_GRID_LENGTH = 10

    def __init__(self, num_mines=DEFAULT_NUM_MINES, grid_length=DEFAULT_GRID_LENGTH, debug=False):
        """
        Initializes a game of Minesweeper.
        Requires that num_mines <= int((grid_length**2) / 2). - i.e. the maximum
            number of mines allowed = half the total number of cells.
        Creates the following instance variables:
        ==> num_mines: The number of mines that are initialized on the grid.
        ==> grid_length: The length of one side of the grid.
        """
        self.num_mines = num_mines
        self.grid_length = grid_length
        self.num_cells = self.grid_length ** 2
        
        assert self.num_mines <= int((self.num_cells) / 2)
        
        self.debug = debug
        self.mines = self._get_mines()
        self.grid = self._get_new_grid(self.mines)
        self.num_visible = 0
        self.in_progress = True

    def __repr__(self):
        rows = []
        top_indices = [" ", " "] + list(map(str, range(self.grid_length)))
        rows.append(" ".join(top_indices))
        border = "-" * ( (self.grid_length + 2) + (self.grid_length + 1) )
        border = "  " + border
        rows.append(border)
        for i, row in enumerate(self.grid):
            row_vals = []
            if self.debug:
                row_vals = [str(cell.value) for cell in row]
            else:
                row_vals = [cell.__repr__() for cell in row]
            row_vals = [str(i), "|"] + row_vals + ["|"]
            rows.append(" ".join(row_vals))
        rows.append(border)
        return "\n".join(rows)

    ## INITIALIZE GRID ##

    def _get_new_grid(self, mines):
        grid = [ [ Cell(row, col, value=0) for col in range(self.grid_length) ] 
                 for row in range(self.grid_length) ]
        for mine in mines:
            grid[mine.row][mine.col] = mine
        for mine in mines:
            self._increment_mine_borders(grid, mine)
        return grid

    def _increment_mine_borders(self, grid, mine):
        row_lower = self._get_valid_coord(mine.row - 1)
        row_upper = self._get_valid_coord(mine.row + 1)
        col_lower = self._get_valid_coord(mine.col - 1)
        col_upper = self._get_valid_coord(mine.col + 1)
        for row in range(row_lower, row_upper + 1):
            for col in range(col_lower, col_upper + 1):
                if not grid[row][col].is_mine:
                    grid[row][col].value += 1

    def _get_valid_coord(self, value):
        assert type(value) == int
        return_value = value
        if return_value < 0:
            return_value = 0
        if return_value > self.grid_length - 1:
            return_value = self.grid_length - 1
        return return_value

    def _get_mines(self):
        mines = []
        for _ in range(self.num_mines):
            new_mine = Cell.get_random_mine(self.grid_length - 1)
            while any([c.equals(new_mine) for c in mines]):
                new_mine = Cell.get_random_mine(self.grid_length - 1)
            mines.append(new_mine)
        return mines

    ## PLAY MOVE ##

    def _play_move(self, row, col):
        """
        Updates the game to accomodate for a move at row, col
        """
        assert self.in_progress
        assert self._is_valid_move(row, col)
        self._update_visibility(row, col)
        self._update_game_status()

    def _update_visibility(self, row, col):
        if not self._is_valid_coord(row) or \
                not self._is_valid_coord(col) or \
                self.grid[row][col].visible:
            return

        self.grid[row][col].visible = True
        self.num_visible += 1

        if self.grid[row][col].value == 0:
            self._update_visibility(row - 1, col)
            self._update_visibility(row + 1, col)
            self._update_visibility(row, col - 1)
            self._update_visibility(row, col + 1)

    def _is_valid_coord(self, value):
        return type(value) == int and 0 <= value < self.grid_length

    def _is_valid_move(self, row, col):
        return self._is_valid_coord(row) and self._is_valid_coord(col) and \
               not self.grid[row][col].visible

    ## CHECK ENDGAME STATUS ##

    def _turn_all_visible(self):
        for row in range(self.grid_length):
            for col in range(self.grid_length):
                self.grid[row][col].visible = True

    def _update_game_status(self):
        has_lost = any([mine.visible for mine in self.mines])
        has_won = self.num_cells - self.num_mines == self.num_visible
        if has_lost:
            self.in_progress = False
            self._turn_all_visible()
            print("You hit a mine... You're dead! :(")
        elif has_won:
            self.in_progress = False
            self._turn_all_visible()
            print("You won!!!")

    ## IMPLEMENT THE GAME ##

    def _is_valid_input_move(self, move):
        try:
            row, col = map(int, move.split(","))
            return self._is_valid_move(row, col)
        except (TypeError, ValueError) as e:
            return False

    def _get_valid_move(self):
        prompt = "Please enter a coordinate to play in the format 'row,col': "
        move = input(prompt)
        while not self._is_valid_input_move(move):
            error_msg = "Sorry, this isn't a valid move!"
            print(error_msg)
            move = input(prompt)
        row, col = map(int, move.split(","))
        return row, col

    def play_game(self):
        print("Welcome to this game of Minesweeper!")
        print("Here is your beginning {n}x{n} sized grid:".format(n=self.grid_length))
        print("There are {} mines... good luck!".format(self.num_mines))
        print(self)
        while self.in_progress:
            print("===============================")
            row, col = self._get_valid_move()
            self._play_move(row, col)
            print(self)
        print()
        print("Thank you for playing!!")

class Cell:

    def __init__(self, row, col, value):
        assert type(row) == int and type(col) == int
        self.row = row
        self.col = col
        self.value = value
        self.is_mine = False
        self.visible = False

    def __repr__(self):
        if not self.visible:
            return " "
        if self.value == 0:
            return "."
        return str(self.value)

    def equals(self, cell):
        return cell.row == self.row and cell.col == self.col

    @classmethod
    def get_random_mine(cls, max_val):
        row = random.randint(0, max_val)
        col = random.randint(0, max_val)
        mine = cls(row, col, "X")
        mine.is_mine = True
        return mine

if __name__ == "__main__":
    ms = Minesweeper()
    ms.play_game()