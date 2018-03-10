

class RecurrentAlarm(object):

    def __init__(self):
        self._when = None
        self._triggered = False
        self._snoozed = False
        self._postpone_by = 0

    def set_every(self, minutes):
        self._when = minutes

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
        trigger_time = self._when
        if self._snoozed:
            trigger_time = self._when + self._postpone_by
        if trigger_time <= current_time:
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
