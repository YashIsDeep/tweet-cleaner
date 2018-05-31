import re
import autocorrect

def replaceMentionsWithNames(text): # Replaces the @names with *Name* and returns the names used
	namePattern = re.compile(r"@[a-zA-Z0-9_]{1,15}")
	names=set()
	modString="" # modStirng stores the modified string ,String will be modified multiple times for different purposes
	matches = re.finditer(namePattern,text)
	end=0
	for match in matches:
		names.add(match.group()[1:])
		modString=modString+text[end:match.start()]+"*NAME*"
		end=match.end()
	modString=modString+text[end:]
	return modString,names

def deleteEmotes(str):
	emoji_pattern = re.compile(":(\(\)\\/OPI|\[\])")
	str=emoji_pattern.sub(r"",str)
	return str

def breakDownHashtags(str):
	return str

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
		# print(eachword.group(),word,correctedword)
		result=result+text[end:eachword.start()]+eachword.group()[0]+correctedword
		end=eachword.end()
	result=result+text[end:]
	return result
	# splitPattern=re.compile(r'[^a-zA-Z0-9_]')
	# words=re.finditer(splitPattern, text) # splits string into words 
	# result=""
	# end=0
	# for eachword in words:
	# 	word=eachword.group()
	# 	if len(word)==0:
	# 		continue
	# 	if word.upper()=="*NAME*":
	# 		result=result+text[end:eachword.start()]+word
	# 		end=eachword.end()
	# 		continue
	# 	correctedword=autocorrect.spell(word)
	# 	result=result+text[end:eachword.start()]+correctedword
	# 	end=eachword.end()
	# result=result+text[end:]
	# return result

# The set 'names' contains all the names now

inputText=input()
modString,names=replaceMentionsWithNames(inputText)
modString=deleteEmotes(modString)
modString=breakDownHashtags(modString)
modString=doSpellCorrection(" "+modString)[1:]



print(modString)



