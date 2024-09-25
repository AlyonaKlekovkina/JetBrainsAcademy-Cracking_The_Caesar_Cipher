# Write your code here
string = ''
inp = input().split(' ')
for i in inp:
    letter = chr(int(i) + 97)
    string += letter
print(string)
