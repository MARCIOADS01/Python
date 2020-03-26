import json
import re
def ler_json():
    with open(caminho_arquivo ,'r',encoding='utf8') as f:
        return json.load(f)

# leitura do arquivo versions.json
caminho_arquivo = 'versions.json'
data1 = ler_json()
versao1 = (data1['registration'])
#print(data1)
versao1 = re.sub('[^0-9]', '', str(versao1))
print("versao arq1 = " + versao1)

# leitura do arquivo package.json
caminho_arquivo = 'package.json'
data2 = ler_json()
versao2 = (data2['version'])
#print(data2)
versao2 = re.sub('[^0-9]', '', str(versao2))
print("versao arq2 = " + versao2)

# realizando o procedimento de comparação entre as versoes dos documentos
if versao1 == versao2:
    print("os arquivos tem mesma versao")
elif versao1 != versao2:
    igual = False

print("os arquivos tem versao diferente")
