from flask import Flask, request, render_template, redirect, url_for
import pymysql

connection = pymysql.connect(
    host = "localhost", 
    user = "root", 
    password = "", 
    database = "myprojectwork")
cursor = connection.cursor()

app = Flask(__name__)

@app.route("/")
def prenotazioni():
    cursor.execute("SELECT * FROM clienti")
    rows = cursor.fetchall()   
    return render_template('index.html', prenotazioni = rows)

@app.route("/update/<int:IDprenotazione>", methods=["POST"])
def update(IDprenotazione): 
    cursor.execute("SELECT * FROM clienti WHERE IDprenotazione = %s", (IDprenotazione))
    rows = cursor.fetchall()   
    return render_template('update.html', prenotazioni = rows)

@app.route("/add_prenotazione", methods=["POST"])
def add_prenotazione():
    if request.method == "POST":
        nome = request.form["nome"]
        cognome = request.form["cognome"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        numPosti = request.form["numPosti"]
        dataOra = request.form["dataOra"]
        cursor.execute ("INSERT INTO clienti (IDprenotazione, nome, cognome, telefono, email, numPosti, dataOra) VALUES (DEFAULT, %s, %s, %s, %s, %s, %s)", (nome, cognome, telefono, email, numPosti, dataOra))
        connection.commit()
        return redirect(url_for('prenotazioni'))
    
@app.route("/update_prenotazione/<int:IDprenotazione>", methods=["POST"])
def update_prenotazione(IDprenotazione):
    if request.method == "POST":
        nome = request.form["newNome"]
        cognome = request.form["newCognome"]
        telefono = request.form["newTelefono"]
        email = request.form["newEmail"]
        numPosti = request.form["newNumPosti"]
        dataOra = request.form["newDataOra"]
        cursor.execute ("UPDATE clienti SET nome = %s, cognome = %s, telefono = %s, email = %s, numPosti = %s, dataOra = %s WHERE IDprenotazione = %s", (nome, cognome, telefono, email, numPosti, dataOra, IDprenotazione))
        connection.commit()
        return redirect(url_for('prenotazioni'))
    
@app.route("/delete_prenotazione/<int:IDprenotazione>", methods=["POST"])
def delete_prenotazione(IDprenotazione):
        cursor.execute("DELETE FROM clienti WHERE IDprenotazione = %s", (IDprenotazione))
        connection.commit()
        return redirect(url_for('prenotazioni'))

if __name__ == "__main__":
    app.run(debug=True)