#############################################################
# FILE : quadratic_equation.py
# WRITER : Areen_Mansour , Areen0507 , 212900211
# EXERCISE : intro2cs1 ex2 2021
# DESCRIPTION : A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH:
#
# WEB PAGES I USED:
# NOTES : ...
#############################################################
import math


def quadratic_equation(x, y, z):
    """
    :param x: coefficient
    :param y: coefficient
    :param z: coefficient
    :return: res1 nd res2
    in this function we want to check how many results we have in 3 situations and the easiest way is to find which case
    the answer belongs to
    """
    if y**2 - 4 * x * z > 0:
        res1 = (-y + math.sqrt(y**2 - 4 * x * z)) / 2 * x
        res2 = (-y - math.sqrt(y ** 2 - 4 * x * z)) / 2 * x
        return res1, res2
    if y**2 - 4 * x * z == 0:
        res1 = (-y) / 2 * x
        return res1, None
    if y**2 - 4 * x * z < 0:
        return None, None


def quadratic_equation_user_input():
    """
    :return: the answer of the quadratic function
    with the help of the function quadratic equation it is possible to know the requested answer in this function
    """
    inp = input("Insert coefficients a, b, and c: ")
    lst = inp.split(" ")
    if lst[0] == '0':
        print("The parameter 'a' may not equal 0")
    else:
        res1, res2 = quadratic_equation(float(lst[0]), float(lst[1]), float(lst[2]))
        if res1 is not None and res2 is not None:
            print("The equation has 2 solutions: " + str(res1) + " and " + str(res2))
        elif res1 is not None and res2 is None:
            print("The equation has 1 solution: " + str(res1))
        elif res1 is None and res2 is None:
            print("The equation has no solutions")

