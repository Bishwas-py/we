# 1978
from nepali_datetime import date as nepDate
from datetime import timedelta
def get_max_np_day(year,month):
    year,month = int(year),int(month)
    month = month+1
    if month == 13:
        max_day = nepDate((year+1),(month-1), 1)-timedelta(days=1)
    elif month <= 12:
        max_day = nepDate((year),(month), 1)-timedelta(days=1)

    return str(max_day).split('-')[-1]

# print(get_max_np_day(2075, 6))