# from board import*
from snake import*

class Apple:
    def __init__(self,location, score):
        self.__location = location
        self.__score = score
    def get_score(self):
        return self.__score
    def get_location(self):
        return self.__location



