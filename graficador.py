#Permite extraer graficas estadísticas
from tqdm import tqdm
import pandas as pd
import seaborn as sns
import os.path as path
import csv
import matplotlib.pyplot as plt

def graficador1(op, nm, nma, tipo):
    datos = pd.read_csv(op)
    nuevo = datos[["micro_f1", "macro_f1", "weighted_f1"]]
    g = sns.catplot(data=nuevo, kind=tipo)
    g.fig.suptitle(nma)
    g.savefig(nm)

def graficador2(op, nm, nma, tipo):
    sns.set_theme(style="darkgrid")
    datos = pd.read_csv(op)
    nuevo = datos.head()
    g = sns.catplot(data=nuevo, kind=tipo, orient="v", height=4, aspect=2, palette="Set1")
    plt.xticks(rotation=45)
    g.fig.suptitle(nma)
#    g.set(xscale="log")
    g.savefig(nm)

def graficador3(op):
    tabla = [0]
    df = pd.read_csv(op)
    nuevo = df.weighted_f1
    return nuevo

def graf_3_comp(graf_gen1, graf_gen2, graf_gen3, graf_gen4, graf_gen5, op, nma, nm, nomb1, nomb2, nomb3, nomb4, nomb5):
    # Grabar resultados en archivo csv
    if not path.exists(op):
        file = open(op, 'w', encoding='utf-8', newline='')
    else:
        file = open(op, 'w', encoding='utf-8', newline='')
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(
        [nomb1, nomb2, nomb3, nomb4, nomb5])
    # writer.writerow([graf_gen1, graf_gen2, graf_gen3, graf_gen4, graf_gen5, graf_gen6])
    for i in range(0, 30):
        writer.writerow([graf_gen1[i], graf_gen2[i], graf_gen3[i], graf_gen4[i], graf_gen5[i]])
    file.close()
    datos = pd.read_csv(op)
    nuevo = datos.head()
    g = sns.catplot(data=nuevo, kind="box", orient="v", height=5, aspect=2, palette="Set3")
    plt.xticks(rotation=45)
    g.fig.suptitle(nma)
    g.savefig(nm)

###### Programa principal #######
def main() -> None:

