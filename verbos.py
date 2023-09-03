##################################IMPORTS##########################################################
import random

####################################################################################################
##################################HILFS FUNTKIONEN##################################################
####################################################################################################

#Checks whether word contains given symbol
def contains(word, symbol):
	for element in word:
		if element == symbol:
			return True
	return False 

#Extracts the word corresponding to given language
def exctract_language(word,is_spanish):
	output = ""
	if is_spanish:
			for letter in word:
				if not letter == "-":
					output += letter
				else:
					return output
	else:
		i = 0
		while i < len(word):
			if word[i] == "-":
				i += 1
				while i < len(word):
					if not word[i] == "[":
						output += word[i]
					else:
						break
					i += 1
				return output
			i += 1

####################################################################################################
##################################GROßE FUNTKIONEN##################################################
####################################################################################################

def start():
	for _ in range(10):
		print("\n")
	print("Herzlich Willkommen!")
	print("\n")
	print("Mit diesem Programm lernst du Verben richtig zu konjugieren!")
	print("\n")
	print("--------------------------------------------------------------------------------------------------")
	print("\n")
	print("Bedienung:")
	print("  -- Nachdem dir die Aufgabe gestellt wird, kannst du deine Lösung in der Kommandozeile eingeben")
	print("  -- Wenn du *Enter* drückst, schickst du deine Antwort ab")
	print("  -- Du kannst jederzeit das Programm durch die Eingabe von 'stop' beenden")
	for _ in range(3):
		print("\n")

#OUTPUT: all words: List 
def get_data():
	def replace_word(word):
		for i, letter in enumerate(word):	
			if letter == "Ã":
				new = str()
				for new_letter in word:
					if new_letter == "¼":
						new += "ü"
					elif new_letter == "¤":
						new += "ä"
					elif new_letter == "±":
						new += "ñ"
					elif new_letter == "¶":
						new += "ö"
					elif new_letter == "Ÿ":
						new += "ß"
					elif new_letter == "–":
						new += "Ö"
					elif new_letter == "œ":
						new += "Ü"
					elif new_letter == "„":
						new += "A"
					elif new_letter == "‘":
						new += "Ñ"
					elif not new_letter == "Ã":
						new += new_letter
		try:
			return new
		except:
			return word

	with open("verbos.txt","r") as file:
		data_in = file.readlines()
	start_data = []
	for line in data_in:
		start_data.append(line[:len(line)-1:])

	#ü,ä,n mit tilde klein, ö, ß, 
	forbidden = {"Ã","¼","¤","±","¶","Ÿ","–","œ","„","‘"}
	data = []
	ja = False
	for word in start_data:
		for letter in word:
			if letter in forbidden:
				new_word = replace_word(word)
		if not new_word == "":
			data.append(new_word)
		else:
			data.append(word)
		new_word = ""

	return data

#Picks a random word from the given list words
def create_bsp(words):
	zufall = random.randrange(0,len(words)-1)
	return words[zufall]

#Creates aufgabe 
#OUTPUT: deutsches Wort, 1-3. Person Sg./Pl.: str
def create_aufgabe(beispiel):
	word_ger = exctract_language(beispiel,False)
	person = random.randrange(1,4)
	sg_oder_pl = random.randrange(1,3)

	return person, sg_oder_pl, word_ger

