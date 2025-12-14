from datetime import datetime, timezone

from django import template

oderian_months = [
    "Gejām",
    "Krnā",
    "Krātjān",
    "Wesrān",
    "Melgintī",
    "Lentān",
    "Dassinī",
    "Esanes",
    "Kaitinān",
    "Kerublēnt",
    "Kruwanes",
    "Jeqlā",
]


def oderian_date(value: datetime) -> str:
    return f"{value.day} {oderian_months[value.month - 1]} {value.year}"


def oderian_dateago(value: datetime) -> str:
    now = datetime.now(tz=timezone.utc)
    diff = now - value
    secs = int(diff.total_seconds())
    mins = int(secs // 60)
    hours = int(mins // 60)
    days = int(hours // 24)
    if secs < 60:
        return "nu"
    elif mins == 1:
        return "frai qēsini"
    elif mins < 60:
        return f"frai {mins} qēsinamas"
    elif hours == 1:
        return "frai daitei"
    elif hours < 24:
        return f"frai {hours} daitimas"
    elif days == 1:
        return "frai deinai"
    elif days < 15:
        return f"frai {days} deinamas"
    else:
        return oderian_date(value)


register = template.Library()
register.filter("oderian_date", oderian_date, is_safe=True, expects_localtime=True)
register.filter(
    "oderian_dateago", oderian_dateago, is_safe=True, expects_localtime=True
)
