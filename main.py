import datetime

from mangotimer.mango import RecurrentAlarm, RealTimeline


if __name__ == '__main__':
    alarm = RecurrentAlarm()
    alarm.set_every(datetime.timedelta(minutes=1))

    context = RealTimeline()

    context.add(alarm)

    context.run()
