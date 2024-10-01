import string


def get_positions(word, encoded_word):
    positions_list = []
    for i in range(len(encoded_word)):
        first_word_index = letters.index(encoded_word[i])
        second_word_index = letters.index(word[i])
        shift =  second_word_index - first_word_index
        positions_list.append(shift)
    return positions_list


def decode_message(len_of_keyword, target_message, the_code):
    alphabet_lenght = len(letters)
    start = 0
    end = len_of_keyword
    decoded_word = ''
    while end < len(target_message) + len_of_keyword:
        substring = target_message[start: end]
        for i in range(len(the_code)):
            pos_message = letters.index(substring[i])
            shift_pos = the_code[i]
            decoded_letter_position = (pos_message) + (shift_pos)
            if decoded_letter_position > alphabet_lenght - 1:
                decoded_letter_position = decoded_letter_position - alphabet_lenght
                decoded_letter = letters[decoded_letter_position]
            else:
                decoded_letter = letters[decoded_letter_position]
            if decoded_letter == 'x':
                decoded_word += ' '
            else:
                decoded_word += decoded_letter
            if len(decoded_word) == len(target_message):
                break
        start += len_of_keyword
        end += len_of_keyword
    return decoded_word


letters = string.ascii_lowercase
len_of_keyword = int(input())
word = input().split()
encoded_word = input().split()
target_message = input().split()
shifts_list = get_positions(word, encoded_word)
the_code = shifts_list[:len_of_keyword]
print(decode_message(len_of_keyword, target_message, the_code))
