def suite_de_fibonacci(n):
    a=1
    b=1
    if n>=1:
        yield a
    if n>=2:
        for _ in range(2,n):
                a=b
                b=a+b
        yield b

print("Les", n, "premiers termes de la suite de fibonacci sont :")
for terme in suite_de_fibonacci(n):
print(terme)

