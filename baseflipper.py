import re
import base64

def to_bin_conversion(inp, form):
	formatted = inp.replace(" -2b",'')
	out = []
	if form == "asc":
		for i in formatted:
			Dec = ord(i)
			BinaryValues = bin(Dec)
			out.append(BinaryValues[2:].zfill(8))
		return(''.join(out))

	elif form == "hex":
		formatted = formatted.replace(' ', '')
		byteArray = re.findall(r'.{1,2}',formatted,re.DOTALL)
		for i in range(len(byteArray)):
			BinaryValues = bin(int(byteArray[i], 16))
			out.append(BinaryValues[2:].zfill(8))
		return('00100000'.join(out))

	elif form == "dec":
		byteArray = formatted.split()
		for i in range(len(byteArray)):
			BinaryValues = bin(int(byteArray[i]))
			out.append(BinaryValues[2:].zfill(8))
		return('00100000'.join(out))

	elif form == "b64":
		formatted = base64.b64decode(formatted).decode('utf-8')
		for i in formatted:
			Dec = ord(i)
			BinaryValues = bin(Dec)
			out.append(BinaryValues[2:].zfill(8))
		return(''.join(out))

#	elif form == "oct":

def to_dec_conversion(inp, form):
	formatted = inp.replace(" -2d",'')
	out = []
	if form == "asc":
		for i in formatted:
			Dec = ord(i)
			Dec = str(Dec)
			out.append(Dec)
		return(' '.join(out))

	elif form == "hex":
		formatted = formatted.replace(' ', '')
		byteArray = re.findall(r'.{1,2}',formatted,re.DOTALL)
		for i in range(len(byteArray)):
			DecValues = str(int(byteArray[i], 16))
			out.append(DecValues)
		return(' '.join(out))

	elif form == "bin":
		formatted = formatted.replace(' ', '')
		byteArray = re.findall(r'.{1,8}',formatted,re.DOTALL)
		for i in range(len(byteArray)):
			DecValues = str(int(byteArray[i], 2))
			out.append(DecValues)
		return(' '.join(out))

	elif form == "b64":
		formatted = base64.b64decode(formatted).decode('utf-8')
		for i in formatted:
			Dec = ord(i)
			Dec = str(Dec)
			out.append(Dec)
		return(' '.join(out))

#	elif form == "oct":

def to_hex_conversion(inp, form):
	formatted = inp.replace(" -2h", "")
	formatted = formatted.replace(" -20x", "")
	out = []

	if form == "asc":
		for i in formatted:
			Dec = ord(i)
			HexVal = hex(Dec)
			out.append(HexVal[2:])
		return(''.join(out))

	elif form == "dec":
		byteArray = formatted.split()
		for i in range(len(byteArray)):
			HexVal = hex(int(byteArray[i]))
			out.append(HexVal[2:])
		return('20'.join(out))

	elif form == "bin":
		formatted = formatted.replace(' ', '')
		byteArray = re.findall(r'.{1,8}',formatted,re.DOTALL)
		for i in range(len(byteArray)):
			HexVal = hex(int(byteArray[i], 2))
			out.append(HexVal[2:])
		return('20'.join(out))

	elif form == "b64":
		formatted = base64.b64decode(formatted).decode('utf-8')
		for i in formatted:
			Dec = ord(i)
			HexVal = hex(Dec)
			out.append(HexVal[2:])
		return(''.join(out))

#	elif form == "oct":

def to_ascii_conversion(inp, form):
	formatted = inp.replace(" -2a",'')
	formatted = formatted.replace(" -2t",'')
	out = []

	if form == "hex":
		formatted = formatted.replace(" ","")
		byteArray = re.findall(r'.{1,2}',formatted,re.DOTALL)
		for i in range(len(byteArray)):
			Ascii = chr(int(byteArray[i], 16))
			out.append(Ascii)
		return(''.join(out))

	elif form == "dec":
		byteArray = formatted.split()
		for i in range(len(byteArray)):
			Ascii = chr(int(byteArray[i]))
			out.append(Ascii)
		return(''.join(out))

	elif form == "bin":
		formatted = formatted.replace(" ","")
		byteArray = re.findall(r'.{1,8}',formatted,re.DOTALL)
		for i in range(len(byteArray)):
			Ascii = chr(int(byteArray[i], 2))
			out.append(Ascii)
		return(''.join(out))

	elif form == "b64":
		return(base64.b64decode(formatted).decode('ascii'))

