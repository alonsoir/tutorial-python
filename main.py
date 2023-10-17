# This is a sample Python script.
import signal
from IPython.utils import frame
import modulo as m
import pandas as pd
import sqlalchemy
import pandasql as pdsql
import numpy as np
import matplotlib.pyplot as plt


def createInnerJoinSQLFromDF():
    # DataFrames de ejemplo
    data1 = {
        "ID": [1, 2, 3, 4, 5],
        "Nombre": ["Alice", "Bob", "Charlie", "David", "Eva"],
    }
    df1 = pd.DataFrame(data1)

    data2 = {"ID": [2, 4, 6, 8, 10], "Edad": [25, 30, 22, 28, 32]}
    df2 = pd.DataFrame(data2)

    # Realizar un join de los DataFrames en Pandas. Puedes cambiar el valor de how a 'inner', 'left', 'right', o 'outer' según el tipo de join que desees realizar.
    result = pd.merge(df1, df2, on="ID", how="outer")
    print(result)
    result.plot()
    plt.title("outer join...")


def createSQLFromDF():
    df = pd.DataFrame(
        {
            "nombre": ["Santiago", "Pedro", "Ana", "Julia", "Alonso"],
            "edad": [25, 30, 20, 22, 28],
        }
    )

    # Ejecutar consulta SQL
    query = "edad > 25"
    df_sql = df.query(query)

    # Imprimir DataFrame
    print(df_sql)

    # Plotear DataFrame
    df_sql.plot(x="nombre", y="edad", kind="bar")
    df_sql.plot(x="nombre", y="edad", kind="barh")
    df_sql.plot(x="nombre", y="edad", kind="hist")
    df_sql.plot(x="nombre", y="edad", kind="box")
    df_sql.plot(x="nombre", y="edad", kind="kde")
    df_sql.plot(x="nombre", y="edad", kind="density")
    df_sql.plot(x="nombre", y="edad", kind="area")
    df_sql.plot(x="nombre", y="edad", kind="bar")
    plt.title("Gráfico de edades mayores de 25")


def create2DArray():
    x = np.arange(15, dtype=np.int64).reshape(3, 5)
    return x


# Creacion de un objeto Series
def createSeries():
    s = pd.Series([2, 4, 6, 8, 10])
    print(s)
    suma = np.sum(s)
    print(f"suma: {suma}")


# Creación de un objeto Series denominado Temperaturas
def createSeriesTemperature():
    temperaturas = [4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.7, 5.2, 4.7, 4.1, 3.9]
    s = pd.Series(temperaturas, name="Temperaturas")
    s.plot()
    plt.title("Temperaturas")
    plt.show()


# Creación de un objeto Series inicializándolo con un diccionario de Python
def createSeriesWithDict():
    altura = {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}
    s = pd.Series(altura)
    s.plot()
    plt.title("Nombre y Altura")
    print(s)


# Creación de un objeto Series inicializándolo con algunos
# de los elementos de un diccionario de Python
def createSeriesWithSomeElementsFromDict():
    altura = {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}
    s = pd.Series(altura, index=["Pedro", "Julia"])
    s.plot()
    plt.title("Nombre y alturas desde un diccionario")

    print(s)


# Creación de un objeto Series inicializandolo con un escalar
def createSeriesWithScalar():
    s = pd.Series(34, ["test1", "test2", "test3"])
    s.plot()
    plt.title("Una serie a partir de un scalar")

    print(s)


def createDataFrame():
    df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
    )
    return df


# Creación de un DataFrame inicializándolo con un diccionario de objetios Series
def createPersonasDF():
    personas = {
        "peso": pd.Series(
            [84, 90, 56, 64, 115], ["Santiago", "Pedro", "Ana", "Julia", "Alonso"]
        ),
        "altura": pd.Series(
            {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165, "Alonso": 175}
        ),
        "hijos": pd.Series([2, 3], ["Pedro", "Julia"]),
    }

    df = pd.DataFrame(personas)
    plt.title("Personas...")

    df.plot(kind="bar")
    df.plot(kind="barh")
    df.plot(kind="hist")
    df.plot(kind="box")
    df.plot(kind="kde")
    df.plot(kind="density")
    df.plot(kind="area")

    return df


# Guardar el DataFrame como CSV, HTML y JSON
def savePersonasDF(df):
    df.to_csv("df_personas.csv")
    df.to_html("df_personas.html")
    df.to_json("df_personas.json")
    df.to_parquet("df_personas.parquet")
    df.to_xml("df_personas.xml")


# Inicialización del array con valores aleatorios conforme a una distribución normal
def createRandomNormalDistribution():
    np.random.randn(2, 4)
    return np


def createAirQualityPlot():
    air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
    return air_quality


def handler(signum, frame):
    print("Saliendo...")
    exit()


signal.signal(signal.SIGINT, handler)


def showAirQuality():
    air_quality = createAirQualityPlot()
    air_quality.head()
    air_quality.plot()
    air_quality["station_paris"].plot()
    air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
    air_quality.plot.box()
    axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
    plt.title("createAirQualityPlot...")
    plt.show()


def show2DArray():
    x = create2DArray()
    x[1:, ::2] = -99
    print(f"array2D: {x}")
    x.max(axis=1)
    rng = np.random.default_rng()
    samples = rng.normal(size=2500)
    print(samples)


def showPandasDataFrame():
    df = createDataFrame()
    print(df)


def showNormalDistribution():
    global np
    np = createRandomNormalDistribution()
    c = np.random.randn(1000000)
    plt.hist(c, bins=200)
    plt.title("showNormalDistribution...")
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    m.cabecera()
    createInnerJoinSQLFromDF()
    createSQLFromDF()

    df = createPersonasDF()
    print(df)
    savePersonasDF(df)

    createSeries()
    createSeriesWithDict()
    createSeriesWithScalar()
    createSeriesWithSomeElementsFromDict()
    createSeriesTemperature()

    # playing with pandas dataframe and plots.
    showPandasDataFrame()

    showAirQuality()

    show2DArray()

    showNormalDistribution()

    # while True:
    # En vez de cifrar un disco, voy a mostrar la fecha, si pulso q, se acaba la ejecucion.
    m.imprimir_tiempo()
    m.funcion()
    # Comprueba si el usuario ha pulsado una tecla
    #    tecla = input()
    #    if tecla == "q":
    # Simula la pulsación de `Ctrl+C`
    #        signal.default_int_handler(signal.SIGINT, frame)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
