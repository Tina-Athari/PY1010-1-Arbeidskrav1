class Bil:
    def __init__(self, ant_kjoerte_km:int, bil_type):
        self._ant_kjoerte_km = ant_kjoerte_km
        self._bil_type = bil_type
        self._forsikring = 0
        self._drivstoffbruk = 0
        self._trafikkforsikringsavgift:float = 3058.7 #sum årlig
        self._bomavgift = 0
        self._total_kostnad = 0
    
    def forsikring(self):
        if self._bil_type == "elbil":
            self._forsikring = 5000
            return self._forsikrings
        elif self._bil_type == "bensinbil":
            self._forsikring = 7500
            return self._forsikring
        else:
            print("Feil input på type bil, skriv 'elbil' eller 'bensinbil'.")
    
    def drivstoffbruk(self):
        if self._bil_type == "elbil":
            self._ant_kjoerte_km * 2
            return self._drivstoffbruk
        elif self._bil_type == "bensinbil":
            self._ant_kjoerte_km * 1
            return self._ant_kjoerte_km
        else:
            print("Feil input på type bil, skriv 'elbil' eller 'bensinbil'.")

    def hent_trafikkforsikringsavgift(self):
        return self._trafikkforsikringsavgift
    
    def hent_bomavgift(self):
        if self._bil_type == "elbil":
            self._bomavgift = self._ant_kjoerte_km * 0.1
            return self._bomavgift
        elif self._bil_type == "bensinbil":
            self._bomavgift = self._ant_kjoerte_km * 0,3
            return self._bomavgift
        else:
            print("Feil input på type bil, skriv 'elbil' eller 'bensinbil'.")

    def hent_totalkostnad(self):
        self._total_kostnad = (self._forsikring + self._drivstoffbruk + self._trafikkforsikringsavgift + self._bomavgift)
        return self._total_kostnad

    def __str__(self):
        return(f"Bilen er av type: {self._bil_type} og har kjørt {self._ant_kjoerte_km} km.\n Bilen har total kostnad i et år på: {self._total_kostnad},-")

bil_1 = Bil(10000, "elbil")
bil_1.forsikring()
bil_1.drivstoffbruk()
bil_1.hent_trafikkforsikringsavgift()
bil_1.hent_bomavgift()
bil_1.hent_totalkostnad()

print(bil_1)
