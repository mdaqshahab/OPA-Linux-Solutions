class ParkedVehicle:
    def __init__(self, seq, fourwh, pfor, vpar):
        self.vehicleSeq = seq
        self.fourWheeler = fourwh
        self.parkedFor = pfor
        self.valetParking = vpar
        self.parkedStatus = "Parked"

class ParkingLot:
    def __init__(self,pveh):
        self.parkd_vehicles = pveh
    
    def updateParkedStatus(self, lot_number):
        if lot_number in self.parkd_vehicles.keys():
           parkd_vehicles[lot_number].parkedStatus = "Cleared"
           status=(lot_number, "Cleared")
           return status
        else:
           return None
        
    def getParkingCharges(self, lot_number):
        if lot_number in self.parkd_vehicles.keys():
            charge = 0
            if self.parkd_vehicles[lot_number].fourWheeler == "Yes":
                charge = charge + (50*self.parkd_vehicles[lot_number].parkedFor)
            else:
                charge = charge + (30*self.parkd_vehicles[lot_number].parkedFor)

            if self.parkd_vehicles[lot_number].valetParking == "Yes":
                charge+=10
            return charge
        else:
            return None


if __name__ == '__main__':
    num = int(raw_input())
    parkd_vehicles = {}
    for i in range(num):
        seq = int(raw_input())
        four = raw_input()
        pfor = float(raw_input())
        vpar = raw_input()
        lot = int(raw_input())
        vehicle = ParkedVehicle(seq,four,pfor,vpar)
        parkd_vehicles[lot] = vehicle
    lot_num = int(raw_input())
    p_lot = ParkingLot(parkd_vehicles)
    p_status = p_lot.updateParkedStatus(lot_num)
    p_charge = p_lot.getParkingCharges(lot_num)
    if p_status == None:
        print("Lot Number Invalid")
        print("Lot Number Invalid")
    else:
        print(p_status[0]+" "+p_status[1])
        print(p_charge)