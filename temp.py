#Monitoring system_Krishna singh_202501100700194_B
import random
import time

min_limit = float(input("Enter minimum temperature: "))
max_limit = float(input("Enter maximum temperature: "))

if min_limit > max_limit:
    print("Error: Minimum limit cannot be higher than maximum limit.")
    exit()

print("Monitoring started... (Ctrl+C to stop)")

while True:
    temp = random.randint(0, 100)
    
    if temp > max_limit:
        print("Current Temp:", temp, "- Alert: Temperature is too high")
    elif temp < min_limit:
        print("Current Temp:", temp, "- Alert: Temperature is too low")
    else:
        print("Current Temp:", temp, "- Temperature is within acceptable limit")
        
    time.sleep(2)
