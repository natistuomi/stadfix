import random
tal = random.randint(1, 10)
gissningar = 0

while True:
    gissa = int( input("Gissa på ett tal från 1-10: ") )

    gissningar = gissningar + 1

    if gissa == tal:
        print(f'Grattis! Du gjorde {gissningar} gissningar.')
        break
    elif gissa > tal:
        print("Talet är mindre än din gissning")
    elif gissa < tal:
        print("Talet är större än din gissning")