from time import*
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error = error +1
        except:
            error = error +1
    return error



def speed_time(time_s,time_e,userinput):
    time_delay = time_e-time_s
    time_r=round(time_delay,2)
    speed = len(userinput)/time_r
    return round(speed)
print('************************* WELCOME TO SPEED TESTER ************************\n')

while True:
    ck=input('ready to test : yes/ no :')
    if ck.lower() == 'yes':
        test=["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.", "this is a typing speed tester" , "welcome to the tech world using python","The Moon is a barren, rocky world without air and water.","The greatest glory in living lies not in never falling, but in rising every time we fall"]
        test1=r.choice(test)
        print('***************typing speed*************** ')
        print(test1)
        print()
        print()
        time1= time()
        testInput=input(' Enter : ')
        time2=time()

        print('Speed : ',speed_time(time1,time2,testInput),"word/sec")
        print('Error : ',mistake(test1,testInput))
    elif ck.lower() == 'no':
        print('*********************END********************')
        break
    else:
        print('wrong input')
        break