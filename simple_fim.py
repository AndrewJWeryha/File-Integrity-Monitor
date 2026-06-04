import os
import hashlib
import time
from datetime import datetime, timedelta, timezone

#Setting up file paths
target_file = "C:/Users/Drew6/OneDrive/Desktop/My Portfolio/Projects/Projects/FIM_Lab/test.txt"
log_file = "C:/Users/Drew6/OneDrive/Desktop/My Portfolio/Projects/Projects/FIM_Lab/security_log.txt"

#Define EST timezone
EST = timezone(timedelta(hours =-4))

print("Reading file to set the initial baseline...")

#Calcualte the original hash of the file(The Baseline)
file_contents = open(target_file, "rb").read()
baseline_hash = hashlib.sha256(file_contents).hexdigest()

#Get current time in EST
baseline_time = datetime.now(EST).strftime("%Y-%m-%d %H:%M:%S EST")

print(f"Baseline time set. Last modification: {baseline_time}")
print(f"Baseline set. Target hash is: {baseline_hash[:10]}")
print("Monitoring started. Change the text file to trigger an alert.\n")

#Continuously check the file
while True:
    time.sleep(2) #Wait two seconds before checking again
    
    #Read file to see its current state
    current_contents = open(target_file, "rb").read()
    current_hash = hashlib.sha256(current_contents).hexdigest()
    
    #Compare the current hash to baseline
    if current_hash != baseline_hash:
        
        #Get exact time of modification
        mod_time = datetime.now(EST). strftime("%Y-%m-%d %H:%M:%S EST")
        log_message = (f"{mod_time} ALERT! File modification detected! New hash: {current_hash[:10]}\n")
        
        #Print message
        print(log_message.strip())
        
        #Append the message to security log document
        with open(log_file, "a") as f:
            f.write(log_message)
        
        #Update the baseline with new version
        baseline_hash = current_hash

