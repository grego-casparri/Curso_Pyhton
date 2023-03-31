import itertools

def turno_perfumeria():
    for num in itertools.count(start=1, step=1):
        yield f'P-{num:03d}'

def turno_farmacia():
    for num in itertools.count(start=1, step=1):
        yield f'F-{num:03d}'

def turno_cosmeticos():
    for num in itertools.count(start=1, step=1):
        yield f'C-{num:03d}'

def mensaje_turno(func):
    def wrapper(*args, **kwargs):
        turno = func(*args, **kwargs)
        return f"Su turno es {turno}. Aguarde y será atendido."
    return wrapper
