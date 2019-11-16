def minion_game(str):
    vowels = "AEIOU"
    Kevin, Stuart = 0 ,0
    for i in range(len(str)):
        if str[i] in vowels:
            Kevin += len(str)-i
        else:
            Stuart += len(str)-i
    if Kevin == Stuart:
        print("Draw")
    else:
        winner = "Kevin" if Kevin > Stuart else "Stuart"
        score = max(Kevin,Stuart)
        print("{0} {1}".format(winner, score))

if __name__ == "__main__":
    str = input()
    minion_game(str)
    


