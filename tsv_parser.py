#!/usr/bin/python

# MIT License
# author: David Romic <davidromic@gmail.com>
# a shitty TSV parser for Elektrijada 2017.
# I suck at python
# TODO: handle multiples better, respect conventions

import sys, csv

disciplines = [
        'Analiza elektroenergetskih sustava',
        'Automatika',
        'Električni strojevi',
        'Elektronika 1',
        'Elektronika 2',
        'Engleski jezik',
        'Fizika',
        'Informatika',
        'Košarka - muški tim',
        'Košarka - ženski tim',
        'Kros',
        'Mali nogomet - muški tim',
        'Mali nogomet - ženski tim',
        'Matematika 1',
        'Matematika 2',
        'Objektno orijentirano programiranje',
        'Obnovljivi izvori energije',
        'Odbojka - muški tim',
        'Odbojka - ženski tim',
        'Osnove elektrotehnike',
        'Rukomet - muški tim',
        'Rukomet - ženski tim',
        'Šah',
        'Stolni tenis - muški tim',
        'Stolni tenis - ženski tim',
        'Telekomunikacije',
        'Teorija električnih krugova',
        'Veslanje'
        ]


html_row = '<div class="row" style="font-size:14px">'

html = """   	<div class="col-sm-4"><img alt="" height="267" src="/images/50018703/DominikSekrst.png" width="200" />
        <h6><strong>{}</strong> - {}</h6>
        <p><strong>Ja sam momak na lošem glasu u ovom gradu, a tko si ti?</strong><br /> {}</p>
        <p><strong>Ima li nade za nas?</strong><br /> {}</p>
        <p><strong>Kako ću joj reć' da varin?</strong><br /> {}</p>
    </div>"""

multiples = []


def main():
    with open('elektrijada.tsv', 'r') as tsvf, open('output.html', 'w') as html_file:
        tsv = csv.reader(tsvf, delimiter='\t')

        iterdisc = iter(disciplines)
        current_discipline = next(iterdisc)

        itertsv = iter(tsv)
        next(itertsv)

        html_file.write("<!--" + current_discipline + "-->\n")
        html_file.write(html_row + '\n')

        for row in itertsv:
            print(current_discipline, row[1])
            if ',' in row[4]:
                entry = list(row)
                entry[4] = row[4].split(',')[1]
                multiples.append(entry)
            if current_discipline in row[4]:
                html_file.write(html.format(row[1], row[5], row[6], row[7], row[8]) + '\n')
            else:
                html_file.write('</div>' + '\n\n\n\n')
                html_file.write("<!--" + current_discipline + "-->\n")
                html_file.write(html_row + '\n')
                current_discipline = next(iterdisc)
                html_file.write(html.format(row[1], row[5], row[6], row[7], row[8]) + '\n')

        html_file.write('</div>' + '\n\n\n\n')

        # multiple disciplines
        html_file.write("<!--" + "Multiple disciplines" + "-->\n")
        html_file.write(html_row + '\n')

        for row in multiples:
            html_file.write(html.format(row[1], row[5], row[6], row[7], row[8]) + '\n')
            # print(i[1] + ' ' + i[4])
        html_file.write('</div>' + '\n\n\n\n')



if __name__ == '__main__':
    main()

