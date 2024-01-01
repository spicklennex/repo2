"""
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.

pentru a rula acest trebuie sa se instaleze din terminal, pictograma ">_", din pycharm urmatoarea sintaxa
"pip install numpy" si enter
"""

from numpy import random


x = random.choice([1, 2, 3, 4, 5, 6])
y = int(input("ghiceste numarul zarului aruncat de calculator: "))
#if y not in [1,2,3,4,5,6]: se poate scrie si ca lista
if not((y==1) or (y==2) or (y==3) or (y==4) or (y==5) or (y==6)):
    print("numarul ales nu este intre 1 si 6")
    print("alege un numar inte 1 si 6 ca sa te joci")
else:
    if x==y:
	    print(f"Ai ghicit. Felicitări! Ai ales {y} si zarul a fost {x}.")
	    print(f"calculatorul a aruncat {x}")
    elif x < y:
	    print(f"Ai pierdut. Ai ales un numar mai mare.Ai ales {y} dar a fost {x}.")
	    print(f"calculatorul a aruncat {x}")
    else:
        print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {y} dar a fost {x}")
        print(f"calculatorul a aruncat {x}")