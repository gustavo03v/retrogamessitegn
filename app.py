from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jogar/<console>/<jogo_id>')
def jogar(console, jogo_id):
    return render_template('jogo.html', console=console, jogo_id=jogo_id)

if __name__ == '__main__':
    app.run(debug=True)
