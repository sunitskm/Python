import sys
input_text = sys.argv[1]
list_inputs = input_text.split(',')
with open('user_input.txt','w') as file:
    for item in list_inputs:
        file.write(item+'\n')
