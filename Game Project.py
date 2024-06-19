import random
import time



q=()
name=input('Enter your name ')
print('Hello',name,'Welcome to "LANA Quiz"')
#Rules
print('________________________________________________________________________________________')
print('                                      RULES                                 ')
print('-> Each participant will be give 15 seconds for each question.')
print('-> There will be 3 rounds, each round consists of 5 questions.')
print('-> Qualifications for next round -: No. of correct answers should be 3 or more per round.')
print('-> You can quit the quiz by using #.')
print('-> You can skip a question using *.')
print('-> There will be no negative marking.')
print('_________________________________________________________________________________________')

a='''What is 5*7? 
a. 25
b. 35
c. 75
d. 15'''   

b='''What is the capital of India?
a. Mumbai
b. Banglore
c. Delhi
d. Noida'''     

c='''Who is the Richest Man in the World?
a. Bill Gates
b. Jack Ma
c. Jeff Bezoz
d. Mukesh Ambani'''     

d='''When is Enviornment Day celebrated?
a. 22nd June
b. 5th July
c. 5th June
d. 7th October'''       

e='''Which place is also know as 'MINI SWITZERLAND'?
a. Khajjiar
b. Gulmarg
c. Ladakh
d. Dalhousie'''     

f='''Who discovered Gravity?
a. Thomas Alva Edison
b. Stephen Hawkings
c. Albert Einstein
d. Isaac Newton'''

g='''Who was the first president of India?
a. Jawaharlal Nehru
b. Rajendra Prasad
c. Vallabhbhai Patel
d. S. Radhakrishnan'''

h='''Which is the biggest band in the world?
a. BTS
b. One Direction
c. Blackpink
d. The Vamps'''

I='''Which is the smallest bird in the world?
a. Bee Humming Bird
b. Flowerpecker
c. Sparrow
d. Cuckoo'''

j='''What is the capital of Hungary?
a. Baja
b. Budapest
c. Gyor
d. Sopron'''

k='''Which one of them is bigger?
a. Megabyte
b. Kilobyte
c. Gigabyte
d. Zetabyte'''

l='''Who is known as 'the father of observational astronomy'?
a. Galileo Galilei
b. Nicolaus Copernicus
C. Edmond Halley
d. Johannes Kepler'''

m='''Who is highest paid celebrity in the world?
a. Kanye West
b. Kim Kardashian
c. Kylie Jenner
d. Sofia Vergara'''

n='''Google was founded in
a. 1st January,1996
b. 5th November,1999
c. 29th August,1997
d. 4th September,1998'''

o='''What is Shakespeare's Shortest play?
a. Hamlet
b. Romeo & Juliet
c. Macbeth
d. The Comedy Of Errors'''

p='''What are the security outside of samsumg store called?'''

while q=='@':
    break
