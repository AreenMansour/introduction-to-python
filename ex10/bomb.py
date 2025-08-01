import game_parameters


class Bomb:
    def __init__(self):
        x, y, radius, time = game_parameters.get_random_bomb_data()
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__time = time
        self.__color = "red"

    def get_color(self):
        return self.__color

    def update_color(self):
        self.__color = "orange"

    def update_orange_list(self, radius):
        if radius == 0:
            return [(self.__x, self.__y)]
        orange = []
        for i in range(radius + 1):
            if 0 <= self.__x + i < game_parameters.WIDTH and 0 <= self.__y + radius - i < game_parameters.HEIGHT:
                orange.append((self.__x + i, self.__y + radius - i))
            if 0 <= self.__x + i < game_parameters.WIDTH and 0 <= self.__y - radius - i < game_parameters.HEIGHT:
                orange.append((self.__x + i, self.__y - radius + i))
            if 0 <= self.__x - i < game_parameters.WIDTH and 0 <= self.__y + radius - i < game_parameters.HEIGHT:
                orange.append((self.__x - i, self.__y + radius - i))
            if 0 <= self.__x - i < game_parameters.WIDTH and 0 <= self.__y - radius + i < game_parameters.HEIGHT:
                orange.append((self.__x - i, self.__y - radius + i))
        return orange

    def get_time(self):
        return self.__time

    def get_radius(self):
        return self.__radius

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

# b = Bomb()
# print(b.update_orange_list(0))
# print(b.update_orange_list(1))
# print(b.update_orange_list(2))
