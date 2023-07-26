for num in range (101):
    string = ""

    if num % 3 == 0:
        print ('Fizz')
    if num % 5 == 0:
        print ('Buzz')    
    if num % 3 !=0 and num % 5 !=0:
        string = string + str(num)
    print (string)