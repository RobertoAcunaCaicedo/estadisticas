# Permite obtener Medias, varianza, T, significancia
# Combinación de dos conjuntos de datos a la vez
import math
import csv
import os.path as path
import json
from typing import List, Any, Union
import pandas as pd

def lectura_json(op):
    lista=[]
    with open(op, 'rt', encoding='utf-8') as file:
        measures1 = json.load(file)
        rasa = [""]
        reg = len(measures1)
        num_micro_f1 = 0
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
            rasa.append([simple_ac, balanc_ac, micr_f1, macr_f1, weigh_f1, micr_pr, macr_pr, weigh_pr, micr_rc, macr_rc, weigh_rc, micr_jc, macr_jc, weigh_jc])
        file.close
    return rasa

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


def procesos(rasa, tfid, na1, nm1, nm2, inter_v):
    print("intervalo ", inter_v)
    lista = []
    dif = [""]
    sum1 = sum2 = sum3 = sum4 = sum5 = sum6 = sum7 = sum8 = sum9 = sum10 = sum11 = sum12 = sum13 = sum14 = 0
    # Diferencia entre ambas medidas
    for i in range(0, 30):
        dif_simple_ac = (rasa[i][0]) - (tfid[i][0])
        sum1 += dif_simple_ac
        dif_balanc_ac = (rasa[i][1]) - (tfid[i][1])
        sum2 += dif_balanc_ac
        dif_micr_f1 = (rasa[i][2]) - (tfid[i][2])
        sum3 += dif_micr_f1
        dif_macr_f1 = (rasa[i][3]) - (tfid[i][3])
        sum4 += dif_macr_f1
        dif_weigh_f1 = (rasa[i][4]) - (tfid[i][4])
        sum5 += dif_weigh_f1
        dif_micr_pr = (rasa[i][5]) - (tfid[i][5])
        sum6 += dif_micr_pr
        dif_macr_pr = (rasa[i][6]) - (tfid[i][6])
        sum7 += dif_macr_pr
        dif_weigh_pr = (rasa[i][7]) - (tfid[i][7])
        sum8 += dif_weigh_pr
        dif_micr_rc = (rasa[i][8]) - (tfid[i][8])
        sum9 += dif_micr_rc
        dif_macr_rc = (rasa[i][9]) - (tfid[i][9])
        sum10 += dif_macr_rc
        dif_weigh_rc = (rasa[i][10]) - (tfid[i][10])
        sum11 += dif_weigh_rc
        dif_micr_jc = (rasa[i][11]) - (tfid[i][11])
        sum12 += dif_micr_jc
        dif_macr_jc = (rasa[i][12]) - (tfid[i][12])
        sum13 += dif_macr_jc
        dif_weigh_jc = (rasa[i][13]) - (tfid[i][13])
        sum14 += dif_weigh_jc
        dif.append([dif_simple_ac, dif_balanc_ac, dif_micr_f1, dif_macr_f1, dif_weigh_f1, dif_micr_pr, dif_macr_pr,
                    dif_weigh_pr, dif_micr_rc, dif_macr_rc, dif_weigh_rc, dif_micr_jc, dif_macr_jc, dif_weigh_jc])
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

    # Calculo de la Varianza
    var1 = var2 = var3 = var4 = var5 = var6 = var7 = var8 = var9 = var10 = var11 = var12 = var13 = var14 = 0
    for ii in range(1, 31):
        var1 += pow(((dif[ii][0]) - med1), 2)
        var2 += pow(((dif[ii][1]) - med2), 2)
        var3 += pow(((dif[ii][2]) - med3), 2)
        var4 += pow(((dif[ii][3]) - med4), 2)
        var5 += pow(((dif[ii][4]) - med5), 2)
        var6 += pow(((dif[ii][5]) - med6), 2)
        var7 += pow(((dif[ii][6]) - med7), 2)
        var8 += pow(((dif[ii][7]) - med8), 2)
        var9 += pow(((dif[ii][8]) - med9), 2)
        var10 += pow(((dif[ii][9]) - med10), 2)
        var11 += pow(((dif[ii][10]) - med11), 2)
        var12 += pow(((dif[ii][11]) - med12), 2)
        var13 += pow(((dif[ii][12]) - med13), 2)
        var14 += pow(((dif[ii][13]) - med14), 2)
    varianza1 = var1 / (30 - 1)
    varianza2 = var2 / (30 - 1)
    varianza3 = var3 / (30 - 1)
    varianza4 = var4 / (30 - 1)
    varianza5 = var5 / (30 - 1)
    varianza6 = var6 / (30 - 1)
    varianza7 = var7 / (30 - 1)
    varianza8 = var8 / (30 - 1)
    varianza9 = var9 / (30 - 1)
    varianza10 = var10 / (30 - 1)
    varianza11 = var11 / (30 - 1)
    varianza12 = var12 / (30 - 1)
    varianza13 = var13 / (30 - 1)
    varianza14 = var14 / (30 - 1)
    # print(varianza1, varianza2, varianza3, varianza4, varianza5, varianza6, varianza7, varianza8, varianza9, varianza10, varianza11, varianza12, varianza13, varianza14)
    print("Varianza", varianza5)

    # T-student
    tst1 = med1 / math.sqrt((varianza1 / 30))
    tst2 = med2 / math.sqrt((varianza2 / 30))
    tst3 = med3 / math.sqrt((varianza3 / 30))
    tst4 = med4 / math.sqrt((varianza4 / 30))
    tst5 = med5 / math.sqrt((varianza5 / 30))
    tst6 = med6 / math.sqrt((varianza6 / 30))
    tst7 = med7 / math.sqrt((varianza7 / 30))
    tst8 = med8 / math.sqrt((varianza8 / 30))
    tst9 = med9 / math.sqrt((varianza9 / 30))
    tst10 = med10 / math.sqrt((varianza10 / 30))
    tst11 = med11 / math.sqrt((varianza11 / 30))
    tst12 = med12 / math.sqrt((varianza12 / 30))
    tst13 = med13 / math.sqrt((varianza13 / 30))
    tst14 = med14 / math.sqrt((varianza14 / 30))
    # print(tst1, tst2, tst3, tst4, tst5, tst6, tst7, tst8, tst9, tst10, tst11, tst12, tst13, tst14)
    print(tst5)

    # Determinar el grupo al que pertenece el valor mas alto
    # Determinar su significancia estadistica
    if sum1 > 0:
        grupo1 = nm1
        if (tst1 > inter_v):
            estsig1 = "Si"
            lista.append(tst1)
        else:
            estsig1 = "No"
    else:
        grupo1 = nm2
        if ((tst1 * -1) > inter_v):
            estsig1 = "Si"
            lista.append(tst1 * -1)
        else:
            estsig1 = "No"

    if sum2 > 0:
        grupo2 = nm1
        if (tst2 > inter_v):
            estsig2 = "Si"
            lista.append(tst2)
        else:
            estsig2 = "No"
    else:
        grupo2 = nm2
        if ((tst2 * -1) > inter_v):
            estsig2 = "Si"
            lista.append(tst2 * -1)
        else:
            estsig2 = "No"

    if sum3 > 0:
        grupo3 = nm1
        if (tst3 > inter_v):
            estsig3 = "Si"
            lista.append(tst3)
        else:
            estsig3 = "No"
    else:
        grupo3 = nm2
        if ((tst3 * -1) > inter_v):
            estsig3 = "Si"
            lista.append(tst1 * -1)
        else:
            estsig3 = "No"

    if sum4 > 0:
        grupo4 = nm1
        if (tst4 > inter_v):
            estsig4 = "Si"
            lista.append(tst4)
        else:
            estsig4 = "No"
    else:
        grupo4 = nm2
        if ((tst4 * -1) > inter_v):
            estsig4 = "Si"
            lista.append(tst4 * -1)
        else:
            estsig4 = "No"

    if sum5 > 0:
        grupo5 = nm1
        if (tst5 > inter_v):
            estsig5 = "Si"
            lista.append(tst5)
        else:
            estsig5 = "No"
    else:
        grupo5 = nm2
        if ((tst5 * -1) > inter_v):
            estsig5 = "Si"
            lista.append(tst1 * -1)
        else:
            estsig5 = "No"

    if sum6 > 0:
        grupo6 = nm1
        if (tst6 > inter_v):
            estsig6 = "Si"
            lista.append(tst6)
        else:
            estsig6 = "No"
    else:
        grupo6 = nm2
        if ((tst6 * -1) > inter_v):
            estsig6 = "Si"
            lista.append(tst1 * -1)
        else:
            estsig6 = "No"

    if sum7 > 0:
        grupo7 = nm1
        if (tst7 > inter_v):
            estsig7 = "Si"
            lista.append(tst7)
        else:
            estsig7 = "No"
    else:
        grupo7 = nm2
        if ((tst7 * -1) > inter_v):
            estsig7 = "Si"
            lista.append(tst7 * -1)
        else:
            estsig7 = "No"

    if sum8 > 0:
        grupo8 = nm1
        if (tst8 > inter_v):
            estsig8 = "Si"
            lista.append(tst8)
        else:
            estsig8 = "No"
    else:
        grupo8 = nm2
        if ((tst8 * -1) > inter_v):
            estsig8 = "Si"
            lista.append(tst8 * -1)
        else:
            estsig8 = "No"

    if sum9 > 0:
        grupo9 = nm1
        if (tst9 > inter_v):
            estsig9 = "Si"
            lista.append(tst9)
        else:
            estsig9 = "No"
    else:
        grupo9 = nm2
        if ((tst9 * -1) > inter_v):
            estsig9 = "Si"
            lista.append(tst9 * -1)
        else:
            estsig9 = "No"

    if sum10 > 0:
        grupo10 = nm1
        if (tst10 > inter_v):
            estsig10 = "Si"
            lista.append(tst10)
        else:
            estsig10 = "No"
    else:
        grupo10 = nm2
        if ((tst10 * -1) > inter_v):
            estsig10 = "Si"
            lista.append(tst10 * -1)
        else:
            estsig10 = "No"

    if sum11 > 0:
        grupo11 = nm1
        if (tst11 > inter_v):
            estsig11 = "Si"
            lista.append(tst11)
        else:
            estsig11 = "No"
    else:
        grupo11 = nm2
        if ((tst11 * -1) > inter_v):
            estsig11 = "Si"
            lista.append(tst11 * -1)
        else:
            estsig11 = "No"

    if sum12 > 0:
        grupo12 = nm1
        if (tst12 > inter_v):
            estsig12 = "Si"
            lista.append(tst12)
        else:
            estsig12 = "No"
    else:
        grupo12 = nm2
        if ((tst12 * -1) > inter_v):
            estsig12 = "Si"
            lista.append(tst12 * -1)
        else:
            estsig12 = "No"

    if sum13 > 0:
        grupo13 = nm1
        if (tst13 > inter_v):
            estsig13 = "Si"
            lista.append(tst13)
        else:
            estsig13 = "No"
    else:
        grupo13 = nm2
        if ((tst13 * -1) > inter_v):
            estsig13 = "Si"
            lista.append(tst13 * -1)
        else:
            estsig13 = "No"

    if sum14 > 0:
        grupo14 = nm1
        if (tst14 > inter_v):
            estsig14 = "Si"
            lista.append(tst14)
        else:
            estsig14 = "No"
    else:
        grupo14 = nm2
        if ((tst14 * -1) > inter_v):
            estsig14 = "Si"
            lista.append(tst14 * -1)
        else:
            estsig14 = "No"

    print(grupo1)
    print(estsig1)
    print(lista)
    if lista != []:
        mayor = max(lista)
        # Grabar resultados en archivo csv
        if not path.exists(na1):
            file = open(na1, 'w', encoding='utf-8', newline='')
        else:
            file = open(na1, 'a', encoding='utf-8', newline='')
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow([nm1])
        writer.writerow([nm2])
        writer.writerow(
            [" ", "simple_accuracy", "balanced_accuracy", "micro_f1", "macro_f1", "weighted_f1", "micro_precision",
             "macro_precision", "weighted_precision", "micro_recall", "macro_recall", "weighted_recall", "micro_jaccard",
             "macro_jaccard", "weighted_jaccard"
             ])
        writer.writerow(
            ["Medias ", med1, med2, med3, med4, med5, med6, med7, med8, med9, med10, med11, med12, med13, med14])
        writer.writerow(
            ["Varianza ", varianza1, varianza2, varianza3, varianza4, varianza5, varianza6, varianza7, varianza8, varianza9,
             varianza10, varianza11, varianza12, varianza13, varianza14])
        writer.writerow(["T ", tst1, tst2, tst3, tst4, tst5, tst6, tst7, tst8, tst9, tst10, tst11, tst12, tst13, tst14])
        if inter_v == 2.05:
            writer.writerow([f"Valor critico {inter_v}, al 95% de confianza"])
        elif inter_v == 2.46:
            writer.writerow([f"Valor critico {inter_v}, al 98% de confianza"])
        elif inter_v == 2.75:
            writer.writerow([f"Valor critico {inter_v}, al 99% de confianza"])
        writer.writerow(
            ["Significativo ", estsig1, estsig2, estsig3, estsig4, estsig5, estsig6, estsig7, estsig8, estsig9, estsig10,
             estsig11, estsig12, estsig13, estsig14])
        writer.writerow(
            ["Grupo ", grupo1, grupo2, grupo3, grupo4, grupo5, grupo6, grupo7, grupo8, grupo9, grupo10, grupo11,
             grupo12, grupo13, grupo14])
        writer.writerow(["Mayor valor ", mayor])
        file.close()
    else:
        print("lista vacia")

