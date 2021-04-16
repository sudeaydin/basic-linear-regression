def get_y(m, b, x):
  return m*x+b

def calculate_error(m,b,point):
    x_point=point[0]
    y_point=point[1]
    return abs(get_y(m,b,x_point)-y_point)

def calculate_all_error(m,b,points):
    total=0
    for point in points:
        total+=calculate_error(m, b, point)
    return total


datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
possible_ms=[i*0.1 for i in range(-100,101)]
possible_bs =[i*0.1 for i in range(-200,201)]

smallest_error=float("inf")
best_m=0
best_b=0
for m in possible_ms:
    for b in possible_bs:
        if calculate_all_error(m,b,datapoints)< smallest_error:
            best_m=m
            best_b=b
            smallest_error=calculate_all_error(m,b,datapoints)
print(best_m)
print(best_b)
print(smallest_error)

print(get_y(0.3,1.7,6))
