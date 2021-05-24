# Convertir archivos con formato json a formato csv
# Generar un archivo csv que contenga las medias de todos los archivos
import csv
import os.path as path
import json
import pandas as pd
def conversion(op, nm, ni):
    with open(op, 'rt', encoding='utf-8') as file:
       measures1 = json.load(file)
       grab = [""]
       print(len(measures1))
       sum1 = sum2 = sum3 = sum4 = sum5 = sum6 = sum7 = sum8 = sum9 = sum10 = sum11 = sum12 = sum13 = sum14 = 0
       for a in measures1:
            simple_ac = a.get('simple_accuracy')
            sum1 += simple_ac
            balanc_ac = a.get("balanced_accuracy")
            sum2 += balanc_ac
            micr_f1 = a.get("micro_f1")
            sum3 += micr_f1
            macr_f1 = a.get("macro_f1")
            sum4 += macr_f1
            weigh_f1 = a.get("weighted_f1")
            sum5 += weigh_f1
            micr_pr = a.get("micro_precision")
            sum6 += micr_pr
            macr_pr = a.get("macro_precision")
            sum7 += macr_pr
            weigh_pr = a.get("weighted_precision")
            sum8 += weigh_pr
            micr_rc = a.get("micro_recall")
            sum9 += micr_rc
            macr_rc = a.get("macro_recall")
            sum10 += macr_rc
            weigh_rc = a.get("weighted_recall")
            sum11 += weigh_rc
            micr_jc = a.get("micro_jaccard")
            sum12 += micr_jc
            macr_jc = a.get("macro_jaccard")
            sum13 += macr_jc
            weigh_jc = a.get("weighted_jaccard")
            sum14 += weigh_jc
            grab.append([simple_ac, balanc_ac, micr_f1, macr_f1, weigh_f1, micr_pr, macr_pr, weigh_pr, micr_rc, macr_rc, weigh_rc, micr_jc, macr_jc, weigh_jc])
       file.close()
       med1 = sum1 / 10
       med2 = sum2 / 10
       med3 = sum3 / 10
       med4 = sum4 / 10
       med5 = sum5 / 10
       med6 = sum6 / 10
       med7 = sum7 / 10
       med8 = sum8 / 10
       med9 = sum9 / 10
       med10 = sum10 / 10
       med11 = sum11 / 10
       med12 = sum12 / 10
       med13 = sum13 / 10
       med14 = sum14 / 10

       # Grabar archivos individuales json a csv

       if not path.exists(ni):
           file = open(ni, 'w', encoding='utf-8', newline='')
       else:
           file = open(ni, 'w', encoding='utf-8', newline='')
       writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
       writer.writerow(["simple_accuracy", "balanced_accuracy", "micro_f1", "macro_f1", "weighted_f1", "micro_precision",
                        "macro_precision", "weighted_precision", "micro_recall", "macro_recall", "weighted_recall", "micro_jaccard",
                        "macro_jaccard", "weighted_jaccard"])
       for i in grab:
           writer.writerow(i)
       file.close()

       # Grabar medias de todos los archivos
       if not path.exists(nm):
           file = open(nm, 'w', encoding='utf-8', newline='')
           bb=1
       else:
           bb=2
           file = open(nm, 'a', encoding='utf-8', newline='')
       writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
       if (bb == 1):
           writer.writerow(["simple_accuracy", "balanced_accuracy", "micro_f1", "macro_f1", "weighted_f1",
                        "micro_precision", "macro_precision", "weighted_precision", "micro_recall", "macro_recall",
                        "weighted_recall", "micro_jaccard", "macro_jaccard", "weighted_jaccard"])
       writer.writerow([med1, med2, med3, med4, med5, med6, med7, med8, med9, med10, med11, med12, med13, med14])
       file.close()

####### Bloque principal ##########
def main() -> None:
            ################################
            ### Gold_reddit_corpus_agree ###
            ################################