# Graficos BOX
    # 1. Grupo de experimentos Corpus gold_reddit_corpus_agree

    # Nombre de archivos
    nma1 = "GRCA_Rasa"
    nma2 = "GRCA_Embedding"
    nma3 = "GRCA_Bow"
    nma4 = "GRCA_Tfidfgs"
    nma5 = "GRCA_Embedding_fidfgs"

    # Archivos csv a leer una vez procesados
    op1 = 'E:/experimentos/res_general/GRCA_rasa.csv'
    op2 = 'E:/experimentos/res_general/GRCA_Emb_general.csv'
    op3 = 'E:/experimentos/res_general/GRCA_BoW_general.csv'
    op4 = 'E:/experimentos/res_general/GRCA_tfi_general.csv'
    op5 = 'E:/experimentos/res_general/GRCA_emb_tfi_general.csv'

    # Nombre de archivos imagen
    nm1 = 'E:/experimentos/imagen/box/GRCA_rasa'
    nm2 = 'E:/experimentos/imagen/box/GRCA_Embedding'
    nm3 = 'E:/experimentos/imagen/box/GRCA_Bow'
    nm4 = 'E:/experimentos/imagen/box/GRCA_Tfidfgs'
    nm5 = 'E:/experimentos/imagen/box/GRCA_Embedding_fidfgs'

    # 2. Grupo de experimentos Corpus Life_Corpus

    # Nombre de archivos
    nma6 = "LC_Rasa"
    nma7 = "LC_Embedding"
    nma8 = "LC_Bow"
    nma9 = "LC_Tfidfgs"
    nma10 = "LC_Embedding_fidfgs"

    # Archivos csv a leer una vez procesados
    op6 = 'E:/experimentos/res_general/LC_rasa.csv'
    op7 = 'E:/experimentos/res_general/LC_Emb_general.csv'
    op8 = 'E:/experimentos/res_general/LC_BoW_general.csv'
    op9 = 'E:/experimentos/res_general/LC_tfi_general.csv'
    op10 = 'E:/experimentos/res_general/LC_emb_tfi_general.csv'

    # Nombre de archivos imagen
    nm6 = 'E:/experimentos/imagen/box/LC_rasa'
    nm7 = 'E:/experimentos/imagen/box/LC_Embedding'
    nm8 = 'E:/experimentos/imagen/box/LC_Bow'
    nm9 = 'E:/experimentos/imagen/box/LC_Tfidfgs'
    nm10 = 'E:/experimentos/imagen/box/LC_Embedding_fidfgs'

    # 3. Grupo de experimentos Corpus reddit_corpus_agree

    # Nombre de archivos
    nma11 = "RCA_Rasa"
    nma12 = "RCA_Embedding"
    nma13 = "RCA_Bow"
    nma14 = "RCA_Tfidfgs"
    nma15 = "RCA_Embedding_fidfgs"

    # Archivos csv a leer una vez procesados
    op11 = 'E:/experimentos/res_general/RCA_rasa.csv'
    op12 = 'E:/experimentos/res_general/RCA_Emb_general.csv'
    op13 = 'E:/experimentos/res_general/RCA_BoW_general.csv'
    op14 = 'E:/experimentos/res_general/RCA_tfi_general.csv'
    op15 = 'E:/experimentos/res_general/RCA_emb_tfi_general.csv'

    # Nombre de archivos imagen
    nm11 = 'E:/experimentos/imagen/box/RCA_rasa'
    nm12 = 'E:/experimentos/imagen/box/RCA_Embedding'
    nm13 = 'E:/experimentos/imagen/box/RCA_Bow'
    nm14 = 'E:/experimentos/imagen/box/RCA_Tfidfgs'
    nm15 = 'E:/experimentos/imagen/box/RCA_Embedding_fidfgs'

    # Funcion 1, genera graficos individuales
    # Tipo de graficos
    # Categorical scatterplots:
    # tipo ="strip"
    # tipo ="swarm"
    # Categorical distribution plots:
    tipo = "box"
    # tipo ="violin"
    # tipo ="boxen"
    # Categorical estimate plots:
    # tipo = "point"
    # tipo = "bar"
    # tipo = "count"

    graficador1(op1, nm1, nma1, tipo)
    graficador1(op2, nm2, nma2, tipo)
    graficador1(op3, nm3, nma3, tipo)
    graficador1(op4, nm4, nma4, tipo)
    graficador1(op5, nm5, nma5, tipo)
    graficador1(op6, nm6, nma6, tipo)
    graficador1(op7, nm7, nma7, tipo)
    graficador1(op8, nm8, nma8, tipo)
    graficador1(op9, nm9, nma9, tipo)
    graficador1(op10, nm10, nma10, tipo)
    graficador1(op11, nm11, nma11, tipo)
    graficador1(op12, nm12, nma12, tipo)
    graficador1(op13, nm13, nma13, tipo)
    graficador1(op14, nm14, nma14, tipo)
    graficador1(op15, nm15, nma15, tipo)

# Graficos Bar

    # 1. Grupo de experimentos Corpus gold_reddit_corpus_agree
    # Nombre de archivos imagen
    nm1 = 'E:/experimentos/imagen/bar/GRCA_rasa'
    nm2 = 'E:/experimentos/imagen/bar/GRCA_Embedding'
    nm3 = 'E:/experimentos/imagen/bar/GRCA_Bow'
    nm4 = 'E:/experimentos/imagen/bar/GRCA_Tfidfgs'
    nm5 = 'E:/experimentos/imagen/bar/GRCA_Embedding_fidfgs'

    # 2. Grupo de experimentos Corpus Life_Corpus
    # Nombre de archivos imagen
    nm6 = 'E:/experimentos/imagen/bar/LC_rasa'
    nm7 = 'E:/experimentos/imagen/bar/LC_Embedding'
    nm8 = 'E:/experimentos/imagen/bar/LC_Bow'
    nm9 = 'E:/experimentos/imagen/bar/LC_Tfidfgs'
    nm10 = 'E:/experimentos/imagen/bar/LC_Embedding_fidfgs'

    # 3. Grupo de experimentos Corpus reddit_corpus_agree
    # Nombre de archivos imagen
    nm11 = 'E:/experimentos/imagen/bar/RCA_rasa'
    nm12 = 'E:/experimentos/imagen/bar/RCA_Embedding'
    nm13 = 'E:/experimentos/imagen/bar/RCA_Bow'
    nm14 = 'E:/experimentos/imagen/bar/RCA_Tfidfgs'
    nm15 = 'E:/experimentos/imagen/bar/RCA_Embedding_fidfgs'

    # Funcion 2 genera graficos generales
    # Tipo de graficos
    #Categorical scatterplots:
    #tipo ="strip"
    #tipo ="swarm"
    #Categorical distribution plots:
    #tipo ="box"
    #tipo ="violin"
    #tipo ="boxen"
    #Categorical estimate plots:
    #tipo = "point"
    tipo = "bar"
    #tipo = "count"

    graficador2(op1, nm1, nma1, tipo)
    graficador2(op2, nm2, nma2, tipo)
    graficador2(op3, nm3, nma3, tipo)
    graficador2(op4, nm4, nma4, tipo)
    graficador2(op5, nm5, nma5, tipo)
    graficador2(op6, nm6, nma6, tipo)
    graficador2(op7, nm7, nma7, tipo)
    graficador2(op8, nm8, nma8, tipo)
    graficador2(op9, nm9, nma9, tipo)
    graficador2(op10, nm10, nma10, tipo)
    graficador2(op11, nm11, nma11, tipo)
    graficador2(op12, nm12, nma12, tipo)
    graficador2(op13, nm13, nma13, tipo)
    graficador2(op14, nm14, nma14, tipo)
    graficador2(op15, nm15, nma15, tipo)

