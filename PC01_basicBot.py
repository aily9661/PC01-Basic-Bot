import time #access time module (code used from Mike Driscoll of RealPython.com, https://realpython.com/python-sleep/)
print('Oh god, I hate when people enter my program. Ugh, maybe you will be alright… let us start with a simple question…')
time.sleep(2) #pause for 2 seconds
name = input('What is your name?')
print('Really...? Im sorry to hear that. Cannot imagine what knd of parent would name their kid',name)
time.sleep(1)
age = int(input('What is your age?')) #if prompt (age<21 age>20)
if age<21:
    print('Geez, aren’t you kinda young to use a computer?')
if age>20:
    print('Holy crap you are old!')
time.sleep(1) 
print('Okay let me get this straight... Your name is',name, 'and you are',age, 'years old. Why can I never meet someone my age :(')
time.sleep(2) 
exitPrompt = input('Well... Is it okay if I leave now?')
print('Really?', exitPrompt, '? Haha I do not actually care what you think. Byeeee!')
time.sleep(3)
print('Oh by the way. Never. Ever. Run this code again. Or you will be in for it.')