import random
import time

# wait for the word "micro"
file = open("micro.txt", "r")
key = random.randint(1000, 50000)

while file.readline() != 'micro\n':
    file.seek(0)
    time.sleep(2)

print('Run signal found. Writing randint to text file...')
file_2 = open("micro.txt", "w")
file_2.write(str(key))
file_2.close()
print("Signal sent.")