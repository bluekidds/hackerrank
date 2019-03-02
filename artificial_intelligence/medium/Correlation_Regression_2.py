import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
score_X_str = "15  12  8   8   7   7   7   6   5   3"
score_X = [float(x) for x in score_X_str.split()]
score_Y_str = "10  25  17  11  13  17  20  13  9   15"
score_Y = [float(x) for x in score_Y_str.split()]


length = len(score_X)

x_m = sum(score_X) / length
y_m = sum(score_Y) / length

score_x_m = [x - x_m for x in score_X]
score_y_m = [x - y_m for x in score_Y]

n1 = sum([xm*ym for xm, ym in zip(score_x_m, score_y_m)])
n2 = sum([xm**2 for xm in score_x_m])

slope = round(n1/n2, 3)
print(slope)
