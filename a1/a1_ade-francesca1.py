
''' 
    This program will validate a given string in various forms as a birth date of someone and convert it into a standerd format. It will take a date in the following formats YYYYMMDD, YYYY/MM/DD, YYYY-MM-DD, YYYY.MM.DD and return the date in the mmm dd, yyyy format where mmm is the abbreviated months name (ex. Oct 7,2020 would come from 2020-10-07)
-----------------------------------------------------------------------
OPS435 Assignment 1 - Fall 2020
Program: a1_ade-francesca1.py 
Author: Adriano De Francesca
The python code in this file (a1_ade-francesca1.py) is original work written by
Adriano De Francesca. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(year):
    '''
    This function will take a year in YYYY format, and return True if the gicen year is a leap year, otherwise return False.
    '''	
    lyear = year % 4
    if lyear == 0:
        status = True # this is a leap year
    else:
        status = False # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        status = False # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        status = True # this is a leap year
    return status


def sanitize(obj1,obj2):
    '''
    Remove characters from obj1 that are not in obj2 
    '''
    newstring_list = []
    for char in obj1:
        for charcheck in obj2:
            if char in charcheck:
                newstring_list.append(char)
                results = "".join(newstring_list)

    return results

def size_check(obj, intobj):
    '''
    This function will take the sanitized data and an expected number of items as an interger. If the number of items in the data matches the integer number return true, if not return false.
    '''
    if len(obj) == int(intobj):
        status = True
    else:
        status = False
    return status


def range_check(obj1, obj2):
    '''
    This function will take an integer object and a tuple with two integer values, The first value of the tuple is the low end of the range and the second value is the hign end of the range. If the integer falls in the range from the tuple return true, if not return false.
    '''
    low, high = obj2

    if low <= obj1 <= high:
        status = True
    else:
        status = False
    return status

    
def usage():    
    '''
    This function will take no argument and return a string describing the usage of the script.
    '''

    status = 'Usage: a1_ade-francesca1.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD'
    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   #print('Sanitized user data:', dob)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   #print("Your date of birth is:", new_dob)  
   print(new_dob)
