def minion_game(string):
    p1 = 0;
    p2 = 0;
    string_len = len(string)
    for i in range(string_len):
        if string[i] in "AEIOU":
            p1 += (string_len)-i
        else :
            p2 += (string_len)-i
    
    if p1 > p2:
        print("Kevin", p1)
    elif p1 < p2:
        print("Stuart",p2)
    elif p1 == p2:
        print("Draw")
    else :
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)