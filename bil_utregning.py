#Dette er et program med to klasser, en Elbil-klasse og en Bensinbil-klasse basert på informasjonen i oppgaveteksten. Programmet har i tillegg en funksjon .finn_billigste_bil(bil_1,bil_2) som sammenligner resultatet mellom to biler. Deretter inneholder programmet et testprogrammet som lager et bilobjekt av hver klasse, og sammenligner de årlige kostnadene mellom de før det skrives ut i terminalen det som er det mest kostnadseffektive bilalternativet.

#(NB! Jeg er klar over at klassene burde nok vært i en egen fil, men jeg har valgt å ha alt i samme dokument når oppgaven er så liten :) )

class Elbil:
    def __init__(self, ant_kjoerte_km:int): #Konstruktøren har parameteren antall kjørte kilometer årlig som grunnlag for utregningen.
        self._type_bil = "Elbil" #setter bil_typen
        self._ant_kjoerte_km = ant_kjoerte_km 
        self._forsikring = 5000 #årlig sum på forsikring
        self._trafikkforsikringsavgift = 8.38 * 365 #årlig sum på trafikkforsikringsavgift
        self._drivstoffbruk = 0.2 * 2 * ant_kjoerte_km #drivstoffforbruket til elbilen blir antall kjørte kilometer ganger (0,2 kWh/km * 2.00 kr/kWh) for å få resultatet i kroner per km. 
        self._bomavgift = 0.1 * ant_kjoerte_km #bomavgiften
        self._total_kostnad = self.hent_total_kostnad() #en metode som 
    
    def hent_type_bil(self): #lager denne metoden for å kunne bruke den senere i testprogrammet for å hente type bil i printsetningen.
        return self._type_bil

    def hent_total_kostnad(self): #utregning av totalkostandene årlig for gitt type bil
        total_kostnad = self._forsikring + self._trafikkforsikringsavgift + self._drivstoffbruk + self._bomavgift
        return total_kostnad
    
    def __str__(self): #en __str__ som skriver ut all informasjon om dette bil-objektet
        return f"Elbilen har kjørt: {self._ant_kjoerte_km} km.\nBilens årlige kostnader basert på dette er:\n\n{self._forsikring}kr i forsikring.\n{self._trafikkforsikringsavgift:.01f}kr i trafikkforsikringsavgift.\n{self._drivstoffbruk}kr i drivstoffbruk.\n{self._bomavgift}kr i bomavgift.\n\nBilens totalkostnader er: {self._total_kostnad}kr"

#For klassen Bensinbil gjelder samme kommentarer og oppsett som i klassen Elbil over. Det er derfor ikke skrevet dobbelt opp med kommentarer her.

class Bensinbil:
    def __init__(self, ant_kjoerte_km):
        self._type_bil = "Bensinbil"
        self._ant_kjoerte_km = ant_kjoerte_km
        self._forsikring = 7500
        self._trafikkforsikringsavgift = 8.38 * 365
        self._drivstoffbruk = 1 * ant_kjoerte_km
        self._bomavgift = 0.3 * ant_kjoerte_km
        self._total_kostnad = self.hent_total_kostnad()
    
    def hent_type_bil(self):
        return self._type_bil

    def hent_total_kostnad(self):
        total_kostnad = self._forsikring + self._trafikkforsikringsavgift + self._drivstoffbruk + self._bomavgift
        return total_kostnad

    def __str__(self):
        return f"Bensinbilen har kjørt: {self._ant_kjoerte_km} km.\nBilens årlige kostnader basert på dette er:\n\n{self._forsikring}kr i forsikring.\n{self._trafikkforsikringsavgift:.01f}kr i trafikkforsikringsavgift.\n{self._drivstoffbruk}kr i drivstoffbruk.\n{self._bomavgift}kr i bomavgift.\n\nBilens totalkostnader er: {self._total_kostnad}kr"


#Metode som skal brukes i filen for å sammenligne biltypenes årlige kostnader:
def finn_billigste_bil(bil_1, bil_2): #tar inn to bil-objekter
    billigst_bil = None
 
    if bil_1.hent_total_kostnad() < bil_2.hent_total_kostnad():
        billigst_bil = bil_1 #settes som det gitte bil-objektet hvis det er billigst

    elif bil_2.hent_total_kostnad() < bil_1.hent_total_kostnad():
        billigst_bil = bil_2 #settes som det gitte bil-objektet hvis det er billigst

    return billigst_bil #returnerer det billigste bil-objektet. Returnerer None om bilene koster det samme årlig


#Testprogram:
bil_1 = Bensinbil(10000) #bil 1 settes som en bensinbil som har kjørt 10 000 km
print(bil_1) #printer ut all tilhørende info om bensinbil-objektet ve hjelp av metoden __str__

bil_2 = Elbil(10000) #bil 2 settes som en elbil som har kjørt 10 000 km
print(bil_2) #printer ut all tilhørende info om elbil-objektet ve hjelp av metoden __str__

#sammenligning av de to bilene:
billigst_bil = finn_billigste_bil(bil_1, bil_2)

if billigst_bil is None: #hvis bilene koster det samme printes dette ut
        print("Bilene har lik årlig kostnad.")
else:
    print(f"Billigste bilen er: {billigst_bil.hent_type_bil()}en, som har en årlig kostnad på: {billigst_bil.hent_total_kostnad()},-") #skriver ut hva som er den billigste biltypen av de to som er sammenlignet og hva den totalkostnaden er.