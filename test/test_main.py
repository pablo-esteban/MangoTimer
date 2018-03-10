
from mangotimer.main import RecurrentAlarm, FakeTimeline


def test_should_trigger_alarm_after_set_time():
    alarm = RecurrentAlarm()
    context = FakeTimeline()

    alarm.set_every(minutes=25)

    context.add(alarm)

    context.after(minutes=25)

    assert alarm.is_triggered()
