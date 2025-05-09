from flask import Flask, render_template, redirect, request


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/valor', methods=["POST"])

def valor():

    dizima = request.form.get('dados')
    print(dizima)

    if (dizima == "2025"):
        return render_template("calcula2000.html")
    else:
        return redirect('/')


if __name__ in "__main__":
    app.run(debug=True)