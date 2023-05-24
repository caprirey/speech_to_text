import speech_recognition as sr
# first feature
# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

# Configurar el micrófono como fuente de entrada de audio
with sr.Microphone() as source:
    print("Di algo...")
    # Escuchar el audio del micrófono
    audio = r.listen(source)

# Intentar reconocer el texto del audio usando el reconocedor de voz de Google
try:
    command = r.recognizer.recognize_google(audio, lenguage="es-ES")
    # Imprimir el comando reconocido
    print("Comando: " + command)
except sr.UnknownValueError:
    print("No se pudo entender el comando")
except sr.RequestError as e:
    print("Error al obtener resultados del servicio de reconocimiento de voz: {0}".format(e))