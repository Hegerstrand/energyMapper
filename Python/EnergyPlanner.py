import BBRhandler
import sys

try:
    if(len(sys.argv)>1):
        try:
            kommunekode = sys.argv[1]
        except sys.argv as msg:
            print(msg)
    else:
        print('This version only support one kommunekode', sys.argv)
except:
    print("Not found: sys.argv")
    exit()

if int(kommunekode) > 100:
    try:
        print ('Running EnergyPlanner for kommune:', str(kommunekode), '.')
        BBRhandler.calculateEnergyDemand(int(kommunekode))
    except kommunekode as msg:
        print(msg)

else:
    print('Input for kommunekode not found')