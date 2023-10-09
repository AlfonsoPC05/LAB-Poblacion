import csv
from matplotlib import pyplot as plt
from collections import namedtuple

RegistroPoblacion = namedtuple("RegistroPoblacion", "pais, codigo, año, censo")


def lee_poblaciones(ruta_fichero):
    lista=[]
    with open(ruta_fichero, encoding='utf-8' ) as f:
        lector=csv.reader(f)
        for pais, codigo, año, censo in lector:
            censo=int(censo)
            año=int(año)
            registro_poblacion=RegistroPoblacion(pais, codigo, año, censo)
            lista.append(registro_poblacion)
        return lista 

            
    """
    Lee el fichero de entrada y devuelve una lista de tuplas poblaciones

    @param fichero: nombre del fichero de entrada
    @type fichero: str

    @return: lista de tuplas con la información del fichero
    @rtype: RegistroPoblacion
    """
    


def calcula_paises(poblaciones):
    lista_paises=[]
    
    for i in poblaciones:
        paises=i.pais
        lista_paises.append(paises)
    for _ in lista_paises:
        while lista_paises.count(_)>1:
            lista_paises.remove(_)
    return sorted(lista_paises)
'''
Otra opción es con conjuntos:
def calcula_paises(poblaciones):
    paises=set() #Crea un conjunto vacío, empleamos conjuntos ya que no permite elementos repetidos
    for p in poblaciones:
        paises.add(p.pais)
        ________________________o____________________________
    paises={p.pais for p in poblaciones}
'''


"""
    Calcula la lista de países distintos presentes en una lista de de tuplas de tipo RegistroPoblacion.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)

    @return: lista de paises, ordenada alfabéticamente, sin duplicados
    @rtype: list(str)
    """

def filtra_por_pais(poblaciones, pais_o_codigo):
    lista_pais_censo=[]
   
    for p in poblaciones:
            if p.pais==pais_o_codigo or p.codigo==pais_o_codigo:
                lista_pais_censo.append((p.año, p.censo))
    return lista_pais_censo



        




    """
    Devuelve el año y el censo de las tuplas correspondientes a un determinado pais

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param pais_o_codigo: nombre o código del país del que se seleccionarán los registros
    @type pais_o_codigo: str

    @return: lista de tuplas (año, censo) seleccionadas
    @rtype: list(tuple(int, int))
    """
    


##############################################################################################

##############################################################################################
def filtra_por_paises_y_anyo(poblaciones, año, paises):
    lista_paises_censo=[]
    for p in poblaciones:
        if p.pais in paises and p.año==año:
            lista_paises_censo.append((p.pais, p.censo))
    return lista_paises_censo

    """
    Devuelve el país y el censo de las tuplas correspondientes a un conjunto de paises de un año concreto.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param año: año del que se seleccionarán los registros
    @type año: int
    @param paises: conjunto de nombres de países de los que se seleccionarán los registros
    @type paises: set(str)

    @return: lista de tuplas (pais, censo) seleccionadas
    @rtype: list(tuple(str,int))
    """
    pass


##############################################################################################

###############################################################################################
def muestra_evolucion_poblacion(poblaciones, pais_o_codigo):
    for p in poblaciones:
        if p.pais== pais_o_codigo or p.codigo==pais_o_codigo:
            
    """
    Genera una curva con la evolución de la población de un país. El país puede
    darse como su nombre completo o por su código.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param pais_o_codigo: nombre o código del país del que se generará la gráfica
    @type pais_o_codigo: str
    """
    # TODO Complete la función para asignar los valores correctos
    #  a las variables titulo, lista_años y lista_habitantes
    titulo = ""
    lista_años = []
    lista_habitantes = []

    # Estas instrucciones dibujan la gráfica
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()


###############################################################################################

###############################################################################################
def muestra_comparativa_paises_anyo(poblaciones, año, paises):
    """
    Genera una gráfica de barras en la que se muestra la comparativa de
    la población de varios países en un año concreto

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param año: del que se generará la gráfica
    @type año: int
    @param paises: nombres de los países para los que se generará la gráfica
    @type paises: list(str)
    """
    # TODO Complete la función para asignar los valores correctos
    #  a las variables titulo, lista_paises y lista_habitantes
    titulo = ""
    lista_paises = []
    lista_habitantes = []

    # Estas instrucciones dibujan la gráfica
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
