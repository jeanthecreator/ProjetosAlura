function setup() {
  createCanvas(500, 400);
  trilha.loop();
}

function draw() {
  
  background(imageEstrada);
  mostraAtor();
  mostraCarros();
  movimentoCarro();
  movimentoAtor();
  retornoCarro();
  verificaColisao();
  pontuacao();
  mostrarPontuacao();
}
