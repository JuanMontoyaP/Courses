import random
import os

def read_words():
    with open("./Python_Intermediate/archivos/data.txt", "r", encoding='utf-8') as f:
        words = [word.strip() for word in f]
    return words

def print_word(word_list):
    os.system('cls')
    print(" ".join(word_list))

def user_input():
    while True:
        letter = input("Input letter: ")
        if len(letter) != 1 or not letter.isalpha():
            print("Must enter a valid character")
        else :
            break
    return letter

def main():
    word = random.choice(read_words()).lower()
    # word = "Juan"
    guess = list('_'*len(word))
    tried_letters = []
    score = 0

    print_word(guess)

    while '_' in guess:
        
        while True:

            letter = user_input()

            if letter in tried_letters:
                tried = ', '.join(tried_letters)
                print(f'You already tried {letter} letter') 
                print(f'Letters tried = {tried}')
            elif letter in word :
                tried_letters.append(letter)
                for ind, lett in enumerate(word):
                    if (lett == letter):
                        guess[ind] = letter
                        score += 10

                break
            else :
                tried_letters.append(letter)
                score -= 5

                if score < 0: score = 0
                break
        
        print_word(guess)

    os.system('cls')
    print(f'Congratulations! You guess the word!: {word}')
    print(f'Your score is {score}')

if __name__ == "__main__":
    main()