####### Bloque principal ##########
def main() -> None:

# 1. Grupo de experimentos Corpus gold_reddit_corpus_agree
    na1 = 'E:/experimentos/res_general/estadisticas/GRCA_estadistica.csv'
    if path.exists(na1):
       file = open(na1, 'w', encoding='utf-8', newline='')
    else:
        file = open(na1, 'w', encoding='utf-8', newline='')
    file.close()

# Intervalos de confianza
    inter_v1 = 2.05 # al 99% de confianza al 95%
    inter_v2 = 2.46 # al 99% de confianza al 98%
    inter_v3 = 2.75 # al 99% de confianza al 99%

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
    procesos(a_1, a_2, na1, nm1, nm2, inter_v1)
    procesos(a_1, a_2, na1, nm1, nm2, inter_v2)
    procesos(a_1, a_2, na1, nm1, nm2, inter_v3)

    # Rasa - Bow
    procesos(a_1, a_3, na1, nm1, nm3, inter_v1)
    procesos(a_1, a_3, na1, nm1, nm3, inter_v2)
    procesos(a_1, a_3, na1, nm1, nm3, inter_v3)

    # Rasa - Tfidfgs
    procesos(a_1, a_4, na1, nm1, nm4, inter_v1)
    procesos(a_1, a_4, na1, nm1, nm4, inter_v2)
    procesos(a_1, a_4, na1, nm1, nm4, inter_v3)

    # Rasa - Embedding-Tfidfgs
    procesos(a_1, a_5, na1, nm1, nm5, inter_v1)
    procesos(a_1, a_5, na1, nm1, nm5, inter_v2)
    procesos(a_1, a_5, na1, nm1, nm5, inter_v3)

    # Embeding - Bow
    procesos(a_2, a_3, na1, nm2, nm3, inter_v1)
    procesos(a_2, a_3, na1, nm2, nm3, inter_v2)
    procesos(a_2, a_3, na1, nm2, nm3, inter_v3)

    # Embeding - Tfidfgs
    procesos(a_2, a_4, na1, nm2, nm4, inter_v1)
    procesos(a_2, a_4, na1, nm2, nm4, inter_v2)
    procesos(a_2, a_4, na1, nm2, nm4, inter_v3)

    # Embeding - Embedding-Tfidfgs
    procesos(a_2, a_5, na1, nm2, nm5, inter_v1)
    procesos(a_2, a_5, na1, nm2, nm5, inter_v2)
    procesos(a_2, a_5, na1, nm2, nm5, inter_v3)

    # BoW - Tfidfgs
    procesos(a_3, a_4, na1, nm3, nm4, inter_v1)
    procesos(a_3, a_4, na1, nm3, nm4, inter_v2)
    procesos(a_3, a_4, na1, nm3, nm4, inter_v3)

    # BoW - Embedding-Tfidfgs
    procesos(a_3, a_5, na1, nm3, nm5, inter_v1)
    procesos(a_3, a_5, na1, nm3, nm5, inter_v2)
    procesos(a_3, a_5, na1, nm3, nm5, inter_v3)

    # Tfidfgs - Embedding-Tfidfgs
    procesos(a_4, a_5, na1, nm4, nm5, inter_v1)
    procesos(a_4, a_5, na1, nm4, nm5, inter_v2)
    procesos(a_4, a_5, na1, nm4, nm5, inter_v3)

