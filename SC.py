import pandas
from devices import *

CHANNEL_NAME = "CH001"
PLC_NAME = "IEWPLC01"
ALARM_AREA = "TBDALMXX"
DISPATCH_DICT = {"VFD_Pump": PumpVFD, "SS_Pump": PumpSS, "Mixer": PumpMixer, "Transmitter": GeneralTransmitter,
                 "HW_Transmitter": GeneralTransmitterHW, "LIT": LITransmitter, "FIT": FITransmitter,
                 "Valve": ValveGate, "Gate": ValveGate}

date = pandas.read_excel("Standard_template.xlsx", sheet_name=0)
print(date)

for index, row in date.iterrows():
    device = DISPATCH_DICT[row["Device"]](channel_name=CHANNEL_NAME, plc_name=PLC_NAME, tag=row["Tag"],
                                          description=row["Description"], alarm_area=ALARM_AREA)

    for frame in device.frame_list:
        frame.to_csv(f"{row['Device']}_{row['Tag']}.csv", mode='a', index=False)


