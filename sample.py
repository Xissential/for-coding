ctemp = 25 #selection
thigh = 34.9
tlow = -23.9
if ctemp > tlow and ctemp < thigh:
    print('Current temperature ('+ str(ctemp) +') is within the range of high and low temperatures.')

# iteraton
SENTINEL = -999
n=int(input("Enter a number to display, or -999 to stop: "))
while n!= SENTINEL:
    print(n)
    n=int(input("Enter a number to display, or -999 to stop: "))
print("End of program.")

#example of iteration
#accumalator and counter
score_of_the_player = int(input("Enter a score of the test -1 to stop): "))
total_score = 0
scorecount = 0
while score_of_the_player != -1:
    total_score = total_score + score_of_the_player
    scorecount += 1
    score_of_the_player = int(input("Enter a score of the test -1 to stop): "))
if scorecount > 0:
    print('The average for the test is: ', total_score/scorecount)
else:
    print("No scores were entered.")








