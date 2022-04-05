from datetime import datetime
from time import strftime

class Achievement:
    def __init__(self, sport, date: datetime, duration):
        self.sport = sport
        self.date = date
        self.duration = duration
    
    def __str__(self):
        return f'Date: {self.date}, sport: {self.sport}, duration: {self.duration} min'

