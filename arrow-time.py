# Refer: https://arrow.readthedocs.io/en/stable/

import arrow

utc = arrow.now('IST')
# <Arrow [2020-11-27T22:33:08.989134+05:30]>

utc = arrow.now('IST').format()
# '2020-11-27 22:31:42+05:30'

utc.humanize()
# 'a minute ago'

import time
# Returns time in ms
ms = time.time_ns() // 1000000
