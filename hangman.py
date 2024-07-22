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
word_list = ["ackward","baboon","pissed"]
import random
chosen_word = random.choice(word_list)
print(f"the chosen word is:{chosen_word}")
end_of_game = False
lives=6

display = []
for _ in range(len(chosen_word)):
    display+='_'

while not end_of_game:   
    guess = input("guess a letter:").lower()


    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess  not in chosen_word:
            lives-=1
            if lives == 0:
                end_of_game = True
                print("you lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
      end_of_game = True
      print("you win.")
print(stages[lives])       