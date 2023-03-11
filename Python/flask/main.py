from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogos:

    def __init__(self, nome, categoria, plataforma):

        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma
    
    # def jogo_completo(self, nome, categoria, plataforma):


class Usuario:
    def __init__(self, usuario, nickname, senha) -> None:
        self.usuario = usuario
        self.nickname = nickname
        self.senha = senha


usuario1 = Usuario('Taz Mania', 'taz', 'a12345')
usuario2 = Usuario('Harry Potter', 'potter', 'b12345')
usuario3 = Usuario('Marvin Marciano', 'marciano', 'c12345')

usuarios = {
            usuario1.nickname : usuario1,
            usuario2.nickname : usuario2,
            usuario3.nickname : usuario3
            }

jogo1 = Jogos('Genshin', "MMORPG", "Multiplataform")
jogo2 = Jogos('FF7', 'RPG', 'PS1')
jogo3 = Jogos('God of War', 'Hack Slash', 'PS3')
lista = [jogo1, jogo2, jogo3]
nome_css_file = 'bootstrap.css'
        

app = Flask(__name__)
app.secret_key = 'trovador'


@app.route('/')

def catalogo_jogos():
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
    console = request.form['console']
    jogo = Jogos(nome, categoria, console)
    lista.append(jogo)

    return redirect (url_for('catalogo_jogos'))

@app.route('/login')

def login():

    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route("/autenticar", methods = ["POST" ,])

def autenticar():
   if request.form['usuario'] in usuarios:
        user = usuarios[request.form['usuario']]
        if user.senha == request.form['senha']:
            session['usuario_logado'] = user.nickname
            flash(user.nickname + ' Login efetuado com Sucesso')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
   else:
        flash('Usuario ou senha invalido')
        return redirect(url_for('login'))

@app.route('/logout')

def logout():
    session['usuario_logado'] = None
    flash("Logout efetuado!")
    return redirect(url_for('catalogo_jogos'))
    

app.run(debug = True)
