import string

letters = string.ascii_lowercase
encoded_message = input().split()
shift = 3
decoded_message = ''
for j in encoded_message:
    for i in range(len(letters)):
        if j == letters[i]:
            if i + shift < len(letters):
                decoded_message += letters[i + shift]
            else:
                decoded_message += letters[i + shift - len(letters)]
print(decoded_message)
