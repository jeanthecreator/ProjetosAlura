
//Movimento Ator
let yAtor = 366;
let xAtor = 100;
let pontos = 0;
let colisao = false;

function mostraAtor(){
  image(imageAtor,xAtor, yAtor,30 ,30);
}

function pontuacao(){
  
  if (yAtor == 0 || yAtor < 5 ){
    pontos += 1;
    yAtor = 366;
    pontoSom.play();
  }
}

function mostrarPontuacao(){
  
  textSize(30);
  textAlign(CENTER, TOP);
  text(pontos, 250, 5);
  
}

function movimentoAtor(){
  
  if (keyIsDown(UP_ARROW)){
    yAtor -= 2;
    
  }
  
   if (keyIsDown(DOWN_ARROW)){
    if (yAtor < 366){
      yAtor += 2;
    }
  }
  
}

function verificaColisao(){
  for(let i = 0; i < imageCarros.length; i = i + 1){
  colisao = collideRectRect(xCarros[i], yCarros[i], compCarro, altCarro, xAtor, yAtor, 30, 30);
    
      if (colisao){
          colidiu();
    }
  }
   
}

function colidiu(){
   yAtor = 366;
  colisaoSom.play();
  if(pontos>0){
    pontos -= 1;
  }
}