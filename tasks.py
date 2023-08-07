start_day = 1
start_month = 1
start_year = 1970

months = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31
}

# number of seconds in question
n_s = 321651669
    
#sec_in_yr = 31536000


# add year
years_added = n_s // 31536000
new_year = years_added + start_year
print("YEARS ADDED: ",new_year)

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

leap_days = calc_leap_days(start_year + years_added)
print("LEAP DAYS TO BE ADDED:", leap_days)


# find days left 
days_remain = (n_s - (31536000*years_added)) // 86400
print("DAYS REMAINING: ",days_remain)



# FIND days:
# LEAP DAYS + DAYS REMAINING
if calendar.isleap(new_year):
    if days_remain+leap_days <= 59:
        total_days = days_remain + leap_days - 1
        extra_leap = no
    else:
        total_days = days_remain + leap_days
        extra_leap = yes
        # change Februarys days from 28 -> 29
        months.update({2: 29})


# find month
total = 99
for key,value in months.items():
    if (total - value) <= 0:
        return (total,key)
    else:
        total -= value


"""
def my_func(total):
    
    for key,value in months.items():
        if (total - value) <= 0:
            return (total,key)
        else:
            total -= value

print(my_func(91))


"""
