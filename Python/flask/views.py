from jogoteca import app, nome_css_file, db, nome_css_file_app
from flask import render_template, session, url_for, redirect, request, flash, send_from_directory
from models import Jogos, Usuarios

@app.route('/')

def catalogo_jogos():
    lista = Jogos.query.order_by(Jogos.id)
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

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/capa{novo_jogo.id}.jpg')

    return redirect (url_for('catalogo_jogos'))

@app.route('/edicao/<int:id>')

def verifica_edita(id):

    if 'usuario_logado' not in session or session['usuario_logado'] == None:

        return redirect(url_for('login', proxima = url_for('edita_jogo')))

    jogo = Jogos.query.filter_by(id=id).first()
    return render_template('edita.html', titulo = 'Editar Jogo', css = nome_css_file, jogo = jogo)

@app.route('/editar', methods=["POST",])


def edita_jogo():
    
    jogo = Jogos.query.filter_by(id= request.form['id']).first()
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.plataforma = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    return redirect (url_for('catalogo_jogos'))

@app.route('/delete/<int:id>')

def delete_game(id):
    jogo = Jogos.query.filter_by(id= id).first() #Tambem podemos usar o deletar direto, e só aplicar o commit

    db.session.delete(jogo)
    db.session.commit()

    return redirect(url_for('catalogo_jogos')) 
    

@app.route('/catalogo_jogos')

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

@app.route('/upload/<nome_arquivo>')

def imagem_capa(nome_arquivo):
    return send_from_directory('upload', nome_arquivo)

