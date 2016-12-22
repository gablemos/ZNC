from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print current_day,"/",current_month,"/",current_year
	
#
print"----------------------------------------------------------------------"
#

from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)

#
print"----------------------------------------------------------------------"
#

from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)