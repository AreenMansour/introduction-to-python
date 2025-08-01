class Snake:
    def __init__(self):
        self.__snake_coordinates = [(10, 10), (10, 9), (10, 8)]

    def meet_bomb(self, bomb):
        for a in bomb:
            if a in self.__snake_coordinates:
                return True
        return False

    def get_coordinates(self):
        return self.__snake_coordinates

    def move_requirements(self, move_key):
        head = self.__snake_coordinates[0]
        if move_key == "Up":
            head = (head[0], head[1] + 1)
        elif move_key == "Down":
            head = (head[0], head[1] - 1)
        elif move_key == "Left":
            head = (head[0] - 1, head[1])
        else:
            head = (head[0] + 1, head[1])
        return head

    def move(self, move_key, resize):
        if not resize:
            self.__snake_coordinates.pop()
        head = self.move_requirements(move_key)
        self.__snake_coordinates = [head] + self.__snake_coordinates
