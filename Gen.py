class generate_password:    
    print('Hello, welcome to the password generator! This is my attempt at making a password generator.')
    print('My goal in this project is to apply my knowledge of for loops and if statements')
    length= input('How long would you like your password to be?')
    numbers= input('Would you like numbers in your password? (y/n)')
    letters= input('Would you like letters in your password? (y/n)')
    special= input('Would you like special characters in your password? (y/n)')
    if letters == 'y':
        upper= input('Would you like uppercase letters in your password? (y/n)')
        lower= input('Would you like lowercase letters in your password? (y/n)')
        #password will be a string
    import random
    alphabet = [chr(i) for i in range(97, 123)]
    char = "! # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~"
    characters = char.split(" ")
    password= ""
    usable =[]
    if letters=="y":
        if upper == 'y':
            for i in alphabet:
                usable.append(i.upper())
        if lower == 'y':
            for i in alphabet:
                usable.append(i.lower())
    if numbers == 'y':
        for i in range(0,10):
            usable.append(str(i))
    if special == 'y':
        usable +=characters
    for i in range(int(length)):
        password+= usable[random.randint(0,len(usable)-1)]


      
    for i in range(4):
        print()
    print("here is your password: "+password)
            



