# https://www.guidodiepen.nl/2021/05/include-help-instructions-in-cookiecutter-prompts/
import json

with open("../cookiecutter.json") as f:
    cc_template = json.load(f)

with open("logo.txt", encoding="utf-8") as f:
    cc_template[" "] = f.read()

with open("../cookiecutter.json", "w") as f:
    f.write(json.dumps(cc_template, sort_keys=False, indent=4))
    f.write("\n")
