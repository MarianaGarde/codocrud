from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

# Crear la app
app = Flask(__name__)

# Usar Cors para dar acceso a las rutas(ebdpoint) desde frontend
CORS(app)

# CONFIGURACIÓN A LA BASE DE DATOS DESDE app
#  (SE LE INFORMA A LA APP DONDE UBICAR LA BASE DE DATOS)
                                                    # //username:password@url/nombre de la base de datos
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/proyecto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# COMUNICAR LA APP CON SQLALCHEMY
db = SQLAlchemy(app)

# PERMITIR LA TRANSFORMACIÓN DE DATOS
ma = Marshmallow(app)

# ESTRUCTURA DE LA TABLA producto A PARTIR DE LA CLASE
class Producto(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self,nombre,precio,stock,imagen):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.imagen = imagen 


# CÓDIGO PARA CREAR LAS TABLAS DEFINIDAS EN LAS CLASES
with app.app_context():
    db.create_all()

# CREAR UNA CLASE  ProductoSchema, DONDE SE DEFINEN LOS CAMPOS DE LA TABLA
class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','stock','imagen')


# DIFERENCIAR CUANDO SE TRANSFORME UN DATO O UNA LISTA DE DATOS
producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)


# CREAR LAS RUTAS PARA: productos
# '/productos' ENDPOINT PARA MOSTRAR TODOS LOS PRODUCTOS DISPONIBLES EN LA BASE DE DATOS: GET
# '/productos' ENDPOINT PARA RECIBIR DATOS: POST
# '/productos/<id>' ENDPOINT PARA MOSTRAR UN PRODUCTO POR ID: GET
# '/productos/<id>' ENDPOINT PARA BORRAR UN PRODUCTO POR ID: DELETE
# '/productos/<id>' ENDPOINT PARA MODIFICAR UN PRODUCTO POR ID: PUT

@app.route("/productos", methods=['GET'])
def get_productos():
                    # select * from producto
    all_productos = Producto.query.all()
    # Almacena un listado de objetos

    return productos_schema.jsonify(all_productos)


@app.route("/productos", methods=['POST'])
def create_productos():
    """
    Entrada de datos:
    {
        "imagen": "https://picsum.photos/200/300?grayscale",
        "nombre": "MICROONDAS",
        "precio": 50000,
        "stock": 10
}
    """
    nombre = request.json['nombre']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']

    new_producto = Producto(nombre, precio, stock, imagen)
    db.session.add(new_producto)
    db.session.commit()

    return producto_schema.jsonify(new_producto)


@app.route("/productos/<id>", methods=['GET'])
def get_producto(id):
    producto = Producto.query.get(id)

    return producto_schema.jsonify(producto)


@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    producto=Producto.query.get(id)
    
    # A partir de db y la sesión establecida con la base de datos borrar 
    # el producto.
    # Se guardan lo cambios con commit
    db.session.delete(producto)
    db.session.commit()

    return producto_schema.jsonify(producto)
    

@app.route('/productos/<id>',methods=['PUT'])
def update_producto(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    producto=Producto.query.get(id)
 
    #  Recibir los datos a modificar
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['stock']
    imagen=request.json['imagen']

    # Del objeto resultante de la consulta modificar los valores  
    producto.nombre=nombre
    producto.precio=precio
    producto.stock=stock
    producto.imagen=imagen
#  Guardar los cambios
    db.session.commit()
# Para ello, usar el objeto producto_schema para que convierta con                     # jsonify el dato recién eliminado que son objetos a JSON  
    return producto_schema.jsonify(producto)



# BLOQUE PRINCIPAL 
if __name__=='__main__':
    app.run(debug=True)