word_counts = {}
document="hola mundoo"
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
#print(word_counts)


# Lista de estudiantes con sus intereses ampliados
students = [
    {"id": 1, "name": "Alice", "interests": ["Python", "Machine Learning"]},
    {"id": 2, "name": "Bob", "interests": ["NLP", "Deep Learning", "Artificial Intelligence"]},
    {"id": 3, "name": "Charlie", "interests": ["Data Visualization", "Python", "Big Data"]},
    {"id": 4, "name": "Diana", "interests": ["Statistics", "Data Science", "Machine Learning"]},
    {"id": 5, "name": "Eve", "interests": ["Data Analysis", "SQL", "Business Intelligence"]},
    {"id": 6, "name": "Frank", "interests": ["Python", "Web Development", "APIs"]},
    {"id": 7, "name": "Grace", "interests": ["Deep Learning", "Computer Vision", "AI"]},
    {"id": 8, "name": "Hank", "interests": ["NLP", "Data Engineering", "Big Data"]},
]

# Lista de recursos con etiquetas ampliados
resources = [
    {"id": 101, "title": "Introduction to Python", "tags": ["Python", "Programming", "Beginner"]},
    {"id": 102, "title": "Deep Learning Basics", "tags": ["Deep Learning", "AI", "Neural Networks"]},
    {"id": 103, "title": "Data Visualization with Python", "tags": ["Data Visualization", "Python", "Plots"]},
    {"id": 104, "title": "Advanced NLP Techniques", "tags": ["NLP", "Machine Learning", "Text Analysis"]},
    {"id": 105, "title": "Statistics for Data Science", "tags": ["Statistics", "Data Science", "Mathematics"]},
    {"id": 106, "title": "SQL for Data Analysis", "tags": ["SQL", "Data Analysis", "Databases"]},
    {"id": 107, "title": "Web Development with Python", "tags": ["Python", "Web Development", "Flask"]},
    {"id": 108, "title": "Building RESTful APIs", "tags": ["APIs", "Web Development", "Programming"]},
    {"id": 109, "title": "Big Data Tools and Techniques", "tags": ["Big Data", "Data Engineering", "Hadoop"]},
    {"id": 110, "title": "Business Intelligence Basics", "tags": ["Business Intelligence", "Data Analysis", "Reports"]},
    {"id": 111, "title": "Computer Vision Fundamentals", "tags": ["Computer Vision", "Deep Learning", "AI"]},
    {"id": 112, "title": "Machine Learning for Beginners", "tags": ["Machine Learning", "Data Science", "AI"]},
]


# Función para recomendar un recurso basado en intereses
def recommend_resource(student, resources):
    for resource in resources:
        if any(interest in resource["tags"] for interest in student["interests"]):
            return resource["title"]  # Retorna el título del recurso
    return "No hay recursos disponibles"  # Si no hay coincidencias

for student in students:
    recommendation = recommend_resource(student, resources)
    #print(f"Recomendación para {student['name']}: {recommendation}")

resultado=[]
for estudinates in students:
    print(estudinates["name"])
    #resultado.clear()
    for recurso in resources:
        if estudinates["interests"][0]==recurso["tags"][0] or estudinates["interests"][0]==recurso["tags"][1]:
           #resultado.append(recurso["title"])
           print(recurso["title"])
        elif estudinates["interests"][1]==recurso["tags"][0] or estudinates["interests"][1]==recurso["tags"][1]:
            #resultado.append(recurso["title"])
            print(recurso["title"])
    #print(resultado)


        


      