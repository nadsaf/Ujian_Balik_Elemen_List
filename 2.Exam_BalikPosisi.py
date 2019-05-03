#BALIK POSISI

def balikPosisi(x):
    hasil = []
    for i in range(len(x)-1,-1,-1):
        hasil.append(x[i])
    return hasil

print(balikPosisi([1,2,3,4,5]))
print(balikPosisi(['A','B','C','D','E']))
print(balikPosisi(['Rakitic', 'Dembele', 'Coutinho', 'Suarez', 'Messi']))