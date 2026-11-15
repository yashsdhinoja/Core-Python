# find and print the sum of the fibonacci series.

def fibonacci_series_sum(n):
    if n <= 0:
        return [],0
    elif n == 1:
        return [0],0

    series = [0,1]
    running_sum = 1

    for _ in range(2, n):
        next_term = series[-1] + series[-2]
        series.append(next_term)
        running_sum =+next_term

    return series, running_sum

num_terms = 10 
fib_series, total_sum = fibonacci_series_sum(num_terms)

print(f"Fibonacci Series ({num_terms} terms): {fib_series}")
print(f"total sum of number : {total_sum}")