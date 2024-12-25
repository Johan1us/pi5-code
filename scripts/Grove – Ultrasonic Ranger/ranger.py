import grovepi
import time

# Stel poortnummer in, bijvoorbeeld D5
ultrasonic_port = 5  

while True:
    try:
        distance = grovepi.ultrasonicRead(ultrasonic_port)
        print(f"Afstand: {distance} cm")
        time.sleep(1)

    except KeyboardInterrupt:
        break
    except IOError:
        print("I/O Error")
