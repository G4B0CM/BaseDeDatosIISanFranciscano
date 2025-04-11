from flask  import Flask, render_template
from perfi import profile_bp

app = Flask(__name__)
app.secret_key = 'clave-secreta'

# Registrar blueprint
app.register_blueprint(profile_bp)


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)