else:

    ques=[a,b,c,d,e]
    list=[]
    score=0
    print('-----------ROUND 1-----------')
    print('Each correct answer will give you 10 points')
    while True:
        r= random.choice(ques)
        if r not in list:
            list.append(r)
            time.sleep(15)
            print(r)
            q=str(input('If you want to quit press @' ))
            ans=input('Enter your Answer: ')

            if r==a:
                if ans.lower()=='b' or ans=='35':
                    print("Congratulations,  you are correct. ")
                    score+=10
                elif ans== '*':
                    continue
                else:
                    print('Boooooo!!!!!, You got that wrong.\nThe correct ans is 35.')
            if r==b:
                if ans.lower()=='c' or ans.lower()=='delhi':
                    print("Correct! You are on fire!!")
                    score+=10
                elif ans== '*':
                    continue
                else:
                    print('Better luck next time.\nThe correct ans is Delhi.')
            if r==c:
                if ans.lower()=='c' or ans.lower()=='jeff bezoz':
                    print("You are a genius! ")
                    score+=10
                elif ans== '*':
                    continue
                else:
                    print('You got that wrong. You need to learn Current Affairs.\nThe correct ans is Jeff Bezoz.')
            if r==d:
                if ans.lower()=='c' or ans.lower()=='5th june':
                    print("You got that right. Great going! ")
                    score+=10
                elif ans== '*':
                    continue
                else:
                    print('Oh snap!! Better luck next time.\nThe correct ans is 5th June.')
            if r==e:
                if ans.lower()=='a' or ans.lower()=='khajjiar':
                    print("Way to go!You got that right. ")
                    score+=10
                elif ans== '*':
                    continue
                else:
                    print('You need to improve your Geography!\nThe correct ans is Khajjiar.')
            print()
            if len(list)==5:
                break
          
    print('Your score is',score)
    if score >= 30:
        print('Congratulations! You have qualified for Round 2')

        print('-----------ROUND 2-----------')
        print('Each correct answer will give you 50 points')
        ques2=[f,g,h,I,j]
        list2=[]

        while True:
            i= random.choice(ques2)
            if  i not in list2:
                list2.append(i)
                time.sleep(15)
                print(i)
                ans=input('Enter your Answer: ')

                if i==f:
                    if ans.lower()=='d' or ans.lower()=='isaac newton':
                        print("YOh snap!! Better luck next time ")
                        score+=50
                    elif ans== '*':
                        continue
                    else:
                        print('Get your Scientific facts straight!\nThe correct ans is Isaac Newton.')
                if i==g:
                     if ans.lower()=='b' or ans.lower()=='rajendra prasad':
                        print("Yippee!! You got it right. ")
                        score+=10
                     elif ans== '*':
                        continue
                     else:
                        print('Boooooo!!!!!, You got that wrong.\nThe correct ans is Rajendra Prasad.')
                if i==h:
                    if ans.lower()=='c' or ans.lower()=='blackpink':
                        print("You are becoming Master. ")
                        score+=50
                    elif ans== '*':
                        continue
                    else:
                        print('You are wrong. The girls took the prize.\nThe correct ans is Blackpink.')
                if i==I:
                     if ans.lower()=='a' or ans.lower()=='bee hummingbird':
                        print("congratulations,  you are correct. ")
                        score+=50
                     elif ans== '*':
                        continue
                     else:
                        print('Oh snap!! Better luck next time.\nThe correct ans is Bee Hummingbird.')
                if i==j:
                     if ans.lower()=='b' or ans.lower()=='budapest':
                        print("GREAT GOING!!! ")
                        score+=50
                     elif ans== '*':
                        continue
                     else:
                        print('You need to improve your Geography!\nThe correct ans is Budapest.')
                print()
                if len(list2)==5:
                    break


    print('Your score is',score)
    if score >= 180:
        print('Congratulations! You have qualified for Round 3')
        ques3=[]
        list3=[]
            
        print('-----------ROUND 3-----------')
        print('Each correct answer will give you 100 points')
            
        while True:
            j= random.choice(ques)
            if j not in list3:
                list3.append(j)
                time.sleep(15)
                print(j)
                ans=input('Enter your Answer: ')

                if j==k:
                    if ans.lower()=='d' or ans.lower()=='zetabyte':
                        print("We got a Computer Geek with us!! ")
                        score+=100
                    elif ans== '*':
                        continue
                    else:
                        print('Buck up!\nThe correct ans is Zetabyte.')
                if j==l:
                    if ans.lower()=='a' or ans.lower()=='gallieo gallile':
                        print("Congratulations,  you are a genius! ")
                        score+=100
                    elif ans== '*':
                        continue
                    else:
                        print('Get your science cap on.\nThe correct ans is Gallieo Gallilie.')
                if j==m:
                    if ans.lower()=='c' or ans.lower()=='kylie jenner':
                        print("Yippie, you are correct. ")
                        score+=100
                    elif ans== '*':
                        continue
                    else:
                        print('You can do better!\nThe correct ans is Kylie Jenner.')
                if j==n:
                    if ans.lower()=='d' or ans.lower()=='4th september,1998':
                        print("Perfect! Keep going. ")
                        score+=100
                    elif ans== '*':
                        continue
                    else:
                        print('You need to get your memory refreshed!\nThe correct ans is 4th September,1998.')
                if j==o:
                    if ans.lower()=='d' or ans.lower()=='the comedy of errors':
                        print("You are on fire!! ")
                        score+=100
                    elif ans== '*':
                        continue
                    else:
                        print('You need to improve your Shakespearean Knowledge!\nThe correct ans is The Comedy Of Errors.')
                print()
                if len(list3)==5:
                    break

print('Thank You for Participating in "LANA Quiz"! Have a good day')
choice=input('Do you want to play BONUS QUESTION? (Y/N) ')
if choice.upper()=='Y':
    #BONUS ROUND
    print('---------WELCOME TO BONUS ROUND-----------')
    print('This question will give you 200 points.')
    print(p)
    ans=input('Enter you Answer ')
    if ans.lower()=='gaurdians of galaxy':
        print('Bravo!You got that.')
        score+=200
    else:
        print('OHHHH!!! You lost your bonus points!\nThe ans was Gaurdians Of Galaxy')
print('Your score is',score)


    
