# DEFINICIÓN DE LAS PREGUNTAS CON SUS RESPUESTAS EN UN DICCIONARIO
preguntas = [
    {
        'pregunta': '¿Qué proxy es el que usamos a diario?',
        'opciones': ['a) Proxy Transparente', 'b) Proxy NAT', 'c) Proxy Reverse', 'd) Proxy SSL'],
        'respuesta': 'Proxy NAT'
    },
    {
        'pregunta': '¿Qué proxy se utiliza para transferir archivos de un servidor a otro?',
        'opciones': ['a) Transparente', 'b) Reverse', 'c) FTP', 'd) NAT'],
        'respuesta': 'FTP'
    },
    {
        'pregunta': '¿Qué función principal tiene un servidor proxy caché?',
        'opciones': ['a) Proporcionar anonimato ', 'b) Aumentar la seguridad ', 'c) Filtrar el tráfico ', 'd) Cachear contenido para acelerar el acceso a los sitios web'],
        'respuesta': 'Cachear contenido para acelerar el acceso a los sitios web'
    },
    {
        'pregunta': '¿Qué tipo de proxy es recomendable utilizar para una mayor seguridad en una organización?',
        'opciones': ['a) Proxy Web', 'b) Proxy Caché', 'c) Proxy SSL', 'd) Proxy NAT'],
        'respuesta': 'SSL'
    },
    {
        'pregunta': '¿Qué proxy cifra los datos enviados?',
        'opciones': ['a) Proxy SSL', 'b) Proxy Reverse', 'c) Proxy FTP', 'd) Proxy NAT'],
        'respuesta': 'SSL'
    }
]
# MÓDULO QUE FORMULA LAS PREGUNTAS Y RECOGE EL INPUT DEL USUARIO
def hacer_cuestionario(preguntas):
    puntuacion = 0
    respuestas_usuario = []
    for i, pregunta in enumerate(preguntas):
        print(f'{i + 1}. {pregunta["pregunta"]}')
        for opcion in pregunta['opciones']:
            print(opcion)
        respuesta_usuario = input('Respuesta: ')
        respuestas_usuario.append(respuesta_usuario)
        if respuesta_usuario == pregunta['respuesta']:
            puntuacion += 1
    print(f'Tu puntuación es {puntuacion}/{len(preguntas)}')
    for i, pregunta in enumerate(preguntas):
        if respuestas_usuario[i] != pregunta['respuesta']:
            print(f'Pregunta {i + 1} está mal. Respuesta dada: {respuestas_usuario[i]}. Respuesta correcta: {pregunta["respuesta"]}')


#EJECUCIÓN
hacer_cuestionario(preguntas)
