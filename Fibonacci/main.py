def is_fibonacci(n):
    def fibonacci_sequence(limit):
        a, b = 0, 1
        sequence = [a, b]
        while b <= limit:
            a, b = b, a + b
            sequence.append(b)
        return sequence

    fibonacci_list = fibonacci_sequence(n)


    if n in fibonacci_list:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."
