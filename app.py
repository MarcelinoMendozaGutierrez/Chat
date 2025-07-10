from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"].lower()

    if "hola" in user_input:
        respuesta = "¡Hola! ¿En qué puedo ayudarte?"
    elif "precio" in user_input or "costo" in user_input or "cuanto" in user_input or "a como" in user_input:
        respuesta = "El precio es de $100 por unidad."
    elif "gracias" in user_input or "agradecido" in user_input:
        respuesta = "¡De nada! Estoy para servirte."
    elif "horario" in user_input or "hora" in user_input or "abren" in user_input:
        respuesta = "Atendemos de lunes a viernes de 9 a.m. a 6 p.m."
    elif "ubicación" in user_input or "donde" in user_input:
        respuesta = "Estamos en Real Solare, El Marqués, Querétaro."
    elif "caro" in user_input:
        respuesta = "No compre entonces."
    else:
        respuesta = "Lo siento, no entendí tu mensaje."

    return {"response": respuesta}


if __name__ == "__main__":
    app.run(debug=True)
