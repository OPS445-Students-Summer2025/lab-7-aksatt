#!/usr/bin/env python3
# Student ID: aksatt

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__,
                            format_time, sum_times, change_time,
                            time_to_sec, valid_time, __add__
    """
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Used by print() and str() to display object"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Used by interactive shell to display object"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return time as a string with : separators"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two Time objects and return a new Time object"""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Modify the current Time object by a number of seconds"""
        total_seconds = self.time_to_sec() + seconds
        if total_seconds < 0:
            total_seconds = 0
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second
        return None

    def time_to_sec(self):
        """Convert the Time object into total seconds since midnight"""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check if the Time object has valid hour, minute, and second"""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def __add__(self, t2):
        """Overload the + operator to add two Time objects"""
        return self.sum_times(t2)

# External function
def sec_to_time(seconds):
    """Convert seconds since midnight into a Time object"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
