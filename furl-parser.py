# Reference: https://github.com/gruns/furl/blob/master/API.md

from furl import furl

f = furl('http://www.google.com')

f /= 'path'
# 'http://www.google.com/path'

f.args['one'] = '1'
# 'http://www.google.com/path?one=1'

del f.args['one']
# 'http://www.google.com/path'

furl('http://www.google.com/?one=1').add({'two': '2'}).url
# 'http://www.google.com/?one=1&two=2'

furl('http://www.google.com/?one=1&two=2').set({'three': '3'}).url
# 'http://www.google.com/?three=3'

furl('http://www.google.com/?one=1&two=2').remove(['one']).url
# 'http://www.google.com/?two=2'