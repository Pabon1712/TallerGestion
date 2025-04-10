Clasificación y Clustering de Pokémon: ¿Qué hace a un Pokémon legendario?
Este proyecto es una aplicación web desarrollada con Flask que permite predecir si un Pokémon es legendario o no, a partir de características seleccionadas como estadísticas base y otros atributos relevantes.
El modelo de clasificación se ha entrenado utilizando RandomForestClassifier de scikit-learn, y ha sido guardado en un archivo `.joblib`.

 Google Colab con el modelo de clustering y clasificación
https://colab.research.google.com/drive/1twcOvkJOJkOzDl8bjulkFDOesj8xdYov?usp=sharing

Características del proyecto
- Modelo de clasificación entrenado con RandomForestClassifier (scikit-learn)
- Interfaz web amigable y en español (con Bootstrap)
- Estilo visual en modo oscuro
- Valores predeterminados en los formularios
- Explicación breve de cada característica de entrada
- Implementación y despliegue en contenedores Docker

 Variables utilizadas
Las siguientes variables del Pokémon fueron seleccionadas como features importantes y son utilizadas como entrada para el modelo:

Variable              | Descripción
----------------------|-----------------------------------------
HP                   | Puntos de salud
Attack               | Poder de ataque
Defense              | Poder de defensa
Sp_Atk               | Ataque especial
Sp_Def               | Defensa especial
Speed                | Velocidad
Generation           | Generación del Pokémon
has_mega_evolution   | Tiene mega evolución (1 o 0)

 Cómo ejecutar el proyecto
1. Clona el repositorio
git clone https://github.com/tu_usuario/clasificador-pokemon.git
cd clasificador-pokemon

2. Levanta el entorno con Docker
docker-compose up --build

 Autores
Nombres: Santiago Adalberto Pabon Alvear

Brandon Eduardo Tobar Sanchez

Jaime Andres Cardona Montero

# TallerGestion
