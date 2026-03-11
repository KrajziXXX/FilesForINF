import random
def main(): 
    x = int(input("Podaj liczbe wierszy: "))
    y = int(input("Podaj liczbe kolumn: "))

    if(x == 0 or y == 0):
        return
    pos = [random.randint(0, x-1),random.randint(0, y-1)]
    print(pos)

    goal = [random.randint(0, x-1), random.randint(0, y-1)]
    while goal == pos:
        goal = [random.randint(0, x-1), random.randint(0, y-1)]

    map = [[None] * y for _ in range(x)]
    map[pos[0]][pos[1]] = "X"
    map[goal[0]][goal[1]] = "G"

    while True: 

        w = pos[0]
        s = x - pos[0] - 1
        a = pos[1]
        d = y - pos[1] - 1

        for row in map:
            print(" ".join("[X]" if el == "X" else "[G]" if el == "G" else "[]" for el in row))

        ruch = input("W/S/A/D")
        if(ruch.upper() == "W" and w != 0):
            pos [0]-= 1
        if(ruch.upper() == "S" and s != 0):
            pos [0]+= 1
        if(ruch.upper() == "A" and a != 0):
            pos [1]-= 1
        if(ruch.upper() == "D" and d != 0):
            pos [1]+= 1
        if (ruch.upper() not in ["W", "S", "A", "D"]):
            print("Niepoprawny ruch")
            continue
        if(w == 0 and s == 0 and a == 0 and d == 0):
            print("Nie można się ruszyć")
            break
        if(ruch.upper() == "E"):
            print("Koniec gry")
            break
        if pos == goal:
            print("Gratulacje, wygrałeś!")
            break
        map = [[None] * y for _ in range(x)]
        map[pos[0]][pos[1]] = "X"
        map[goal[0]][goal[1]] = "G"


        

    # while True:
    #     w = pos[0]
    #     s = x - pos[0] - 1
    #     a = pos[1]
    #     d = y - pos[1] - 1
    #     print("Możliwe ruchy:")
    #     if(w != 0):
    #         print("W górę (w):", w)
    #     if(s != 0):
    #         print("W dół  (s):", s)
    #     if(a != 0):
    #         print("W lewo (a):", a)
    #     if(d != 0):
    #         print("W prawo(d):", d)
    #     if w == 0 and s == 0 and a == 0 and d == 0:
    #         break
        
    


main()