# 2. Grupo de experimentos Corpus Life_Corpus
    na1 = 'E:/experimentos/res_general/estadisticas/LC_estadistica.csv'
    if path.exists(na1):
       file = open(na1, 'w', encoding='utf-8', newline='')
    else:
        file = open(na1, 'w', encoding='utf-8', newline='')
    file.close()

# Intervalos de confianza
    inter_v1 = 2.05 # al 99% de confianza al 95%
    inter_v2 = 2.46 # al 99% de confianza al 98%
    inter_v3 = 2.75 # al 99% de confianza al 99%

# Nombre de archivos
    nm1 = "LC_Rasa"
    nm2 = "LC_Embedding"
    nm3 = "LC_Bow"
    nm4 = "LC_Tfidfgs"
    nm5 = "LC_Embedding_fidfgs"


# Archivos csv a leer una vez procesados
    op1 = 'E:/experimentos/res_general/LC_rasa.csv'
    op2 = 'E:/experimentos/res_general/LC_Emb_general.csv'
    op3 = 'E:/experimentos/res_general/LC_BoW_general.csv'
    op4 = 'E:/experimentos/res_general/LC_tfi_general.csv'
    op5 = 'E:/experimentos/res_general/LC_emb_tfi_general.csv'

# Archivos csv cargados a un lista
    a_1 = lectura_csv(op1)
    a_2 = lectura_csv(op2)
    a_3 = lectura_csv(op3)
    a_4 = lectura_csv(op4)
    a_5 = lectura_csv(op5)

    # Rasa - Embeding
    procesos(a_1, a_2, na1, nm1, nm2, inter_v1)
    procesos(a_1, a_2, na1, nm1, nm2, inter_v2)
    procesos(a_1, a_2, na1, nm1, nm2, inter_v3)

    # Rasa - Bow
    procesos(a_1, a_3, na1, nm1, nm3, inter_v1)
    procesos(a_1, a_3, na1, nm1, nm3, inter_v2)
    procesos(a_1, a_3, na1, nm1, nm3, inter_v3)

    # Rasa - Tfidfgs
    procesos(a_1, a_4, na1, nm1, nm4, inter_v1)
    procesos(a_1, a_4, na1, nm1, nm4, inter_v2)
    procesos(a_1, a_4, na1, nm1, nm4, inter_v3)

    # Rasa - Embedding-Tfidfgs
    procesos(a_1, a_5, na1, nm1, nm5, inter_v1)
    procesos(a_1, a_5, na1, nm1, nm5, inter_v2)
    procesos(a_1, a_5, na1, nm1, nm5, inter_v3)

    # Embeding - Bow
    procesos(a_2, a_3, na1, nm2, nm3, inter_v1)
    procesos(a_2, a_3, na1, nm2, nm3, inter_v2)
    procesos(a_2, a_3, na1, nm2, nm3, inter_v3)

    # Embeding - Tfidfgs
    procesos(a_2, a_4, na1, nm2, nm4, inter_v1)
    procesos(a_2, a_4, na1, nm2, nm4, inter_v2)
    procesos(a_2, a_4, na1, nm2, nm4, inter_v3)

    # Embeding - Embedding-Tfidfgs
    procesos(a_2, a_5, na1, nm2, nm5, inter_v1)
    procesos(a_2, a_5, na1, nm2, nm5, inter_v2)
    procesos(a_2, a_5, na1, nm2, nm5, inter_v3)

    # BoW - Tfidfgs
    procesos(a_3, a_4, na1, nm3, nm4, inter_v1)
    procesos(a_3, a_4, na1, nm3, nm4, inter_v2)
    procesos(a_3, a_4, na1, nm3, nm4, inter_v3)

    # BoW - Embedding-Tfidfgs
    procesos(a_3, a_5, na1, nm3, nm5, inter_v1)
    procesos(a_3, a_5, na1, nm3, nm5, inter_v2)
    procesos(a_3, a_5, na1, nm3, nm5, inter_v3)

    # Tfidfgs - Embedding-Tfidfgs
    procesos(a_4, a_5, na1, nm4, nm5, inter_v1)
    procesos(a_4, a_5, na1, nm4, nm5, inter_v2)
    procesos(a_4, a_5, na1, nm4, nm5, inter_v3)

