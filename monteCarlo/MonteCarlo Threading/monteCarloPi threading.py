import random
import threading
import time
from multiprocessing import Process

TOTAL_POINTS = 100000
RADIUS = 10000

def monteCarloPi(totalPoints, pt):
	xs = []
	ys = []

	for i in range(totalPoints):
		xs.append(random.randint(0,RADIUS))
		ys.append(random.randint(0,RADIUS))

	for i in range(totalPoints):
		if(xs[i]*xs[i] + ys[i]*ys[i]) < RADIUS*RADIUS:
			pt[0] += 1

	return pt



def main():
	p1 = [0]
	p2 = [0]
	p3 = [0]
	p4 = [0]

	p4[0] = 0

	t1 = threading.Thread(target = monteCarloPi, args = (int(TOTAL_POINTS/4), p1,))
	t2 = threading.Thread(target = monteCarloPi, args = (int(TOTAL_POINTS/4), p2,))
	t3 = threading.Thread(target = monteCarloPi, args = (int(TOTAL_POINTS/4), p3,))
	start = time.time()

	t1.start()
	t2.start()
	t3.start()

	ret = monteCarloPi(TOTAL_POINTS - 3 * int(TOTAL_POINTS/4), p4)
	
	t1.join()
	t2.join()
	t3.join()

	monteCarloPI = float(p1[0] + p2[0] + p3[0] + p4[0])/TOTAL_POINTS * 4.0
	print("pi:" + str(monteCarloPI))