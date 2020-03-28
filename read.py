#coding = utf-8
import json

def ler_json():
    with open(caminho_arquivo ,'r',encoding='utf8') as f:
        return json.load(f)

# leitura do arquivo versions.json
caminho_arquivo = 'versions.json'
version_file = ler_json()

# leitura do arquivo package.json
caminho_arquivo = 'package.json'
package_file = ler_json()
package_version = (package_file['version'])
package_version = package_version.split('.')

if str(version_file['registration'][2]) == package_version[2]:
    print('Versoes iguais.')
else:
    version_file['registration'][2] = int(package_version[2])
    arquivo_version = open('versions.json', 'w', encoding='utf8')
    json.dump(version_file, arquivo_version)
    arquivo_version.close()
    print('Versao atualizada.')