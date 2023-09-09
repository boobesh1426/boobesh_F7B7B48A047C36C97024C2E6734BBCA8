# Leap year

"""
Year % 4 == 0 &
Year % 100 != 0 /
Year % 400 == 0

"""
def isLeapYear(year):
  if(year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
     return True 
  else:
     return False

year = 2012
if isLeapYear(year):
  print("{} is a leap year.". format (year))
else:
  print ("{} is not a leap year.".format(year))