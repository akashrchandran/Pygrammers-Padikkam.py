import random

dice = [
    '''
    ┌─────────┐
    │         │
    │    ●    │
    │         │
    └─────────┘
    ''',
    '''
    ┌─────────┐
    │  ●      │
    │         │
    │      ●  │
    └─────────┘
    ''',
    '''
    ┌─────────┐
    │  ●      │
    │    ●    │
    │      ●  │
    └─────────┘
    ''',
    '''
    ┌─────────┐
    │  ●   ●  │
    │         │
    │  ●   ●  │
    └─────────┘
    ''',
    '''
    ┌─────────┐
    │  ●   ●  │
    │    ●    │
    │  ●   ●  │
    └─────────┘
    ''',
    '''
    ┌─────────┐
    │  ●   ●  │
    │  ●   ●  │
    │  ●   ●  │
    └─────────┘
    '''
]
while 1:
    ans = input("Do you want to roll the dice[Y/N]: ").upper()
    if ans in ['Y', 'YES']:
        n = random.randint(1,6)
        print("The dice lands on:")
        print(dice[n-1])
    elif ans in ['N', 'NO']:
        break
    else:
        print("Wrong selection!")
