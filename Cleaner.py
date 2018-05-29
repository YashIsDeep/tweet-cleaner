import re

text = input()
namePattern = re.compile(r"@[a-zA-Z0-9_]{1,15}")
names=set()
modString="" # modStirng stores the modified string ,String will be modified multiple times for different purposes

matches = re.finditer(namePattern,text)

end=0
for match in matches:
	names.add(match.group()[1:])
	modString=modString+text[end:match.start()]+"*NAME*";
	end=match.end()

modString=modString+text[end:]
# The set 'names' contains all the names now

print(modString)

modString=deleteEmotes(modString)
modString=breakDownHashtags(modString)
modString=doSpellCorrection(modString)

# now replace the 