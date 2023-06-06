import requests
import pytest
import random
import json
import jsonschema
from schema import schema_1
from const import *
from param import *



def test_ballers_season_1():
  URL = f"{HOST}/?apikey={APIKEY}&t={TITLE_B}&Season={SEASON_1}"
  req = requests.get(URL)
  assert req.status_code == 200
  content = req.json()
  assert content["Title"] == TITLE_B
  assert content["Season"] == SEASON_1
  episodes = content["Episodes"]
  title_ep0 = episodes[0]["Title"]
  assert title_ep0 == TITLE_B1_ep0
  imdbID_ep5 = episodes[4]["imdbID"]
  assert imdbID_ep5 == imdbID_B1_ep5
  episode_num10 = episodes[8]["Episode"]        # нету серии с №1, есть №0 и №2, посему крайний словарь 8
  assert episode_num10 in EPISIDE_B_LIST
  print(req.json())


@pytest.mark.parametrize("TITLE", TITLE_LIST)
def test_title_list(TITLE):
  URL = f"{HOST}/?apikey={APIKEY}&t={TITLE}&Season={SEASON_1}"
  req = requests.get(URL)
  assert req.status_code == 200
  content = req.json()
  assert content["Title"] == TITLE


@pytest.fixture(scope="function")
def random_season():
  return random.choice(SEASON_LIST)


def test_random_season(random_season):
  URL = f"{HOST}/?apikey={APIKEY}&t={TITLE_B}&Season={random_season}"
  req = requests.get(URL)
  assert req.status_code == 200
  content = req.json()
  assert content["Season"] == random_season
  print(random_season)


def test_jsonschema():
  URL = f"{HOST}/?apikey={APIKEY}&t={TITLE_B}&Season={SEASON_1}"
  req = requests.get(URL)
  data = json.loads(req.text)
  print(data)
  try:
    jsonschema.validate(data, schema_1)
  except jsonschema.exceptions.ValidationError:
    assert False
  else:
    assert True




