import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
#Helper function to do a case insensitive check
def helper(word1,word2,curr_ratio):
    if(SequenceMatcher(None,word1,word2).ratio()>curr_ratio and (SequenceMatcher(None,word1,word2).ratio()>0.8) or SequenceMatcher(None,word1.title(),word2).ratio()>curr_ratio and (SequenceMatcher(None,word1.title(),word2).ratio()>0.8) or SequenceMatcher(None,word1.upper(),word2).ratio()>curr_ratio and (SequenceMatcher(None,word1.upper(),word2).ratio()>0.8)):
        return (True)
    return (False)


data = json.load(open('data.json'))
word = input('\nEnter a word: ')
meaning = []
best_word = ""
match_ratio = 0
#print(word)
formatted_word = word.lower()
#data_keys = [i .lower() for i in data.keys()]
#print (data_keys)
#print(formatted_word)
#checking if work is in keys
if word.upper() in data:
    meaning = data[word.upper()]
if word.title() in data:
    meaning = data[word.title()]
if formatted_word in data:
    #storing the meaning in a variable
    meaning = data[formatted_word]
if len(meaning)>0:
    print("Definition")
    #multiple meanings of same word
    for i in meaning:
        print(i)
else:
    #finding closest word
    #scan through all the keys to get the one with the best ratio
    for key in data:
        if(helper(formatted_word,key,match_ratio)):
            match_ratio = max([SequenceMatcher(None,formatted_word,key).ratio(),SequenceMatcher(None,formatted_word.upper(),key).ratio(),SequenceMatcher(None,formatted_word.title(),key).ratio()])
            best_word = key
    if best_word != "":
        print('Did you mean ' + best_word + ' instead of ' + word + '?')
            #print('Y/N')
        response = input('Y/N\n')
        if response.upper() == 'N':
            print("No such word exists")
        else:
            meaning = data[best_word]
            print("Definition")
            for i in meaning:
                print(i)
    else:
        print("No such words exist. Please check")

#print(get_close_matches(formatted_word,data.keys())[0])
