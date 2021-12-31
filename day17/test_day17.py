import pytest
import day17_1 as d

def test_in_range():
    assert d.in_target(1,2) == False, "1,2"
    assert d.in_target(20,2) == False, "20,2"
    assert d.in_target(2,-5) == False, "2, -5"
    assert d.in_target(20,-5) == True, "20,-5"
    assert d.in_target(25,-7) == True, "25,-7"
    assert d.in_target(30,-10) == True, "30,-10"
    assert d.in_target(30,-12) == False, "30,-12"
    assert d.in_target(35,-10) == False, "35,-10"
    assert d.in_target(35,-15) == False, "35,-15"

def test_max_height():
    assert d.max_height(7, 2) == 3
    assert d.max_height(6, 3) == 6
    assert d.max_height(9, 0) == 0
    assert d.max_height(17, -4) == -1
