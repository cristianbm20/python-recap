"""
Funcion que devuelve el angulo que forma el sol con el
horizonte segun la hora que se le pase. A las 6:00 el
angulo es 0, a las 12:00 es 90 y a las 18:00 180. Si la
hora pasada no esta entre 6:00 y 18:00 devolvera el
mensaje: no veo el sol!
"""
from typing import Union
import math


def sun_angle(time: str) -> Union[int, str]:
    """
    input: the time of the day (str)
    output: the angle of the sun, rounded to 2 decimal places (str)
    """
    time = time.split(":")
    h = int(time[0])
    m = int(time[1])
    angle = 0
    if h >= 0 and h <= 23 and m >= 0 and m <= 59:
        if h > 18 or h < 6 or h == 18 and m > 0:
            return "I don't see the sun!"
        else:
            angle = (h - 6) * 15 + m * 0.25
            decimal = math.modf(angle)
            if decimal == 0.0:
                angle = int(angle)
            return str(angle) + "°"
    else:
        return "Invalid time"


print(sun_angle("06:00"))
print(sun_angle("12:35"))
print(sun_angle("18:00"))
print(sun_angle("05:30"))
print(sun_angle("28:90"))