def create_solution(beispiel, information):
	if information[1] == 1:
		numerus = information[0]
	else:
		numerus = information[0]+3

	def exctract_language(word,is_spanish):
		output = ""
		if is_spanish:
				for letter in word:
					if not letter == "-":
						output += letter
					else:
						output = output.split(" ")
						return output[0]
		else:
			i = 0
			while i < len(word):
				if word[i] == "-":
					i += 1
					while i < len(word):
						if not word[i] == "[":
							output += word[i]
						else:
							break
						i += 1
					return output
				i += 1

	#Extracts the "[]" part at the end of a irregular verb
	def extract_type(word):
		output = ""
		i = 0
		while i < len(word):
			if word[i] == "[":
				while i < len(word):
					output += word[i]
					i += 1
			i += 1
		output = output[1:len(output)-1]
		output = output.split(",")
		return output

	#Checks wether a word is regular; returns True/False 
	def is_regular(beispiel):
		for element in beispiel:
			if element == "[":
				return False
		return True

	#Checks wether a word is regular; returns True/False
	def is_reflexsiv(beispiel):
		beispiel = exctract_language(beispiel,True)
		if beispiel[len(beispiel)-1] == "e" and beispiel[len(beispiel)-2] == "s":
			return True
		return False

	#REGULAR
	def regular(verb,person):
		verb_ending = verb[-2:]
		if verb_ending == "ar":
			result = a_konjugation(verb[:len(verb)-2],person)
		elif verb_ending == "er":
			result = e_konjugation(verb[:len(verb)-2],person)
		elif verb_ending == "ir":
			result = i_konjugation(verb[:len(verb)-2],person)
		else:
			return "ERROR START"
		
		return result

	def a_konjugation(verb,person):
		if person == 0:
			konjugation_liste = []
			for i in range(1,7):
				if i == 1:
					konjugation_liste.append(verb + "o")
				elif i == 2:
					konjugation_liste.append(verb + "as")
				elif i == 3:
					konjugation_liste.append(verb + "a")
				elif i == 4:
					konjugation_liste.append(verb + "amos")
				elif i == 5:
					konjugation_liste.append(verb + "ais")
				elif i == 6:
					konjugation_liste.append(verb + "an")
			return konjugation_liste
		elif person == 1:
			return (verb+"o")
		elif person == 2:
			return (verb+"as")
		elif person == 3:
			return (verb+"a")
		elif person == 4:
			return (verb+"amos")
		elif person == 5:
			return (verb+"áis")
		elif person == 6:
			return (verb+"an")
		else:
			return "ERROR A"
	def e_konjugation(verb,person):
		if person == 0:
			konjugation_liste = []
			for i in range(1,7):
				if i == 1:
					konjugation_liste.append(verb + "o")
				elif i == 2:
					konjugation_liste.append(verb + "es")
				elif i == 3:
					konjugation_liste.append(verb + "e")
				elif i == 4:
					konjugation_liste.append(verb + "emos")
				elif i == 5:
					konjugation_liste.append(verb + "éis")
				elif i == 6:
					konjugation_liste.append(verb + "en")
			return konjugation_liste
		elif person == 1:
			return (verb+"o")
		elif person == 2:
			return (verb+"es")
		elif person == 3:
			return (verb+"e")
		elif person == 4:
			return (verb+"emos")
		elif person == 5:
			return (verb+"éis")
		elif person == 6:
			return (verb+"en")
		else:
			return "ERROR E"
	def i_konjugation(verb,person):
		if person == 0:
			konjugation_liste = []
			for i in range(1,7):
				if i == 1:
					konjugation_liste.append(verb + "o")
				elif i == 2:
					konjugation_liste.append(verb + "es")
				elif i == 3:
					konjugation_liste.append(verb + "e")
				elif i == 4:
					konjugation_liste.append(verb + "imos")
				elif i == 5:
					konjugation_liste.append(verb + "ís")
				elif i == 6:
					konjugation_liste.append(verb + "en")
			return konjugation_liste
		elif person == 1:
			return (verb+"o")
		elif person == 2:
			return (verb+"es")
		elif person == 3:
			return (verb+"e")
		elif person == 4:
			return (verb+"imos")
		elif person == 5:
			return (verb+"ís")
		elif person == 6:
			return (verb+"en")
		else:
			return "ERROR I"

	#REFLEXSIV
	def reflexsiv(verb,person):
		verb = verb[:len(verb)-2]
		if person == 1:
			verb += "me"
		elif person == 2:
			verb += "te"
		elif person == 3:
			verb += "se"
		elif person == 4:
			verb += "nos"
		elif person == 5:
			verb += "os"
		elif person == 6:
			verb += "se"
		return verb

	#IRREGULAR: mit [*]
	def irr_ser(person):
		if person == 1:
			return "soy"
		elif person == 2:
			return "eres"
		elif person == 3:
			return "es"
		elif person == 4:
			return "somos"
		elif person == 5:
			return "sois"
		elif person == 6:
			return "son"
		else:
			return "ERROR SER"
	def irr_ir(person):
		if person == 1:
			return "voy"
		elif person == 2:
			return "vas"
		elif person == 3:
			return "va"
		elif person == 4:
			return "vamos"
		elif person == 5:
			return "vais"
		elif person == 6:
			return "van"
		else:
			return "ERROR IR"
	def irr_haber(person):
		if person == 1:
			return "he"
		elif person == 2:
			return "has"
		elif person == 3:
			return "ha"
		elif person == 4:
			return "hamos"
		elif person == 5:
			return "habéis"
		elif person == 6:
			return "han"
		else:
			return "ERROR HABER"
	def irr_estar(person):
		if person == 1:
			return "estoy"
		elif person == 2:
			return "estás"
		elif person == 3:
			return "están"
		elif person == 4:
			return "estamos"
		elif person == 5:
			return "estáis"
		elif person == 6:
			return "estan"
		else:
			return "ERROR ESTAR"

	#IRREGULAR: mit [ie]
	def irr_ie(word):
		return word.replace("e","ie",1)

	def irr_i(word):
		return word.replace("e","i",1)

	def irr_ue(word):
		for letter in word:
			if letter == "o":
				return word.replace("o","ue",1)
			if letter == "u":
				return word.replace("u","ue",1)

	def irr_g(word):
		word = word[:len(word)-2]
		word += "go"
		return word

	def irr_zc(word):
		word = word[:len(word)-3]
		word += "zco"
		return word

	word_esp = exctract_language(beispiel,True)
	#Verb is regular && not reflexsiv
	if is_regular(beispiel) and not is_reflexsiv(beispiel):
		return regular(word_esp,numerus)
	#Verb is regular && reflexsiv
	elif is_regular(beispiel) and is_reflexsiv(beispiel):
		return reflexsiv(word_esp,numerus)
	#Verb is not regular && not reflexsiv
	elif not is_regular(beispiel) and not is_reflexsiv(beispiel):
		typen = extract_type(beispiel)
		for element in typen:
			if element == "*":
				if word_esp == "ser":
					return irr_ser(numerus)
				elif word_esp == "ir":
					return irr_ir(numerus)
				elif word_esp == "haber":
					return irr_haber(numerus)
				elif word_esp == "estar":
					return irr_estar(numerus)
			elif element == "**":
				if numerus == 1:
					if word_esp == "ver":
						return "veo"
					elif word_esp == "dar":
						return "doy"
					elif word_esp == "saber":
						return "sé"
					else:
						return regular(word_esp,numerus)
			elif element == "ie":
				if numerus == 1 or numerus == 2 or numerus == 3 or numerus == 6:
					return regular(irr_ie(word_esp),numerus)
				else:
					return regular(word_esp,numerus)
			elif element == "i":
				if numerus == 1 or numerus == 2 or numerus == 3 or numerus == 6:
					return regular(irr_i(word_esp),numerus)
				else:
					return regular(word_esp,numerus)
			elif element == "ue":
				if numerus == 1 or numerus == 2 or numerus == 3 or numerus == 6:
					return regular(irr_ue(word_esp),numerus)
				else:
					return regular(word_esp,numerus)
			elif element == "g":
				if numerus == 1:
					return irr_g(word_esp)
				else:
					return regular(word_esp,numerus)
			elif element == "zc":
				if numerus == 1:
					return irr_zc(word_esp)
				else:
					return regular(word_esp,numerus)
			else:
				return "ERROR IRREGULAR 1"
	#Verb is not regular && reflexsiv
	elif not is_regular(beispiel) and is_reflexsiv(beispiel):
		typen = extract_type(beispiel)
		for element in typen:
			if element == "ie":
				if numerus == 1 or numerus == 2 or numerus == 3 or numerus == 6:
					return reflexsiv(irr_ie(word_esp),numerus)
				else:
					return reflexsiv(word_esp,numerus)
			elif element == "i":
				if numerus == 1 or numerus == 2 or numerus == 3 or numerus == 6:
					return reflexsiv(irr_i(word_esp),numerus)
				else:
					return reflexsiv(word_esp,numerus)
			elif element == "ue":
				if numerus == 1 or numerus == 2 or numerus == 3 or numerus == 6:
					return reflexsiv(irr_ue(word_esp),numerus)
				else:
					return reflexsiv(word_esp,numerus)
			elif element == "g":
				if numerus == 1:
					return irr_g(word_esp)
				else:
					return reflexsiv(word_esp,numerus)
			elif element == "zc":
				if numerus == 1:
					return irr_zc(word_esp)
				else:
					return reflexsiv(word_esp,numerus)
			else:
				return "ERROR IRREGULAR 2"
	else:
		return "ERROR TYPE"

