

class RecurrentAlarm(object):

    def __init__(self):
        self._when = None
        self._triggered = False

    def set_every(self, minutes):
        self._when = minutes

    def is_triggered(self):
        return self._triggered

    def notify(self, current_time):
        if self._when >= current_time:
            self._triggered = True


class FakeTimeline(object):

    def __init__(self):
        self._alarms = []
        self._current_time = 0

    def add(self, alarm):
        self._alarms.append(alarm)

    def run_for(self, minutes):
        self.monitor()
        self._current_time += minutes
        self.monitor()

    def monitor(self):
        for alarm in self._alarms:
            alarm.notify(self._current_time)
