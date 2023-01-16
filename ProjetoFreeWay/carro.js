
let xCarros = [600, 600, 600, -55, -55, -55];
let xInicial = [600, 600, 600, -55, -55, -55];
let yCarros = [40, 95, 150, 210, 262, 318];
let velocidadeCarros = [5, 2.8, 4, -5, -2.7, -3];
let compCarro = 50;
let altCarro= 40;


function movimentoCarro(){
  
  for (let i=0; i < xCarros.length; i++){
   xCarros[i] -= velocidadeCarros[i];
  }
}

function retornoCarro(){
  for (let i = 0; i < xCarros.length; i++){
    if(carroSumiu(xCarros[i])){
      xCarros[i] = xInicial[i];
    }
  }
    
}

function mostraCarros(){
  
  for(let i = 0; i < xCarros.length; i ++){
    image(imageCarros[i], xCarros[i], yCarros[i], compCarro,altCarro);
  }
}

function carroSumiu(xCarro){
  
  if (xCarro < -60 || xCarro > 620){
    return xCarro;
  }
  
}