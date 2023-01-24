import unittest
from car import car
from mes import mes
from log import log

class Testcal(unittest.TestCase):
    l = log()
    mes = mes()
    def setUp(self):
        self.car = car()
    
    def test_stop(self):
        """Hana, 22.01.2023
        check if the speed = 0
         when the car stop"""
        try:
            self.car.etop()
            self.assertEqual(self.car.speed, 0)
        except Exception:
            self.l.write(self.mes.dict['mes6'])
        self.l.write(self.mes.dict['mes7'])

    def test_refueling_feul(self):
        """Hana, 22.01.2023
        check if the feul update after refueling func"""
        try:
          self.car.refueling()
          self.assertEqual(self.car.feul, 60)
        except Exception:
            self.l.write(self.mes.dict['mes17'])
        self.l.write(self.mes.dict['mes16'])

    def test_start(self):
     """Hana, 22.01.2023
     check if the fule update after start func"""
     try:
        self.car.start()
        self.car.driving(20)
        self.assertEqual(self.car.feul, 49)
     except Exception:
         self.l.write(self.mes.dict['mes8'])
     self.l.write(self.mes.dict['mes9'])

    def test_refueling_mony(self):
        """Hana, 22.01.2023
        check if the mony update after refueling func"""
        try:
            self.car.refueling()
            self.assertEqual(self.car.mony, 390)
        except Exception:
            self.l.write(self.mes.dict['mes17'])
        self.l.write(self.mes.dict['mes16'])

    def test_gearUp(self):
        """Hana, 22.01.2023
        check if the gear up after gearUp func"""
        try:
            self.car.gearUp()
            self.assertEqual(self.car.gear, 1)
        except Exception:
            self.l.write(self.mes.dict['mes18'])
        self.l.write(self.mes.dict['mes19'])

    def test_gearDown(self):
        """Hana, 22.01.2023
        check if the gear Down after gearUp func"""
        try:
            self.car.gearDown()
            self.assertEqual(self.car.gear, 0)
        except Exception:
            self.l.write(self.mes.dict['mes20'])
        self.l.write(self.mes.dict['mes21'])


if __name__ == '__main__':
    unittest.main()