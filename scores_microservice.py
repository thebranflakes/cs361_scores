import random
import time

while True:
    service_file = open("house_price.txt", "r")
    random_num = random.randint(100000, 1200000)


    if service_file.readline() == "go\n":
        service_file.close()
        
        service_file = open("house_price.txt", "w")
        print("Message Received, writing int...")
        service_file.write(str(random_num))
        print("Message Sent")
        service_file.close

