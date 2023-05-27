import random

response = input("Do you want to roll? ")

while response=="y" or "Y":
    number = random.randint(1, 6)
    
    if number == 1:
        print("[   ]")
        print('[ 0 ]')
        print("[   ]")
    elif number == 2:
        print("[0  ]")
        print('[   ]')
        print("[  0]")
    elif number == 3:
        print("[0  ]")
        print('[ 0 ]')
        print("[  0]")
    elif number == 4:
        print("[0 0]")
        print('[   ]')
        print("[0 0]")
    elif number == 5:
        print("[0 0]")
        print('[ 0 ]')
        print("[0 0]")
    else:
        print("[0 0]")
        print('[0 0]')
        print("[0 0]")

    response = input("Press Y to roll again and N to exit:")