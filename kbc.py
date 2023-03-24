from time import sleep
import os
import sys

WinAmount = 0
LastCheckpoint = None

Introduction = """
Rules to be followed:

1. The game consists of 16 MCQ questions.
2. There are 4 checkpoints in this game at question number 4, 8, 11 and 13.
3. At any point you can quit the game by entering "q".

Press [Enter] to start the game.
"""

GameQ=["What is the strongest block you can find in Minecraft?","Which edition of Fifa sold the most amount of copies?","Which of these best-selling video game franchises without a main character has been sold the most?","Which video game shattered the record for most sales in 24 hours, making over $800 million?","In what year was the first video game invented?","Pacman was designed to resemble which food?","How is a Charged Creeper created?","According To Free Fire's Documentation, Each Battle Royale Match Lasts For?","Which Of These Is Not Is Not A SMG","In BGMI Or PUBG, Which Of These Guns Have Automatic Fire Mode?","Which Map has two types of Ghillie Suits?",'In BGMI Or PUBG,What Will Be The Magazine Size Of M249 With Extended Mag?','In BGMI Or PUBG,Cheek Pad Is Not Supported In?','At How Much Rank Points Would You Attain The Platinum 1 Rank In Free Fire BR Mode?','What Is The Old Name Of The Nulla Character In Free Fire?','According To Free Fire, Which Character Is Shown In The  Maintainance Of Antiban Feature Of Game?']
	
QOpt=["A.Obsidian\nB.Diamond Ender\nC.chest\nD.Ancient debris","A.Fifa 10\nB.Fifa 15\nC.Fifa 18\nD.Fifa 07","A.The Sims\nB.Minecraft\nC.Need For Speed\nD.Tetris","A.Fifa 18\nB.Grand Theft Grand Theft Auto V\nC.Call of Duty: Black Ops\nD.Cyberpunk 2077","A.1958\nB.1969\nC.1943\nD.1962","A.Cookie\nB.Burger\nC.Pizza\nD.Sandwich","A.When a creeper eats a plate of rocks\nB.When a creeper collects a battery\nC.When lightning strikes within four blocks of a creeper\nD.Even the game's creators can't explain","A.10 Minutes\nB.15 Minutes\nC.25 Minutes\nD.20 Minutes","A.MP40\nB.BIZON\nC.CG15\nD.MINI UZI",'A.MK14\nB.Mini14\n3.SKS\n4.SLR','A.Vikendi\nB.Miramar\n3.Errangel\n4.Sanhok','A.100\nB.150\nC.75\nD.200','A.Kar98K\nB.M24\nC.Mini14\nD.SKS','A.2000+\nB.2100+\nC.2200+\nD.2150+','A.Eve\nB.May\nC.Caroline\nD.Nerlona','A.Moco\nB.Laura\nC.Caroline\nD.A124']

QAns=["a" ,"c","d","b","a","c","c",'b','d','a','a','b','c','a','b','c']
am=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000]

def print_in_slow(string, lag):
	for s in string:
		if s not in '\t\n':
			print(s, end='')
			sleep(lag)
			sys.stdout.flush()
		else:
			print(s, end='')
			sys.stdout.flush()

def print_line_in_slow(string, lag):
	lines = string.split('\n')
	for line in lines:
		if line:
			print(line, end='\n')
			sleep(lag)
			sys.stdout.flush()
		else:
			print(line, end='\n')
			sys.stdout.flush()

def generator():
	for question, options, answer, amount in zip(GameQ, QOpt, QAns, am):
		yield (question, options, answer, amount)

everything = generator()

LengthOfGame = len(GameQ)

print_in_slow(Introduction, 0.05)
input()
os.system('cls')
print_in_slow("Welcome to KBC Game🕵️‍\n\n", 0.1)
for i in range(1, LengthOfGame+1):
	question, options, answer, amount = next(everything)
	print_in_slow(f'Question Number {i}', 0.06)
	print()
	print_in_slow(question, 0.07)
	print()
	print_line_in_slow(options, 0.9)
	print()
	choice = str(input('Enter your option: '))
	choice = choice.strip().lower()
	while choice not in 'abcdq' or choice == '':
		print('Not a valid option\nTry Again\n')
		choice = str(input('Enter your option: '))
		choice = choice.strip().lower()
	if choice == 'q':
		if LastCheckpoint:
			WinAmount=am[LastCheckpoint-1]
		print()
		print_line_in_slow(f'Game Ending!!\n\nThe Correct Answer is option {answer.upper()}\n\nYou won ₹{WinAmount:,}', 0.9)
		sys.exit()
	else:
		if choice == answer:
			WinAmount+=amount
			print_line_in_slow(f'\nCorrect Answer!!\nYou won ₹{amount:,}', 0.9)
			if i in [4,8,11,13]:
				LastCheckpoint = i
		else:
			if LastCheckpoint:
				WinAmount = am[LastCheckpoint-1]
			print()
			print_line_in_slow(f'Sorry Incorrect Option\nCorrect Answer is option {answer.upper()}!!\n\nGame Over\n\nYou won ₹{WinAmount:,}', 0.9)
			sys.exit()
	print()
	if i != LengthOfGame:
		print_in_slow('Next question in 3',0.02)
		print()
		sleep(1)
		print(2)
		sleep(1)
		print(1)
		sleep(1)
		os.system('cls')
else:
	print_in_slow('Congratulations you completed the KBC game.',0.05)

