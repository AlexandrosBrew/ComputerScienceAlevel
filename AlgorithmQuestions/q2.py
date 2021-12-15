temperatures = []*365
for i in range(0,365):
  temperatures.append(i%35)
bandA, bandB, bandC, bandD = 0, 0, 0, 0
for i in range(len(temperatures)):
	if temperatures[i] <= 10:
		bandA += 1
	elif temperatures[i] <= 20:
		bandB += 1
	elif temperatures[i] <= 30:
		bandC += 1
	elif temperatures[i] >= 31:
		bandD += 1

print('bandA: ' + str(bandA) + ' bandB: '+str(bandB)+ ' bandC: '+ str(bandC)+ ' bandD: '+str(bandD))