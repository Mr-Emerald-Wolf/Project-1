#Creating Report Card
n = input("Enter Your Name: ")
a = int(input("Enter Marks for English: "))
b = int(input("Enter Marks for Maths: "))
c = int(input("Enter Marks for Science: "))
d = int(input("Enter Marks for SST: "))
+e = int(input("Enter Marks for Hindi: "))
s = a+b+c+d+e
p = (s/500)
print("Hi", n,"you got a total of", s,"/500 marks in your exams.")
print("Your average was ", p, "and total percentage was ", p*100,"%")
