def hacer_diagnostico(nodo):
    if 'diagnostico' in nodo:
        return nodo['diagnostico']

    respuesta = input(nodo['pregunta'] + ' (si/no): ')
    if respuesta == 'si':
        return hacer_diagnostico(nodo['si'])
    elif respuesta == 'no':
        return hacer_diagnostico(nodo['no'])
    else:
        print("Respuesta no válida.")
        return hacer_diagnostico(nodo)


def recorrido_postorden(nodo):
    if 'diagnostico' in nodo:
        print(f"Diagnóstico encontrado: {nodo['diagnostico']}")
        return

    recorrido_postorden(nodo['si'])
    recorrido_postorden(nodo['no'])
    print(f"Nodo revisado: {nodo['pregunta']}")


def actualizar_arbol(nodo):
    print(f"El diagnóstico proporcionado fue: {nodo['diagnostico']}")
    correcto = input("¿Fue correcto? (si/no): ")

    if correcto == 'no':
        nueva_pregunta = input("Introduce una nueva pregunta para diferenciar este diagnóstico: ")
        nuevo_diagnostico = input("Introduce el diagnóstico correcto: ")
        nodo['pregunta'] = nueva_pregunta
        nodo['si'] = {'diagnostico': nuevo_diagnostico}
        nodo['no'] = {'diagnostico': nodo['diagnostico']}
        del nodo['diagnostico']


def main():
    arbol = crear_arbol()

    print("Bienvenido al sistema de diagnóstico médico")
    diagnostico = hacer_diagnostico(arbol)
    print(f"Diagnóstico final: {diagnostico}")

    opcion = input("¿Deseas actualizar el árbol? (si/no): ")
    if opcion == 'si':
        actualizar_arbol(arbol)

    print("Recorrido postorden para verificar estructura del árbol:")
    recorrido_postorden(arbol)


if __name__ == "__main__":
    main()
