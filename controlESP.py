import requests
from time import sleep

class ESPController:
    def __init__(self, url: str, direction: str):
        self.url = url
        self.direction = direction

    def disable(self):
        try:
            response = requests.get(self.url + "off")
        except requests.exceptions.Timeout as e:
            print(e.request.url)
            return "Error al detener el motor"
        return "Motor detenido"

    def enable(self):
        try:
            response = requests.get(self.url + "on")
        except requests.exceptions.Timeout as e:
            print(e.request.url)
            return "Error al encender el motor"
        return "Motor encendido"

    def step(self):
        try:
            response = requests.get(self.url + "step")
        except requests.exceptions.Timeout as e:
            print(e.request.url)
            return "Error al mover el motor"
        return "Motor movido"

    def status(self):
        try:
            response = requests.get(self.url)
        except requests.exceptions.Timeout as e:
            print(e.request.url)
            return "Error al obtener el estado del motor"
        return "Motor funcionando"

esp0 = ESPController("http://172.20.10.5/", "adelante")
esp1 = ESPController("http://172.20.10.6/", "atras")

def moveForward():
    esp1.disable()
    esp0.enable()
    esp0.step()
    return "Moviendo hacia adelante"

def moveBack():
    esp0.disable()
    esp1.enable()
    esp1.step()
    return "Moviendo hacia atras"


try:
    while True:
        try:
            status0 = esp0.status()
        except requests.exceptions.Timeout as e:
            print(e.request.url)
            continue
        try:
            status1 = esp1.status()
        except requests.exceptions.Timeout as e:
            print(e.request.url)
        
        if status0 == "Motor funcionando" and status1 == "Motor funcionando":
            print("Ambos motores funcionando")
            user_input = input("Movimiento (f/b/q): ")
            if user_input == "f":
                print(moveForward())
            elif user_input == "b":
                print(moveBack())
            elif user_input == "q":
                break
except KeyboardInterrupt:
    pass

