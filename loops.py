
# count = 1
# while count <= 5 : (stop[ing condition)
#     print("hello world")
#     count = count + 1
    
# print(count)


# i = 1
# while i <= 1000: #initilization
#     print("Aashish",i)
#     i = i + 1

# print(i)


#print number from 1 to 5
# i = 5
# while i >= 1 :
#     print(i)
#     i = i - 1

# print("loop ended")


# practice questions ; 1 ==> print 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i = i+1

# print("loop ended")

# question 2 ==> : print 100 to 1
# i = 100
# while i >= 1 :
#     print(i)
#     i = i - 1

#question 3 ==>print the multipli table of a number 3: in loop
# n = int(input("enter number : \n"))
# i = 1
# while i <= 10 :
#     print(n * i)
#     i = i + 1

#question 4 ==>: print the elements of the following list using a loop
# nums = [1,4,9,16,25,36,49,64,81,100]

# i = 0
# while i < len(nums):
#     print(nums[i])
#     i +=1

# heroes= ["ironman", "Batman", "superman"]

# i = 0
# while i < len(heroes):
#     print(heroes[i])
#     i += 1

# question 5 ==> ;search for number x = anynumb from in this tuple using loop;
# numbs = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 81)

# x = 25

# i = 0
# while i < (len(numbs)):
#     if(numbs[i]== x):
#        print('found at idx',i)
#        break
#     else:
#         print("finding")
#     i +=1
# print("ended of lopop")

# two important keyword in loop break and continue ==> break and continue.

# i = 1
# while i <= 5:
#     print(i)
#     if(i==4): 
#         break
#     i =i + 1


# i = 1
# while i<=5:
#     print(i)
#     if(i == 3):
#         break  #output is = instruction thgen it break there.and you out of the loop
#     i = i + 1

# print("end of loop")
    

# i = 0
# while i<=10:
#     if(i%2 == 0): #odd/even numberr print
#         i = i + 1
#         continue    # act as skip
#     print(i)
#     i = i + 1

# print("end of loop")
    

################## For looop: its means travel in sequence 
# list = [1,2,3,4,5]

# for el in list:
#     print(el)

# veggies = ["potato","brinjal","ladyfinger"]

# for value in veggies:
#     print(value)

# ####you can create tuple:
# nums=(1,2,3,4,5,6,6)

# for value in nums:
#     print(el)


# ####you can create str:
# str=("aashish") 
# for char in str:  #for print individual char
#     print(char)

#### for loop with else:
# str=("aashish")

# for char in str:
#     if(char == 'h'):
#         print("h found")
#         break       #else doesnot execute in break function
#     print(char)
# else:
#     print("end")

#practice question 1 :

# nums = [1,4,9,16,25,36,49,64,81,100]

# for el in nums:
#     print(el)

########question in tuple find x :(this way is called linear seach, serch one by one in single line)

# nums = [1,4,9,16,25,36,49,64,81,100,16]
# x = 16
# idx = 0

# for el in nums:
#     if(el==x):
#         print("number found at idx", idx) #you cant print indx here so you have to aasign value
#         break
    # idx = idx + 1
##thats how for loop work with our built in data type


#############################
# range():
# print(range(5))

# for i in range(10):
#     print(i)

# for i in range(2 , 10): #range (start inclu, stop not includ)
#     print(i)


# for i in range(2 ,10, 2): #range (start,stop,step):
#     print(i)


##how to print odd and even number using range loop:
# for i in range(2,101,2):  #(print even by using logic)
#     print(i)

# for i in range(1,101,2):  #(print odd using logic)
#     print(i)
#####################################################################

# lets practice using range and for: question 1
# for i in range(101):
#     print(i)

# for i in range(100, 0, -1): #thats how you print decreasing numbr:
#     print(i)


# n = int(input("ener number :\n")) #print table using range

# for i in range(1, 11):
#     print(n * i)

#############################################
# pass statement:pass is a null statement that does nothing.it isn used as a place holder
# for future code

# n = 7  # thats how you calculate sum of n

# sum = 0
# for i in range(1, n+1):
#     sum += i

# print("total sum =",sum)




