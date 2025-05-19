import random
import string
import os

# get user input
wordlist = str(input("Location of the .txt file: "))

# check if file exists
print("Checking file...")
isExist = os.path.exists(wordlist)

if isExist == True:
    # read word lists
    with open(wordlist, 'r') as infile:
        words = infile.read().strip(' \n').split('\n')

    num = int(input("Number of words to generate: "))

    # generate usernames
    for i in range(num):

        # construct username
        word1 = random.choice(words)
        word2 = random.choice(words)

        # check if the number less than 10
        number = random.randint(1, 99)
        if (number < 10): number = "0" + str(number)

        # print the username
        username = '{}{}{}'.format(word1, word2, number)

        # success
        print(username)
else:
    print("Err: File does not exist!")
