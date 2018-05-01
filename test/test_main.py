
from mangotimer.mango import RecurrentAlarm, FakeTimeline


def test_should_trigger_alarm_after_set_time():
    alarm = RecurrentAlarm()
    context = FakeTimeline()

    alarm.set_every(minutes=25)

    context.add(alarm)

    context.run_for(minutes=25)

    assert alarm.is_triggered()

    alarm.switch_off()

    assert not alarm.is_triggered()


def test_should_not_trigger_alarm_if_time_is_before_set_time():
    alarm = RecurrentAlarm()
    context = FakeTimeline()

    alarm.set_every(minutes=25)

    context.add(alarm)

    context.run_for(minutes=20)

    assert not alarm.is_triggered()


def test_should_snooze_alarm_for_some_time():
    alarm = RecurrentAlarm()
    context = FakeTimeline()

    alarm.set_every(minutes=25)
    context.add(alarm)

    context.run_for(minutes=25)

    alarm.snooze(minutes=5)

    context.run_for(minutes=5)

    assert alarm.is_triggered()


def test_should_still_be_triggered_if_not_switched_off():
    alarm = RecurrentAlarm()
    context = FakeTimeline()

    alarm.set_every(minutes=5)
    context.add(alarm)
    context.run_for(minutes=5)
    assert alarm.is_triggered()

    context.run_for(minutes=1)

    assert alarm.is_triggered()


def test_should_not_trigger_until_next_period():
    alarm = RecurrentAlarm()
    context = FakeTimeline()

    alarm.set_every(minutes=5)
    context.add(alarm)

    context.run_for(minutes=5)
    assert alarm.is_triggered()
    alarm.switch_off()

    context.run_for(minutes=1)
    assert not alarm.is_triggered()

    context.run_for(minutes=4)
    assert alarm.is_triggered()
