import hashlib
import random

#testHash = hashlib.new("sha256")

#testHash.update("1".encode())

#print(testHash.hexdigest())

value = "1"
#value = random.randint(0, 4294967295)
re = "10000"
count = 1
"""
00000 = 145113
"""

testHash = hashlib.sha256()

while (re[:4] != "0000"):

    testHash.update(value.encode())
    re = testHash.hexdigest()
    print(re)
    count += 1
    #value = str( int(value) + 1 )
    value = "1"
    value += str( random.randint(0, 4294967295) )


print(count)


"""
This is a simulation of a blockchain miner, it will start with a value string 1 at this point and it will attempt to find 
a has that stats with x amount of 0. Every cycle it will increment the value with a random int between of max 32bit value.
"""