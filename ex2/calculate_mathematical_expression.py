#############################################################
# FILE : calculate-mathematical_expression.py
# WRITER : Areen_Mansour , Areen0507 , 212900211
# EXERCISE : intro2cs1 ex2 2021
# DESCRIPTION : A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH:
#
# WEB PAGES I USED:
# NOTES : ...
#############################################################

def calculate_mathematical_expression(num1, num2, ex):
    """
    :param num1: float
    :param num2: float
    :param ex: str
    :return: float
    calculate num1 and num2 according to the expression that he give us in the exercise. if we calculate num1 and num2
    it must to be a float number but if we divided by zero or use another expression that's not defined in the exercise
    we will get None
    """
    if ex == "+":
        return num1 + num2
    if ex == "-":
        return num1 - num2
    if ex == "*":
        return num1 * num2
    if ex == ":":
        if num2 == 0:
            return None
        return num1 / num2
    return None


def calculate_from_string(string):
    """
    :param string: str
    :return: float
    the function returns the calculation value of the expression in the order of the numbers in the string
    """
    lst = string.split(" ")
    return calculate_mathematical_expression(float(lst[0]), float(lst[2]), lst[1])

