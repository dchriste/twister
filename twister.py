#python3.8

import platform, random, time, os

class twisty ():
	def __init__(self, d, a, c):
	   	self.dir = str(d).strip()
	   	self.col = str(c).strip()
	   	self.app = str(a).strip()
	   	self.print = '{0.dir} {0.app} on {0.col}'.format(self)
	   	self.rank = 5
	   	tmp = d + a
	   	if tmp == 'leftfoot':
	   		self.rank = 0
	   	elif tmp == 'lefthand':
	   		self.rank = 1
	   	elif tmp == 'righthand':
	   		self.rank = 2
	   	elif tmp == 'rightfoot':
	   		self.rank = 3

def getNew():
	global prev
	appendage = ['foot','hand']
	direction = ['left','right']
	color = ['red','blue','green','yellow']
	inv = [1,0]
	
	rand1 = random.randint(0,1)
	if rand1 == prev: rand1 = inv[prev]
	prev = rand1
	rand3= random.randint(0,3)
	rand2 = random.randint(0,1)
	
	return twisty(direction[rand1],appendage[rand2],color[rand3])

def genNew(oldList):
	aFlag = False
	
	while aFlag == False:
		tmp = getNew()
		i = 0
		for pos in oldList: i += 1 if tmp.print == pos.print else 0
		if i == 0: aFlag = True

	return tmp

def main():
	global prev
	clrStr = 'clear' if platform.system() != 'Windows' else 'cls'
	clear = lambda: os.system(clrStr)

	prev = 0
	vaildQuit = ['e','exit','q','quit','n','no']
	userInput = ''
	
	tmp = ''
	mostRecent = [twisty('left','foot',''),twisty('left','hand',''),twisty('right','hand',''),twisty('right','foot','')]
	current = mostRecent[0]
	
	startTime = time.time()
	spinCount = 0

	while userInput not in vaildQuit:
		clear()
		
		current = genNew(mostRecent) #pass list to check against
		mostRecent[current.rank] = current
		
		print('{}\n\nYou should have your...\n'.format(current.print))
		for i in mostRecent: tmp = '{}\n{}'.format(tmp,i.print)
		print(tmp.strip())
		
		tmp = ''
		spinCount += 1
		userInput = input('\nAgain? [enter=yes]\n')
	
	endTime = time.time()
	
	runTime = round((endTime-startTime),2)
	units = 'seconds'
	
	if runTime > 60:
		runTime = round((runTime/60),2)
		units = 'minutes'
	
	print('\nYour game lasted {num} {units} and {s} spins!\n'.format(num=runTime,units=units,s=spinCount))
	
if __name__ == '__main__':
	main()