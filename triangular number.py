def print_triangular_numbers(x):
    sum = 0
    for num in range(1, x+1):
        sum += num
        print(num, "\t", sum)
print_triangular_numbers(5)