#############################################################
# FILE : shapes.py
# WRITER : Areen_Mansour , Areen0507 , 212900211
# EXERCISE : intro2cs1 ex2 2021
# DESCRIPTION : A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH:
#
# WEB PAGES I USED:
# NOTES : ...
#############################################################
import math


def shape_area():
    """
    :return: the size of the shape
    in this function we have to calculate the size of each one of the shapes that he gives to us in the the exercise
    """
    inp = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if inp != '1' and inp != '2' and inp != '3':
        return None
    if inp == '1':
        r = input()
        return float(r)**2 * math.pi
    if inp == '2':
        a = input()
        b = input()
        return float(a) * float(b)
    if inp == '3':
        x = input()
        return (math.sqrt(3) * float(x)**2) / 4
