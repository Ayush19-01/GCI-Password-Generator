#Made for the sole purpose of GCI 2019
import random
list1=["Enter your first name:","Enter your surname:","Enter your hometown:","Enter name of your first school:","Enter the first name of your mother:","Enter your current country:"]
list2=["Enter your date of birth(mm/dd/yyyy):","Enter your current age:"]
list3=[]
list4=[]
list5=[]
for i in list1:
    a=input(i)
    list3.append(a)
for j in list2:
    b=input(j)
    b=b.split("/")
    list4.extend(b)
m=10
print("Possible Passwords:")
while m!=0:
    s=""
    r=random.choice(list3)
    t=random.choice(list4)
    s=r+t
    if s in list5:
        continue
    else:
        list5.append(s)
        print(s)
        m-=1