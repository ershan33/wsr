import datetime


dir(datetime.date)  # 日期：年月日
dir(datetime.datetime)  # 日期：年月日时分秒...

today = datetime.date(2022, 5, 4)
today.strftime("%Y-%m-%d")

today = datetime.date.today()
date = today.strftime("%Y-%m-%d")