

class RecurrentAlarm(object):

    def __init__(self):
        self._when = None
        self._trigger_time = None
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
        if self._trigger_time is None:
            self._trigger_time = current_time + self._when
        else:
            self._trigger_time = self._trigger_time - current_time

        if self._snoozed:
            self._trigger_time += self._postpone_by

        if self._trigger_time <= 0:
            self._triggered = True
            self._trigger_time = current_time + self._when


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
