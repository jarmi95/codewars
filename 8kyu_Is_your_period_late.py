from datetime import timedelta, date

def period_is_late(last, today, cycle_length):
    if today - last > timedelta(cycle_length):
        result = True
    else:
        result = False
    return result
