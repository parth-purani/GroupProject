#!/usr/bin/env python3
#Date: 2023/03/21

#group member1 : Tirth Padsala
#group member2 : Parth Purani 
#group member3 : Ashish Senma

import random
import hashlib


with open('sampleData.txt', 'r') as f:
    data = f.readlines()

PH = "None"  #Starting now, the previous block's initialization to none would be the first step.

for line in data:
    semester_number = line[1:3]
    courses = [line[i:i+9] for i in range(3, len(line), 9)]  #We need to extract the classes we've completed.
    RN = random.randint(1, 1000000)  #This would be in charge of producing a random number that could range from 1 to 1000,000
    CH_data = " ".join(courses)  #Concatenation will be used to combine the completed courses into a single string
    CH = hashlib.sha256(CH_data.encode()).hexdigest()
    #printing block information in the following manner:
    print("PH:", PH)
    print("D:", line.strip())
    print("RN:", RN)
    print("CH:", CH)
    print()

    PH = CH  
