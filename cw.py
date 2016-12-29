#bin/python
tm = open('timemachine.txt','r')

for line in tm:
        line = line.strip()
        line = line.translate(None, '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        line = line.lower()
        line = line.split(' ')
