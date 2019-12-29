import KeyboardHex as kh

arr = 'karan k'

for x in arr:
    print(kh.KEYS[x])
    pass


while True:
	key = input('-->')
	try:
		print(kh.KEYS[key.lower()])
		pass
	except:
		for x in key:
			print(kh.KEYS[x.lower()])
			pass
	finally:
		pass
	
	pass