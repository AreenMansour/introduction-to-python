class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.__board = []
        for i in range(7):
            lst = []
            for j in range(7):
                lst.append("_")
            if i == 3:
                lst.append("_")
            self.__board.append(lst)
        self.__car_names = set()
        self.__cars = set()


    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        #The game may assume this function returns a reasonable representation
        #of the board for printing, but may not assume details about it.
        x = [str(l) for l in self.__board]
        return str("\n".join(x))


    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        #In this board, returns a list containing the cells in the square
        #from (0,0) to (6,6) and the target cell (3,7)
        lst = []
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                lst.append((i, j))
        return lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        #From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        board_possible_moves = []
        for car in self.__cars:
            for tup in car.possible_moves().items():
                movement = car.movement_requirements(tup[0])
                if self.check_car_coordinates(movement):
                    board_possible_moves.append((car.get_name(),)+tup)
        return board_possible_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        #In this board, returns (3,7)
        return (3,7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        if self.__board[coordinate[0]][coordinate[1]] == "_":
            return None
        return self.__board[coordinate[0]][coordinate[1]]

    def check_car_coordinates(self, coordinates):
        borders = self.cell_list()
        for coordinate in coordinates:
            if coordinate not in borders or self.cell_content(coordinate) is not None:
                return False
        return True

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        #Remember to consider all the reasons adding a car can fail.
        #You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        name = car.get_name()
        coordinates = car.car_coordinates()
        if name not in self.__car_names and self.check_car_coordinates(coordinates):
            for coordinate in coordinates:
                self.__board[coordinate[0]][coordinate[1]] = name
            self.__cars.add(car)
            self.__car_names.add(name)
            return True
        return False

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        possible_moves = [(tup[0], tup[1]) for tup in self.possible_moves()]
        if (name, movekey) in possible_moves:
            car = None
            for c in self.__cars:
                if c.get_name() == name:
                    car = c
            car_coordinates = {coord for coord in car.car_coordinates()}
            if car.move(movekey):
                new_car_coordinates = {coord for coord in car.car_coordinates()}
                for coord in car_coordinates-new_car_coordinates:
                    self.__board[coord[0]][coord[1]] = "_"
                for coord in new_car_coordinates - car_coordinates:
                    self.__board[coord[0]][coord[1]] = name
                return True
        return False