# 3. Grupo de experimentos Corpus reddit_corpus_agree
    na1 = 'E:/experimentos/res_general/estadisticas/RCA_estadistica.csv'
    if path.exists(na1):
       file = open(na1, 'w', encoding='utf-8', newline='')
    else:
        file = open(na1, 'w', encoding='utf-8', newline='')
    file.close()

# Intervalos de confianza
    inter_v1 = 2.05 # al 99% de confianza al 95%
    inter_v2 = 2.46 # al 99% de confianza al 98%
    inter_v3 = 2.75 # al 99% de confianza al 99%

# Nombre de archivos
    nm1 = "RCA_Rasa"
    nm2 = "RCA_Embedding"
    nm3 = "RCA_Bow"
    nm4 = "RCA_Tfidfgs"
    nm5 = "RCA_Embedding_fidfgs"


# Archivos csv a leer una vez procesados
    op1 = 'E:/experimentos/res_general/RCA_rasa.csv'
    op2 = 'E:/experimentos/res_general/RCA_Emb_general.csv'
    op3 = 'E:/experimentos/res_general/RCA_BoW_general.csv'
    op4 = 'E:/experimentos/res_general/RCA_tfi_general.csv'
    op5 = 'E:/experimentos/res_general/RCA_emb_tfi_general.csv'

