import random

TOTAL_POINTS = 10000000
RADIUS = 10000

xs = []
ys = []
pt = 0

for i in range(TOTAL_POINTS):
	xs.append(random.randint(0,RADIUS))
	ys.append(random.randint(0,RADIUS))

for i in range(TOTAL_POINTS):
	if(xs[i]*xs[i] + ys[i]*ys[i]) < RADIUS*RADIUS:
		pt += 1
monteCarloPi = float(pt)/TOTAL_POINTS * 4.0

print("pi:" + str(monteCarloPi))