



def is_leap_year(input_year):
    """ Returns bool if the input year is a leap year. """
    if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
      return True
    else:
      return False


def calc_leap_days(input_year):
    start_year = 1970 + 2
    leap_days = 0
    while start_year <= input_year:
        if is_leap_year(start_year):
            leap_days +=1
        start_year +=4
    return leap_days

"""
def calc_leap_days(input_year):
    leap_days = (input_year - 1972) // 4 + 1
    if input_year % 4 != 0:
        leap_days -= 1
    return leap_days
"""

def my_datetime(num_sec):
    #start_day = 1
    #start_month = 1
    #start_year = 1970
    months = { 1: 31, 2: 28, 3: 31, 4: 30,
              5: 31, 6: 30, 7: 31, 8: 31,
              9: 30, 10: 31, 11: 30, 12: 31
            }

    secs_yr = int(365.242189 * 24 * 60 *60)
    years_added = num_sec // secs_yr

    # Find Year
    new_year = years_added + 1970
    
    # Find days left
    # find raw days left 
    raw_days_added = (num_sec - (secs_yr * years_added)) // 86400

    leap_days = calc_leap_days(new_year)


"""
    # adjust 'raw_days_added' for current years leap day
    if is_leap_year(new_year):
        if raw_days_added + leap_days < 59:
            total_days = raw_days_added + leap_days -1
        else:
            total_days = raw_days_added + leap_days
            # change Februarys days from 28 -> 29
            months.update({2: 29})
    else:
        total_days = raw_days_added + leap_days

"""
    total_days = raw_days_added

    # Find day, month
    # check if total_days > 365
    if total_days >= 365:
        total_days = total_days % 365
    for key,value in months.items():
        if (total_days - value) <= 0:
            month, day =  key, total_days
            if day == 0:
                day = 1
            break
        else:
            total_days -= value

    # format days-month-year for output
    return (month, day, new_year)


print(my_datetime(0))
print(my_datetime(123456789))
print(my_datetime(9876543210)) # way off
#print(my_datetime(201653971200)) 


# attempt 2 -------------------------------------------------------------------------------------------
# best working method so far


def is_leap_year(input_year):
    """ Returns bool if the input year is a leap year. """
    if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
      return True
    else:
      return False


def calc_leap_days(input_year):
    start_year = 1970 + 2
    leap_days = 0
    while start_year <= input_year:
        if is_leap_year(start_year):
            leap_days +=1
        start_year +=4
    return leap_days


def my_datetime(num_sec):
    #start_day = 1
    #start_month = 1
    #start_year = 1970
    months = { 1: 31, 2: 28, 3: 31, 4: 30,
              5: 31, 6: 30, 7: 31, 8: 31,
              9: 30, 10: 31, 11: 30, 12: 31
            }

    secs_yr = int(365.242189 * 24 * 60 *60)
    years_added = num_sec // secs_yr

    # Find Year
    new_year = years_added + 1970
    
    # Find days left
    # find raw days left 
    total_days = (num_sec - (secs_yr * years_added)) // 86400

    #change feb
    if is_leap_year(new_year):
        months.update({2:29})

    # Find day, month
    # check if total_days > 365
    if total_days >= 365:
        total_days = total_days % 365
    for key,value in months.items():
        if (total_days - value) <= 0:
            month, day =  key, total_days
            if day == 0:
                day = 1
            break
        else:
            total_days -= value

    # format days-month-year string output with 0 padding
    date_output = f"{month:02d}-{day:02d}-{new_year:04d}"
    return date_output


print(my_datetime(0))
print(my_datetime(123456789))
print(my_datetime(9876543210)) # way off
print(my_datetime(201653971200)) 


# --- 3rd attempt raw: ----------------------------------------------

def is_leap_year(input_year):
    """ Returns bool if the input year is a leap year. """
    if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
      return True
    else:
      return False
    
def my_datetime(num_sec):
    start_day = 1
    start_month = 1
    start_year = 1970
    total_days = num_sec // (24*60*60)
    months = { 1: 31, 2: 28, 3: 31, 4: 30,
              5: 31, 6: 30, 7: 31, 8: 31,
              9: 30, 10: 31, 11: 30, 12: 31
            }
    
    while total_days >= 365:
        if is_leap_year(start_year) and total_days == 365:
            break
        elif is_leap_year(start_year):
            total_days -=366
        else:
            total_days -= 365
        start_year +=1
  

    # handle edge case 01-01-xxxx
    if total_days == 0:
        return f"{start_month:02d}-{start_day:02d}-{start_year:04d}"
    
    # set feb
    if is_leap_year(start_year):
        months.update({2:29})

    total_days += start_day
    for key,value in months.items():      

        if (total_days - value) <= 0:
            month, day =  key, total_days
            if day == 0:
                day = 1
            break
        else:
            total_days -= value
                    
    return f"{month:02d}-{day:02d}-{start_year:04d}"



# 3rd attempted - FINAL - refactored to be shorter ------------------------------------------


def is_leap_year(input_year):
    """ Returns bool if the input year is a leap year. """
    return (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0)

def my_datetime(num_sec):
    """
    This function takes in an integer value that represents the number of 
    seconds since the epoch: January 1st, 1970. The function takes num_sec 
    and converts it to a date and returns it as a string with the following 
    format: MM-DD-YYYY
    """
    start_day = 1
    start_year = 1970
    total_days = num_sec // (24*60*60)
    months = { 1: 31, 2: 28, 3: 31, 4: 30,
              5: 31, 6: 30, 7: 31, 8: 31,
              9: 30, 10: 31, 11: 30, 12: 31
             }

    # Find year, reduce total_days
    while total_days >= 365:
        if is_leap_year(start_year) and total_days == 365:
            break
        elif is_leap_year(start_year):
            total_days -=366
        else:
            total_days -= 365
        start_year +=1

    # Set leap year February
    if is_leap_year(start_year):
        months.update({2:29})

    # Find month/day
    total_days += start_day
    for key,value in months.items():
        if total_days <= value:
            month, day =  key, total_days
            break
        total_days -= value

    return f"{month:02d}-{day:02d}-{start_year:04d}"
