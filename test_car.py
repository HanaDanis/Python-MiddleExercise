import pytest
from car import car
from log import log
from mes import mes
  
c = car()
l = log()
m = mes()

def test_start():
    """Hana, 22.01.2023
    check if the fule update after start func"""
    try:
        c.start()
        c.driving(20)
        assert c.feul == 49
    except Exception:
        l.write(m.dict['mes8'])
    l.write(m.dict['mes9'])

def test_refueling_mony():
    """Hana, 22.01.2023
    check if the mony update after refueling func"""

    try:
        c.refueling()
        assert c.mony == 390
    except Exception:
        l.write(m.dict['mes17'])
    l.write(m.dict['mes16'])

@pytest.mark.gear
def test_gearUp():
    """Hana, 22.01.2023
    check if the gear up after gearUp func"""
    try:
      c.gearUp()
      assert c.gear == 1
    except Exception:
            l.write(m.dict['mes18'])
    l.write(m.dict['mes19'])

def test_gearDown():
    """Hana, 22.01.2023
    check if the gear Down after gearUp func"""
    try:
        c.gearDown()
        assert c.gear == 0
    except Exception:
            l.write(m.dict['mes20'])
    l.write(m.dict['mes21'])

def test_gear_more_than_max():
    """Hana, 22.01.2023
    check if the gear can up more than max"""
    try:
        for i in range(6):
            c.gearUp()
        with pytest.raises(Exception):
            c.gearUp()
    except Exception:
        l.write(m.dict['mes23'])

def test_gear_less_than_min():
    """Hana, 22.01.2023
    check if the gear can up less than min"""
    try:
            for i in range(6):
                c.gearDown()
            with pytest.raises(Exception):
                c.gearDown()
    except Exception:
            l.write(m.dict['mes22'])

def test_stop_failure():
    try:
        car.status=False
        with pytest.raises(Exception):
            car.stop()
        l.write(m.dict['mes21'])
    except:
       l.write(m.dict['mes21'])