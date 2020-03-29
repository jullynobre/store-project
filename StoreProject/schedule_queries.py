from crontab import CronTab
from decouple import config

cron = CronTab(user='diulinobre')
job = cron.new(command='cd /Documents/store-project/StoreProject && '
                       'conda activate store-project && '
                       'export PYTHONPATH=$PYTHONPATH:$PWD && '
                       'sudo python queries/manager.py publish-queries')
job.minute.every(1)
cron.write()
