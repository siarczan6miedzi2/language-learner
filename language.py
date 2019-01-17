from time import time
from time import sleep
from random import *
import os
import sys
import editor as ed

lang = {
	"esperanto" : 0,
	"italiano"  : 1,
	"francais"  : 2,
	"deutsch"   : 3
}

lg = lang[sys.argv[1]]

filename = (
	"vortoj",
	"parole",
	"mots",
	"worter"
)

correct = (
	"Korekte!",
	"Corretto!",
	"Correctement!",
	"Richtig!"
)

onceMore = (
	"Penu refoje:",
	"Prova un'altra volta:",
	"Essaie une fois encore:",
	"Versuche noch einmal:"
)

correctAnswer = (
	"Korekta respondo: ",
	"La risposta corretta: ",
	"La solution correcte: ",
	"Richtige Antwort: "
)

endOfWords = (
	"Fino de vortoj",
	"Fine de parole",
	"Fin de mots",
	ed.diacritize("Ende der W\\:orter")
)

learnt = (
	"Lernita vorto: ",
	"La parola imparata",
	"Le mot appris: ",
	"Gelerntes Wort: "
)

polishWord = (
	"Pola vorto: ",
	"La parola polacca: ",
	"Le mot polonais: ",
	"Polnisches Wort: "
)

foreignWord = (
	"Esperanta vorto: ",
	"La parola italiana: ",
	ed.diacritize("Le mot fran\\ccais"),
	"Deutsches Wort: "
)

confirmation = (
	"konfirmi [C], reenigi [T] aux konfirmi kaj cxesi [Q]: ",
	"confermare [C], immettere di nuovo [T] o confermare e smettere [Q]: ",
	"confirmer [C], entrer une fois encore [T] ou confirmer et quitter [Q]: ",
	ed.diacritize("best\\:atigen [C], eingeben noch einmal [T] oder best\\:atigen und verlassen [Q]: ")
)

header = (
	"\nESPERANTOJ VORTOJ",
	"\nPAROLE ITALIANE",
	ed.diacritize("\nLES MOTS FRAN\\cCAIS"),
	ed.diacritize("\nDEUTSCHE W\\:ORTER")
)

chooseMode = (
	"lerni [L], krei [C] aux cxesi [Q]?: ",
	"imparare [L], creare [C] o smettere [Q]?: ",
	ed.diacritize("apprendre [L], cr\\'eer [C] ou quitter [Q]?: "),
	"lernen [L], erschaffen [C] oder verlassen [Q]?: "
)

class vorto:
	def __init__(self, polski, foreign):
		self.polski = polski
		self.foreign = foreign
		self.time = time()
		self.stage = 0
		
	def str(self): # '*' is used as a delimiter, because why not?
		return (self.polski + "*" + self.foreign + "*" + str(self.time) + "*" + str(self.stage))
		
def readVorto(file):
	v = file.readline()
	if (v == ""): return None
	pl, fg, tm, st = v.split('*')
	v = vorto(pl, fg)
	v.time = eval(tm)
	v.stage = eval(st)
	return v
		
def ok(v):
	if (v.stage == 0):
		v.time = time() + randint(250000, 550000)
	elif (v.stage == 1):
		v.time = time() + randint(700000, 1100000)
	elif (v.stage == 2):
		v.time = time() + randint(1250000, 1750000)
	elif (v.stage == 3):
		v.time = time() + randint(1800000, 2400000)
	v.stage += 1
	
def qok(v):
	if (v.stage == 0 or v.stage == 1):
		v.time = time() + randint(100000, 200000)
	elif (v.stage == 2):
		v.time = time() + randint(250000, 550000)
	elif (v.stage == 3):
		v.time = time() + randint(700000, 1100000)
	elif (v.stage == 4):
		v.time = time() + randint(1250000, 1750000)
	
def neok(v):
	v.time = time() + randint(100000, 200000)
	v.stage = 0
		
def lerni():
	vortoj = []
	file = open(filename[lg], 'r', encoding='utf-8')
	while True: # read all words
		v = readVorto(file)
		if not v: break
		else: vortoj.append(v)
	file.close()
	for v in vortoj: # learning
		if (v.time > time()): continue
		s = input(v.polski + " - ")
		s = ed.diacritize(s)
		if (s == v.foreign):
			print(correct[lg])
			ok(v)
		else:
			print(onceMore[lg], end = " ")
			s = input(v.polski + " - ")
			s = ed.diacritize(s)
			if (s == v.foreign):
				print(correct[lg])
				qok(v)
			else:
				print(correctAnswer[lg], v.polski, "-", v.foreign)
				neok(v)
				
	print(endOfWords[lg])
	
	# create backup file and the up-to-date new one
	os.system("cp " + filename[lg] + " " + filename[lg] + "-backup")
	file = open(filename[lg], 'w', encoding='utf-8')
	for v in vortoj:
		if not (v.stage > 4): # word is learnt
			file.write(v.str())
			file.write('\n')
		else: print(learnt[lg], v.polski, "-", v.foreign)

def krei():
	file = open(filename, 'a+', encoding='utf-8')
	
	while True:
		pl = input(polishWord[lg])
		fg = input(foreighWord[lg])
		fg = ed.diacritize(fg)
		
		ch = input(confirmation[lg])
		
		if not (ch == 't' or ch == 'T'): # try again
			v = vorto(pl, fg)
			v.time += randint(100000, 200000)
			file.write(v.str())
			file.write('\n')
		
		if (ch == 'q' or ch == 'Q'): break # quit
		
	file.close()
		
def main():

	arg = None
	MODE = "normal"
	if len(sys.argv) > 2: arg = sys.argv[2]
	if (arg == 'a'): MODE = "auto" # when bulk learning different languages
	
	if (MODE == "auto"):
		print(header[lg])
		lerni()
		sleep(2)
	else:
		ch = ' '
		while True:
			ch = input(chooseMode[lg])
			if (ch == 'l' or ch == 'L'): lerni()
			elif (ch == 'c' or ch == 'C'): krei()
			elif (ch == 'q' or ch == 'Q'): break
		
main()