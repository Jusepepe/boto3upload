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

    def step(self, steps: int):
        try:
            response = requests.get(self.url + "step/" + str(steps))
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

    def limitSwitch(self):
        try:
            response = requests.get(self.url + "limitSwitch")
            state = response.text.split(":")[1].strip()
            return state
        except requests.exceptions.Timeout as e:
            print(e.request.url)
            return "Error al obtener el estado del switch"

esp0 = ESPController("http://172.20.10.5/", "adelante")
esp1 = ESPController("http://172.20.10.6/", "atras")

def moveForward():
    esp1.disable()
    esp0.enable()
    esp0.step(2000)
    return "Moviendo hacia adelante"

def moveBack():
    esp0.disable()
    esp1.enable()
    esp1.step(2000)
    return "Moviendo hacia atras"

def checkLimitSwitch():
    state0 = esp0.limitSwitch()
    state1 = esp1.limitSwitch()
    return state0, state1

def returnToInitialPosition():
    esp0.disable()
    esp1.enable()
    esp1.step(100000)
    return "Moviendo hacia la posición inicial"

if __name__ == "__main__":
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


