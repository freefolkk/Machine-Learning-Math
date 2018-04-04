import csv

#fetching data from a csv file
filepath = open("data.csv")
csvReader = csv.reader(filepath)

points = []

for x,y in csvReader:
    points.append([float(x),float(y)])

#calculating error
def calculate_error(points, m , b):
    error = 0     
    N = float(len(points))
    for point in points:
        x = point[0]
        y = point[1]
        temp = y - (m*x + b)
        error+= temp*temp

    return error/N     

def gradient_descent( b_initial, m_initial, points):
        b_gradient = 0
        m_gradient = 0
        N = float(len(points))
        for point in points:
            x = point[0]
            y = point[1]
            b_gradient += -(2/N) * (y - ((m_initial * x) + b_initial))
            m_gradient += -(2/N) * x * (y - ((m_initial * x) + b_initial))
        
        b = b_initial - b_gradient*(.0001) # .0001 is the learning rate
        m = m_initial - m_gradient*(.0001)
        return [b, m]

#initial b,m values and number of iterations
iterations = 1000
b=0
m=0
for i in range(iterations):
   b, m = gradient_descent(b, m, points)
   print(" (b , m , error) => " ,(b, m , calculate_error(points, m , b))) 