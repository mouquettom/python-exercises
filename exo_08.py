def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Avant d'exécuter la fonction '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"Après l'exécution de la fonction '{func.__name__}'")
        return result

    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
