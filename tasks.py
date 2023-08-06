start_day = 1
start_month = 1
start_year = 1970

# number of seconds in question
n_s = 321651669
    
#sec_in_yr = 31536000

# add year
years_added = n_s // 31536000
print(years_added)

# find days left 
days_remain = (n_s - (31536000*years_added)) // 86400
print(days_remain)

# days until leap day = after 59 days


import calendar
def calc_leap_days(yr):
    # should replaced .isleap() with custome function
    start_year = 1970 + 2
    leap_days = 0
    while start_year <= yr:
        if calendar.isleap(start_year):
            leap_days +=1
        start_year +=4
    return leap_days
    
print(calc_leap_days(2120))
