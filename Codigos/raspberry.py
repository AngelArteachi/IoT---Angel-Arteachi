import network
import urequests
import utime
from machine import ADC

# Configuración Wi-Fi
WIFI_SSID = "NOMBRE_DE_TU_WIFI"
WIFI_PASSWORD = "CONTRASEÑA_DE_TU_WIFI"
THING_SPEAK_CHANNEL_ID = "TU_CHANNEL_ID"
THING_SPEAK_API_KEY = "TU_API_KEY"
THING_SPEAK_URL = f"https://api.thingspeak.com/update?api_key={THING_SPEAK_API_KEY}"

# Conectar a Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        print("Conectando a Wi-Fi...")
        utime.sleep(1)
    print("Conectado a Wi-Fi! IP:", wlan.ifconfig()[0])

# Leer temperatura desde el sensor interno
def read_temperature():
    sensor_temp = ADC(4)  # Sensor interno de la Pico W
    conversion_factor = 3.3 / 65535  # Factor de conversión de ADC a voltaje
    reading = sensor_temp.read_u16() * conversion_factor  # Lectura en voltios
    temperature = 27 - (reading - 0.706) / 0.001721  # Fórmula de conversión a °C
    return round(temperature, 2)

# Enviar datos a ThingSpeak
def send_to_thingspeak(temperature):
    query_string = f"&field1={temperature}"
    response = urequests.get(THING_SPEAK_URL + query_string)
    print("Enviado a ThingSpeak: ", response.text)
    response.close()

# Ejecutar el sistema
connect_wifi()
while True:
    temp = read_temperature()
    print(f"Temperatura: {temp} °C")
    send_to_thingspeak(temp)
    utime.sleep(180)  # Esperar 180 segundos