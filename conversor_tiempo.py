"""
Funcion que recibe un string de fecha y hora y 
devuelve esa fecha y hora en formato humano.
Ej: "20.04.1995 12:00" -> 20 april 1995 year 12 hours 00 minutes
"""

from datetime import datetime


def date_time(time: str) -> str:
    """
    input: time (str)
    output: time (str)
    """
    try:
        time = datetime.strptime(time, '%d.%m.%Y %H:%M')
        day = int(time.strftime("%d"))
        hour = int(time.strftime("%H"))
        minutes = int(time.strftime("%M"))
        h = "hours"
        m = "minutes"
        if hour == 1:
            h = "hour"
        if minutes == 1:
            m = "minute"
        return time.strftime(str(day) + " %B %Y year " + str(hour) + " " + h + " " + str(minutes) + " " + m)
    except ValueError:
        return "Fecha/hora no válida"


print(date_time("20.04.1995 01:01"))
print(date_time("04.10.1999 18:21"))
print(date_time("43.10.1990 28:00"))
