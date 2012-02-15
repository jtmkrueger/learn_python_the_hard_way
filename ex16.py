from sys import argv

script, filename = argv

print "were going to erase %r." % filename
print "If your don't want that, hit ctrl-c (^C)."
print "if yoru do want that, hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "truncating the file. Goodbye!"
target.truncate()

print "now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
