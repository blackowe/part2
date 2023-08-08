
from datetime import datetime

def convert_seconds_to_date(num_sec):
    dt = datetime.utcfromtimestamp(num_sec)
    formatted_date = dt.strftime('%m-%d-%Y')
    return formatted_date

# Example usage
num_seconds = 9999999999
formatted_date = convert_seconds_to_date(num_seconds)
#print(formatted_date)


print(convert_seconds_to_date(999999))
print(convert_seconds_to_date(999999))
print(convert_seconds_to_date(999999))
print(convert_seconds_to_date(999999))
