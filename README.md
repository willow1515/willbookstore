# Willbookstore

Prototipo web modular de una librería, desarrollado con **Flask** y plantillas **Jinja2**.
Actividad de *Fundamentos de programación web* (UNIMINUTO).

**Autor:** William Alexander Ramírez Torres

## Características

- Tres páginas: **Inicio**, **Servicios** y **Contacto**.
- Plantilla base (`base.html`) con los bloques `{% block title %}` y `{% block content %}`.
- Todas las páginas usan `{% extends "base.html" %}`.
- Secciones reutilizables incluidas con `{% include %}`: `header.html`, `navbar.html` y `footer.html`.
- Estilos propios en `static/css/estilos.css` (diseño minimalista en café claro, blanco y gris).

## Estructura del proyecto

```
willbookstore/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── servicios.html
│   ├── contacto.html
│   └── includes/
│       ├── header.html
│       ├── navbar.html
│       └── footer.html
└── static/
    └── css/
        └── estilos.css
```

## Requisitos

- Python 3.9 o superior
- pip

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/TU_USUARIO/willbookstore.git
   cd willbookstore
   ```

2. Crear y activar un entorno virtual:

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

```bash
python app.py
```

Abrir en el navegador: <http://127.0.0.1:5000>

## Rutas

| Ruta         | Página    |
|--------------|-----------|
| `/`          | Inicio    |
| `/servicios` | Servicios |
| `/contacto`  | Contacto  |

## Referencias

- Adictos al trabajo. (2024). *Diseño y renderizado de páginas HTML en Python con Flask: guía completa.*
- Pinto Demera, L. N., & Morejón López, G. E. (2025). *FLASK: El microframework para el desarrollo rápido de aplicaciones con Python.* Revista Social Fronteriza, 5(1), e597.
- LabEx. (2025). *Generando plantillas dinámicas y seguras con Jinja2.*
