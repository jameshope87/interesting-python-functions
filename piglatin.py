from time import sleep
def translate(word):
    word = word[1:] + word[0] + 'ay'
    return word
    
if __name__ == "__main__":
    print("Please enter a word...")
    word = input('>>').lower()
    while (not word.isalpha()) or len(word) <= 0:
        print("Sorry, please enter a valid string")
        word = input('>>')
    print("Thank you...")
    translated = translate(word)
    sleep(0.5)
    for i in range(3):
        print("Translating; please wait...")
        sleep(1)
    print("Your translated word is...")
    print(translated)
