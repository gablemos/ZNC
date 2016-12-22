# coding: UTF-8

"""
line 1
line 2
line 3
"""
def spam(): #function 
    eggs = 12
    return eggs #return var eggs(12)
        
print spam() #print function's return

#
print "----------------------------------------------------------------------------------"
#

var = 10+10 
print var

#
print "----------------------------------------------------------------------------------"
#

eggs = 10**2

print eggs 

#
print "----------------------------------------------------------------------------------"
#

print 'This isn\'t flying, this is falling with style!'

#
print "----------------------------------------------------------------------------------"
#

fifth_letter = "MONTY"[4]

print fifth_letter

#
print "----------------------------------------------------------------------------------"
#

parrot = "Norwegian Blue"

print len(parrot)
print parrot.lower()
print parrot.upper()

#
print "----------------------------------------------------------------------------------"
#

pi = 3.14
print str(pi)

#
print "----------------------------------------------------------------------------------"
#

print "The value of pi is around " + str(3.14)
print "The value of pi is around",3.14

#
print "----------------------------------------------------------------------------------"
#

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)