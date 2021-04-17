import sys

a = 0

try:
	a = int(sys.argv[1])
	if (a <= 0):
		raise
except:
	print "\nUsage: python reducer.py <reduction factor> [input file] [output file]"
	print "\nPositional argument:\n\t<reduction factor> - The integer by which to reduce the list"
	print "\nOptional arguments:\n\t[input file] : Default is CLSID.list"
	print "\t[output file] : Default is CLSID.list.new"
	sys.exit()

b = ""
c = ""

try:
	b = str(sys.argv[2])
except:
	b = "CLSID.list"
	
try:
	c = str(sys.argv[3])
except:
	c = "CLSID.list.new"

if (b == c):
	print "Please choose a different output file name"
	sys.exit()


print "\nReading file " + b + "..."

file1 = open(b, 'r')
Lines = file1.readlines()
 
file2 = open(c, 'w')

print "\nReducing contents by factor of " + str(a) + "..."

count = 0

for line in Lines:
    if count%a == 0:
    	file2.write(line)
    
    count += 1
    
print "\nWriting to file " + c + "..." 
    
file1.close();
file2.close();

print "\nDone!"
    
