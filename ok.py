#BANO QABIL PROJECT MAKE A MAGIC 8 BALL PROGRAM:
import random
while True:
    question=input("ASK THE MAGIC 8 BALL QuUESTION:(PRESS ENTER TO QUIT) ")
    answer=random.randint(1,20)
    if question=="":
        print("stopping the game.")
        break
    if answer==1:
        print("It is cartain.")
    elif answer==2:
        print("It is decidedly so.")
    elif answer==3:
        print("Without a doubt.")
    elif answer==4:
        print("Yes definitely.")
    elif answer==5:
        print("You may rely on it.")
    elif answer==6:
        print("As i see it,yes.")
    elif answer==7:
        print("Most likely.")
    elif answer==8:
        print("Signs point to yes.")
    elif answer==9:
        print("Yes.")
    elif answer==10:
        print("Better not tall you now.")
    elif answer==11:
        print("Ask again later.")
    elif answer==12:
        print("My reply is no.")
    elif answer==13:
        print("Reply hazy, try again.")
    elif answer==14:
        print("concentrate and ask again.")
    elif answer==15:
        print("Outlook not so good.")
    elif answer==16:
        print("don't count on it.")
    elif answer==17:
        print("My sources say no.")
    elif answer==18:
        print("Very doubtfull.")
    elif answer==19:
        print("It is decidedly so.")
    elif answer==20:
        print("Without a doubt.")
