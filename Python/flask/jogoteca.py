from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

nome_css_file = 'bootstrap.css'

app = Flask(__name__)
app.secret_key = 'trovador'
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "{SGBD}://{username}:{password}@{local_port}/{database}".format(
        SGBD = 'mysql+mysqlconnector',
        username = 'root',
        password = 'admin',
        local_port = 'localhost',
        database = 'jogoteca'
)
db = SQLAlchemy(app)

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    plataforma = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>'% self.name

class Usuarios(db.Model):
    nickname = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String(8), nullable=False)
    senha = db.Column(db.String(20), nullable=False)


@app.route('/')

def catalogo_jogos():
    lista =     Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo = 'Jogos', jogos = lista, css = nome_css_file)

@app.route('/novo')

def adiciona_jogo():

    if 'usuario_logado' not in session or session['usuario_logado'] == None:

        return redirect(url_for('login', proxima = url_for('adiciona_jogo')))
    
    return render_template('novo.html', titulo = 'Novo Jogo', css = nome_css_file)

@app.route('/criar', methods=["POST",])

def adiciona_novo():

    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['console']

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        print("Jogo já existe no seu catalogo!")
        return redirect(url_for('catalogo_jogos'))

    novo_jogo = Jogos(nome=nome, categoria=categoria, plataforma=plataforma)
    db.session.add(novo_jogo)
    db.session.commit()
        
    return redirect (url_for('catalogo_jogos'))

@app.route('/login')

def login():

    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route("/autenticar", methods = ["POST" ,])

def autenticar():
   user = Usuarios.query.filter_by(nickname=request.form['usuario']).first()

   if user:
        if user.senha == request.form['senha']:
            session['usuario_logado'] = user.nickname
            flash(user.nickname + ' Login efetuado com Sucesso')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)

        else:
            flash('Usuario ou senha invalido')
            return redirect(url_for('login'))
        
   else:
        flash('Usuario ou senha invalido')
        return redirect(url_for('login'))

@app.route('/logout')

def logout():
    session['usuario_logado'] = None
    flash("Logout efetuado!")
    return redirect(url_for('catalogo_jogos'))
    

app.run(debug = True)
