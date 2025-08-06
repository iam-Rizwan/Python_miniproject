def factorial_iterative(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        product = 1
        for i in range(1, n + 1):
            product *= i
        return product
n=int(input("enter a N value"))
product=factorial_iterative(n)
print(product)