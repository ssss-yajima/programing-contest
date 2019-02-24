import datetime
s =datetime.datetime.strptime(input(), '%Y/%m/%d')

if s<=datetime.datetime(2019,4,30,0,0,0):
    print('Heisei')
else:
    print('TBD')