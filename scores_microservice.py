import random

while True:
    service_file = open(r"service.txt", "r+")
    random_num = random.randint(100000, 1200000)

    if service_file.readline() == "go":
        service_file.seek(0)
        service_file.truncate(0)

        print("Message Received, writing int...")
        service_file.write(str(random_num))
        service_file.close()
        print("Message Sent")
