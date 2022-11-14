num = int(input("\033[34mESCOLHA UM NÚMERO: \n"))
tab = print("Sua tabuada é:")
for val in range(1, 11):
    res = num * val
    print("\033[97m{} x {} = {} ".format(num, val, res))

