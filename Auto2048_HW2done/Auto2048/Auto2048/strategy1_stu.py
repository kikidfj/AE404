import sys
import math
import random

MAP_FILE_NAME = "MAPFILE.txt"
STEPS_FILE_NAME = "steps.txt"
UP_DOWN_SCORE_HIGHER = True
LEFT_RIGHT_SCORE_HIGHER = False

def readMap():
	
	currentMap = []
	
	# TODO: please read map from MAP_FILE_NAME
	fReadMap = open(MAP_FILE_NAME, "r")
	lines = fReadMap.readlines()
	
	for line in lines:
		currentMap.append(line.split("\t"))
	
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

	#TODO: Please decide moving Up Down or Left Right by which will get higher score
	if int(_score_higher) == int(UP_DOWN_SCORE_HIGHER):
		if res == 0:
			f.write("w")
		if res == 1:
			f.write("s")
	if int(_score_higher) == int(LEFT_RIGHT_SCORE_HIGHER):
		if res == 0:
			f.write("a")
		if res == 1:
			f.write("d")
	f.close()
	return


def sum_up_down(_currentMap):
	
	#Please try to calculate the score added after moving up or down
	for j in range(4):
		last_num = int(_currentMap[0][j])
		for i in range(1,4):
			if int(_currentMap[i][j]) != 0 and int(_currentMap[i][j]) == last_num:
				score_add = score_add + last_num*2
				last_num = -1
			else:
				last_num = int(_currentMap[i][j])
	return score_add


def sum_left_right(_currentMap):

	#Please try to calculate the score added after moving left or right
	for i in range(4):
		last_num = int(_currentMap[i][0])
		for j in range(1,4):
			if int(_currentMap[i][j]) != 0 and int(_currentMap[i][j]) == last_num:
				score_add = score_add + last_num*2
				last_num = -1
			else:
				last_num = int(_currentMap[i][j])
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
