"IMPORTS"

from Kata.Anagram.Word_List import Words as Word_List
from Kata.Anagram.Word_List import *

"Take in a name and generate a word list that matches the amount of letters."
name = "eli butler"

"Match the Number letters in name to a combination of letters and words in the word list."
Matching_List = Name_Number_Match(name)
# print(len(Matching_List))

"Now I must determine if this has a matching set of letters."
Letter_Match = Match_Letters(Matching_List, name)

# print(Letter_Match)

"Removing duplicate items."
No_Dups = Remove_Dups(Letter_Match)
# print("Duplicate Removal: ", No_Dups)

"""Printing Final Result"""
Final_Result(name, No_Dups)





