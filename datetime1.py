import datetime

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d"))
now_day = now.day
now_month = now.month
now_year = now.year
curr_date = str(now_month) + '-' + str(now_day) + '-' + str(now_year)
print (curr_date)
filename =  curr_date + 'status.txt'
print(filename)
with open(filename,'w') as file:
    file.write("This file is dated now")
