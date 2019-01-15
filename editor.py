def diacritizeChar(ch, FLAG):
	if (FLAG == ':'): # dieresis
		if (ch == 'A'): return 'Ä'
		if (ch == 'E'): return 'Ë'
		if (ch == 'I'): return 'Ï'
		if (ch == 'O'): return 'Ö'
		if (ch == 'U'): return 'Ü'
		if (ch == 'Y'): return 'Ÿ'
		if (ch == 'a'): return 'ä'
		if (ch == 'e'): return 'ë'
		if (ch == 'i'): return 'ï'
		if (ch == 'o'): return 'ö'
		if (ch == 'u'): return 'ü'
		if (ch == 'H'): return 'Ḧ'
		if (ch == 'W'): return 'Ẅ'
		if (ch == 'X'): return 'Ẍ'
		if (ch == 'h'): return 'ḧ'
		if (ch == 'w'): return 'ẅ'
		if (ch == 't'): return 'ẗ'
		if (ch == 'x'): return 'ẍ'
		return ch
		
	if (FLAG == "'"): # acutus
		if (ch == 'A'): return 'Á'
		if (ch == 'E'): return 'É'
		if (ch == 'I'): return 'Í'
		if (ch == 'O'): return 'Ó'
		if (ch == 'U'): return 'Ú'
		if (ch == 'Y'): return 'Ý'
		if (ch == 'a'): return 'á'
		if (ch == 'e'): return 'é'
		if (ch == 'i'): return 'í'
		if (ch == 'o'): return 'ó'
		if (ch == 'u'): return 'ú'
		if (ch == 'y'): return 'ý'
		if (ch == 'C'): return 'Ć'
		if (ch == 'G'): return 'Ǵ'
		if (ch == 'K'): return 'Ḱ'
		if (ch == 'L'): return 'Ĺ'
		if (ch == 'M'): return 'Ḿ'
		if (ch == 'N'): return 'Ń'
		if (ch == 'P'): return 'Ṕ'
		if (ch == 'R'): return 'Ŕ'
		if (ch == 'S'): return 'Ś'
		if (ch == 'W'): return 'Ẃ'
		if (ch == 'Z'): return 'Ź'
		if (ch == 'c'): return 'ć'
		if (ch == 'g'): return 'ǵ'
		if (ch == 'l'): return 'ĺ'
		if (ch == 'm'): return 'ḿ'
		if (ch == 'n'): return 'ń'
		if (ch == 'p'): return 'ṕ'
		if (ch == 'r'): return 'ŕ'
		if (ch == 'w'): return 'ẃ'
		if (ch == 's'): return 'ś'
		if (ch == 'z'): return 'ź'
		return ch
		
	if (FLAG == '`'): # gravis
		if (ch == 'A'): return 'À'
		if (ch == 'E'): return 'È'
		if (ch == 'I'): return 'Ì'
		if (ch == 'O'): return 'Ò'
		if (ch == 'U'): return 'Ù'
		if (ch == 'Y'): return 'Ỳ'
		if (ch == 'a'): return 'à'
		if (ch == 'e'): return 'è'
		if (ch == 'i'): return 'ì'
		if (ch == 'o'): return 'ò'
		if (ch == 'u'): return 'ù'
		if (ch == 'y'): return 'ỳ'
		if (ch == 'N'): return 'Ǹ'
		if (ch == 'W'): return 'Ẁ'
		if (ch == 'n'): return 'ǹ'
		if (ch == 'w'): return 'ẁ'
		return ch
		
	if (FLAG == '~'): # tilde
		if (ch == 'A'): return 'Ã'
		if (ch == 'E'): return 'Ẽ'
		if (ch == 'I'): return 'Ĩ'
		if (ch == 'O'): return 'Õ'
		if (ch == 'U'): return 'Ũ'
		if (ch == 'Y'): return 'Ỹ'
		if (ch == 'a'): return 'ã'
		if (ch == 'e'): return 'ẽ'
		if (ch == 'i'): return 'ĩ'
		if (ch == 'o'): return 'õ'
		if (ch == 'u'): return 'ũ'
		if (ch == 'y'): return 'ỹ'
		if (ch == 'N'): return 'Ñ'
		if (ch == 'V'): return 'Ṽ'
		if (ch == 'n'): return 'ñ'
		if (ch == 'v'): return 'ṽ'
		return ch
		
	if (FLAG == 'o'): # ring above
		if (ch == 'A'): return 'Å'
		if (ch == 'U'): return 'Ů'
		if (ch == 'a'): return 'å'
		if (ch == 'o'): return 'ů'
		if (ch == 'y'): return 'ẙ'
		if (ch == 'w'): return 'ẘ'
		return ch
		
	if (FLAG == '&'): # digraph analogues or special letters
		if (ch == 'A'): return 'Æ'
		if (ch == 'E'): return 'Ə'
		if (ch == 'O'): return 'Œ'
		if (ch == 'a'): return 'æ'
		if (ch == 'e'): return 'ə'
		if (ch == 'o'): return 'œ'
		if (ch == 'D'): return 'Ð'
		if (ch == 'N'): return 'Ŋ'
		if (ch == 'S'): return 'Ʃ'
		if (ch == 'T'): return 'Þ'
		if (ch == 'd'): return 'ð'
		if (ch == 'n'): return 'ŋ'
		if (ch == 's'): return 'ʃ'
		if (ch == 't'): return 'þ'
		if (ch == 'z'): return 'ß'
		return ch
		
	if (FLAG == '^'): # circumflexus / ĉapelo
		if (ch == 'A'): return 'Â'
		if (ch == 'E'): return 'Ê'
		if (ch == 'I'): return 'Î'
		if (ch == 'O'): return 'Ô'
		if (ch == 'U'): return 'Û'
		if (ch == 'Y'): return 'Ŷ'
		if (ch == 'a'): return 'â'
		if (ch == 'e'): return 'ê'
		if (ch == 'i'): return 'î'
		if (ch == 'o'): return 'ô'
		if (ch == 'u'): return 'û'
		if (ch == 'y'): return 'ŷ'
		if (ch == 'C'): return 'Ĉ'
		if (ch == 'G'): return 'Ĝ'
		if (ch == 'H'): return 'Ĥ'
		if (ch == 'J'): return 'Ĵ'
		if (ch == 'S'): return 'Ŝ'
		if (ch == 'Ẑ'): return 'Ẑ'
		if (ch == 'c'): return 'ĉ'
		if (ch == 'g'): return 'ĝ'
		if (ch == 'h'): return 'ĥ'
		if (ch == 'j'): return 'ĵ'
		if (ch == 's'): return 'ŝ'
		if (ch == 'z'): return 'ẑ'
		return ch
		
	if (FLAG == 'c'): # cedilla
		if (ch == 'E'): return 'Ȩ'
		if (ch == 'e'): return 'ȩ'
		if (ch == 'C'): return 'Ç'
		if (ch == 'D'): return 'Ḑ'
		if (ch == 'G'): return 'Ģ'
		if (ch == 'H'): return 'Ḩ'
		if (ch == 'K'): return 'Ķ'
		if (ch == 'L'): return 'Ļ'
		if (ch == 'N'): return 'Ņ'
		if (ch == 'R'): return 'Ŗ'
		if (ch == 'S'): return 'Ş'
		if (ch == 'T'): return 'Ţ'
		if (ch == 'c'): return 'ç'
		if (ch == 'd'): return 'ḑ'
		if (ch == 'h'): return 'ḩ'
		if (ch == 'g'): return 'ģ'
		if (ch == 'k'): return 'ķ'
		if (ch == 'l'): return 'ļ'
		if (ch == 'n'): return 'ņ'
		if (ch == 'r'): return 'ŗ'
		if (ch == 's'): return 'ş'
		if (ch == 't'): return 'ţ'
		return ch
		
	if (FLAG == ','): # ogonek
		if (ch == 'A'): return 'Ą'
		if (ch == 'E'): return 'Ę'
		if (ch == 'I'): return 'Į'
		if (ch == 'O'): return 'Ǫ'
		if (ch == 'U'): return 'Ų'
		if (ch == 'a'): return 'ą'
		if (ch == 'e'): return 'ę'
		if (ch == 'i'): return 'į'
		if (ch == 'o'): return 'ǫ'
		if (ch == 'u'): return 'ų'
		return ch
		
	if (FLAG == '/'): # stroke or bar
		if (ch == 'A'): return 'Ⱥ'
		if (ch == 'E'): return 'Ɇ'
		if (ch == 'I'): return 'Ɨ'
		if (ch == 'O'): return 'Ø'
		if (ch == 'U'): return 'Ʉ'
		if (ch == 'Y'): return 'Ɏ'
		if (ch == 'e'): return 'ɇ'
		if (ch == 'i'): return 'ɨ'
		if (ch == 'o'): return 'ø'
		if (ch == 'u'): return 'ʉ'
		if (ch == 'y'): return 'ɏ'
		if (ch == 'B'): return 'Ƀ'
		if (ch == 'C'): return 'Ȼ'
		if (ch == 'D'): return 'Đ'
		if (ch == 'J'): return 'Ɉ'
		if (ch == 'G'): return 'Ǥ'
		if (ch == 'H'): return 'Ħ'
		if (ch == 'L'): return 'Ł'
		if (ch == 'R'): return 'Ɍ'
		if (ch == 'T'): return 'Ŧ'
		if (ch == 'Z'): return 'Ƶ'
		if (ch == 'z'): return 'ƶ'
		if (ch == 'b'): return 'ƀ'
		if (ch == 'c'): return 'ȼ'
		if (ch == 'd'): return 'đ'
		if (ch == 'g'): return 'ǥ'
		if (ch == 'h'): return 'ħ'
		if (ch == 'j'): return 'ɉ'
		if (ch == 'l'): return 'ƚ'
		if (ch == 'r'): return 'ɍ'
		if (ch == 't'): return 'ŧ'
		return ch
		
	if (FLAG == '-'): # macron
		if (ch == 'A'): return 'Ā'
		if (ch == 'E'): return 'Ē'
		if (ch == 'I'): return 'Ī'
		if (ch == 'O'): return 'Ō'
		if (ch == 'U'): return 'Ū'
		if (ch == 'Y'): return 'Ȳ'
		if (ch == 'a'): return 'ā'
		if (ch == 'e'): return 'ē'
		if (ch == 'i'): return 'ī'
		if (ch == 'o'): return 'ō'
		if (ch == 'u'): return 'ū'
		if (ch == 'y'): return 'ȳ'
		if (ch == 'G'): return 'Ḡ'
		if (ch == 'g'): return 'ḡ'
		return ch
		
	if (FLAG == 'u'): # breve
		if (ch == 'A'): return 'Ă'
		if (ch == 'E'): return 'Ĕ'
		if (ch == 'I'): return 'Ĭ'
		if (ch == 'O'): return 'Ŏ'
		if (ch == 'U'): return 'Ŭ'
		if (ch == 'a'): return 'ă'
		if (ch == 'e'): return 'ĕ'
		if (ch == 'i'): return 'ĭ'
		if (ch == 'o'): return 'ŏ'
		if (ch == 'u'): return 'ŭ'
		if (ch == 'G'): return 'Ğ'
		if (ch == 'g'): return 'ğ'
		return ch
		
	if (FLAG == '.'): # dot above (or dotless)
		if (ch == 'A'): return 'Ȧ'
		if (ch == 'E'): return 'Ė'
		if (ch == 'I'): return 'İ'
		if (ch == 'O'): return 'Ȯ'
		if (ch == 'Y'): return 'Ẏ'
		if (ch == 'a'): return 'ȧ'
		if (ch == 'e'): return 'ė'
		if (ch == 'i'): return 'ı'
		if (ch == 'o'): return 'ȯ'
		if (ch == 'y'): return 'ẏ'
		if (ch == 'B'): return 'Ḃ'
		if (ch == 'C'): return 'Ċ'
		if (ch == 'D'): return 'Ḋ'
		if (ch == 'F'): return 'Ḟ'
		if (ch == 'G'): return 'Ġ'
		if (ch == 'H'): return 'Ḣ'
		if (ch == 'M'): return 'Ṁ'
		if (ch == 'N'): return 'Ṅ'
		if (ch == 'P'): return 'Ṗ'
		if (ch == 'R'): return 'Ṙ'
		if (ch == 'S'): return 'Ṡ'
		if (ch == 'T'): return 'Ṫ'
		if (ch == 'W'): return 'Ẇ'
		if (ch == 'X'): return 'Ẋ'
		if (ch == 'Z'): return 'Ż'
		if (ch == 'b'): return 'ḃ'
		if (ch == 'c'): return 'ċ'
		if (ch == 'd'): return 'ḋ'
		if (ch == 'f'): return 'ḟ'
		if (ch == 'g'): return 'ġ'
		if (ch == 'h'): return 'ḣ'
		if (ch == 'j'): return 'ȷ'
		if (ch == 'm'): return 'ṁ'
		if (ch == 'n'): return 'ṅ'
		if (ch == 'p'): return 'ṗ'
		if (ch == 'r'): return 'ṙ'
		if (ch == 's'): return 'ṡ'
		if (ch == 't'): return 'ṫ'
		if (ch == 'w'): return 'ẇ'
		if (ch == 'x'): return 'ẋ'
		if (ch == 'z'): return 'ż'
		return ch
		
	if (FLAG == 'h'): # caron
		if (ch == 'A'): return 'Ǎ'
		if (ch == 'E'): return 'Ě'
		if (ch == 'I'): return 'Ǐ'
		if (ch == 'O'): return 'Ǒ'
		if (ch == 'U'): return 'Ǔ'
		if (ch == 'a'): return 'ǎ'
		if (ch == 'e'): return 'ě'
		if (ch == 'i'): return 'ǐ'
		if (ch == 'o'): return 'ǒ'
		if (ch == 'u'): return 'ǔ'
		if (ch == 'C'): return 'Č'
		if (ch == 'D'): return 'Ď'
		if (ch == 'G'): return 'Ǧ'
		if (ch == 'H'): return 'Ȟ'
		if (ch == 'K'): return 'Ǩ'
		if (ch == 'N'): return 'Ň'
		if (ch == 'R'): return 'Ř'
		if (ch == 'S'): return 'Š'
		if (ch == 'T'): return 'Ť'
		if (ch == 'Z'): return 'Ž'
		if (ch == 'c'): return 'č'
		if (ch == 'g'): return 'ǧ'
		if (ch == 'h'): return 'ȟ'
		if (ch == 'j'): return 'ǰ'
		if (ch == 'ǩ'): return 'ǩ'
		if (ch == 'n'): return 'ň'
		if (ch == 'r'): return 'ř'
		if (ch == 's'): return 'š'
		if (ch == 't'): return 'ť'
		if (ch == 'z'): return 'ž'
		
	if (FLAG == 'H'): # double acutus (hungarian dieresis)
		if (ch == 'O'): return 'Ő'
		if (ch == 'U'): return 'Ű'
		if (ch == 'o'): return 'ő'
		if (ch == 'u'): return 'ű'

def diacritize(s):
	FLAG = "STD"
	ss = ""
	for ch in s:
		
		if (FLAG == "WAIT"):
			if (ch in [':', "'", '`', '~', 'o', '&', '^', 'c', ',', '/', '-', 'u', '.', 'h', 'H']):
				FLAG = ch
			else:
				ss += ch
				FLAG = "STD"
			
		elif (ch == '\\'):
			FLAG = "WAIT"
			
		elif (FLAG == "STD"):
			ss += ch
			
		else: # flag is a char!
			ss += diacritizeChar(ch, FLAG)
			FLAG = "STD"
			
	return ss

def main():
	s = input("Input:  ")
	s = diacritize(s)
	print("Output: " + s)

if __name__ == "__main__":	
	main()