for a in range(1,101):
##逢7就过的小游戏
    if a % 7 == 0 or a % 10 ==7 or a // 10 ==7:
        continue
    print(a)

