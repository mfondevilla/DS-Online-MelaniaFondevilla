## ⚙️ Configuración inicial


### 1. Clonar el repositorio
```bash
git clone <https://github.com/mrguezrodriguez/whiteberry>
cd whiteberry
```

### 2. Usuarios de Windows — habilitar scripts de PowerShell
> Solo necesitas hacerlo **una vez** en tu máquina.

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Crear y activar el entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Mantener las dependencias actualizadas

Cada vez que instales un paquete nuevo, ejecuta:

```bash
pip freeze > requirements.txt
```

Y luego haz commit del archivo actualizado. Así tus compañeros podrán sincronizar las dependencias con:

```bash
pip install -r parte2/requirements.txt
```

## 📌 Descripción del proyecto

Este proyecto tiene como objetivo construir una base de datos completa para una tienda de productos informáticos usando **Google Big Query** cmo motor principal de almacenamiento y análisis.
El proyecto abarca desde el diseño del modelo de datos hasta la validación mediante consultas SQL.