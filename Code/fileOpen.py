import random

def getMood() :
    data = []
    with open('C:\\Users\\meghapatil\\Major-Project-I\\Dataset\\train.txt.','r') as f:
       line = f.readlines()
    #    print(line)
       for i in line :
           data.append(i.split(';'))
            
    ques = random.randint(0,len(data)-1)
    print(data[ques][0])
    x= input()

    if x in  ['yes','YES','Yes'] :
        mood = data[ques][1]
             
    else :
        mood = 'Calm'
    print(mood)
    f.close()
    return mood

"""for i in range(1) :
    getMood()"""
# getMood()
