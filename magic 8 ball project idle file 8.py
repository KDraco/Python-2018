import random
import time

answers = ["you will have no luck in finding out even from me" , "you should spend your time on something with more importance" , "all will be revealed in time" , "to find the answers you must walk the long difficult road" , "ask yourself the question most likley you already know the answer"]
name = input("what is your name? ")
while True:
    time.sleep(2)
    print("if you want to stop please enter stop for your question")
    question = input ("what is your question %s? " %name)
    time.sleep(2)
    if question.strip() == 'stop':
        break
    else:
        print( random.choice(answers) + " %s." %name )
        time.sleep(2)
        print("thank you now lets go again shal we %s?" %name)
print("thank you for using the magic 8 ball %s!" %name)
