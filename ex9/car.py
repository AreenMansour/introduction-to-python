class Car:
    """
    Add class description here
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        # implement your code and erase the "pass"
        lst = []
        x = self.__location[0]
        y = self.__location[1]
        if self.__orientation == 0:
            for i in range(self.__length):
                lst.append((x,y))
                x += 1
        if self.__orientation == 1:
            y = self.__location[1]+self.__length-1
            for i in range(self.__length):
                lst.append((x,y))
                y -= 1
        return lst



    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        #For this car type, keys are from 'udrl'
        #The keys for vertical cars are 'u' and 'd'.
        #The keys for horizontal cars are 'l' and 'r'.
        #You may choose appropriate strings.
        # implement your code and erase the "pass"
        #The dictionary returned should look something like this:
        #result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        #A car returning this dictionary supports the commands 'f','d','a'.
        if self.__orientation == 0:
            return {"u" : "cause the car to go up", "d": "cause the car to go down"}
        if self.__orientation == 1:
            return {"r": "cause the car to go right", "l": "cause the car to go left"}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        #For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        #be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        if self.__orientation == 0 and  movekey == "u":
            return [(self.__location[0] -1, self.__location[1])]
        elif self.__orientation == 0 and movekey == "d":
            return [(self.__location[0] + self.__length, self.__location[1])]
        elif self.__orientation == 1 and movekey == "l":
            return [(self.__location[0], self.__location[1] - 1)]
        elif self.__orientation == 1 and movekey == "r":
            return [(self.__location[0], self.__location[1] + self.__length)]


    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        # movekeys = self.possible_moves().keys()
        # return movekey in movekeys
        if self.__orientation == 0 and movekey == "u":
            self.__location = (self.__location[0] - 1, self.__location[1])
            return True
        elif self.__orientation == 0 and movekey == "d":
            self.__location = (self.__location[0] + 1, self.__location[1])
            return True
        elif self.__orientation == 1 and movekey == "l":
            self.__location = (self.__location[0], self.__location[1] - 1)
            return True
        elif self.__orientation == 1 and movekey == "r":
            self.__location = (self.__location[0], self.__location[1] + 1)
            return True

        return False
    def get_name(self):
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        return self.__name


