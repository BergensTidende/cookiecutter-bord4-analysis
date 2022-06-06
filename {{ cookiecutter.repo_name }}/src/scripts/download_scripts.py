import requests
import zipfile
from io import BytesIO
import os

def main():
  PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
  
  src_url = "https://github.com/BergensTidende/bord4-analysis-templates/blob/master/src.zip?raw=true"
  
  r = requests.get(src_url, allow_redirects=True)
  print('Downloading zip file form Github')

  # extracting the zip file contents
  src_zip = zipfile.ZipFile(BytesIO(r.content))
  src_zip.extractall(PROJECT_DIRECTORY)
  print('Extractet zip to src directory')

if __name__ == '__main__':
    main()