# Archivos csv cargados a un lista
    a_1 = lectura_csv(op1)
    a_2 = lectura_csv(op2)
    a_3 = lectura_csv(op3)
    a_4 = lectura_csv(op4)
    a_5 = lectura_csv(op5)

    # Rasa - Embeding
    procesos(a_1, a_2, na1, nm1, nm2, inter_v1)
    procesos(a_1, a_2, na1, nm1, nm2, inter_v2)
    procesos(a_1, a_2, na1, nm1, nm2, inter_v3)

    # Rasa - Bow
    procesos(a_1, a_3, na1, nm1, nm3, inter_v1)
    procesos(a_1, a_3, na1, nm1, nm3, inter_v2)
    procesos(a_1, a_3, na1, nm1, nm3, inter_v3)

    # Rasa - Tfidfgs
    procesos(a_1, a_4, na1, nm1, nm4, inter_v1)
    procesos(a_1, a_4, na1, nm1, nm4, inter_v2)
    procesos(a_1, a_4, na1, nm1, nm4, inter_v3)

    # Rasa - Embedding-Tfidfgs
    procesos(a_1, a_5, na1, nm1, nm5, inter_v1)
    procesos(a_1, a_5, na1, nm1, nm5, inter_v2)
    procesos(a_1, a_5, na1, nm1, nm5, inter_v3)

    # Embeding - Bow
    procesos(a_2, a_3, na1, nm2, nm3, inter_v1)
    procesos(a_2, a_3, na1, nm2, nm3, inter_v2)
    procesos(a_2, a_3, na1, nm2, nm3, inter_v3)

    # Embeding - Tfidfgs
    procesos(a_2, a_4, na1, nm2, nm4, inter_v1)
    procesos(a_2, a_4, na1, nm2, nm4, inter_v2)
    procesos(a_2, a_4, na1, nm2, nm4, inter_v3)

    # Embeding - Embedding-Tfidfgs
    procesos(a_2, a_5, na1, nm2, nm5, inter_v1)
    procesos(a_2, a_5, na1, nm2, nm5, inter_v2)
    procesos(a_2, a_5, na1, nm2, nm5, inter_v3)

    # BoW - Tfidfgs
    procesos(a_3, a_4, na1, nm3, nm4, inter_v1)
    procesos(a_3, a_4, na1, nm3, nm4, inter_v2)
    procesos(a_3, a_4, na1, nm3, nm4, inter_v3)

    # BoW - Embedding-Tfidfgs
    procesos(a_3, a_5, na1, nm3, nm5, inter_v1)
    procesos(a_3, a_5, na1, nm3, nm5, inter_v2)
    procesos(a_3, a_5, na1, nm3, nm5, inter_v3)

    # Tfidfgs - Embedding-Tfidfgs
    procesos(a_4, a_5, na1, nm4, nm5, inter_v1)
    procesos(a_4, a_5, na1, nm4, nm5, inter_v2)
    procesos(a_4, a_5, na1, nm4, nm5, inter_v3)

