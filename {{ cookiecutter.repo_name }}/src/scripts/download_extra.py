import requests
import questionary
import os

def list_extras():
  ##
  # Lists all extra folders in the src/extra folder
  #
  url = "https://api.github.com/repos/BergensTidende/bord4-analysis-templates/contents/src/extra"
  r = requests.get(url)
  r.raise_for_status()
  
  data = r.json()
  extras = [extra["name"] for extra in data]
  
  return extras

def main():
  PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
  extras = list_extras()
    
  extra = questionary.select(
    "What folder do you want to download?",
    choices=extras,
  ).ask()
  
  extra_url = f"https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/src/extra/{extra}"
  
  new_file_path = os.path.join(PROJECT_DIRECTORY, "src", extra)
  
  r = requests.get(extra_url, allow_redirects=True)
  open(new_file_path, 'wb').write(r.content)
  
  print("Downloaded", extra, "and saved it to", new_file_path)

if __name__ == '__main__':
    main()
