
# ======================
# 27_Date_and_Time.py
# ======================


# This is the link for time module

# https://docs.python.org/2/library/time.html
# We see an explanation of epoch (start of time)

# The epoch is the point where the time starts. On January 1st of that year,
# at 0 hours, the “time since the epoch” is zero. For Unix, the epoch is 1970.
# To find out what the epoch is, look at gmtime(0).

# We have to import time module

import time

print(time.gmtime(0))  # Prints tuple with epoch time (1970) because we gave it parameter 0
print()
print(time.localtime())  # prints tuple with current local time
print()
print(time.time())  # Prints local time in seconds from epoch (1970) to current time
print()
print(time.localtime(time.time()))  # We passed local time to it. So it prints local time
print()

print("="*40)


# We can go through the time tuple above and get the year, month, and day

# Method 1 to printing Year, Month, Day etc using keys

import time
time_here = time.localtime()  # Assign localtime() to variable time_here


print(time_here)  # print time here to show the whole tuple containing time
print()
print("Year:", time_here[0])  # prints year which is first element in time_here
print("Month:", time_here[1])  # prints month which is the second element in time_here
print("Day:", time_here[2])    # prints Day which is the third element in time_here

print("="*40)

# Method 2 of printing Year, Month, Day etc using named tuple
# This method is easier to read because it indicates what you are printing

import time
print()
time_here = time.localtime()  # Assign localtime() to variable time_here

print(time_here)  # print time tuple. Shows naming e.g. tm_year for year, tm_mon for month etc
print()

print("Year:", time_here.tm_year)  # prints year by using the named tuple - tm_year
print("Month:", time_here.tm_mon)  # prints month by using the named tuple - tm_mon
print("Day:", time_here.tm_mday)    # prints Day by using the named tuple - tm_mday
print("Hour:", time_here.tm_hour)   # prints hour by using the named tuple - tm_hour

print("="*40)



# Reaction Game

# This game measures your reaction time by asking you to press enter and then
# checking how fast you press Enter



import time
from time import time as my_timer

print("time directory:")
print(dir(time))
print()

print("time.time is number of seconds from 1970 to now:")
print(time.time())
print()

print("time.time was assigned to my_timer :")
print(my_timer())
print()

import random

print("random directory:")
print(dir(random))
print()
input("Press enter to start: ")
print()

# documentation for random.randint
# https://docs.python.org/2/library/random.html

wait_time = random.randint(1, 6)  # randint is a function of random. Returns random integer between 1 and 6

# use time.sleep to make program sleep for the random time (wait_time) from above
# https://docs.python.org/2/library/time.html

time.sleep(wait_time)

# start_time is my_timer (which is seconds from 1970 to Now
# programs records the start time

start_time = my_timer()

# Then gives this message to have you press enter to stop

input("Press Enter to Stop: ")

# When you press enter, it runs this line to record the time in seconds from 1970 to when this line ran (right after you pressed Enter)
end_time = my_timer()

# time.strftime(format[, t]) stand for "string from time" and converts tuple representing time into a string
# https://docs.python.org/2/library/time.html
# %X <<== Locale’s appropriate time representation.

# Here we convert start_time, end_time into local time format, then convert it to string.

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("End at " + time.strftime("%X", time.localtime(end_time)))
print()

# reaction time will be end_time subtract start_time

print("Your reaction time was {} seconds".format(end_time - start_time))


print("="*40)




# Above program had a flaw that would enable you to cheat
# you can press enter twice after "start" prompt and it will accept the second
# enter and hence give a very small reaction time

# Another issue is that during daylight savings time, time can change before you
# press the second enter and it can show start time as being later than end time

# Another issue is computer clock can change during daylight savings again and this
# can result in start time being later than end time

# Python provides three more functions (other than time) that help us measure elapsed time



# using "time.perf_counter"

# This is the best way to measure elapsed time

# perf_counter gives an accurate measure of the elapsed time, but the value return
# does not represent actual time, but we can count the difference to find elapsed time

# https://docs.python.org/3/library/time.html
# time.perf_counter() - Return the value (in fractional seconds) of a performance counter,
# i.e. a clock with the highest available resolution to measure a short duration.
# It does include time elapsed during sleep and is system-wide.


