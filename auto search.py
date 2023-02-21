import pyautogui
import random
from time import sleep
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def random_word():
    word_length=random.randrange(1,20)
    word=""
    for i in range(0,word_length):
        random_alphabet_index=random.randrange(0,25)
        word+=alphabet[random_alphabet_index]
    return word
n=1
word=""
while n<61:
    pyautogui.moveTo(random.randrange(300,450),random.randrange(125,130))
    pyautogui.click()
    with pyautogui.hold('ctrl'):
        pyautogui.press('a')
    pyautogui.press('backspace')
    pyautogui.click()
    word=random_word()
    pyautogui.write(word,interval=(random.randrange(1,3)/10))
    pyautogui.press("enter")
    sleep(random.randrange(1,5))
    n+=1