# Graficador 3
# Permite graficar la columna GRCA_Macro_precision del grupo de archivos GRCA

    # 1. Grupo de experimentos Corpus gold_reddit_corpus_agree
    graf_gen1 = graficador3(op1)
    graf_gen2 = graficador3(op2)
    graf_gen3 = graficador3(op3)
    graf_gen4 = graficador3(op4)
    graf_gen5 = graficador3(op5)
    op = "E:/experimentos/res_general/GRCA_mac_prec.csv"
    nma = "GRCA_Macro_precision"
    nm = "E:/experimentos/imagen/mac_pre/GRCA_mac_prec"

    nomb1 = 'GRCA_rasa'
    nomb2 = 'GRCA_Emb_general'
    nomb3 = 'GRCA_BoW_general'
    nomb4 = 'GRCA_tfi_general'
    nomb5 = 'GRCA_emb_tfi_general'

    graf_3_comp(graf_gen1, graf_gen2, graf_gen3, graf_gen4, graf_gen5, op, nma, nm, nomb1, nomb2, nomb3, nomb4, nomb5)

# 2. Grupo de experimentos Corpus Life_Corpus
    graf_gen1 = graficador3(op6)
    graf_gen2 = graficador3(op7)
    graf_gen3 = graficador3(op8)
    graf_gen4 = graficador3(op9)
    graf_gen5 = graficador3(op10)
    op = "E:/experimentos/res_general/LC_mac_prec.csv"
    nma = "LC_Macro_precision"
    nm = "E:/experimentos/imagen/mac_pre/LC_mac_prec"

    nomb1 = 'LC_rasa'
    nomb2 = 'LC_Emb_general'
    nomb3 = 'LC_BoW_general'
    nomb4 = 'LC_tfi_general'
    nomb5 = 'LC_emb_tfi_general'


    graf_3_comp(graf_gen1, graf_gen2, graf_gen3, graf_gen4, graf_gen5, op, nma, nm, nomb1, nomb2, nomb3, nomb4, nomb5)

# 3. Grupo de experimentos Corpus reddit_corpus_agree
    graf_gen1 = graficador3(op11)
    graf_gen2 = graficador3(op12)
    graf_gen3 = graficador3(op13)
    graf_gen4 = graficador3(op14)
    graf_gen5 = graficador3(op15)
    op = "E:/experimentos/res_general/RCA_mac_prec.csv"
    nma = "RCA_Macro_precision"
    nm = "E:/experimentos/imagen/mac_pre/RCA_mac_prec"

    nomb1 = 'RCA_rasa'
    nomb2 = 'RCA_Emb_general'
    nomb3 = 'RCA_BoW_general'
    nomb4 = 'RCA_tfi_general'
    nomb5 = 'RCA_emb_tfi_general'

    graf_3_comp(graf_gen1, graf_gen2, graf_gen3, graf_gen4, graf_gen5, op, nma, nm, nomb1, nomb2, nomb3, nomb4, nomb5)


if __name__ == '__main__':
    main()

