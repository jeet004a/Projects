#Singly Linkedlist using user entry


class Node:
     def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.head=None

    def printlist(self):
        a=self.head
        while a is not None:
            print(a.data,end="->")
            a=a.next


n=int(input("Enter your number of elements:-"))

l=linklist()
if n==0:
    print("Empty list")
elif n==1:
    a=int(input("Enter your elements:-"))
    l.head=Node(a)
    l.printlist()
elif n>1:
    n=n-1       #Because we added head node manually
    q=[]
    x=int(input("Enter your head node:-"))
    l.head=Node(x)
    for i in range(0,n):
        p=int(input())
        q.append(Node(p))

    l.head.next=q[0]
    for i in range(0,len(q)-1):
        q[i].next=q[i+1]

    l.printlist()




