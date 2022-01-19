# hiragana excersicer 2
# by Ezek_


# MODULES
import random # for random choosing
import time



# HARD WORK
print('welcome to hiragana quiz! are u ready??')
input('press enter to start...')
print()

start=time.time()

fhand=open('hiragana.txt', encoding='utf8')
line=fhand.readline()
chara=line.split()
tot=len(chara)
fails=0

while len(chara)>=1:
	choice=random.choice(chara)
	rom=choice[1:]
	print(choice[0])
	# print(rom)
	while True:
		anw=input('ingress your anwser:').upper()
		if anw==rom:
			break
		else:
			print('you failed, try again')
			fails=fails+1
	chara.remove(choice)

end=time.time()

print()
print('good job! your done.')
input('press enter to see your statistics...')
print()
print('amount of fails: {} of {}'.format(fails, tot))
print('time taken: {time} minutes'.format(time=(end-start)/60))
input('press enter to exit')

