class Board:
    def __init__(self, n, m):
        self.__board = []
        for i in range(n):
            lst_m = []
            for j in range(m):
                lst_m.append(None)
            self.__board.append(lst_m)
        self.__snake = None
        self.__apples = dict()
        self.__i = 0
        self.__score = 0

    def get_score(self):
        return self.__score

    def add_snake(self, snake):
        coordinates = snake.get_coordinates()
        for coordinate in coordinates:
            x, y = coordinate
            self.__board[x][y] = 'Black'
        self.__snake = snake

    def get_apples_coordinates(self):
        return self.__apples.keys()

    def get_snake_coordinates(self):
        return self.__snake.get_coordinates()

    def move_snake(self, move_key):
        for x, y in self.__snake.get_coordinates():
            self.__board[x][y] = None
        if self.__i > 0:
            self.__snake.move(move_key, True)
            self.__i -= 1
        else:
            self.__snake.move(move_key, False)
        for x, y in self.__snake.get_coordinates():
            self.__board[x][y] = "Black"

    def update_board_apples(self, coordinate):
        self.__score += self.__apples[coordinate]
        self.__board[coordinate[0]][coordinate[1]] = None
        self.__apples.pop(coordinate)
        self.__i += 3

    def get_board(self):
        return self.__board

    def delete_bomb(self, bomb, r):
        for coordinate in bomb.update_orange_list(r):
            self.__board[coordinate[0]][coordinate[1]] = None

    def add_bomb(self, bomb, r):
        for coordinate in bomb.update_orange_list(r):
            self.__board[coordinate[0]][coordinate[1]] = bomb.get_color()

    def is_snake(self, coordinate):
        return self.__board[coordinate[0]][coordinate[1]] == "Black"

    def is_apple(self, coordinate):
        return self.__board[coordinate[0]][coordinate[1]] == "Green"

    def is_bomb(self, coordinate):
        return self.__board[coordinate[0]][coordinate[1]] == "Red" or \
               self.__board[coordinate[0]][coordinate[1]] == "orange"

    def get_type(self, row, col):
        return self.__board[row][col]

    def add_apple(self, apple):
        coordinate = apple.get_location()
        if self.__board[coordinate[0]][coordinate[1]] is not None:
            return False
        self.__board[coordinate[0]][coordinate[1]] = "Green"
        self.__apples[coordinate] = apple.get_score()
        return True
