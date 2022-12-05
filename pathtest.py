import datetime
import os
from devices import *

def operate_on_xlsx(file):
    now = datetime.datetime.now()
    time_stamp = now.strftime("%c").replace(" ", "")
    time_stamp = time_stamp.replace(":", "")
    Current_Directory = os.getcwd()
    target_folder = Current_Directory + f'/{time_stamp}'
    os.mkdir(target_folder)
    t = target_folder
    print(t)

    CHANNEL_NAME = "CH001"
    PLC_NAME = "IEWPLC01"
    ALARM_AREA = "TBDALMXX"
    DISPATCH_DICT = {"VFD_Pump": PumpVFD, "SS_Pump": PumpSS, "Mixer": PumpMixer, "Transmitter": GeneralTransmitter,
                    "HW_Transmitter": GeneralTransmitterHW, "LIT": LITransmitter, "FIT": FITransmitter,
                    "Valve": ValveGate, "Gate": ValveGate}



    # File coming from drop box will be here repalce "Standard_template.xlsx"
    date = pandas.read_excel(file, sheet_name=0)
    print(date)

    for index, row in date.iterrows():
        device = DISPATCH_DICT[row["Device"]](channel_name=CHANNEL_NAME, plc_name=PLC_NAME, tag=row["Tag"],
                                            description=row["Description"], alarm_area=ALARM_AREA)

        for frame in device.frame_list:
            frame.to_csv(f"{target_folder}/{row['Device']}_{row['Tag']}.csv", mode='a', index=False)

    # ZIP target_folder here and push it back to website
    return t