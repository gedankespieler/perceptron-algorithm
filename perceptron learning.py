def perceptron_algorithm(w, b, x, y):
    while sum_misclassified_points(w, b, x, y) > 0:
        for i in range(0, len(x)):
            if (y[i] * (dot_product(w , x[i]) + b) <= 0):
                for j in range(0, len(w)):
                    w[j] = w[j] + y[i]*x[i][j]
                b = b + y[i]
    print([w, b])
    print(sum_elements(w, b))

def sum_misclassified_points(w, b, x, y):
    s = 0
    for i in range(0, len(w)):
        if (y[i]*(dot_product(w, x[i]) + b) <= 0):
            s += 1
    return s

def dot_product(a, c):
    return sum([a[i] * c[i] for i in range(0, len(a))])
    
def sum_elements(w, b):
    return sum(w) + b

if __name__ == "__main__":
    w = [0, 0]
    b = 0
    x = [[-1, 1], [0, -1], [10, 1]]
    y = [1, -1, 1]
    k = 0

    perceptron_algorithm(w, b, x, y)
