# Stack Implementation 

n=int(input("Enter your number of elements you want to enter:-"))

s=[]

for i in range(0,n):
    a=input("Enter your elements:-")
    s.append(a)

print("Your stack contains:-",end="")
for i in range(0,len(s)): 
    print(s.pop(),end="")
   