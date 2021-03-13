import time
import typeOnce_DankMemerCommands

timeInterval = 0

time.sleep(5)

while True:
    print(timeInterval)
    timeInterval = 1
    while timeInterval <= 60:
        if timeInterval == 30:
            typeOnce_DankMemerCommands.Seconds30()
        if timeInterval == 40:
            typeOnce_DankMemerCommands.Seconds40()
        if timeInterval == 45:
            typeOnce_DankMemerCommands.Seconds45()

        time.sleep(1)
        timeInterval += 1