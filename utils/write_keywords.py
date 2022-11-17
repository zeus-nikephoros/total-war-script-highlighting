import json

keywordsFilePath = "utils\\events.json"
keywordsID = "events"

syntaxDefinitionFilePath = "syntaxes\\total_war_script.tmLanguage.json"

keywords_file = open(keywordsFilePath)
keywords_json = json.load(keywords_file)
keywords_file.close()

match = ""
for idx, keyword in enumerate(keywords_json[keywordsID]):
    if idx == 0:
        match += keyword
    else:
        match += "|" + keyword

match = "\\" + "b(" + match + ")" + "\\b"

syntaxFile = open(syntaxDefinitionFilePath)
syntaxJson = json.load(syntaxFile)
syntaxFile.close()

syntaxFile = open(syntaxDefinitionFilePath, "w")
if syntaxJson:
    syntaxJson["repository"][keywordsID]["match"] = match
    json.dump(syntaxJson, syntaxFile, indent = 2)
syntaxFile.close()