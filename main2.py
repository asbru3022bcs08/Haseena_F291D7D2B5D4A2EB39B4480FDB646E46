#leap year
def is Leapyear(year):
  if(year%4==0and year%100!=0):or year%400==0:
    return True
else:
return False
year=int(input("Enter a year:"))
if is Leapyear (year):
  print('{}is a leapyear.'.format(year))
else:
print('{}is not a leapyear.'.format year))
