import math
import os
import platform
import datetime

import seconds as seconds

if __name__ == '__main__':
    show_today = datetime.datetime.today()
    print(type(show_today))
    show_future = show_today + datetime.timedelta(days=-30)

    show_today = show_today.timestamp()
    show_future = show_future.timestamp()

    print(f"Today: {show_today}, {type(show_today)} | Past: {show_future}")
    print(show_today > show_future)