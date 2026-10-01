from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "willbookstore-clave-de-desarrollo"

# Catálogo de ejemplo para la página de Inicio
LIBROS_DESTACADOS = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "genero": "Novela"},
    {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "genero": "Clásicos"},
    {"titulo": "Hábitos atómicos", "autor": "James Clear", "genero": "Desarrollo personal"},
    {"titulo": "Sapiens", "autor": "Yuval Noah Harari", "genero": "Historia"},
]

# Servicios de la librería
SERVICIOS = [
    {"nombre": "Venta de libros nuevos",
     "detalle": "Novedades y títulos de catálogo en novela, ensayo, ciencia, infantil y juvenil."},
    {"nombre": "Libros usados",
     "detalle": "Ediciones de segunda mano revisadas, a mejor precio y con una nueva vida en tu estantería."},
    {"nombre": "Pedidos por encargo",
     "detalle": "Si el libro que buscas no está en tienda, lo pedimos por ti y te avisamos cuando llegue."},
    {"nombre": "Club de lectura",
     "detalle": "Un encuentro mensual para leer y conversar sobre un libro elegido entre todos."},
    {"nombre": "Papelería y útiles",
     "detalle": "Cuadernos, marcapáginas y lo necesario para estudiar o escribir."},
    {"nombre": "Regalos y empaque",
     "detalle": "Te ayudamos a escoger un libro para regalar y lo dejamos empacado."},
]


@app.route("/")
def index():
    return render_template("index.html", libros=LIBROS_DESTACADOS)


@app.route("/servicios")
def servicios():
    return render_template("servicios.html", servicios=SERVICIOS)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        if nombre:
            flash(f"Gracias, {nombre}. Recibimos tu mensaje y te responderemos pronto.")
        return redirect(url_for("contacto"))
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)
