import random
n_sample = 50

with open("demo.tsv", "w") as record_file:
    record_file.write("City	State	lat	lon	Amount\n")
    for i in range(n_sample):
        city = "HN"
        state= "VN"
        lat = random.randrange(2000,2200)/100.0
        lon = random.randrange(10500,10700)/100.0
        amount = random.randrange(10, 1000)
        record_file.write(str("%s	%s	%s	%s	%s\n"%(city, state, lat, lon, amount)))
