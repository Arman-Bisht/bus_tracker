import pandas as pd

dict1 = {
    "Serial": ["1", "2", "3"],
    "Number": ["UK07TA1234", "UK07TA2345", "UK07TB3445"],
    "Time": ["5:30", "6:00", "7:00"],
    "City": ["Delhi", "Lucknow", "Mumbai"],
    "Status": ["NA", " NA", " NA"]
}
df = pd.DataFrame(dict1)
df.to_csv("Bus.csv", index=False)


def available(a):
    for i in range(0, 3):
        if a in dict1["Number"][i]:
            df["Status"][i] = "Available"


available("UK07TA2345")
print(df)
