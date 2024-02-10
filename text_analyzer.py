"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tereza Trojanová
email: trojanovate@gmail.com
discord: tereza4859
"""

#############set variables
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#registered users
users_dict = {
    "bob"  : '123',
    "ann"  : 'pass123',
    "mike"  : 'password123',
    "liz" : 'pass123'
    }

#numbers of text to be chosen by user to analyze
text_numbers = [1,2,3]

#############

#user input no1 -> user credentials
username = input('username: ')
password = input('password: ')

print("-"*40)

#check if provided credentials are valid
if username not in users_dict:
    print("Unregistered user, terminating the program..")
elif username in users_dict and users_dict[username] != password:
    print("Invalid password.")
elif username in users_dict and users_dict[username] == password:
    print("Welcome to the app, " + username + ".\nWe have 3 texts to be analyzed.")


    print("-"*40)

    #user input no2 -> select text
    input_number = input("Enter a number btw. 1 and 3 to select: ")

    print("-"*40)

    #if the input is valid, continue, if not, show the error message
    if input_number.isdigit() and int(input_number) not in text_numbers:
        print("Number is out of range. Please enter a number between 1 and 3.")
    elif input_number.isdigit() == False:
        print("Input is not a number. Please enter a number between 1 and 3.")
    elif input_number.isdigit() and int(input_number) in text_numbers:
        selected_text = texts[int(input_number)-1]

        #output of the text analyzer
        words = selected_text.split()
        words_stripped = [item.strip(".") for item in words]

        words_total = len(words_stripped)

        words_titlecase = 0
        words_uppercase = 0
        words_lowercase = 0
        numeric_strings = 0
        sum_of_numeric_strings = 0

        for word in words_stripped:
            if word.istitle():
                words_titlecase += 1
            elif word.isupper():
                words_uppercase += 1
            elif word.islower():
                words_lowercase += 1
            elif word.isdigit():
                numeric_strings += 1
                sum_of_numeric_strings += int(word)

        print("There are " + str(words_total) + " words in the selected text.")
        print("There are " + str(words_titlecase) + " titlecase words.")
        print("There are " + str(words_uppercase) + " uppercase words.")
        print("There are " + str(words_lowercase) + " lowercase words.")
        print("There are " + str(numeric_strings) + " numeric strings.")
        print("The sum of all the numbers " + str(sum_of_numeric_strings) + ".")

        print("-"*40)

        #data prep for word length occurance charts

        word_len_dict = {}

        words_total = len(words_stripped)

        for word in words_stripped:
            word_length = len(word)
            if word_length not in word_len_dict.keys():
                word_len_dict[word_length] = 1
            elif word_length in word_len_dict.keys():
                word_len_dict[word_length] += 1

        #################### chart version 1 ####################

        print("LEN|  OCCURENCES  |NR.")

        col1_width = len("LEN")
        col2_width = len("  OCCURENCES  ")

        word_len_dict_sorted = dict(sorted(word_len_dict.items()))

        max_length = max(word_len_dict_sorted.keys())

        plot_width = max_length + 1

        for i in word_len_dict_sorted:
        #  if len(str(i)) == 1:
            print(" "*(col1_width-len(str(i))) + str(i) + "|" + word_len_dict_sorted[i]*"*" + (col2_width-word_len_dict_sorted[i])*" " + "|" + str(word_len_dict_sorted[i]))
        #  else:
        #    print(" "*1 + str(i) + "|" + word_len_dict_sorted[i]*"*" + (plot_width-word_len_dict_sorted[i])*" " + "|" + str(word_len_dict_sorted[i]))

        #################### chart version 2 ####################

        print("-"*40)
        print()

        import numpy as np
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()

        y_values = list(word_len_dict_sorted.keys())
        x_values = list(word_len_dict_sorted.values())

        plt.barh(y_values, x_values, color ='teal')

        plt.xticks(np.arange(1,max(word_len_dict_sorted.values())+1, step=1))
        plt.yticks(np.arange(1,max(word_len_dict_sorted.keys())+1, step=1))

        ax.invert_yaxis()

        plt.xlabel("Number of word length occurences")
        plt.ylabel("Word length")
        plt.show()
