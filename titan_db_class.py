from __future__ import annotations
from enum import Enum
import numpy as np

class fundamental_attributes(Enum):
  adjustment_factor = 1
  global_cap = 2
  local_cap = 3
  free_cap = 4
  price_to_book = 5
  price_earnings = 6
  return_on_equity = 7

valid_attributes = [attribute.name for attribute in fundamental_attributes]

def mock_insert_value_to_db(date: str, symbol_id: str, attribute: str, value: float):
  return True

def mock_query_value_from_db(date: str, symbol_id: str, attribute: str):
  return 0

def update_fundamental_info(dates: list[str], symbol_ids: list[str], attribute: str, data: np.array):
  
  if attribute not in valid_attributes:
    raise Exception(f"{attribute} table does not exist in DB.")

  #with MockTitanMysqlDb() as db:
  for i, date in enumerate(dates):
    for j, symbol_id in enumerate(symbol_ids):
      value = data[i, j]
      mock_insert_value_to_db(date, symbol_id, attribute, value)
  
  return True

def query_fundamental_info(dates: list[str], symbol_ids: list[str], attribute: str):

  if attribute not in valid_attributes:
    raise Exception(f"{attribute} table does not exist in DB.")

  # with MockTitanMysqlDb() as db:
  shape = (len(dates), len(symbol_ids))
  result = np.full(shape, np.nan)
  for i, date in enumerate(dates):
    for j, symbol_id in enumerate(symbol_ids):
      value = mock_query_value_from_db(date, symbol_id, attribute)
      result[i, j] = value
  
  return result
