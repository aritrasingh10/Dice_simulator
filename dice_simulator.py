import random

while True:
    print('Enter the choice : 1. for play. 2. for exit')
    n = int(input())
    if(n==1):
        result = random.randint(1,6)
        print(result)
    else:
        break    
