# Problem Definition: -
# In this problem we have to find the maximum number of activities that
# can be perfomed by a user. We are provided with the start time (at index 1)
# and end time (at index 2).

# Approach to solve the problem: -
# To solve this problem we will first sort the activities based on the end time
# then we will see if the end time of the previous activity is less
# than the start time of the current activity. If the condition satisfies we will
# perform the activity else we will go for the next activity


activities = [
    ["A1", 0, 6],
    ["A2", 3, 4],
    ["A3", 1, 2],
    ["A4", 5, 8],
    ["A5", 5, 7],
    ["A6", 8, 9],
]


def printMaxActivities(activities):
    i = 0
    activities.sort(key=lambda x: x[2])
    firstA = activities[i][0]
    print(firstA)

    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j


printMaxActivities(activities)
