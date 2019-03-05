import pytest
from .airport import Airport

class TestAirport(object):
  def test_1_airport_has_empty_hangar(self):
    airport = Airport()
    assert airport.hangar == []