def ausgabe(person, sg_oder_pl, word_ger):

	if sg_oder_pl == 1:
		numerus = "Singular"
	else:
		numerus = "Plural" 

	return ("Wie lautet die Spanische Übersetztung von: " + str(word_ger) + ", " + str(person) + ". Person " + str(numerus))

def eingabe():
	print("\n")
	return input("Eingabe: ")

####################################################################################################
######################################MAIN PART#####################################################
####################################################################################################

start()

words = get_data()
incorrect = []
wrongs = 0
total_correct = 0
total_incorrect = 0
old_beispiel = ""

while True:
	if wrongs < 3:
		beispiel = create_bsp(words)
		while beispiel == old_beispiel:
			beispiel = create_bsp(words)
		aufgabe = create_aufgabe(beispiel)
	else:
		zufall = random.randrange(0,len(incorrect)-1)
		beispiel = incorrect[zufall][0]
		while beispiel == old_beispiel:
			zufall = random.randrange(0,len(incorrect)-1)
			beispiel = incorrect[zufall][0]
		aufgabe = incorrect[zufall][1]

	solution = create_solution(beispiel, aufgabe)
	print(ausgabe(aufgabe[0],aufgabe[1],aufgabe[2]))
	user_input = eingabe()

	if user_input == solution:
		print("correcto!!")
		total_correct += 1
		try:
			incorrect.remove((beispiel,aufgabe))
			wrongs -= 1
		except:
			pass
	elif user_input == "stop":
		break
	elif user_input == "skip":
		pass
	else:
		total_incorrect += 1
		print("incorrecto :/")
		print("Korrekte Lösung:",solution)
		incorrect.append((beispiel, aufgabe))
		wrongs += 1

	old_beispiel = beispiel

	print("\n")
	print("\n")
	print("\n")

try:
	quote = (total_correct/(total_correct+total_incorrect))*100
except ZeroDivisionError:
	quote = 0.0

print("\n")
print("Du hast insgesamt: " + str(total_correct) + " Aufgaben richtig gelöst und insgesamt " + str(total_incorrect) + " Aufgaben falsch.")
print("Das entspricht einer Quote von ca.: " + str(int(quote)) + "% !")
print("\n")
print("Das Programm wurde erfolgreich beendet.")
print("Du kannst das Fenster jetzt schließen.")

