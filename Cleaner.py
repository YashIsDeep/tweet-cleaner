import re
import autocorrect # for spell correction
import wordninja

# Currently supports only English
# Need to add a way to replace backslash characters

def replaceMentionsWithNames(text): # Replaces the @names with *Name* and returns the names used
	namePattern = re.compile(r"@[a-zA-Z0-9_]{1,15}")
	names=set()
	modString="" 
	matches = re.finditer(namePattern,text)
	end=0
	for match in matches:
		names.add(match.group()[1:])
		modString=modString+text[end:match.start()]+"*NAME*"
		end=match.end()
	modString=modString+text[end:]
	return modString,names

def deleteEmotes(str):  # Needs improvement
	emoji_pattern = re.compile(r":(\(\)\\/OPI|\[\])")
	# emoji_pattern = re.compile(r"[^a-zA-Z0-9_ !?.,]") Possible alternative
	str=emoji_pattern.sub(r"",str)
	return str

def breakDownHashtags(text):
	def splitWordAndAddSpaces(word): # add space in front as well as end    ##DEPENDENCY to remove##
			wordlist = wordninja.split(word)
			string = ' '.join(eachword for eachword in wordlist )
		return " "+string+" "
	tagPattern= re.compile(r"#[a-zA-Z0-9_]")
	tags=re.finditer(tagPattern,text)
	end=0
	brokenString=""
	for tag in tags:
		formattedword=splitWordAndAddSpaces(word)
		modString=modString+text[end:tag.start()]+changedword
		end=tag.end()
	modString=modString+text[end:]
	return modString

def doSpellCorrection(text):
	wordPattern = re.compile(r"[^a-zA-Z0-9_][a-zA-Z0-9_]+")
	words = re.finditer(wordPattern,text)
	end=0
	result=""
	for eachword in words:
		word=eachword.group()[1:]
		if len(word)==0:
			continue
		if word.upper()=="NAME":
			result=result+text[end:eachword.start()]+eachword.group()
			end=eachword.end()
			continue
		correctedword=autocorrect.spell(word)
		# print(eachword.group(),word,correctedword) --log--
		result=result+text[end:eachword.start()]+eachword.group()[0]+correctedword
		end=eachword.end()
	result=result+text[end:]
	return result

def substituteNames(text , names):
	for eachname in names:
		text=text.replace(eachname,"*NAME*")
	return text

inputText=input()
modString,names=replaceMentionsWithNames(inputText) # modStirng stores the modified string ,String will be modified multiple times for different purposes , names stores the list of names mentioned in the text
modString=deleteEmotes(modString)
modString=breakDownHashtags(modString)
modString=doSpellCorrection(" "+modString)[1:]
modString=substituteNames(modString)

print(modString)