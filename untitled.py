words = [ 'chair', 'the pot', 'ganja', 'the crystals', 'my money', 'the guns', 'the children', 'my homies', 'yo mom'] 
mmenia = [ 'I', 'we', 'you', 'they', 'he', 'she'] #1
vbs = ['are', 'am', 'is', 'aint'] #2
F_bombs = ['sheesh', 'lick', 'make', 'blow', 'love', 'call', 'phone', 'shoot', 'doodoo', 'gonna', 'boil', 'trade', 'smoke'] #2
import random as rd
txt = ''

for i in range(int(input())): #ho many senteces
         sent = ' '
         sent += rd.choice(mmenia) + ' '
         sent += rd.choice([rd.choice(F_bombs), rd.choice(vbs)]) + ' '
         if 'gonna' in sent:
                  sent += rd.choice( ['sheesh', 'lick', 'make', 'blow', 'love', 'call', 'phone', 'shoot', 'doodoo']) + ' '
         sent += rd.choice(words)
         txt += sent + rd.choice(['.', '.','.','.','.','!', '!', '?'])
print(txt + '\n This text is generated automatically by the machine called: "untitled"')
