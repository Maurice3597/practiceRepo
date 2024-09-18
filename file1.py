import time as dt
#import os
created_on = (dt.strftime("%m-%d-%y"))
with open(created_on, 'x') as date_file:
    date_file.write("today")