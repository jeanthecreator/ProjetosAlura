//Variaveis das Images e sons

let imageEstrada;
let imageAtor;
let imageCarros;
let trilha;
let colisaoSom;
let pontoSom;


function preload(){
  
  trilha = loadSound("/sound/trilha.mp3");
  colisaoSom = loadSound("/sound/colidiu.mp3");
  pontoSom = loadSound("/sound/pontos.wav");
  
  imageEstrada = loadImage("/images/estrada.png");
  imageAtor = loadImage("/images/ator-1.png");
  imageCarro1 = loadImage("/images/carro-1.png");
  imageCarro2 = loadImage("/images/carro-2.png");
  imageCarro3 = loadImage("/images/carro-3.png");
  imageCarro4 = loadImage("/images/carro-4.png");
  imageCarro5 = loadImage("/images/carro-5.png");
  imageCarro6 = loadImage("/images/carro-6.png");
  imageCarros = [imageCarro1, imageCarro2, imageCarro3, imageCarro4, imageCarro6, imageCarro5]; 
  
}