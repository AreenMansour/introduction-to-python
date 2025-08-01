from hangman_helper import *

LOWER_LET = "qwertyuiopasdfghjklzxcvbnm"


def update_word_pattern(word, pattern, letter):
    new_pattern = ""
    for i in range(len(pattern)):
        if word[i] == letter:
            new_pattern += letter
        else:
            new_pattern += pattern[i]
    return new_pattern


def run_single_game(word_list, score):
    word = get_random_word(word_list)
    wrong_guess_lst = []
    pattern = '_' * len(word)
    msg = "start play"
    while score > 0 and pattern != word:
        display_state(pattern, wrong_guess_lst, score, msg)
        choice = get_input()
        if choice[0] == LETTER:
            if len(choice[1]) > 1 or choice[1] not in LOWER_LET:
                msg = "the letter you choose incorrect"
            elif choice[1] in pattern:
                msg = "you choose this incorrect letter before!"
            elif choice[1] not in word and choice[1] not in wrong_guess_lst:
                msg = "wrongggg!"
                score -= 1
                wrong_guess_lst.append(choice[1])
            elif choice[1] in word:
                pattern = update_word_pattern(word, pattern, choice[1])
                score -= 1
                sum_letter = 0
                for i in range(len(word)):
                    if choice[1] == word[i]:
                        sum_letter += 1
                score += ((sum_letter * (sum_letter + 1)) // 2)
        elif choice[0] == WORD:
            score -= 1
            if choice[1] == word:
                sum_letter = pattern.count("_")
                score += ((sum_letter * (sum_letter + 1)) // 2)
                pattern = word
        elif choice[0] == HINT:
            score -= 1
            lst_filt = filter_words_list(word_list, pattern, wrong_guess_lst)
            if len(lst_filt) > HINT_LENGTH:
                lst_updated = []
                n = len(lst_filt)
                for i in range(HINT_LENGTH):
                    lst_updated.append(lst_filt[int((i * n) // HINT_LENGTH)])
                lst_filt = lst_updated
            show_suggestions(lst_filt)
            msg = "do you want a hint"
        if score == 0:
            msg = "you looose :(" + word
        elif score > 0:
            msg = "congrats!!!"
    display_state(pattern, wrong_guess_lst, score, msg)
    return score


def main():
    lst_word = load_words()
    score = run_single_game(lst_word, POINTS_INITIAL)
    sum_letter_rounds = 1
    flag_game = True
    while flag_game:
        msg = f"you played {sum_letter_rounds} times and your  score is {score}"
        if score > 0:
            if play_again(msg) is True:
                sum_letter_rounds += 1
                score = run_single_game(lst_word, score)
            else:
                flag_game = False
        elif score == 0:
            if play_again(msg) is True:
                sum_letter_rounds = 1
                score = POINTS_INITIAL
                score = run_single_game(lst_word, score)
            else:
                flag_game = False


def count(word, letter):
    counter = 0
    for i in range(len(word)):
        if word[i] == letter:
            counter += 1
    return counter


def filter_words_list(words, pattern, wrong_guess_lst):
    lst = []
    for word in words:
        if len(word) == len(pattern):
            x = True
            for i in range(len(word)):
                n1 = count(word, pattern[i])
                n2 = count(pattern, pattern[i])
                if pattern[i] in LOWER_LET and n1 != n2:
                    x = False
                if pattern[i] in LOWER_LET and word[i] != pattern[i]:
                    x = False
            if x:
                add = True
                for i in range(len(word)):
                    if word[i] in wrong_guess_lst:
                        add = False
                if add is True:
                    lst.append(word)
    return lst



