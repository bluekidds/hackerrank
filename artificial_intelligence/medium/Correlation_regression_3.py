# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


score_X_str = "15  12  8   8   7   7   7   6   5   3"
score_X = [float(x) for x in score_X_str.split()]
score_Y_str = "10  25  17  11  13  17  20  13  9   15"
score_Y = [float(x) for x in score_Y_str.split()]
def OLS_model(X, Y):
    length = len(X)

    x_m = sum(X) / length
    y_m = sum(Y) / length

    # Ordinary Least Square Method
    x_res = [x - x_m for x in X]
    y_res  = [x - y_m for x in Y]

    n1 = sum([xm*ym for xm, ym in zip(x_res, y_res)])
    n2 = sum([xm**2 for xm in x_res])
    slope = round(n1/n2, 3)

    intercept = y_m - slope * x_m
    return (slope, intercept)

def predict(model, X_test):
    slope, intercept = model
    return slope * X_test + intercept

model = OLS_model(score_X, score_Y)

print(predict(model, 10))
