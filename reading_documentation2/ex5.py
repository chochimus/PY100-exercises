from datetime import date

today = date.today()

today_year = today.year
# .year is a read only instance attribute of a date object
iso_year = today.isocalendar()[0]
# .isocalendar returns a tuple that has a year component.
# ISO is a variation of the Gregorian calendar