#
# comp_v3.py - input scores and competitors and receive scores
#

def inputValue(lower, upper, prompt):
    value = int(input())
    while value < lower or value > upper:
        print("Error - re-enter number (", lower, "-", upper, ")")
        print(prompt)
        value = int(input())
    return(value)

numJudges = 7
print("A number of competitors (between 3 - 16 inc)")
numComps = inputValue(3, 16, "A number of competitors (between 3 - 16 inc)")

for i in range(numComps):
    totalC = 0
    print("input scores between 0 and 10 for each judge \n")
    for j in range(numJudges):
        scoreJ = inputValue(0, 10, "input scores between 0 and 10 for each judge")
        totalC = totalC + scoreJ
    scoreC = totalC / numJudges
    print("\nScore for competitor ", j, "is ", scoreC)

