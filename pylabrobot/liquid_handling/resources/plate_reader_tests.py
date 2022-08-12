""" Tests for Resource """
# pylint: disable=missing-class-docstring

from multiprocessing.sharedctypes import Value
import unittest

from pylabrobot.liquid_handling.resources.abstract.plate import Plate
from pylabrobot.liquid_handling.resources.plate_reader import PlateReader


class TestPlateReader(unittest.TestCase):
  def test_add_plate(self):
    plate = Plate("plate", size_x=1, size_y=1, size_z=1, dx=0, dy=0, dz=0, one_dot_max=1)
    plate_reader = PlateReader("plate_reader")
    plate_reader.assign_child_resource(plate)

  def test_add_plate_full(self):
    plate = Plate("plate", size_x=1, size_y=1, size_z=1, dx=0, dy=0, dz=0, one_dot_max=1)
    plate_reader = PlateReader("plate_reader")
    plate_reader.assign_child_resource(plate)

    another_plate = Plate("another_plate", size_x=1, size_y=1, size_z=1,
      dx=0, dy=0, dz=0,one_dot_max=1)
    with self.assertRaises(ValueError):
      plate_reader.assign_child_resource(another_plate)

  def test_get_plate(self):
    plate = Plate("plate", size_x=1, size_y=1, size_z=1, dx=0, dy=0, dz=0, one_dot_max=1)
    plate_reader = PlateReader("plate_reader")
    plate_reader.assign_child_resource(plate)

    self.assertEqual(plate_reader.get_plate(), plate)

if __name__ == "__main__":
  unittest.main()