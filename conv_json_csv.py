# Convertir archivos con formato json a formato csv
# Generar un archivo csv que contenga las medias de todos los archivos
import csv
import os.path as path
import json
import pandas as pd

def conversion(op, nm, nma):
    with open(op, 'rt', encoding='utf-8') as file:
       measures1 = json.load(file)
       grab = [""]
       print(len(measures1))
       for a in measures1:
            simple_ac = a.get('simple_accuracy')
            balanc_ac = a.get("balanced_accuracy")
            micr_f1 = a.get("micro_f1")
            macr_f1 = a.get("macro_f1")
            weigh_f1 = a.get("weighted_f1")
            micr_pr = a.get("micro_precision")
            macr_pr = a.get("macro_precision")
            weigh_pr = a.get("weighted_precision")
            micr_rc = a.get("micro_recall")
            macr_rc = a.get("macro_recall")
            weigh_rc = a.get("weighted_recall")
            micr_jc = a.get("micro_jaccard")
            macr_jc = a.get("macro_jaccard")
            weigh_jc = a.get("weighted_jaccard")
            grab.append([simple_ac, balanc_ac, micr_f1, macr_f1, weigh_f1, micr_pr, macr_pr, weigh_pr, micr_rc, macr_rc, weigh_rc, micr_jc, macr_jc, weigh_jc])
       file.close()

       # Grabar archivos individuales json a csv
       if not path.exists(nm):
           file = open(nm, 'w', encoding='utf-8', newline='')
       else:
           file = open(nm, 'w', encoding='utf-8', newline='')
       writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
       writer.writerow(["simple_accuracy", "balanced_accuracy", "micro_f1", "macro_f1", "weighted_f1", "micro_precision", "macro_precision", "weighted_precision", "micro_recall", "macro_recall", "weighted_recall", "micro_jaccard", "macro_jaccard", "weighted_jaccard"
    ])
       for i in grab:
           writer.writerow(i)
       file.close()

####### Bloque principal ##########

def main() -> None:
    op1 = "E:/experimentos/rasa/rasa_RCA.json"
    nm1 = 'E:/experimentos/rasa/RCA_rasa.csv'
    nma1 = 'LC_rasa'
    conversion(op1, nm1, nma1)

if __name__ == '__main__':
    main()


