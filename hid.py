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

send_char(kh.KEY_K)
send_char(kh.KEY_A)
send_char(kh.KEY_R)
send_char(kh.KEY_A)
send_char(kh.KEY_N)
send_char(kh.KEY_ENTER)

send_char_cap(kh.KEY_K)
send_char(kh.KEY_A)
send_char_cap(kh.KEY_R)
send_char(kh.KEY_A)
send_char_cap(kh.KEY_N)
send_char(kh.KEY_ENTER)

# Press a
write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
# Release keys
release()

# Press SHIFT + a = A
write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)

# Press b
write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
# Release keys
release()

# Press SHIFT + b = B
write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)

# Press SPACE key
write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)

# Press c key
write_report(NULL_CHAR*2+chr(6)+NULL_CHAR*5)
# Press d key
write_report(NULL_CHAR*2+chr(7)+NULL_CHAR*5)

# Press RETURN/ENTER key
write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)

# Press e key
write_report(NULL_CHAR*2+chr(8)+NULL_CHAR*5)
# Press f key
write_report(NULL_CHAR*2+chr(9)+NULL_CHAR*5)

# Release all keys
write_report(NULL_CHAR*8)
