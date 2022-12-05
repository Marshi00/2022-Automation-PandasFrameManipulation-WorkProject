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

"""a = pandas.read_csv"weather_data.csv")
print(data["temp"])

# Get data in columns
print(data["condition"])
print(data.condition)
# Get data in rows
print(data[data.day == "Wednesday"])
print(data[data.temp == data["temp"].max()])

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Joe", "David"],
    "score": [40, 49, 41]
}
data_frame = pandas.DataFrame(data_dict)
print(data_frame)
# Making CSV
data_frame.to_csv("new_Data.csv")

# Central_Park_DATA
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_data = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_data = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_data = len(data[data["Primary Fur Color"] == "Black"])
central_park_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_data, Cinnamon_data, Black_data]
}
central_park_data_frame = pandas.DataFrame(central_park_data_dict)
central_park_data_frame.to_csv("central_park.csv")
"""
"""
data = pandas.read_csv("Standard_template.xlsx")
# print(data)
dict = data.to_dict("list")
# print(dict)
# data_frame = pandas.DataFrame(dict)
# print(data_frame)
# Making CSV
# data_frame.to_csv("new_Data.csv")
"('dict', list, 'series', 'split', 'records', 'index')"
dev = devices.GeneralTransmitterHW(channel_name="CH001", plc_name="IEWPLC01", tag="IEW_EWP1", description="Pump 2",
                        alarm_area="TBDALMXX")
frame_list = dev.gen_hw_trans_frame_list()
for item in frame_list:
    item.to_csv("gentrasHW.csv", mode='a', index=False)

print(dev.runtime_hours.tag)
"""
# low = signals.AI()
# vfd = signals.generate_header(low.ai_header_attributes)
"""
print(vfd)
vfd.to_csv("new_Data.csv", index=False)
"""
