//Variaveis da bolinha

let pXb = 300;
let pYb  = 200;
let dB = 18;
let rB = dB / 2;

//Velocidade da boliha

let vXb = 5;
let vYb = 5;

//Variaveis da raquete Player

let pXrp = 10;
let pYrp = 150;
let lRp = 5;
let aRp = 70;

let pXra = 585
let pYra = 150;
let vRa;


//Marcação do placar variaveis

let placarPlayer = 0;
let placarAdversario = 0;
let chanceDeErrar = 0;

function setup() {
  createCanvas(600, 400);
  trilha.loop();
  
}

function draw() {
  background(0);
  Bolinha();
  MoviBolinha();
  VdeAtritoBolinha();
  raquete(pXrp, pYrp);
  raquete(pXra, pYra);
  MovimentoRaquete();
  Colisao();
  movimentoRaqueteA();
  colisaoRaqueteA();
  marcaPlacar();
  placarTexto(); 
  meioDoCampo();
  bolinhaNaoFicaPresa();
  
      
}


function Bolinha(){
  circle(pXb, pYb, dB)
}

function raquete(x,y){
  
  rect (x, y, lRp, aRp)

}

function MovimentoRaquete(){
  
  if (keyIsDown(UP_ARROW)){
      
    pYrp -= 6;
      
      }
  if (keyIsDown(DOWN_ARROW)){
    pYrp += 6;
  }
                             
  
} 

function MoviBolinha(){
  
  pXb += vXb;
  pYb += vYb;
}

function VdeAtritoBolinha(){
  
  if (pXb + rB > width || pXb - rB < 0){
    vXb *= -1;
  }
  
  if (pYb + rB > height || pYb - rB < 0){
    vYb *= -1;
  }
    
  
}

function Colisao(){
  
  if (pXb - rB < pXrp + lRp && pYb < pYrp + aRp && pYb > pYrp){
    vXb *= -1;
    
    raquetada.play();
  }
}


function movimentoRaqueteA(){
    
  vRa = pYb - pYra - (aRp/2) - 30;
  pYra += vRa + chanceDeErrar;
  
  calculaChanceDeErrar()
}

function colisaoRaqueteA(){
  
   if (pXb + rB > pXra - lRp && pYb < pYra + aRp && pYb > pYra ){
    vXb *= -1;
     
     raquetada.play();
  }
  
}

function placarTexto(){
  
  stroke(255);  
  textAlign(CENTER);
  fill(255,153,51);
  rect(150, 10, 40,30);
  
  textSize(35);
  fill(255);
  textAlign(CENTER, TOP);
  text (placarAdversario, 170, 10);
  
  
  textAlign(CENTER);
  fill(255,153,51);
  rect(410, 10, 40,30);
  
  textSize(35);
  fill(255);
  textAlign(CENTER, TOP);
  text (placarPlayer, 430, 10);
  
  
}

function marcaPlacar(){
  
  if (pXb < 10){
    placarAdversario += 1;
    ponto.play();
  }
  
  if (pXb > 590){
    placarPlayer += 1;
    ponto.play();
  }
  
  
}

function meioDoCampo(){
  
  noStroke();
  fill(255,140,0);
  rect(0, 0.2, 600,3);
  rect(0, 397, 600,3);
  rect(0.2, 1, 3,400);
  rect(597, 1, 3,400);
  
  fill(255);
  rect(width/2, 1, 2,400);
 
}

function preload(){
  
  trilha = loadSound("trilha.mp3");
  ponto = loadSound("ponto.mp3");
  raquetada = loadSound("raquetada.mp3");
}

function calculaChanceDeErrar() {
  if (placarAdversario >= placarPlayer) {
    chanceDeErrar += 1
    if (chanceDeErrar >= 69){
    chanceDeErrar = 70
    }
  } else {
    chanceDeErrar -= 1
    if (chanceDeErrar <= 45){
    chanceDeErrar = 45
    }
  }
}


function bolinhaNaoFicaPresa(){
    if (pXb - rB < 0){
    pXb = 23
    }
}

