import os
import sys
import time
import string
from contextlib import suppress


exit_command_list = ['exit', 'e', 'leave', 'back', '-exit', '-e', '-back', '-leave']

def is_digit(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True
    
    
def valid_int_input():
    n = 'wrong'
    while is_digit(n) == False:
        n = input('>')
        if n in exit_command_list:
            main()
        
        if is_digit(n) == False:
            print('Must be a digit')
            time.sleep(1)
            print ("\033[A                             \033[A")
            print ("\033[A                             \033[A")
        else:
            return int(n)


def cipher():
    txt = input('Input sentence to cipher:\n>')
    if txt in exit_command_list:
        main()
    os.system('cls')
    print('How many shifts?')
    shift = abs(valid_int_input())
    alphabet = string.ascii_lowercase
    new_txt = []
    
    for char in txt:
        if char.lower() not in alphabet:
            new_txt.append(char)
        else:
            index = alphabet.find(char.lower())
            new_index = index + shift

            if new_index // 26 >= 1:
                new_index -= 26 * (new_index // 26)
            
            if char in alphabet.upper():
                new_txt.append(alphabet[new_index].upper())
            else:
                new_txt.append(alphabet[new_index])
    
    new_txt = ''.join(new_txt)
    print('-' * 20)
    print(f'{new_txt}')
    print('-' * 20)
    input('Press enter to continue')


def decipher():
    txt = input('Input sentence to decipher:\n>')
    if txt in exit_command_list:
        main()
    os.system('cls')
    print('How many shifts?')
    shift = abs(valid_int_input())
    alphabet = string.ascii_lowercase
    new_txt = []
    
    for char in txt:
        if char.lower() not in alphabet:
            new_txt.append(char)
        else:
            index = alphabet.find(char.lower())
            new_index = index + shift * -1

            if abs(new_index) // 26 >= 1: 
                new_index -= 26 * (new_index // 26)
            
            if char in alphabet.upper():
                new_txt.append(alphabet[new_index].upper())
            else:
                new_txt.append(alphabet[new_index])

    new_txt = ''.join(new_txt)
    print('-' * 20)
    print(f'{new_txt}')
    print('-' * 20)
    input('Press enter to continue')
    
# iterates through every possible shift
def bruteforce():
    txt = input('Input sentence to decipher:\n>')
    alphabet = string.ascii_lowercase
    results = []
    
    for shift in range(1, 26):
        new_txt = []
        
        for char in txt:
            if char.lower() not in alphabet:
                new_txt.append(char)
            else:
                index = alphabet.find(char.lower())
                new_index = index + shift

                if abs(new_index) // 26 >= 1: 
                    new_index -= 26 * (new_index // 26)
                if char in alphabet.upper():
                    new_txt.append(alphabet[new_index].upper())
                else:
                    new_txt.append(alphabet[new_index])
        
        new_txt = ''.join(new_txt)
        results.append(new_txt)
    
    index = -1
    display = []
    print('-'*20)
    for sentence in results:
        index += 1
        if len(sentence) > 20:
            display.append(f'{index+1}. {sentence[0:21]}')
        else:
            display.append(f'{index+1}. {sentence}')
           
    for index, line in enumerate(display):
        if index < 9:
            print(' ' + line)
        else:
            print(line)
    
    choice = 'wrong'
    in_range = False
    while is_digit(choice) == False:
        
        print('-' * 20)
        choice = input('Type index to show full text or type exit to skip\n>')
        print('-' * 20)
        os.system('cls')
        
        for line in display:
            print(line)
        
        if is_digit(choice) == False:
            
            if choice.lower() in exit_command_list:
                break
            print('-' * 20)
            print('Must be a digit')
            time.sleep(1)
            print ("\033[A                             \033[A")
        else:
            while int(choice) not in range(1, 26):
                print('-' * 20)
                print('This index does not exist')
                time.sleep(1)
                print('-' * 20)
                print ("\033[A                             \033[A")
                print ("\033[A                             \033[A")
                choice = input('Type number to show full text\nWrite exit to skip\n>')
                if choice.lower() in exit_command_list:
                    main()
                else:
                    choice = int(choice)
            else:
                os.system('cls')
                print('-' * 3)
                print(results[int(choice) - 1])
                print('-' * 3)
                time.sleep(2)
                input('Press enter to continue')


def info():
    text = ('''In cryptography, a Caesar cipher  is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed
number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A,
E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
''')
    print(text)
    input('Press enter to continue')
       

def main():
    header = f"{'-' * 34}\nCaesar Cipher Tool by Wiktor Fałek\ngithub.com/wiktor-falek\n{'-' * 34}"
    commands = 'Available commands:\n\n-cipher\n-decipher\n-bruteforce\n-info\n-exit\n>'
    
    while True:
        os.system('cls')
        print(header)
        choice = input(commands).lower()
        os.system('cls')
        if choice.lower() in exit_command_list:
            os.system("taskkill /f /im cmd.exe")
            exit()
        elif choice in ['cipher', '-cipher', 'c', '-c']:
            cipher()
        elif choice in ['decipher', '-decipher', 'd', '-d']:
            decipher()
        elif choice in ['bruteforce', '-bruteforce', 'b', '-b']:
            bruteforce()
        elif choice in ['info', '-info', 'i', '-i']:
            info()
        else:
            os.system('cls')
            print(header)
            print(commands)
            print('Wrong command')
            time.sleep(1)


while True:
    # prevents ctrl+c and ctrl+z crash
    with suppress(KeyboardInterrupt, EOFError):
            main()
        

            
    
    
    
