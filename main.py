import datetime

from mangotimer.mango import RecurrentAlarm, RealTimeline


if __name__ == '__main__':
    alarm = RecurrentAlarm(datetime.timedelta(minutes=1))

    context = RealTimeline()

    context.add(alarm)

    context.run()
