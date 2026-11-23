from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal con los dos botones
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el Ejercicio 1: Notas y Asistencia
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    
    if request.method == 'POST':
        # Recogemos los datos del formulario y los convertimos a número
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        
        # Calculamos el promedio
        promedio = round((nota1 + nota2 + nota3) / 3, 1)
        
        # Evaluamos las dos condiciones de aprobación
        if promedio >= 40 and asistencia >= 75:
            estado = 'APROBADO'
        else:
            estado = 'REPROBADO'
            
    return render_template('ejercicio1.html', promedio=promedio, estado=estado)

# Ruta para el Ejercicio 2: Comparación de Nombres
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    cantidad_caracteres = None
    
    if request.method == 'POST':
        # Recogemos los tres nombres
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        
        # Guardamos en una lista y buscamos el de mayor longitud con max()
        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mayor)
        
    return render_template('ejercicio2.html', 
                           nombre_mayor=nombre_mayor, 
                           cantidad_caracteres=cantidad_caracteres)

if __name__ == '__main__':
    app.run(debug=True)