#	elif form == "oct":

def to_b64_conversion(inp, form):
	formatted = inp.replace(" -2b64", '')
	return(base64.b64encode(bytes(formatted, 'utf-8')).decode('utf-8'))

""" //should i have this, idrk, might be useful in the future, leave it for now and add it later?
def to_oct_conversion(inp, form):
	formatted = inp.replace(" -2o",'')
	formatted = inp.replace(" -20", '')
	out = []

	if form == "asc":
		for i in formatted:
			Dec = ord(i)
			OctVal = oct(Dec)
			out.append(OctVal)
		return(''.join(out))

	elif form == "hex":

	elif form == "dec":

	elif form == "bin":
"""

#====================================================================================================================================

try:
	info = input()

	if "-help" in info:
		print("baseflipper.py: 'string' [--format] [--outputformat] \n\n"\
		" --formats:\n -h		hexadecimal \n -b	 	binary \n "\
		"-a		ascii text \n -d		decimal \n -b64 "\
		" 		base64 \n\n --outputformats: \n -2h		"\
		"hexadecimal \n -2b		binary \n -2a	 	ascii text"\
		"  \n -2d		decimal\n -2b64 		base64")

	if "-a" in info:
		info = info.replace(" -a",'')

		if "-2b64" in info:
			info = to_b64_conversion(info, "asc")
		elif "-2d" in info:
			info = to_dec_conversion(info, "asc")
		elif "-2b" in info:
			info = to_bin_conversion(info, "asc")
		elif "-2h" in info:
			info = to_hex_conversion(info, "asc")
		elif "-2o" in info:
			info = to_oct_conversion(info, "asc")


	elif "-h" in info:
		info = info.replace(" -h", '')

		if "-2b64" in info:
			info = to_b64_conversion(info, "hex")
		elif "-2d" in info:
			info = to_dec_conversion(info, "hex")
		elif "-2a" in info:
			info = to_ascii_conversion(info, "hex")
		elif "-2o" in info:
			info = to_oct_conversion(info, "hex")
		elif "-2b" in info:
			info = to_bin_conversion(info, "hex")


	elif "-b64" in info:
		info = info.replace(" -64",'')

		if "-2h" in info:
			info = to_hex_conversion(info, "b64")
		elif "-2a" in info:
			info = to_ascii_conversion(info, "b64")
		elif "-2b" in info:
			info = to_bin_conversion(info, "b64")
		elif "-2d" in info:
			info = to_dec_conversion(info, "b64")
		elif "-2o" in info:
			info = to_oct_conversion(info, "b64")

	elif "-b" in info:
		info = info.replace(" -b",'')

		if "-2h" in info:
			info = to_hex_conversion(info, "bin")
		elif "-2a" in info:
			info = to_ascii_conversion(info, "bin")
		elif "-2d" in info:
			info = to_dec_conversion(info, "bin")
		elif "-2o" in info or "-20" in info:
			info = to_oct_conversion(info, "bin")
		elif "-2b64" in info:
			info = to_b64_conversion(info, "bin")

	elif "-d" in info:
		info = info.replace(" -d",'')

		if "-2h" in info:
			info = to_hex_conversion(info, "dec")
		elif "-2a" in info:
			info = to_ascii_conversion(info, "dec")
		elif "-2b64" in info:
			info = to_b64_conversion(info, "dec")
		elif "-2b" in info:
			info = to_bin_conversion(info, "dec")
		elif "-2o" in info:
			info = to_oct_conversion(info, "dec")

	else:
		raise ValueError()
	print(info)


	'''
	future addition maybe
		elif "-o" in info:
			info = info.replace(" -o",'')

			if "-2h" in info:
				info = to_hex_conversion(info, "oct")
			elif "-2a" in info:
				info = to_ascii_conversion(info, "oct")
			elif "-2b64" in info:
				info = to_b64_conversion(info, "oct")
			elif "-2b" in info:
				info = to_bin_conversion(info, "oct")
			elif "-2d" in info:
				info = to_dec_conversion(info, "oct")
	'''

except:
	print("baseflipper.py: invalid configuration type [-help] for more info")

