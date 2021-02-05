import os
import random as rd

DatePath = "./words.txt"
Random_rate = 0.3 #30%

class reciteWords(object):
    def __init__(self, theWords: str):
        self.theWords = theWords.rstrip("\n")
        self.wordsArray = theWords.rstrip("\n").split(" ")

    def Println(self):
        def blodText(s: str): return '\033[1m' + s + '\033[0m'
        print(" Question: " + blodText(self.wordsArray[2]))
        self.Answers()
        self.Tonext()

    def Answers(self):
        answers_input = input("\n Your answers['a' to see the answers]: ")
        if answers_input == 'a': print('\n The Answers: ', self.theWords)
        elif answers_input == self.wordsArray[0]: print('\033[1;32m', 'Good job!', '\033[0m')
        else: print('\033[1;31m', 'Error!', '\033[0m')

    def Tonext(self):
        continue_or_exit = input("\n Do you want to continue or exit?['q' to exit]: ")
        if continue_or_exit == 'q':
            print('\033[1;32m', 'Goodbye!', '\033[0m')
            exit(0)


with open(DatePath, 'r') as words:
    os.system('clear')
    number_of_words = int(input(" Input number of words[Max: 20, '0' to exit]: "))
    while(number_of_words >= 20):
        print('\033[1;31m', 'Number is very big', '\033[0m')
        number_of_words = int(input("\n Input number of poem[Max: 20]: "))
    count, random_max_num = 0, int(1/Random_rate) - 1
    for i in words.readlines():
        if count == number_of_words: break
        os.system('clear')
        random_number = rd.randint(1, random_max_num)
        if random_number == 1:
            count += 1
            ob = reciteWords(i)
            ob.Println()
    if number_of_words == 0:
        print('\033[1;31m', 'What are you doing?', '\033[0m')
    else:
        print('\033[1;32m', 'You are great!You passed!😎', '\033[0m')
