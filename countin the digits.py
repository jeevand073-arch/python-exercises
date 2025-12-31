#asking input form users

num = int(input('enter the numbers'))
  
count = 0

n = abs(num) #handle the negative number


if n == 0 :
    count = 1
else:
    while n > 0 :
        n= n//10 #reve the last digit
        count = count +1

print('the totoal number is',count)
