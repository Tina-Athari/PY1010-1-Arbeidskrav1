class Elbil:
    def __init__(self, ant_kjoerte_km:int):
        self._ant_kjoerte_km = ant_kjoerte_km
        self._forsikring = 5000
        self._trafikkforsikringsavgift = 8.38 * 365
        self._drivstoffbruk = 0.2 * 2 * ant_kjoerte_km
        self._bomavgift = 0.1 * ant_kjoerte_km
        self._total_kostnad = self.hent_total_kostnad()

    def hent_total_kostnad(self):
        total_kostnad = self._forsikring + self._trafikkforsikringsavgift + self._drivstoffbruk + self._bomavgift
        return total_kostnad
    
    def __str__(self):
        return f"Elbilen har kjørt: {self._ant_kjoerte_km} km.\nBilens årlige kostnader basert på dette er:\n\n{self._forsikring}kr i forsikring.\n{self._trafikkforsikringsavgift:.01f}kr i trafikkforsikringsavgift.\n{self._drivstoffbruk}kr i drivstoffbruk.\n{self._bomavgift}kr i bomavgift.\n\nBilens totalkostnader er: {self._total_kostnad}kr"

class Bensinbil:
    def __init__(self, ant_kjoerte_km):
        self._ant_kjoerte_km = ant_kjoerte_km
        self._forsikring = 7500
        self._trafikkforsikringsavgift = 8.38 * 365
        self._drivstoffbruk = 1 * ant_kjoerte_km
        self._bomavgift = 0.3 * ant_kjoerte_km
        self._total_kostnad = self.hent_total_kostnad()

    def hent_total_kostnad(self):
        total_kostnad = self._forsikring + self._trafikkforsikringsavgift + self._drivstoffbruk + self._bomavgift
        return total_kostnad

    def __str__(self):
        return f"Bensinbilen har kjørt: {self._ant_kjoerte_km} km.\nBilens årlige kostnader basert på dette er:\n\n{self._forsikring}kr i forsikring.\n{self._trafikkforsikringsavgift:.01f}kr i trafikkforsikringsavgift.\n{self._drivstoffbruk}kr i drivstoffbruk.\n{self._bomavgift}kr i bomavgift.\n\nBilens totalkostnader er: {self._total_kostnad}kr"

bil_1 = Bensinbil(10000)
print(bil_1)

bil_2 = Elbil(10000)
print(bil_2)