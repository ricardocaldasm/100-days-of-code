import random_word

print(
    r"""
 _   _   ___   _   _ _____ ___  ___  ___   _   _ 
| | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |
| |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |
|  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |
| | | || | | || |\  | |_\ \| |  | || | | || |\  |
\_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/
"""
)

# criando a palavra
# word = random_word.RandomWords().get_random_word()
word = "asd"
print(word)

# criando a lista com cada letra da palavra
word_list = list()
for p in word:
    word_list.append(p)

print(word_list)

# criando a lista com underline de cada letra
underline = list()
for i in range(len(word)):
    underline.append("_")

lose_life = 6

while True:
    # mostrando a lista de underline
    for p, v in enumerate(underline):
        print(v, end=" ")

    # mostrando o número de letras da palavra
    print(f"({len(underline)})", "\n")

    # entrada da letra
    letter = str(input("Guess a letter: "))

    # checando se a letra escolhida faz parte da lista da palavra
    if letter in word:
        for p, v in enumerate(word_list):
            if letter == v:
                underline[p] = letter
    else:
        print("FORCA")  # fazer a forca
        lose_life -= 1
        if lose_life == 0:
            print("GAME OVER")
            break

    if r"_" not in underline:
        print("YOU WIN!")
        break
