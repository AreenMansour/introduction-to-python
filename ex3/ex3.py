##################################################
# FILE : EX3.PY
# WRITER : Areen_Mansour , Areen0507 , 212900211
# EXERCISE : Intro2cs2 ex3 2021
#
# STUDENTS I DISCUSSED THE EXERCISE WITH:
#
#
# NOTES: ...
##################################################


def input_list():
    lst = []
    n = input()
    sum = 0
    while n != "":
        s = float(n)
        lst.append(s)
        sum = sum + s
        n = input()
    lst.append(sum)
    return lst


def inner_product(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        return None
    if vec_1 == [] or vec_2 == []:
        return 0
    counter = 0
    for i in range(len(vec_1)):
        counter = counter + vec_1[i] * vec_2[i]
    return counter


def sequence_monotonicity(sequence):
    lst = []
    if sequence == [] or len(sequence) == 1:
        return [True, True, True, True]
    i = 1
    x = True
    while i != len(sequence):
        if sequence[i-1] > sequence[i]:
            x = False
        i = i + 1
    lst.append(x)
    i = 1
    x = True
    while i != len(sequence):
        if sequence[i-1] >= sequence[i]:
            x = False
        i = i + 1
    lst.append(x)
    i = 1
    x = True
    while i != len(sequence):
        if sequence[i-1] < sequence[i]:
            x = False
        i = i + 1
    lst.append(x)
    i = 1
    x = True
    while i != len(sequence):
        if sequence[i-1] <= sequence[i]:
            x = False
        i = i + 1
    lst.append(x)
    return lst


def monotonicity_inverse(def_bool):
    if sequence_monotonicity([1, 2, 3, 3]) == def_bool:
        return [1, 2, 3, 3]
    if sequence_monotonicity([1, 2, 3, 4]) == def_bool:
        return [1, 2, 3, 4]
    if sequence_monotonicity([4, 3, 2, 1]) == def_bool:
        return [4, 3, 2, 1]
    if sequence_monotonicity([1, 2, 0, 5]) == def_bool:
        return [1, 2, 0, 5]
    if sequence_monotonicity([1, 1, 1, 1]) == def_bool:
        return [1, 1, 1, 1]
    if sequence_monotonicity([4, 1, 1, 0]) == def_bool:
        return [4, 1, 1, 0]
    return None

def is_prime(n):
    divisers = [i for i in range(round(n**0.5 + 1)) if i > 1]
    for d in divisers:
        if n % d == 0:
             return False
    return n!=1


def primes_for_asafi(n):
    if n == 0:
        return []
    prime_lst = [2]
    i = 3
    while len(prime_lst) != n:
        if is_prime(i):
            prime_lst.append(i)
        i += 1
    return prime_lst


def sum_of_vectors(vec_lst):
    if vec_lst == []:
        return None
    elif vec_lst[0] == []:
        return []
    else:
        n = len(vec_lst[0])
        vec_len = len(vec_lst)
        result = []
        for i in range(n):
            x = 0
            for j in range(vec_len):
                x += vec_lst[j][i]
            result.append(x)
        return result


def num_of_orthogonal(vectors):
    count_vector = 0
    for i in range(len(vectors)-1):
        for j in range(i + 1, len(vectors)):
            if inner_product(vectors[i], vectors[j]) == 0:
                count_vector = count_vector + 1
    return count_vector