'''

# Primer grupo de experimentos
    na1 = 'E:/Cursos/Python/Codigo/significancia/csv/estadistica1.csv'
    if path.exists(na1):
       file = open(na1, 'w', encoding='utf-8', newline='')
    file.close()
    op1 = 'E:/Cursos/Python/Codigo/significancia/datos/rasa_golds.json'
    op2 = 'E:/Cursos/Python/Codigo/significancia/datos/tfidfgs.json'
    op3 = 'E:/Cursos/Python/Codigo/significancia/datos/gold_reddit_corpus_agree.json'
    op4 = 'E:/Cursos/Python/Codigo/significancia/datos/rasa_gold_reddit_corpus_agree.json'
    op5 = 'E:/Cursos/Python/Codigo/significancia/datos/rasa_reddit_corpus_agree.json'
    op6 = 'E:/Cursos/Python/Codigo/significancia/datos/reddit_corpus_agree.json'
    #inter_v = 2.05 # al 99% de confianza al 95%
    #inter_v = 2.46 # al 99% de confianza al 98%
    inter_v = 2.75 # al 99% de confianza al 99%

    # Primer grupo de ejercicios
    rasa_golds = lectura_json(op1)
    tfid1 = lectura_json(op2)
    nm1 = "rasa_golds"
    nm2 = "tfidfgs"
    procesos(rasa_golds, tfid1, na1, nm1, nm2, inter_v)

    # Nombre de archivos
    nm3 = 'gold_reddit_corpus_agree'
    nm4 = 'rasa_gold_reddit_corpus_agree'
    nm5 = 'rasa_reddit_corpus_agree'
    nm6 = 'reddit_corpus_agree'

    # Carga de datos
    #gold_reddit = lectura_json(op3)
    #rasa_gold = lectura_json(op4)
    #rasa_reedit = lectura_json(op5)
    #reedit_corpus = lectura_json(op6)

    a_3 = lectura_json(op3)
    b_4 = lectura_json(op4)
    c_5 = lectura_json(op5)
    d_6 = lectura_json(op6)


    #Segundo grupo de ejercicios
    procesos(a_3, b_4, na1, nm3, nm4, inter_v)

    #Tercer grupo de ejercicios
    procesos(a_3, c_5, na1, nm3, nm5, inter_v)

    #Cuarto grupo de ejercicios
    procesos(a_3, d_6, na1, nm3, nm6, inter_v)

    #Quinto grupo de ejercicios
    procesos(b_4, c_5, na1, nm4, nm5, inter_v)

    #Sexto grupo de ejercicios
    procesos(b_4, d_6, na1, nm4, nm6, inter_v)

    #Septimo grupo de ejercicios
    procesos(c_5, d_6, na1, nm5, nm6, inter_v)

'''


if __name__ == '__main__':
    main()
