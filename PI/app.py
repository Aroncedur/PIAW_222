from flask import Flask, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

if __name__ == "__main__":
    app.run(port=5000)