import KeyboardHex as kh

a = chr(kh.KEY_B)

print(a)

a = chr(71) + 'a'

#!/usr/bin/env python3
NULL_CHAR = chr(0)

def write_report(report):
	#print('-')
	#print(report)
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())

def release():
	write_report(NULL_CHAR*8)

def send_char(key):
	write_report(NULL_CHAR*2+chr(key)+NULL_CHAR*5)
	release()

def send_char_cap(key):
	write_report(chr(32)+NULL_CHAR+chr(key)+NULL_CHAR*5)
	release()

while True:
    key = input('-->')
    send_char(kh.KEYS[key])
    pass