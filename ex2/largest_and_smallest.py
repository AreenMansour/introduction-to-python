#############################################################
# FILE : largest_and_smallest.py
# WRITER : Areen_Mansour , Areen0507 , 212900211
# EXERCISE : intro2cs1 ex2 2021
# DESCRIPTION : A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH:
#
# WEB PAGES I USED:
# NOTES : ...
#############################################################
def largest_and_smallest(num1, num2, num3):
    """
    :param num1: float
    :param num2: float
    :param num3: float
    :return: largest and smallest one
    to know what the largest and the smallest number we have to do a comparison of each of two parameters and in the end
    it will return to us the largest and the smallest
    """
    largest = 1
    smallest = 0
    if num1 >= num2 and num1 >= num3:
        largest = num1
    if num2 >= num1 and num2 >= num3:
        largest = num2
    if num3 >= num1 and num3 >= num2:
        largest = num3
    if num1 <= num2 and num1 <= num3:
        smallest = num1
    if num2 <= num1 and num2 <= num3:
        smallest = num2
    if num3 <= num1 and num3 <= num2:
        smallest = num3
    return largest, smallest


def check_largest_and_smallest():
    """
    :return: boolean number
    in this function we have to check if it returns true or false according to the largest and the smallest number that
    we found from the function largest and smallest
    """

    largest1, smallest1 = largest_and_smallest(17, 1,  6)
    largest2, smallest2 = largest_and_smallest(1, 17, 6)
    largest3, smallest3 = largest_and_smallest(1, 1, 2)
    # this function call checks if our function is able to support two of the numbers being
    # identical and still return the correct value
    largest4, smallest4 = largest_and_smallest(8, 8, 4)
    largest5, smallest5 = largest_and_smallest(20, 12, 4)
    if largest1 != 17 or smallest1 != 1:
        return False
    if largest2 != 17 or smallest2 != 1:
        return False
    if largest3 != 2 or smallest3 != 1:
        return False
    if largest4 != 8 or smallest4 != 4:
        return False
    if largest5 != 20 or smallest5 != 4:
        return False
    return True
