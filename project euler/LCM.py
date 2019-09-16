#cerner_2^5_2019
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lcm = 1
print([i for i in numbers if i>1])
while(any([i != 1 for i in numbers])):
    remaining_numbers = [i for i in numbers if i>1]
    #print(remaining_numbers)
    if len(remaining_numbers) != 0:
        first_number = remaining_numbers[0]
        lcm = lcm * first_number
        #print(first_number)
        numbers = [i//first_number if i%first_number == 0 else i for i in numbers]
    #print(numbers)
print(lcm)
