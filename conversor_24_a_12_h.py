"""
Funcion que recibe una hora en formato 24h y 
devuelve la misma hora en formato 12h a.m/p.m
"""

from datetime import datetime


def time_converter(time):
    """
    input: time (str)
    output: time (str)
    """
    time = datetime.strptime(time, "%H:%M")
    hour = int(time.strftime("%I"))
    midday = "a.m."
    if int(time.strftime("%H")) >= 12:
        midday = "p.m."
    return time.strftime(str(hour) + ":%M " + midday)


print(time_converter("21:00"))  # 9:00 p.m.
