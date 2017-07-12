# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#
 
print (1.0%1)
a = 1.0
print (a%1)
 
 
def convert_seconds(seconds):
    seconds = float(seconds)
    hours = seconds/3600
#    print hours
    minutes_dec = hours - int(hours)
    minutes = minutes_dec * 60
    seconds = seconds -(int(hours)*3600 + int(minutes)*60)
    if int(hours) == 1:
        hours_str = str(int(hours)) + " hour, "
    else:
        hours_str = str(int(hours)) + " hours, "
    if int(minutes) == 1:
        minutes_str = str(int(minutes)) + " minute, "
    else:
        minutes_str = str(int(minutes)) + " minutes, "
    print (seconds)
    print (seconds%1)
    if seconds%1 == 0.0:
        if int(seconds) == 1:
            seconds_str = str(int(seconds)) + " second"
        else:
            seconds_str = str(int(seconds)) + " seconds"
    else:
        seconds_str = str(seconds) + " seconds"
    return hours_str + minutes_str + seconds_str
 
 
print (convert_seconds(3661))
#>>> 1 hour, 1 minute, 1 second
 
#print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds
 
#print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
