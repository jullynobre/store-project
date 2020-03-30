from crontab import CronTab

cron = CronTab(user='diulinobre')
job = cron.new(command='python example1.py')
job.minute.every(1)

cron.write()