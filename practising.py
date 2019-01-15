#handcricket from 0 to 6
import random
s=0
v=0
while (True):
  a=random.randint(0,6)
  b=int(input("bat"))
  print(a,"opponent")
  if a==b:
      print("you are out")
      break
  else:
      if b==0:
          b=a
          print(a)
      s=s+b
print("-------------",s,"    Is your score--------------")
while(True):
    c = random.randint(0, 6)
    d= int(input("bowl"))
    print(c,"opponent")

    if c == d:
        print("opponent is out")
        break
    else:
        if c == 0:
            c = d
        v = v + c
        if v>s:
            print("----------------------your opponent is the winner---------------------------")
            break
print("------   ",v, "is the opponent score-")
if(s>v):
    print(" ----------------------------You are the winner-------------------------------------------")
elif(s==v):
    print("the match is drawn")
