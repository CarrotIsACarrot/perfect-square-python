currentNum = 1
squareNum = currentNum
answer = 1

while True:
    squareNum = squareNum + 1
    printNum = squareNum
    answer = squareNum * squareNum
    print(str(printNum) + " is the squareroot of " + str(answer))
    input("Press enter to see next.\n")