import time
from time import perf_counter as my_timer  # import perf_counter

print("time directory:")
print(dir(time))
print()
print("time.perf_counter has reference that does not represent actual time:")
print(time.perf_counter())
print()
print("time.perf_counter was assigned to my_timer :")
print(my_timer())
print()

import random

print("random directory:")
print(dir(random))
print()
input("Press enter to start: ")
print()
wait_time = random.randint(1, 6)  # randint is a function of random. Returns random integer between 1 and 6
time.sleep(wait_time)
start_time = my_timer()
input("Press Enter to Stop: ")
end_time = my_timer()
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("End at " + time.strftime("%X", time.localtime(end_time)))
print()
print("Your reaction time was {} seconds".format(end_time - start_time))

print("="*40)




# using "time.monotonic"

# https://docs.python.org/3/library/time.html
# time.monotonic() - Return the value (in fractional seconds) of a monotonic clock,
# i.e. a clock that cannot go backwards. The clock is not affected by system clock updates.
# The reference point of the returned value is undefined, so that only the difference
# between the results of consecutive calls is valid.

# This means even if time changes in daylight savings or computer clock changes
# it does not affect the time references for monotonic

import time
from time import monotonic as my_timer  # import monotonic

print("time directory:")
print(dir(time))
print()
print("time.monotonic is a random number that cannot go backwards:")
print(time.monotonic())
print()
print("time.monotonic was assigned to my_timer :")
print(my_timer())
print()

import random

print("random directory:")
print(dir(random))
print()
input("Press enter to start: ")
print()
wait_time = random.randint(1, 6)  # randint is a function of random. Returns random integer between 1 and 6
time.sleep(wait_time)
start_time = my_timer()
input("Press Enter to Stop: ")
end_time = my_timer()
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("End at " + time.strftime("%X", time.localtime(end_time)))
print()
print("Your reaction time was {} seconds".format(end_time - start_time))

print("="*40)




# Using "process_time"
#
# process_time returns the time computer CPU uses to process the commands.
# Hence it gives very short reaction times which are impossible for a human to achieve
#
# https://docs.python.org/3/library/time.html
# time.process_time() =- Return the value (in fractional seconds) of the sum of the system and user
# CPU time of the current process. It does not include time elapsed during sleep.
# It is process-wide by definition. The reference point of the returned value is undefined,
# so that only the difference between the results of consecutive calls is valid


import time
from time import process_time as my_timer  # import monotonic

print("time directory:")
print(dir(time))
print()
print("Prints time.process_time i.e time CPU takes to process:")
print(time.process_time())
print()
print("time.process_time was assigned to my_timer :")
print(my_timer())
print()

import random

print("random directory:")
print(dir(random))
print()
input("Press enter to start: ")
print()
wait_time = random.randint(1, 6)  # randint is a function of random. Returns random integer between 1 and 6
time.sleep(wait_time)
start_time = my_timer()
input("Press Enter to Stop: ")
end_time = my_timer()
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("End at " + time.strftime("%X", time.localtime(end_time)))
print()
print("Your reaction time was {} seconds".format(end_time - start_time))

print("="*40)


# Monitonic time are discussed more in PEP (Python Enhancement Proposal) 0418
# https://www.python.org/dev/peps/pep-0418/



# ================
# Time Challenge:
# ================


# Write a small program to display information on the four clocks whose functions
# we have just discussed above i.e. time(), perf_counter(), monotonic(), and
# process_time().

# Use the documentation for the get_clock_info() function to work out how to
# call it for each of the clocks


# https://docs.python.org/3/library/time.html

# time.get_clock_info(name)
# Get information on the specified clock as a namespace object.
# Supported clock names and the corresponding functions to read their value are:
#
# 'clock': time.clock()
# 'monotonic': time.monotonic()
# 'perf_counter': time.perf_counter()
# 'process_time': time.process_time()
# 'time': time.time()

import time

print("Time() \t\t\t:", time.get_clock_info("time"))   # adjustable=True meaning time is adjustable
print("perf_counter() \t:", time.get_clock_info("perf_counter"))
print("monotonic() \t:", time.get_clock_info("monotonic"))
print("process_time \t:", time.get_clock_info("process_time"))

print("="*40)
