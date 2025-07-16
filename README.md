# FLUJO DE TRABAJO
El sistema automático consta de:

## Sistema de captura de imágenes
1. Encendido del sistema en una hora en punto.
2. Se verifica si el carril llegó al final de carrera.
3. Se ejecuta un script que moverá el motor paso a paso hasta cierta posición.
4. Si no llegó, se capturan las imágenes y se suben al S3. 
5. Se repite el proceso hasta que el carril llegue al final de carrera.
6. El carril se mueve de regreso.

## Sistema de conteo de plagas
1. Se ejecuta un script que realizará el conteo de plagas y suben los resultados a S3
2. El sistema se apaga.

### 1. Encendido del sistema
Se ejecuta un servicio que enciende el sistema una hora en punto.

### 2. Se verifica si el carril llegó al final de carrera.
Bucle que verifica si el carril llegó al final de carrera.

### 3. Se ejecuta un script que moverá el motor paso a paso hasta cierta posición.
Petición al ESP32 para mover el motor paso a paso hasta cierta posición.

### 4. Si no llegó, se capturan las imágenes y se suben al S3. 
Raspberry captura las imágenes y las sube al S3.

### 5. Se repite el proceso hasta que el carril llegue al final de carrera.
Regresa al punto 2.

### 6. El carril se mueve de regreso.
Petición al ESP32 para mover el carril de regreso.

### 7. Se ejecuta un script que realizará el conteo de plagas y suben los resultados a S3
Petición al ESP32 para mover el carril de regreso.

