import BBRhandler
import datafordeleren
import csvHandler
import emoweb
import NeoGrid

#BBRhandler.calculateEnergyDemand(630)
#datafordeleren.getHusnummer(3310, "Ølsted.csv", 100*1000)
#datafordeleren.getAdresser("Bygninger_udenadresser.xlsx", "Husnummer", "Adresser.csv")
#datafordeleren.getAdgangsadressebetegnelse("0a3f508e-9638-32b8-e044-0003ba298018")
#emoweb.getLabelSerialIdentifierForBulding(621, 1302969, 3)
emoweb.getAllBuildingsInKommune(621, "id=b491375f-65c1-49c1-9ff6-9d22a753ebb0")
#emoweb.getEnergyLabelForLabelSerialIdentifierFromTo(200053229, 200053239)
#datafordeleren.getBygninger(151, "BallerupBBR200stk.csv", 200)
#datafordeleren.antalAdresseBygning("003f2878-10e4-4515-84de-ad3db3a44dda")
#emoweb.getAllBuildingsInKommune(370)
#emoweb.getAllBuildingsInKommune(655)
#datafordeleren.getAdresseIdList("adresser.xls", "adresser", "adresserID.csv")
#NeoGrid.LinkSensors("NeoGrid.csv")