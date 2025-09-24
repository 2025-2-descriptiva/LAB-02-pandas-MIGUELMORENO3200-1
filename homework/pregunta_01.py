"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

df0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
df1 = pd.read_csv("files/input/tbl1.tsv", sep="\t")
df2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    return len(df0)

print(pregunta_01())