from urllib.request import urlopen
import xml.etree.ElementTree as ET
import json
import bank_list

def parse_bank():
    for i in bank_list.bank_list:
        root = ET.parse(urlopen(f'https://www.{i}.ru/For_CBRF/Deposits.xml')).getroot()
        bank_list_json = {
            'date': root.attrib['DocDate'],
            'name': root[0].attrib['Name']
        }
        for n, currence in enumerate(['rub', 'usd', 'eur']) :
            bank_list_json[currence] = {
                'CallDep': root[0][n][0].text,
                'Dep90': root[0][n][1].text,
                'Dep91-180': root[0][n][2].text,
                'Dep181-1': root[0][n][3].text,
                'Dep1up': root[0][n][4].text
            }

        with open('parse_bank.json', 'a') as write_file:
            json.dump(bank_list_json, write_file, ensure_ascii=False)
            write_file.write('\n')
#open('parse_bank.json', 'w')

parse_bank()
parse_bank_json.truncate()
'''
        'rub': {
            'CallDep': root[0][0][0].text,
            'Dep90': root[0][0][1].text,
            'Dep91-180': root[0][0][2].text,
            'Dep181-1': root[0][0][3].text,
            'Dep1up': root[0][0][4].text
        },
        'usd': {
            'CallDep': root[0][1][0].text,
            'Dep90': root[0][1][1].text,
            'Dep91-180': root[0][1][2].text,
            'Dep181-1': root[0][1][3].text,
            'Dep1up': root[0][1][4].text
        },
        'eur': {
            'CallDep': root[0][2][0].text,
            'Dep90': root[0][2][1].text,
            'Dep91-180': root[0][2][2].text,
            'Dep181-1': root[0][2][3].text,
            'Dep1up': root[0][2][4].text
        },
    }'''