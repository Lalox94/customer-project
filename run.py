from flask import Flask,request
from flask import render_template
from flask import redirect, url_for
import sqlite3 

app = Flask(__name__)


@app.route("/")
def show_menu():    
    sqli_products_1 = get_data_pro()
    sqli_customer_1 = get_data_cus()
    return render_template("index.html",rows1 = sqli_products_1,rows = sqli_customer_1)   
                                                               

@app.route("/hijo")
def test(): 
    
    return render_template("test.html")   

@app.route("/register/<id>",methods=['POST','GET'])
def register(id):
    """
        Inserta 
    """
    if id == Null:
        if request.method == 'POST':
            name = request.form['name']
            descrip = request.form['descrip']
            cant = request.form['cant']
            dictionary ={"name2":name,"descrip2":descrip,"cant2":cant}
            insert(dictionary)
        
        return render_template("view.html")
    else:
        if request.method == 'GET':
            name = request.form['name']
            descrip = request.form['descrip']
            cant = request.form['cant']
            dictionary_u ={"name2":name,"descrip2":descrip,"cant2":cant}
            update_product(dictionary_u,id)            

        return render_template("view.html",date = cant[0])    

@app.route("/register2",methods=['POST','GET'])
def register2():
    """
    """
    if request.method == 'POST':
        name = request.form['name']
        rfc = request.form['rfc']
        city = request.form['city']
        dire = request.form['dire']
        dictionary2 ={"name1":name,"rfc1":rfc,"city1":city,"dire1":dire}
        insert2(dictionary2)
    
    return render_template("view2.html")

def get_data_cus():
    try:
        conn = connection_db()
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("select * from customer")
        rows_customer= c.fetchall()
        return rows_customer
        
    except Exception as e:
        print(e)
    finally:                                                                
        conn.close()


def get_data_pro():
    
    try:
        conn = connection_db()
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("select * from producto")
        rows_products = c.fetchall()
        return rows_products
        
    except Exception as e:
        print(e)
    finally:                                                                
        conn.close()


def insert(dictionary):
    try:
        conn = connection_db()
        c = conn.cursor()
        nombre = dictionary['name2']
        descripcion = dictionary['descrip2']
        cantidad = dictionary['cant2']
        c.execute(f"INSERT INTO producto(nombre,descripcion,cantidad) values ('{nombre}','{descripcion}',{cantidad})")
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
    
    return render_template("view.html")

def insert2(dictionary2):
    try:
        conn = connection_db()
        c = conn.cursor()
        nombre = dictionary2['name1']
        rfc = dictionary2['rfc1']
        ciudad = dictionary2['city1']
        direccion = dictionary2['dire1']
        c.execute(f"INSERT INTO customer(nombre,rfc,ciudad,direccion) values ('{nombre}','{rfc}','{ciudad}','{direccion}')")
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
    
    return render_template("view2.html")

def connection_db():
    conn = sqlite3.connect('sql/producto.db')
    return conn

@app.route('/delete/<id>',methods=['GET', 'POST'])
def delete_product(id):
    try:
        conn = connection_db()
        c = conn.cursor()
        sentencia = "DELETE FROM producto WHERE id = ?;"
        c.execute(sentencia, [id])
        conn.commit()
        print("Se elimino")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        
    return redirect(url_for('show_menu'))


def delete_costomer(idc):    
    try:
        conn = connection_db()
        c = conn.cursor()
        sentencia = "DELETE FROM customer WHERE id = ?;"
        c.execute(sentencia, [idc])
        conn.commit()
        print("Se elimino")    
    except Exception as e:
        print(e)
    finally:
        conn.close()

def update_product(dictionary_u,id):

    try:
        conn = connection_db()
        c = conn.cursor()
        nombre = dictionary['name2']
        descripcion = dictionary['descrip2']
        cantidad = dictionary['cant2']
        sentencia = "UPDATE producto SET nombre = ?, descripcion = ?, cantidad = ? WHERE id = ?;"
        c.execute(sentencia, [nombre, descripcion, cantidad, idt])
        conn.commit()
        print("Datos guardados")
    except Exception as e:
        print(e)
    finally:
        conn.close()

def update_customer():

    try:
        conn = connection_db()
        c = conn.cursor()
        sentencia = "UPDATE customer SET nombre = ?, rfc = ?, ciudad = ? , direccion = ? WHERE id = ?;"
        c.execute(sentencia, [nombre, descripcion, cantidad, idt])
        conn.commit()
        print("Datos guardados")
    except Exception as e:
        print(e)
    finally:
        conn.close()






if __name__ == "__main__":
    app.run()
