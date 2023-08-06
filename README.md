# part2 - function #2

Function 2 Specification
This function must have the following header: def my_datetime(num_sec). This function takes in an integer value that represents the number of seconds since the epoch: January 1st, 1970. The function takes num_sec and converts it to a date and returns it as a string with the following format: MM-DD-YYYY. It has the following specifications:

It may be assumed that num_sec will always be an int value  
It may be assumed that num_sec will always be a non-negative value  
Must be able to handle leap years  
Some examples:  

my_datetime(0) returns 01-01-1970  
my_datetime(123456789) returns 11-29-1973  
my_datetime(9876543210) returns 12-22-2282  
my_datetime(201653971200) returns 02-29-8360  
Your function handle all the computation itself. You are not permitted to use any library that can convert seconds to a date. This includes, but is not limited to:  

datetime  
arrow  
moment  
maya  
delorean  
freezegun  
