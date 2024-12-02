from datetime import datetime

def format_date(date):
    """Formatiert ein Datum im Format DD.MM.YYYY"""
    return date.strftime("%d.%m.%Y")

def is_overdue(date):
    """Prüft, ob ein Datum in der Vergangenheit liegt"""
    return date < datetime.now().date()
