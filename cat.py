# python version of cat from coding academy 2015 mag
#!/usr/bin/python3
import sys
from optparse import OptionParser

class CatCommand:
	def__init__(self):
		self.count = 1

	def run(self, i, options):
	#set default options
	e =""

	for line in i:
		#modify printing line accouridnd to optnos
		if options.showend:
			line = line.rstrip()
			e = "$\n"
		if options.shownum:
			#line = str(self.count) + " " + line
			line = "{0} {1}".format(self.count, line)

		self.count += 1
		print(line, end=e)

def main():
	#setup up options
	usage = "usage: %prog [OPTION]... [FILE]..."
	parser = OptionParser(usage=usage)
	parser.add_option("-E", dest="showend", action="store_true", help="Show $ at line ending
	parser.add_option("-n", dest="shownum", action="store_true", help="Show line numbers")
	(options, args) = parser.parse_args()

	c = CatCommand()

	#if filenames given
	if len(args) > 1:	
		for a in args:
			f = open(a, "r")
			c.run(f, options)

	#otherwise  read from stdin
	else:
		c.run(sys.stdin, options)

if __name__ == "__main__":
	main()
