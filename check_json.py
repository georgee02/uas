import json

f = open('data/kode_negara_lengkap.json')
data_n = json.load(f)

ins = input("Masukan Nama Negara : ")

for negara in data_n:
    if negara['name'] == ins:
        print(negara['alpha-3'])
