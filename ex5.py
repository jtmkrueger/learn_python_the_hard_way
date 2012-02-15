name = 'zed a shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print "lets talk about %s." % name
print "he's %r inches tall." % height
print "he's %d pounds heavy." % weight
print "actually that not too heavy"
print "he's got %s eyes and %s hair." % (eyes, hair)
print "his teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %r." % (age, height, weight, age + height + weight)
