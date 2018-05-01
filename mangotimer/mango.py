import datetime


class RecurrentAlarm(object):

    def __init__(self):
        self._every = None
        self._trigger_time = None
        self._triggered = False
        self._snoozed = False
        self._postpone_by = 0

    def set_every(self, minutes):
        self._every = minutes

    def is_triggered(self):
        return self._triggered

    def switch_off(self):
        self._triggered = False
        self._snoozed = False
        self._postpone_by = 0

    def snooze(self, minutes):
        self._snoozed = True
        self._postpone_by = minutes

    def notify(self, current_time):
        if self._trigger_time is None:
            self._trigger_time = current_time + self._every

        if self._snoozed:
            self._trigger_time += self._postpone_by

        if self._trigger_time <= current_time:
            self._triggered = True
            self._trigger_time = current_time + self._every
            print('BEEP! BEEP!')


class FakeTimeline(object):

    def __init__(self):
        self._alarms = []
        self._current_time = 0

    def add(self, alarm):
        self._alarms.append(alarm)
        alarm.notify(self._current_time)

    def run_for(self, minutes):
        self._current_time += minutes
        self.monitor()

    def monitor(self):
        for alarm in self._alarms:
            alarm.notify(self._current_time)


class RealTimeline(object):

    def __init__(self):
        self._alarms = []
        self._current_time = datetime.datetime.now()
        self._time_increment = None

    def add(self, alarm):
        self._alarms.append(alarm)
        alarm.notify(self._current_time)

    def run(self):
        while True:
            now = datetime.datetime.now()
            self._time_increment = now - self._current_time
            self._current_time = now
            self.monitor()

    def monitor(self):
        for alarm in self._alarms:
            alarm.notify(self._current_time)
