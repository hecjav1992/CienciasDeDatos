'''Salarios y experiencia
Justo cuando se iba a comer, el vicepresidente de Relaciones Públicas le
pregunta si le puede suministrar datos curiosos sobre lo que ganan los
científicos de datos. Los datos de sueldos son, por supuesto, confidenciales,
pero se las arregla para conseguir un conjunto de datos anónimo que contiene
el salario (salary) de cada usuario (en dólares) y su antigüedad en el puesto
(tenure) como científico de datos (en años):'''

from matplotlib import pyplot as mp
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),
(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]


salaries=[]
tenuaries=[]
for i,j in salaries_and_tenures:
    print(j)
    salaries.append(i)
    tenuaries.append(j)
fig, ax = mp.subplots()
ax.scatter(tenuaries,salaries)
mp.show()

from collections import defaultdict

diciono=defaultdict(list)
for i,j in salaries_and_tenures:
    diciono[j].append(i)
print(diciono)

average_salary_by_tenure = {
tenure: sum(salaries) / len(salaries)
for tenure, salaries in diciono.items()
}

print(average_salary_by_tenure)

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

 
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Las claves son buckets de años de antigüedad, los valores son el salario
average_salary_by_bucket = {
tenure_bucket: sum(salaries) / len(salaries)
for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

print(average_salary_by_bucket)
