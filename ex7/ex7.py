##################################################################
# FILE : ex7.py
# WRITER : Areen_Mansour , Areen0507 , 212900211
# DESCRIPTION : A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH:
#
# WEB PAGES I USED : https://youtu.be/0u7g9C0wSIA
# NOTES: ...
##################################################################
from typing import List, Any
import ex7_helper


def mult(x: float, y: int) -> float:
    if y == 0:
        return 0
    else:
        m = ex7_helper.add(mult(x, ex7_helper.subtract_1(y)), x)
        return m


def is_even(n: int) -> bool:
    return is_even_helper(n, 0)


def is_even_helper(n: int, i: int) -> bool:
    if n == i:
        return True
    if n == i + 1:
        return False
    return is_even_helper(n, i+2)


def log_mult(x: float, y: int) -> float:
    if y == 0:
        return 0
    else:
        if ex7_helper.is_odd(y):
            m = log_mult(x, ex7_helper.divide_by_2(y))
            return ex7_helper.add(ex7_helper.add(m, m),x)
        else:
            m = log_mult(x, ex7_helper.divide_by_2(y))
            return ex7_helper.add(m, m)


def is_power_helper(res: int, x: int, b: int) -> bool:
    if res > x:
        return False
    if res == x:
        return True
    return is_power_helper(int(log_mult(res, b)), x, b)


def is_power(b: int, x: int) -> bool:
    if b == x:
        return True
    if b == 1 or b == 0:
        return False
    return is_power_helper(1, x, b)


def helper_reverse(s: str, m: int, w: str, k: str) -> str:
    if m < 0:
        k = w
        return k
    w = ex7_helper.append_to_end(w, s[m])
    return helper_reverse(s, m-1, w, k)


def reverse(s: str) -> str:
    if s == "":
        return ""
    return helper_reverse(s, len(s)-1, "", "")


def play_hanoi(Hanoi: Any, n: int, src: Any, dst: Any, temp:Any) -> None:
    if n <= 0:
        return
    if n == 1:
        Hanoi.move(src, dst)
    else:
        play_hanoi(Hanoi, n-1, src, temp, dst)
        play_hanoi(Hanoi, 1, src, dst, temp)
        play_hanoi(Hanoi, n-1, temp, dst, src)


def magic_list(n: int) -> List[Any]:
    if n == 0:
        return []
    return magic_h([], n)


def magic_h(lst: List[Any], n: int) -> List[Any]:
    if n == 0:
        return lst
    res = magic_h(lst, n-1)
    lst.append(magic_h([], n - 1))
    return res


def helper_helper(k: int, counter: int) -> int:
    if k == 0:
        return counter
    if k % 10 == 1:
        counter +=1
    return helper_helper(k // 10, counter)


def number_of_ones_helper(n: int, c: int) -> int:
    if n == 0:
        return c
    m = helper_helper(n, 0)
    return number_of_ones_helper(n-1,c+m)


def number_of_ones(n: int) ->int:
    return number_of_ones_helper(n,0)


def helper_2d_helper(li1: list[int], li2: list[int], booli: bool, j: int) -> bool:
    if j == len(li1):
        return True
    if len(li1) == 0 and len(li2) == 0:
        return booli
    if li1[j] != li2[j]:
        return False
    return helper_2d_helper(li1,li2,booli, j+1)


def compare_2d_lists_helper(l1: List[List[int]], l2: List[List[int]], booli: bool, i: int) -> bool:
    if booli is False:
        return False
    if i == len(l1):
        return True
    if len(l1[i]) != len(l2[i]):
        return False
    meme: bool = helper_2d_helper(l1[i], l2[i], True, 0)
    if not meme:
        return False
    return compare_2d_lists_helper(l1, l2, meme, i + 1)


def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    if len(l1) != len(l2):
        return False
    return compare_2d_lists_helper(l1, l2, True, 0)
