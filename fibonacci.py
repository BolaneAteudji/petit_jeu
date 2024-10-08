def suite_de_fibonacci(n):
    a, b = 1, 1
    if n >= 1:
        yield a
    if n >= 2:
        yield b
    for _ in range(2, n):
        a, b = b, a + b
        yield b

def afficher_suite_fibonacci(n):
    print(f"Les {n} premiers termes de la suite de Fibonacci sont :")
    for terme in suite_de_fibonacci(n):
        print(terme)

if __name__ == "__main__":
    try:
        n = int(input("Entrez le nombre de termes de la suite de Fibonacci à générer : "))
        if n < 1:
            print("Veuillez entrer un nombre entier positif.")
        else:
            afficher_suite_fibonacci(n)
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

