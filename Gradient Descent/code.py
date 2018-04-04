import numpy
import csv

filepath = open("housingData.csv")
csvReader = csv.reader(filepath)

points = []

for x,y in csvReader:
    points.append([float(x),float(y)])


def calculate_error(points, m , b):
    error = 0
    N = len(points)
    for point in points:
        x = point[0]
        y = point[1]
        temp = y - (m*x + b)
        error+= temp*temp

    return error/N     

print(calculate_error(points,0,0))