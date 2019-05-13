import sys
import re

pattern = re.compile(r'[A-Z,0-9]{2}_[A-Z]{3}_[A-Z]{2}')
result = pattern.match('S6_CRC_OK')

print result