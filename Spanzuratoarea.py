
f1 = open("cuvinte_de_verificat.txt")
f2 = open("litere.txt")
litere = f2.readline().split(' ')
id_student = 1
id_joc = 2
cuvant = "telefon"
pattern = "******n"
incercari = 0
def unde_se_potriveste_litera(id_student, id_joc, litera):
    pozitii = []
    for i in range(0, len(cuvant)):
        if(litera == cuvant[i]):
            pozitii.append(i)
    return pozitii

def verifica_cuvantul(id_student, id_joc, cuvant_format):
    if(cuvant_format == cuvant):
        return 1
    return 0

x = 0
while(x < len(litere)):
    l = []
    l = unde_se_potriveste_litera(1, 2, litere[x])
    incercari += 1
    for i in l:
        pattern = pattern[:i] + litere[x] + pattern[i + 1:]
    x += 1
    if(verifica_cuvantul(1, 2, pattern) == 1):
        break
print("cuvantul:",cuvant)
print("incercari:",incercari)
