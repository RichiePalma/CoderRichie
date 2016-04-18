import time

def stopwatch(seconds):
    start = time.time() #.time Return time in seconds

    #time.clock()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print (elapsed +1) #time.clock, elapsed
        #There was a glitch between 1 and 2 seconds when it printed the same value, barely.
        #So +1 to avoid this glitch
        time.sleep(1) #Return value per second
stopwatch(20) #When the count will stop
#Because of the +1 in the printing, the counter will print always an extra second
#Example: stopwatch(10) then counter will reach 11
#Each 10 seconds the count desynchronizes a maximum of 0.6 seconds
#This was known by comparing it with my cellphone's chronometer
