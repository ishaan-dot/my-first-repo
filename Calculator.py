def calculator():
 operations = input("Enter an operator : ADD / SUB / MULTIPLY / DIVIDE :").lower()
 
 if operations == "add":
   try :
    x = int(input("Enter a number :"))
    y = int(input("Enter an another number :"))
   except ValueError as err :
    print(err)
   add = lambda x , y : x + y
 
   result = add(x,y)
   print(result)

 elif operations == "sub":
  
   try :
    x = int(input("Enter a number :"))
    y = int(input("Enter an another number :"))
   except ValueError as err :
    print(err)
   sub = lambda x , y : x - y
 
   result = sub(x,y)
   print(result)

 
 elif operations == "multiply":
  
   try :
    x = int(input("Enter a number :"))
    y = int(input("Enter an another number :"))
   except ValueError as err :
    print(err)
   multiply = lambda x , y : x * y
 
   result = multiply(x,y)
   print(result)
  
 elif operations == "divide":
   try :
    x = int(input("Enter a number :"))
    y = int(input("Enter an another number :"))
   except ValueError as err :
    print(err)
   try :
    divide = lambda x , y : x/y
   except ZeroDivisionError as err :
    print(err)
  
 
   result = divide(x,y)
   print(result)
 else:
  print("invalid Input")

calculator()
while True:
 user_Input = input("Do you want to calculate again : YES / NO :").lower()
 if user_Input == "yes":
  calculator()
 elif user_Input == "no":
  break
 else :
  print("invalid Input")
