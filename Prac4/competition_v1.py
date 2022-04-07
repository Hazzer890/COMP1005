#
# comp_v1.py - input scores and competitors and receive scores
#

numJudges = 7
numComps = int(input("A number of competitors (between 3 - 16 inc): "))

for i in range(numComps-1):
    totalC = 0
    print("input scores between 0 and 10 for each judge \n")
    for j in range(numJudges-1):
        scoreJ = int(input("input score for judge: "))
        totalC = totalC + scoreJ
    scoreC = totalC / numJudges
    print("\nScore for competitor ", j, "is ", scoreC)

