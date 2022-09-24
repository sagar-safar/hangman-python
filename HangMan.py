import random
word_list = [["apple", "fruits"], ["banana", "fruits"], ["car", "vehicle"], ["bike", "vehicle"], ["scooter", "vehicle"], ["potato", "vegetable"], ["pencil", "stationery"], ["notebook", "stationery"], ["python", "coding_lan"], ["english", "language"], ["february", "month"]]
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(f"Welcome to {logo}\n")


chosen_word = random.choice(word_list)
lives_count = 7
set_ = set()
word_count = len(chosen_word[0])
N = word_count
display = ["⬜️"]*word_count
print(f"Field : {chosen_word[1]}\n")
print(" ".join(display))
print()
while word_count != 0 and lives_count != 0:
    guess = input("guess a letter : ")
    while guess in set_:
        print("you reentered a letter \n")

        guess = input("Guess a letter : ")

    flag = False
    for i in range(0, N):
        if chosen_word[0][i] == guess:
            word_count = word_count-1
            display[i] = guess+" "
            set_.add(guess)
            flag = True
    if not flag:
        print()
        print(f"You guessed a letter {guess} , that's not in the word. You lose a life")
        print(stages[lives_count-1])
        lives_count = lives_count-1
    print(" ".join(display))
    print()
if word_count == 0:
    print("Well Done! ")
else:
    print("Oops...you failed!")








