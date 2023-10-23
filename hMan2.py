import random
from words import word_list, stages, logo

print(logo)
display = []
chosen_word = random.choice(word_list)
num_chosen_word = len(chosen_word)

lives = 6
for i in range(num_chosen_word):
    display += "_"
end = False

while not end:
    letter = input("\nChoose a letter ")

    for j in range(len(chosen_word)):
        if letter == chosen_word[j]:
            display[j] = letter
    if not letter in chosen_word:
        lives = lives - 1

    print(stages[lives])
    print(f"{' '.join(display)}")

    if not "_" in display:
        end = True
        print("You win")
    if lives == 0:
        end = True
        print("You lose")
        print(f"The word was {chosen_word}")
