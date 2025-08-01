#############################################################
# FILE : temperature.py
# WRITER : Areen_Mansour , Areen0507 , 212900211
# EXERCISE : intro2cs1 ex2 2021
# DESCRIPTION : A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH:
#
# WEB PAGES I USED:
# NOTES : ...
#############################################################
def is_vormir_safe(t, td1, td2, td3):
    """
    :param t: float
    :param td1: float
    :param td2: float
    :param td3: float
    :return: true or false
    in this function we have to compare between the temperature and the rest of the temperature that we get on each day
    """

    if t < td1 and t < td2:
        return True
    elif t < td1 and t < td3:
        return True
    elif t < td2 and t < td3:
        return True
    else:
        return False
