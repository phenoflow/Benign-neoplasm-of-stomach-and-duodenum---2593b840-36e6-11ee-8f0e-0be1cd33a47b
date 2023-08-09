# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"B711000","system":"readv2"},{"code":"B711100","system":"readv2"},{"code":"B711200","system":"readv2"},{"code":"B711300","system":"readv2"},{"code":"B711400","system":"readv2"},{"code":"B711z00","system":"readv2"},{"code":"B712100","system":"readv2"},{"code":"B712200","system":"readv2"},{"code":"14949.0","system":"med"},{"code":"15203.0","system":"med"},{"code":"19143.0","system":"med"},{"code":"2151.0","system":"med"},{"code":"25671.0","system":"med"},{"code":"31943.0","system":"med"},{"code":"41334.0","system":"med"},{"code":"43341.0","system":"med"},{"code":"48001.0","system":"med"},{"code":"51733.0","system":"med"},{"code":"52425.0","system":"med"},{"code":"54667.0","system":"med"},{"code":"57870.0","system":"med"},{"code":"62625.0","system":"med"},{"code":"62798.0","system":"med"},{"code":"70275.0","system":"med"},{"code":"70651.0","system":"med"},{"code":"70965.0","system":"med"},{"code":"95911.0","system":"med"},{"code":"9930.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benign-neoplasm-of-stomach-and-duodenum-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benign-neoplasm-of-stomach-and-duodenum---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benign-neoplasm-of-stomach-and-duodenum---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benign-neoplasm-of-stomach-and-duodenum---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
