import pytest
from .airport import Airport
from .plane import Plane

class TestAirport(object):
  def test_1_airport_has_empty_hangar(self):
    airport = Airport()
    assert airport.hangar == []

  def test_2_airport_can_land_plane(self):
    airport = Airport()
    plane1 = Plane()
    airport.land(plane1)
    assert airport.hangar == [plane1]

  def test_3_airport_can_takeoff_plane(self):
    airport = Airport()
    plane1 = Plane()
    airport.land(plane1)
    airport.takeoff(plane1)
    assert airport.hangar == []

  def test_4_airport_has_a_default_capacity(self):
    airport = Airport(10)
    assert airport.capacity == 10

  # def test_5_airport_can_not_land_plane_if_full(self):
  #   airport = Airport()
  #   plane1 = Plane()
  #   for x in range(10):
  #     airport.land(plane1)
  #   assert airport.hangar.count(plane1) == 10

  # def test_raises(self):

  #   with pytest.raises(Exception) as excinfo:   
  #       raise Exception('some info')   
  #   assert excinfo.value.message == 'some info'  

  