import random as r
correct  = "That's correct. Well Done!"
wrong = "Sorry! Wrong answer"
cont = "Y"
while cont == "Y":
        level = raw_input("Choose level(easy, intermediate,hard) ")
        print("The level is " + level)
        num_question = int(raw_input("Please give us the number of question "))
        print("Number of questions {0}".format(num_question))
        type_question = raw_input("Specify the question type (multiplication:M, addition:A, subtraction:S, division:D) ")
        list_nums = []
        answers = []
        if level == 'easy':
            for i in range(num_question):
                num1 = r.randrange(1,11)
                num2 = r.randrange(1,11)
                if type_question == 'M':
                        answers.append(num1*num2)
                if type_question == 'D':
                        answers.append(num1/num2)
                if type_question == 'A':
                        answers.append(num1+num2)
                if type_question == 'S':
                        answers.append(num1-num2)
                list_nums.append((num1,num2))
        if level == 'intermediate':
            for i in range(num_question):
                num1 = r.randrange(11,50)
                num2 = r.randrange(11,50)
                if type_question == 'M':
                        answers.append(num1*num2)
                if type_question == 'D':
                        answers.append(num1/num2)
                if type_question == 'A':
                        answers.append(num1+num2)
                if type_question == 'S':
                        answers.append(num1-num2)
                list_nums.append((num1,num2))
        if level == 'hard':
            for i in range(num_question):
                num1 = r.randrange(11,500)
                num2 = r.randrange(11,500)
                if type_question == 'M':
                        answers.append(num1*num2)
                if type_question == 'D':
                        answers.append(num1/num2)
                if type_question == 'A':
                        answers.append(num1+num2)
                if type_question == 'S':
                        answers.append(num1-num2)
                list_nums.append((num1,num2))
        print("Numbers are")
        print(list_nums)
        print("Answers are")
        print(answers)
        if type_question == "M":
            question = "multiplied by"
        if type_question == "D":
            question = "divided by"
        if type_question == "A":
            question = "added with"
        if type_question == "S":
            question = "Subtracted by"
        print ("Question Type {0}").format(type_question)
        for i in range(num_question):
            try:
                ans = input("What is %d %s %d "%(list_nums[i][0],question,list_nums[i][1]))
                if(ans == answers[i]):
                    print correct
                else:
                    print wrong
            except:
                print(wrong)
        choice = raw_input ("Do you want to play again? Y/N ")
        if choice == "N":
            cont = "N"
else:
    print "Bye. Play again"
