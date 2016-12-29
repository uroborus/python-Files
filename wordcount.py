#bin/python
tm = open('timemachine.txt','r')

for line in tm:
	line = line.strip()
	line = line.translate(None,'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
	line = line.lower()
	line = line.split(' ')

dict = {}
for word in list:
	dict[word] = 1
if word in dict:
	count = dict[word]
	count += 1
	dict[word] = count
else:
	dict[word] = 1

for word,count in dict.iteritems():
	print word + ": " + str(count)
