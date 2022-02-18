         ###Disclaimer###
#If there is print(input("what is your name")[0])
#it will never print "w" as output it will always print the value that u wrote after executing the code" example:-
#print(input("two number digit\n")[0])


           #Data Types

#1: Strings
#Ex. any character in "" so "hello"
#print("Hello"[0])
#print("Shwetank"[4])

#2: Integer
#print( 12 + 12)
#as we put comma in between of large number like 1,212,121 we can do same in coding like 1_212_121 and its equivalent of something written as 1212121

#3: Float
#For decimals 

#4: Boolean
#these are only two:-
#True
#False

               #Type
#We can check what type of thing is in the code example:-
#Num = 123
#print(type(Num))
#that code with give answer as that thing is INTEGER, cuz its INTEGER
#print(type(len("welcome")))
#so it proves that len() is a <class 'int'>

#Sus = len(input("what is your name"))
#print("our name have" + Sus + " Characters.")
#The whole thing under print will show error as there are two type of things 'strings' and Integers. and code cant print two things together, like this.
#Now how to print all these strings and integers together, so Example:-
#str called string fucntion converts anything to string.
#Sus = len(input("What is your name?"))
#New_Sus = str(Sus)
#print("Your name have " + New_Sus + " characters."

         #Type Conversiton :-
#like we saw, we converted int into str datatype, similarly we can do for many, like:-

#1.a
# a = float(0.34)
# b = str(a)
# print(b)
#1.b
# print(float(3.4))
# both are same 1.a and 1.b.

#2.a
#a = "123"
#print(type(a))
#2.b
#a = str(123)
#print(type(a))
# are same.

#3.a
#print(23 + 23.3)
#3.b
#print(23 + float(23.3))
#3.c
#print(23 + float("23.3"))
#are all same.

#4
#if data type is in string or float or anything and you wanna convert into integer then use int()



      #Mathematical Operations
#+ , - , / , * , ** = exponent(If you wanna raise power to any number)
     #Order of Priority
#PEMDAS
#Parentheses
#Exponent
#Mutiplication
#Division 
#Addition 
#Substraction
# (* /) are equally important
# (+ -) are equally important
#and calculation happen from left to right 
#Example:-
#print(3 * 3 + 3 / 3 - 3)
#So answer is 7 cuz first 3*3 = 9 then 3/3 = 1 then 9 + 1 = 10 then 10 - 3 = 7

      #Rounding the number
#you can round number by using round() function
#Example:-
#print(round(19/5))
#You can also add till how many decimals you wanna round like:-
#print(round(8/3, 2)) it will round the output to two decimal places only

        #Important Notes:-
#1: when we use / then it divides number in float formate, but if we want it to divide and in integer we can use //.
#Example print(4//2) 
#2: If we wanna add, divide, multiply, substract number from the the number thats already there we can simply use, +=, /=, *=, -= . 
#Example 1: 
#result = 4//2
#result //= 2  
#print(result)    

#Example 2:
#print("score board:-\n")
#score = 0
#score += 1
#print(score)


            #f-String
#whenever we want any other datatype to get converted in string we use str() but we cant keep using forever if its going so long so there is shortcut way to do so:-
#Example:- 
#Score = 69
#Skill = 32
#Winning = True
#print(f"your score is {Score}, Your skill is {Skill}, Your Winning is {Winning}.")
#That's how all got converted into strings without a lot of struggle :)



