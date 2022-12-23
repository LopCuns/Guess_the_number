from random import randint

def generate():
    return randint(0,10)

print('---BIENVENIDO---')
print('Intenta adivinar el número comprendido entre el 0 y el 10')
def game(response = generate(),score = 10):
    num =int(input('Introduce tu intento  '))

    if num == response:
        print('---FELICIDADES--')
        print(f"--HAS ACERTADO, EL NÚMERO CORRECTO ERA EL {response}; tu puntuación ha sido : {score}")
        cont = input('--SI QUIERES JUGAR OTRA VEZ INTRODUCE Y,SINO, INTRODUCE N  ')
        if cont.upper() == 'Y':
            restart()
    elif num > response:
        print('--CASI, EL NÚMERO ES MÁS PEQUEÑO--')
        print('--SIGUE INTENTÁNDOLO')
        game(response,score - 1)
    elif num < response:
        print('--CASI-EL NÚMERO ES MÁS GRANDE--')
        print('--SIGUE INTENTÁNDOLO--')
        game(response,score - 1)
    else:
        print('--EL NÚMERO DEBE SER UN NÚMERO ENTERO COMPRENDIDO ENTRE EL 0 Y EL 10--')
        game(response,score - 1)
def restart():
    game(generate(),10)
game()