# 1. Experimentos con BoW
    nm1 = 'E:/experimentos/res_general/GRCA_BoW_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/gold_reddit_corpus_agree/BoW/prueba{i}.json"
        ni = f"E:/experimentos/gold_reddit_corpus_agree/BoW/resultados/BoW{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

# 2. Experimentos con Embeding
    nm1 = 'E:/experimentos/res_general/GRCA_Emb_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/gold_reddit_corpus_agree/emb/emb{i}.json"
        ni = f"E:/experimentos/gold_reddit_corpus_agree/emb/resultados/emb{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

# 3. Experimentos con tfiidf
    nm1 = 'E:/experimentos/res_general/GRCA_tfi_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/gold_reddit_corpus_agree/tfi/tfi{i}.json"
        ni = f"E:/experimentos/gold_reddit_corpus_agree/tfi/resultados/tfi{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

# 4. Experimentos con Embeding - tfiidf
    nm1 = 'E:/experimentos/res_general/GRCA_emb_tfi_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/gold_reddit_corpus_agree/emb_tf/emb_tfi{i}.json"
        ni = f"E:/experimentos/gold_reddit_corpus_agree/emb_tf/resultados/emb_tfi{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

            ################################
            ###        Life Corpus       ###
            ################################

# 1. Experimentos con BoW
    nm1 = 'E:/experimentos/res_general/LC_BoW_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/life_corpus/bow_LC/bow_LC{i}.json"
        ni = f"E:/experimentos/life_corpus/bow_LC/resultados/bow_LC{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

# 2. Experimentos con Embeding
    nm1 = 'E:/experimentos/res_general/LC_Emb_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/life_corpus/emb_LC/emb_LC{i}.json"
        ni = f"E:/experimentos/life_corpus/emb_LC/resultados/emb_LC{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

# 3. Experimentos con tfiidf
    nm1 = 'E:/experimentos/res_general/LC_tfi_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/life_corpus/tfi_LC/tfi_LC{i}.json"
        ni = f"E:/experimentos/life_corpus/tfi_LC/resultados/tfi_LC{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

# 4. Experimentos con Embeding - tfiidf
    nm1 = 'E:/experimentos/res_general/LC_emb_tfi_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/life_corpus/emb_tfi_LC/emb_tfi_LC{i}.json"
        ni = f"E:/experimentos/life_corpus/emb_tfi_LC/resultados/emb_tfi_LC{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

            ################################
            ###    Reddit_corpus_agree   ###
            ################################

# 1. Experimentos con BoW
    nm1 = 'E:/experimentos/res_general/RCA_BoW_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/reddit_corpus_agree/bow_RCA/bow_RCA{i}.json"
        ni = f"E:/experimentos/reddit_corpus_agree/bow_RCA/resultados/bow_RCA{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

# 2. Experimentos con Embeding
    nm1 = 'E:/experimentos/res_general/RCA_Emb_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/reddit_corpus_agree/emb_RCA/emb_RCA{i}.json"
        ni = f"E:/experimentos/reddit_corpus_agree/emb_RCA/resultados/emb_RCA{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

# 3. Experimentos con tfiidf
    nm1 = 'E:/experimentos/res_general/RCA_tfi_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/reddit_corpus_agree/tfi_RCA/tfi_RCA{i}.json"
        ni = f"E:/experimentos/reddit_corpus_agree/tfi_RCA/resultados/tfi_RCA{i}.csv"
        print(i)
        conversion(op1, nm1, ni)

# 4. Experimentos con Embeding - tfiidf
    nm1 = 'E:/experimentos/res_general/RCA_emb_tfi_general.csv'
    for i in range(1, 31):
        op1 = f"E:/experimentos/reddit_corpus_agree/emb_tfi_RCA/emb_tfi_RCA{i}.json"
        ni = f"E:/experimentos/reddit_corpus_agree/emb_tfi_RCA/resultados/emb_tfi_RCA{i}.csv"
        print(i)
        conversion(op1, nm1, ni)



if __name__ == '__main__':
    main()