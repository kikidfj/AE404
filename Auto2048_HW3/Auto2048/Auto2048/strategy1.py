import sys
import math
import random

MAP_FILE_NAME = "MAPFILE.txt"
STEPS_FILE_NAME = "steps.txt"
UP_DOWN_SCORE_HIGHER = True
LEFT_RIGHT_SCORE_HIGHER = False

def readMap():
	fReadMap = open(MAP_FILE_NAME, "r")
	lines = fReadMap.readlines()

	currentMap = []

	for line in lines:
		currentMap.append(line.split('\t'))
	id = 0
	for line in currentMap:
		print('row=' + str(id))
		strTemp = ""
		for item in line:
			strTemp = strTemp + "\t" + item
		print(strTemp)
		id+=1
	return currentMap



def writeStep(_score_higher):
	f = open(STEPS_FILE_NAME, "a")
	res = random.randint(0, 1)

	if(_score_higher == UP_DOWN_SCORE_HIGHER):
		if res == 0:
			f.write('w')
		elif res == 1:
			f.write('s')
	else:
		if res == 0:
			f.write('a')
		elif res == 1:
			f.write('d')
	f.close()
	return


def sum_up_down(_currentMap):
	score_add = 0 
	for j in range(4):
		last_num = int(_currentMap[0][j])
		for i in range(1, 4):
			if last_num != 0 and int(_currentMap[i][j]) == last_num:
				score_add += last_num * 2
				last_num = -1 # prevent next comparison
			else:
				last_num = int(_currentMap[i][j])
	print("score add left_right:" + str(score_add))
	return score_add


def sum_left_right(_currentMap):
	score_add = 0 
	for i in range(4):
		last_num = int(_currentMap[i][0])
		for j in range(1, 4):
			if last_num != 0 and int(_currentMap[i][j]) == last_num:
				score_add += last_num * 2
				last_num = -1 # prevent next comparison
			else:
				last_num = int(_currentMap[i][j])
	print("score add left_right:" + str(score_add))
	return score_add

def main():
	#print("debug here")
	currentMap = readMap()
	if sum_up_down(currentMap) > sum_left_right(currentMap):
		writeStep(UP_DOWN_SCORE_HIGHER)
	else:
		writeStep(LEFT_RIGHT_SCORE_HIGHER)


if __name__ == '__main__':
    main()
