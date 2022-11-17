import json

console_commands_json_file = open("utils\\console_commands.json")
console_commands_json = json.load(console_commands_json_file)
console_commands_json_file.close()

match = ""
for idx, command in enumerate(console_commands_json["console_commands"]):
    if idx == 0:
        match += command
    else:
        match += "|" + command

match = "\\" + "b(" + match + ")" + "\\b"

syntaxFile = open("syntaxes\\total_war_script.tmLanguage.json")
syntaxJson = json.load(syntaxFile)
syntaxFile.close()

syntaxFile = open("syntaxes\\total_war_script.tmLanguage.json", "w")
if syntaxJson:
    syntaxJson["repository"]["console_commands"]["match"] = match
    json.dump(syntaxJson, syntaxFile, indent = 2)
syntaxFile.close()