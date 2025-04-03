import json


def cargar_arbol(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {
            "pregunta": "¿Es un ser vivo?",
            "si": {
                "pregunta": "¿Es un animal?",
                "si": {
                    "pregunta": "¿Vuela?",
                    "si": {
                        "pregunta": "¿Tiene plumas?",
                        "si": {"adivinanza": "Un loro"},
                        "no": {"adivinanza": "Un murciélago"}
                    },
                    "no": {
                        "pregunta": "¿Es doméstico?",
                        "si": {"adivinanza": "Un perro"},
                        "no": {"adivinanza": "Un tigre"}
                    }
                },
                "no": {
                    "pregunta": "¿Tiene raíces?",
                    "si": {
                        "pregunta": "¿Da frutos comestibles?",
                        "si": {"adivinanza": "Un manzano"},
                        "no": {"adivinanza": "Un pino"}
                    },
                    "no": {"adivinanza": "Un hongo"}
                }
            },
            "no": {
                "pregunta": "¿Se puede usar para comunicarse?",
                "si": {
                    "pregunta": "¿Tiene pantalla?",
                    "si": {"adivinanza": "Un teléfono móvil"},
                    "no": {"adivinanza": "Un walkie-talkie"}
                },
                "no": {
                    "pregunta": "¿Es un alimento?",
                    "si": {
                        "pregunta": "¿Es dulce?",
                        "si": {"adivinanza": "Un pastel"},
                        "no": {"adivinanza": "Una pizza"}
                    },
                    "no": {
                        "pregunta": "¿Tiene ruedas?",
                        "si": {
                            "pregunta": "¿Se usa para transporte personal?",
                            "si": {"adivinanza": "Una bicicleta"},
                            "no": {"adivinanza": "Un camión"}
                        },
                        "no": {"adivinanza": "Una roca"}
                    }
                }
            }
        }


def guardar_arbol(nombre_archivo, arbol):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(arbol, archivo, ensure_ascii=False, indent=4)


def jugar_adivinanza(nodo):
    if 'adivinanza' in nodo:
        respuesta = input(f"¿Es {nodo['adivinanza']}? (si/no): ")
        if respuesta.lower() == 'si':
            print("¡Genial! He adivinado.")
        else:
            nuevo_objeto = input("¿Qué era entonces?: ")
            nueva_pregunta = input(f"Escribe una pregunta para diferenciar {nuevo_objeto} de {nodo['adivinanza']}: ")
            respuesta_correcta = input(f"Para {nuevo_objeto}, ¿la respuesta a '{nueva_pregunta}' es 'si' o 'no'?: ")

            nodo['pregunta'] = nueva_pregunta
            if respuesta_correcta.lower() == 'si':
                nodo['si'] = {"adivinanza": nuevo_objeto}
                nodo['no'] = {"adivinanza": nodo['adivinanza']}
            else:
                nodo['si'] = {"adivinanza": nodo['adivinanza']}
                nodo['no'] = {"adivinanza": nuevo_objeto}

            del nodo['adivinanza']
    else:
        respuesta = input(nodo['pregunta'] + ' (si/no): ')
        if respuesta.lower() == 'si':
            jugar_adivinanza(nodo['si'])
        else:
            jugar_adivinanza(nodo['no'])


def recorrido_preorden(nodo):
    if 'adivinanza' in nodo:
        print(f"Adivinanza: {nodo['adivinanza']}")
        return

    print(f"Pregunta: {nodo['pregunta']}")
    recorrido_preorden(nodo['si'])
    recorrido_preorden(nodo['no'])


def main():
    nombre_archivo = "arbol_adivinanzas.json"
    arbol = cargar_arbol(nombre_archivo)

    print("Bienvenido al juego de adivinanzas")
    jugar_adivinanza(arbol)

    print("Guardando el árbol actualizado...")
    guardar_arbol(nombre_archivo, arbol)

    print("Recorrido preorden del árbol:")
    recorrido_preorden(arbol)


if __name__ == "__main__":
    main()


