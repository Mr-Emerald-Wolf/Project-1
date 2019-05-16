#To check for leap year
while 1 == 1:
     try:
          a = int(input("Enter Year: "))
          b = a%4
          if b == 0:
               print("It is a leap year. ")
               break
          elif b == 1:
               print("It is not a leap year. ")
               break
          else:
               print("Enter 4 Digits only.")
               break
     except:
          print("An error was found.")
          break             
