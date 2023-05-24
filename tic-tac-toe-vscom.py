import sys
import os
import time
import random as rand

board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]


def getmove():
	a, b = 0, 0
	try :
		a, b = map(int, input("Enter : ").split())
		if a == 0:
			raise Exception
		if b == 0:
			raise Exception
	except :
		print("Not a valid move.")
		
	return a, b

def movcheck(key):
	for i in range(len(board)):
		ind = []
		a = 0
		b = 0
		for j in range(len(board[i])):
			if board[i][j] == 0:
				a = a + 1
				ind.append([int(i), int(j)])
			elif board[i][j] == key:
				b = b + 1
			if a > 1:
				break
		
		if b > 1 and a == 1:
			x, y = ind[0][0], ind[0][1]
			return x + 1, y + 1
	
	for j in range(len(board)):
		ind = []
		a = 0
		b = 0
		for i in range(len(board[j])):
			if board[i][j] == 0:
				a = a + 1
				ind.append([int(i), int(j)])
			elif board[i][j] == key:
				b = b + 1
			if a > 1:
				break
		
		if b > 1 and a == 1:
			x, y = ind[0][0], ind[0][1]
			return x + 1, y + 1
	
	ind = []
	a = 0
	b = 0
	for i in range(len(board)):
		if board[i][i] == 0:
			a = a + 1
			ind.append([int(i), int(i)])
		elif board[i][i] == key:
			b = b + 1
		if a > 1:
			break
		if b > 1 and a == 1:
			x, y = ind[0][0], ind[0][1]
			return x + 1, y + 1
	
	ind = []
	a = 0
	b = 0
	for i in range(len(board)):
		if board[i][(len(board[i]) - 1)- i] == 0:
			a = a + 1
			ind.append([int(i), (len(board[i]) - 1) - int(i)])
		elif board[i][(len(board[i]) - 1) - i] == key:
			b = b + 1
		if a > 1:
			break
		if b > 1 and a == 1:
			x, y = ind[0][0], ind[0][1]
			return x + 1, y + 1
	
	return 0, 0
def enemymove():
	tx, ty = movcheck(1)
	if tx != 0 and ty != 0:
			return tx, ty
		
	tx, ty = movcheck(2)
	if tx != 0 and ty != 0:
			return tx, ty
			
	while True:
		x = rand.randint(0, len(board) - 1)
		y = rand.randint(0, len(board[x]) - 1)
		if board[y][x] == 0:
			return y + 1, x + 1
	

def game(turn):
	os.system("clear")
	for i in board:
		sys.stdout.write("|")
		for j in i:
			if j == 0:
				sys.stdout.write(" ")
			elif j == 1:
				sys.stdout.write("O")
			elif j == 2:
				sys.stdout.write("X")
			
			sys.stdout.write("|")
		print("")
		for j in i:
			sys.stdout.write(" —")
		print("")

	temp = check()
	if temp > 0 and temp < 100:
		return -1
	elif temp == 100:
		return -2
	
	x, y = 0, 0
	if turn % 2 == 0:
		while x == 0 or y == 0:
#			x, y = getmove()
			x, y = enemymove()
		print(x, y)
		time.sleep(1)
	elif turn % 2 != 0:
		while x == 0 or y == 0:
			x, y = enemymove()
		print(x, y)
		time.sleep(1)
	
	if(board[x - 1][y - 1] == 0): 
		if turn % 2 == 0:
			board[x - 1][y - 1] = 2
		elif turn % 2 != 0:
			board[x - 1][y - 1] = 1
	else :
		print("Space occupied.")
		time.sleep(1)
		return turn
		
	turn += 1
	return turn

def check():
	key = 0
	
	zero = 0
	
	for i in board:
		for j in i:
			if j == 0:
				zero = zero + 1
	
	if zero == 0:
		return 100
	
#	horizontal
	for i in range(len(board)):
		flag = False
		if board[i][0] != 0:
			key = board[i][0]
		else: 
			continue
		for j in range(len(board)):
			if board[i][j] == key:
				flag = True
				continue
			else:
				flag = False
				break
				
		if flag == True:
			return key
	
#	vertical
	for i in range(len(board)):
		flag = False
		if board[0][i] != 0:
			key = board[0][i]
		else: 
			continue
		for j in range(len(board)):
			if board[j][i] == key:
				flag = True
				continue
			else:
				flag = False
				break
		if flag == True:
			return key
			
#	diagonal_1
	key = board[i][i]
	for i in range(len(board)):
		flag = False
		if board[i][i] == 0:
			break
	
		if board[i][i] == key:
			flag = True
			continue
		else:
			flag = False
			break
			
	if flag == True:
		return key
		
#	diagonal_2
	key = board[0][2 - 0]
	for i in range(len(board)):
		flag = False
		if board[i][2 - i] == 0:
			break
	
		if board[i][2 - i] == key:
			flag = True
			continue
		else:
			flag = False
			break
			
	if flag == True:
		return key	
			
	return 0



_turn = 1
while True:
	_turn = game(_turn)
	
	if _turn == -1:
		print("Game Won")
		time.sleep(2)
	elif _turn == -2:
		print("Game Draw")
		time.sleep(2)
	
	if _turn == -1 or _turn == -2:
		for i in range(len(board)):
			for j in range(len(board[i])):
				board[i][j] = 0
		_turn = 1