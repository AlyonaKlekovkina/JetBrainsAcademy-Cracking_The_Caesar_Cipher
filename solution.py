import string


def secret_word_indexes(secret_word):
    list_of_indexes = []
    for i in secret_word:
        index = letters.index(i)
        list_of_indexes.append(index)
    return list_of_indexes


def input_indexes(first_input):
    list_of_input_indexes = []
    for i in first_input:
        index = letters.index(i)
        list_of_input_indexes.append(index)
    return list_of_input_indexes


def get_shitf(sw_index, inp_index):
    secret_word_to_check = []
    count = 0
    while count < 26:
        for i in sw_index:
            if i + count < 26:
                index = i + count
            else:
                index = (i + count) - 26
            secret_word_to_check.append(index)
        for i in range(len(inp_index)):
            start = 0
            end = len(sw_index)
            if secret_word_to_check == inp_index[start + i:end + i]:
                return count
        count += 1
        secret_word_to_check.clear()


def decode_message(letters, input, shift):
    decoded_message = ''
    for j in input:
        index = letters.index(j) + shift
        if index < len(letters):
            decoded_message += letters[index]
        elif index > len(letters):
            result = index - len(letters)
            decoded_message += letters[result]
    final_message = ''
    for i in decoded_message:
        if i == 'x':
            final_message += ' '
        else:
            final_message += i
    return final_message


letters = string.ascii_lowercase
first_input = input().split()
secret_word = 'butterscotch'
second_input = input().split()
sw_index = secret_word_indexes(secret_word)
inp_index = input_indexes(first_input)
decoded_shift = get_shitf(sw_index, inp_index)
print(decode_message(letters, second_input, -decoded_shift))
