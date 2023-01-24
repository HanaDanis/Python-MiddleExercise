import os
from dotenv import load_dotenv
from log import log
from mes import mes

class car:
    l = log()
    mes = mes()
    load_dotenv()
    
    # init var
    def __init__(self):
        self.fuelPrice = int(os.getenv('FEULPRICE'))
        self.fulTank = int(os.getenv('FULTANK'))
        self.feul = int(os.getenv('FEUL'))
        self.literPerKm = int(os.getenv('LITERPERKM'))/100
        self.mony = int(os.getenv('MONY'))
        self.maxg = int(os.getenv('MAXG'))
        self.speedg = int(os.getenv('SPEEDG'))
        self.speed = 0
        self.gear = 0
        self.status = False

    def start(self):
       """Hana, 22.01.2023
       start the car"""
       self.status = True
       self.l.write(self.mes.dict['mes10'])

    def driving(self, drive):
            """Hana, 22.01.2023
            chack if have feul to drive"""
            if self.feul >= drive * self.literPerKm:
                self.feul-= drive * self.literPerKm
            else:
                self.refueling(drive * self.literPerKm - self.feul)
                self.l.write(self.mes.dict['mes1'])
                raise Exception(self.mes.dict['mes1'])
            self.l.write(self.mes.dict['mes11'])
            
    def stop(self):
            """Hana, 22.01.2023
            stop the care"""
            self.gear = 0
            self.speed = 0
            self.status = False
            self.l.write(self.mes.dict['mes12'])

    def gearUp(self):
            """Hana, 22.01.2023
            Each call advances gear by one"""
            if self.gear < self.maxg and self.status:
                self.speed+=self.speedg
                self.gear+=1
            else:
                raise Exception(self.mes.dict['mes3'])
            self.l.write(self.mes.dict['mes13'])

    def gearDown(self):
        """Hana, 22.01.2023
        Each call sub gear by one"""
        if self.gear > 0 and self.status:
                self.speed-=self.speedg
                self.gear-=1
        else:       
            raise Exception(self.mes.dict['mes21'])
        self.l.write(self.mes.dict['mes14'])

    def refueling(self,userF=0):
            """Hana, 22.01.2023
            Fills up with gas as long as there is enough space and money"""
            self.stop()
            while self.mony and self.feul < self.fulTank and self.feul < userF:
                self.feul+= 1
                self.mony -= self.fuelPrice * 1
            else:
                raise Exception(self.mes.dict['mes5'])
            self.l.write(self.mes.dict['mes15'])


    



