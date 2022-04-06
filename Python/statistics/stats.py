import pandas as pd
tfuds_df = pd.read_csv("Q1TPROEST.csv")


frequencia_simples = tfuds_df['fi']
tfuds_df.loc[8, "fi"] = frequencia_simples.sum()
fitot = tfuds_df.loc[8, "fi"]

fri = []
for fi in frequencia_simples:
    fri.append(round((fi/fitot)*100, 1))

fritot = sum(fri)
if fritot == 100.0:
    fri.append(fritot)
    tfuds_df.loc[:, "fri"] = fri
else:
    print("got an error. fri sum doesnt match the expected.")

Fi = []
Fitot = 0
for fi in frequencia_simples:
    Fitot+= fi
    Fi.append(Fitot)

if fitot != Fitot:
    print("got and error. Fi doesnt match the expected.")
else:
    Fi.append(None)

tfuds_df.loc[:, "Fi"] = Fi
frequencia_acumulada = tfuds_df["Fi"]

Fri = []
for fa in frequencia_acumulada:
    Fri.append(round((fa / fitot) * 100, 1))

if  Fri[-1] != 100.0:
    print("got and error. Fi doesnt match the expected.")
else:
    Fri.append(None)

tfuds_df.loc[:, "Fri"] = Fri

invFi = []
invFitot = 0
for i in range(len(frequencia_simples) - 1, -1, -1):
    invFitot += frequencia_simples[i]
    invFi.append(invFitot)

if fitot != invFitot:
    print("got and error. invFi doesnt match the expected.")
    quit()
else:
    invFi.sort(reverse=True)
    invFi.append(None)

tfuds_df.loc[:, "invFi"] = invFi

frequencia_inversa = tfuds_df["invFi"]

invFri = []
for inv in frequencia_inversa:
    invFri.append(round((inv / fitot) * 100, 1))

print(invFri)
if  invFri[0] != 100.0:
    print("got and error. Fi doesnt match the expected.")

tfuds_df.loc[:, "invFri"] = invFri
print(tfuds_df)
