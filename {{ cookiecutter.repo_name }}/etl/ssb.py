# Post spørring og få Pandas dataframe i retur
# benytter biblioteket pyjstat for JSON-stat

from pyjstat import pyjstat
import requests

# Demo: Salmon export
POST_URL = 'https://data.ssb.no/api/v0/no/table/03024'

def fetch_data():
  # API spørring, kan tas fra Konsoll  - fryst og fersk laks siste 53 uker
  payload = {"query": [
        {"code": "VareGrupper2", "selection": {"filter": "item", "values": ["01", "02"] } },
        {"code": "ContentsCode", "selection": {"filter": "item", "values": ["Vekt", "Kilopris"] } },
        {"code": "Tid", "selection": {"filter": "top", "values": ["53"] } }
      ],
      "response": {"format": "json-stat2"}
      }

  resultat = requests.post(POST_URL, json = payload)

  dataset = pyjstat.Dataset.read(resultat.text)
  df = dataset.write('dataframe')
  
  return df