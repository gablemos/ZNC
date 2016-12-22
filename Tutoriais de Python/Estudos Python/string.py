# coding: UTF-8

print 'C:\some\name'  # here \n means newline!
print r'C:\some\name'  # note the r before the quote

#
print "----------------------------------------------------------------------------------"
#

print """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
#
print "----------------------------------------------------------------------------------"
#

# 3 times 'un', followed by 'ium'
print 3 * 'un ' + 'ium'

#
print "----------------------------------------------------------------------------------"
#

print 'Py' 'thon'

#
print "----------------------------------------------------------------------------------"
#

prefix = 'Py'
prefix += 'thon'
print prefix

#
print "----------------------------------------------------------------------------------"
#

word = 'Python'
print word[0]  # character in position 0
print word[5]  # character in position 5
#

print "----------------------------------------------------------------------------------"
#

print word[-1]  # last character
print word[-2]  # second-last character
print word[-6]

#
print "----------------------------------------------------------------------------------"
#

print word[0:2]  # characters from position 0 (included) to 2 (excluded)

print word[-4:-2]  # characters from position 2 (included) to 5 (excluded)

#
print "----------------------------------------------------------------------------------"
#
# coding: UTF-8

print word[:2]   # character from the beginning to position 2 (excluded)

print word[4:]   # characters from position 4 (included) to the end

print word[-2:]  # characters from the second-last (included) to the end

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

#
print "----------------------------------------------------------------------------------"
#
#teste dã é s
s = 'supercalifragilisticexpialidocious'
print len(s) #funão len retorna o tamanho do string, lengh

#
print "----------------------------------------------------------------------------------"
#