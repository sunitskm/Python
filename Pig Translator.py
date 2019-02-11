pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
   word  = original.lower()
   first = word[0]
   new_word = word + first + "ay"
   new_word = new_word[0:len(new_word)]
   print new_word
else:
    print 'empty'