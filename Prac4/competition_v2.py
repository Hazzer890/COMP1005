#
# comp_v2.py - input scores and competitors and receive scores
#

numJudges = 7
numComps = int(input("A number of competitors (between 3 - 16 inc): "))
while numComps < 3 or numComps > 16:
    numComps = int(input("Error - Re-enter number of competitors (between 3 - 16 inc)"))

for i in range(numComps):
    totalC = 0
    print("input scores between 0 and 10 for each judge \n")
    for j in range(numJudges):
        scoreJ = int(input("input score for judge: "))
        while scoreJ < 0 or scoreJ > 10:
            scoreJ = int(input("Error - Re-enter score (0-10)"))
        totalC = totalC + scoreJ
    scoreC = totalC / numJudges
    print("\nScore for competitor ", j, "is ", scoreC)

