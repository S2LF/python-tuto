a = 6

# variable magique qui permet d'executer du code uniquement si on est dans le module (pas d'import)
if __name__ == '__main__':
    print("C'est le script principal")
print("C'est le module")

def add(a, b):
    """Fonction qui additionne deux nombres

    Args:
        a (int): Le premier nombre
        b (int): Le second nombre

    Returns:
        int: La somme des deux nombres
    """
    return a + b