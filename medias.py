# Permite obtener Medias
import math
import csv
import os.path as path
import json
from typing import List, Any, Union
import pandas as pd

def lectura_csv(op):
    lista=[]
    rasa = []
    with open(op, 'rt', encoding='utf-8', newline='') as file:
        lineas = file.read().splitlines()  # Leer el archivo linea por linea
        lineas.pop(0)  # No se toma encuenta la primera linea por lo general la de titulo
        for l in lineas:
            linea = l.split(',')
            rasa.append([float(linea[0]), float(linea[1]), float(linea[2]), float(linea[3]), float(linea[4]),
                         float(linea[5]), float(linea[6]), float(linea[7]), float(linea[8]), float(linea[9]),
                         float(linea[10]), float(linea[11]), float(linea[12]), float(linea[13])])
        file.close
    return rasa


def procesos(rasa, na1, nm):
    lista = []
    dif = [""]
    sum1 = sum2 = sum3 = sum4 = sum5 = sum6 = sum7 = sum8 = sum9 = sum10 = sum11 = sum12 = sum13 = sum14 = 0
    # Diferencia entre ambas medidas
    for i in range(0, 30):
        sum1 += (rasa[i][0])
        sum2 += (rasa[i][1])
        sum3 += (rasa[i][2])
        sum4 += (rasa[i][3])
        sum5 += (rasa[i][4])
        sum6 += (rasa[i][5])
        sum7 += (rasa[i][6])
        sum8 += (rasa[i][7])
        sum9 += (rasa[i][8])
        sum10 += (rasa[i][9])
        sum11 += (rasa[i][10])
        sum12 += (rasa[i][11])
        sum13 += (rasa[i][12])
        sum14 += (rasa[i][13])
    # Calculo de la media
    med1 = sum1 / 30;
    med2 = sum2 / 30;
    med3 = sum3 / 30;
    med4 = sum4 / 30;
    med5 = sum5 / 30;
    med6 = sum6 / 30;
    med7 = sum7 / 30
    med8 = sum8 / 30;
    med9 = sum9 / 30;
    med10 = sum10 / 30;
    med11 = sum11 / 30;
    med12 = sum12 / 30;
    med13 = sum13 / 30;
    med14 = sum14 / 30
    # print(med1, med2, med3, med4, med5, med6, med7, med8, med9, med10, med11, med12, med13, med14)
    print("media", med5)
    # Grabar resultados en archivo csv
    if not path.exists(na1):
        file = open(na1, 'w', encoding='utf-8', newline='')
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            [" ", "simple_accuracy", "balanced_accuracy", "micro_f1", "macro_f1", "weighted_f1", "micro_precision",
             "macro_precision", "weighted_precision", "micro_recall", "macro_recall", "weighted_recall", "micro_jaccard",
             "macro_jaccard", "weighted_jaccard"
             ])
        writer.writerow([nm, med1, med2, med3, med4, med5, med6, med7, med8, med9, med10, med11, med12, med13, med14])
    else:
        file = open(na1, 'a', encoding='utf-8', newline='')
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow([nm, med1, med2, med3, med4, med5, med6, med7, med8, med9, med10, med11, med12, med13, med14])
    file.close()

####### Bloque principal ##########
def main() -> None:

    na = 'E:/experimentos/res_general/estadisticas/medias.csv'

# 1. Grupo de experimentos Corpus gold_reddit_corpus_agree

# Nombre de archivos
    nm1 = "GRCA_Rasa"
    nm2 = "GRCA_Embedding"
    nm3 = "GRCA_Bow"
    nm4 = "GRCA_Tfidfgs"
    nm5 = "GRCA_Embedding_fidfgs"

# Archivos csv a leer una vez procesados
    op1 = 'E:/experimentos/res_general/GRCA_rasa.csv'
    op2 = 'E:/experimentos/res_general/GRCA_Emb_general.csv'
    op3 = 'E:/experimentos/res_general/GRCA_BoW_general.csv'
    op4 = 'E:/experimentos/res_general/GRCA_tfi_general.csv'
    op5 = 'E:/experimentos/res_general/GRCA_emb_tfi_general.csv'

# Archivos csv cargados a un lista
    a_1 = lectura_csv(op1)
    a_2 = lectura_csv(op2)
    a_3 = lectura_csv(op3)
    a_4 = lectura_csv(op4)
    a_5 = lectura_csv(op5)

    # Rasa - Embeding
    procesos(a_1, na, nm1)
    procesos(a_2, na, nm2)
    procesos(a_3, na, nm3)
    procesos(a_4, na, nm4)
    procesos(a_5, na, nm5)

# 2. Grupo de experimentos Corpus Life_Corpus

# Nombre de archivos
    nm6 = "LC_Rasa"
    nm7 = "LC_Embedding"
    nm8 = "LC_Bow"
    nm9 = "LC_Tfidfgs"
    nm10 = "LC_Embedding_fidfgs"

# Archivos csv a leer una vez procesados
    op6 = 'E:/experimentos/res_general/LC_rasa.csv'
    op7 = 'E:/experimentos/res_general/LC_Emb_general.csv'
    op8 = 'E:/experimentos/res_general/LC_BoW_general.csv'
    op9 = 'E:/experimentos/res_general/LC_tfi_general.csv'
    op10 = 'E:/experimentos/res_general/LC_emb_tfi_general.csv'

# Archivos csv cargados a un lista
    a_6 = lectura_csv(op6)
    a_7 = lectura_csv(op7)
    a_8 = lectura_csv(op8)
    a_9 = lectura_csv(op9)
    a_10 = lectura_csv(op10)

    # Rasa - Embeding
    procesos(a_6, na, nm6)
    procesos(a_7, na, nm7)
    procesos(a_8, na, nm8)
    procesos(a_9, na, nm9)
    procesos(a_10, na, nm10)

# 3. Grupo de experimentos Corpus reddit_corpus_agree

# Nombre de archivos
    nm11 = "RCA_Rasa"
    nm12 = "RCA_Embedding"
    nm13 = "RCA_Bow"
    nm14 = "RCA_Tfidfgs"
    nm15 = "RCA_Embedding_fidfgs"


# Archivos csv a leer una vez procesados
    op11 = 'E:/experimentos/res_general/RCA_rasa.csv'
    op12 = 'E:/experimentos/res_general/RCA_Emb_general.csv'
    op13 = 'E:/experimentos/res_general/RCA_BoW_general.csv'
    op14 = 'E:/experimentos/res_general/RCA_tfi_general.csv'
    op15 = 'E:/experimentos/res_general/RCA_emb_tfi_general.csv'

# Archivos csv cargados a un lista
    a_11 = lectura_csv(op11)
    a_12 = lectura_csv(op12)
    a_13 = lectura_csv(op13)
    a_14 = lectura_csv(op14)
    a_15 = lectura_csv(op15)

    # Rasa - Embeding
    procesos(a_11, na, nm11)
    procesos(a_12, na, nm12)
    procesos(a_13, na, nm13)
    procesos(a_14, na, nm14)
    procesos(a_15, na, nm15)

if __name__ == '__main__':
    main()
