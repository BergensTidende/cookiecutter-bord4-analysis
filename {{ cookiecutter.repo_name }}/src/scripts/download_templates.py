import requests
import questionary
import os
import shutil

def list_templates():
  ##
  # Lists all templates in the template folder in the github repo
  #
  url = "https://api.github.com/repos/BergensTidende/bord4-analysis-templates/contents/templates"
  r = requests.get(url)
  r.raise_for_status()
  
  data = r.json()
  templates = [template["name"] for template in data]
  
  return templates

def main():
  PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
  templates = list_templates()
    
  destination = questionary.select(
    "Choose destination folder ?",
    choices=["etl", "eda", "publish"],
  ).ask()
  
  template = questionary.select(
    "What template do you want to use?",
    choices=templates,
  ).ask()
  
  file_name = questionary.text("What's the name of the file?").ask()
  template_url = f"https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/{template}"
  
  template_file_extension = template.split(".")[1]
  
  new_file_path = os.path.join(PROJECT_DIRECTORY, destination, file_name + "." + template_file_extension)
  
  r = requests.get(template_url, allow_redirects=True)
  open(new_file_path, 'wb').write(r.content)
  
  print("Created", new_file_path, "from template", template)

if __name__ == '__main__':
    main()
