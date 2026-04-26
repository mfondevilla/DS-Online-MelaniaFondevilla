# Team Challenge SQL
## 🧭 Introducción
Este repositorio reúne dos ejercicios independientes con el fin de consolidar habilidades técnicas en consulta y creación de bases de datos:

## 🗂️ Estructura del Repositorio


```

tc-sql/
├── parte1/
│   └── sql_murder_mystery.ipynb
├── parte2/
│   ├── bigquery_setup.ipynb
│   ├── docs/
│   │   └── er_diagram.png          ← diagrama ER (a completar)
│   └── requirements.txt
├── .env.example                    ← plantilla de variables de entorno
├── .gitignore
└── README.md
```

# Parte 1: 🔍 SQL Murder Mystery
## 📌 Descripción del ejercicio

En esta primera parte del TC se propone un ejercicio para practicar consultas SQL mediante la resolución de un juego planteado en la página: [SQL Murder Mystery](https://mystery.knightlab.com/)
En el directorio correspondiente se incluye la explicación del proceso seguido, las deducciones realizadas y la solución final del caso.

# Parte 2:🛢️ Diseño e implementación de base de datos en BigQuery

## 📌 Descripción del proyecto

Este proyecto tiene como objetivo construir una base de datos completa para una tienda de productos informáticos usando **Google Big Query** cmo motor principal de almacenamiento y análisis.
El proyecto abarca desde el diseño del modelo de datos hasta la validación mediante consultas SQL.


## 🎯 Objetivos Principales

- Diseñar un modelo ER 
- Crear las tablas en Google BigQuery siguiendo buenas prácticas de normalización.
- Cargar datos de ejemplo (CSV, JSON o datasets generados).
- Validar la estructura y calidad de los datos mediante consultas SQL.
- Realizar consultas analíticas de verificación

---



## 🧩 Modelo de Datos
Se puede consultar el modelo de datos en el directorio docs de la parte2, tanto su descripción como su visualización generada con [dbdiagram.io](https://dbdiagram.io/home)


## ☁️ Configuración de Google BigQuery


## ⚙️ Setup

### 1. Clonar el repositorio
```bash
git clone https://github.com/[usuario]/tc-sql.git
cd tc-sql
```

### 2. Crear el entorno virtual
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows
```

### 3. Instalar dependencias
```bash
pip install -r parte2/requirements.txt
```

### 4. Configurar credenciales
```bash
cp .env.example .env
# Editar .env con vuestros valores reales
```

El fichero `.env` **nunca se sube al repositorio**.

### 5. Credenciales de Google Cloud

Dos opciones:
- **Service Account**: descargad el JSON desde IAM → Service Accounts y apuntad la ruta en `GOOGLE_APPLICATION_CREDENTIALS`
- **Application Default Credentials**: `gcloud auth application-default login`

---

## 👥 Equipo

| Nombre | Rol | 
|--------|-----|
| María Rodriguez | Scrum Master | 
| William Walker | Data Modeler | 
| Paula Comas | Data Engineer 1 | 
| Ana Corrochano | Data Engineer 1 | 
| Melania Fondevilla | QA / Docs | 

---

## Presentación — Sprint 8

- Duración total: **10 minutos** (ambas partes)
- Lugar: sesión Team Challenge Sprint 8
