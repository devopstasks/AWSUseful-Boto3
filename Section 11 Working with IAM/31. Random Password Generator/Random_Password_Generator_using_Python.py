#The random password generator is useful while creating IAM user password.
from random import choice

len_of_password=8
valid_chars_for_password="abcdjkdwdjwdkk8378040*$$^*66t6(';'.,``~@#%*)_&%"

password=[]
'''
for each_char in range(len_of_password):
    password.append(choice(valid_chars_for_password))
random_pass="".join(password)
print(random_pass)
'''

random_pass="".join(choice(valid_chars_for_password) for each_char in range(len_of_password))
print(random_pass)
