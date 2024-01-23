'''Write a program that prompts the user to enter a word and checks if it is
a palindrome. A palindrome is a word that reads the same backward as
forward. Use string slicing and an if-else statement to compare the
original word with its reverse.'''



str_1 = input()
if str_1 == str_1[::-1]:
    print(True)
else:
    print(False)