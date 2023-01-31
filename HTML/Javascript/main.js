function tocaTecla(idTecla){

    const elemento = document.querySelector(idTecla);

    // if (elemento === null){
    //     console.log('Elemento não existe');
    // }

    if (elemento != null && elemento.localName === 'audio'){
        elemento.currentTime = 0;
        elemento.play();
    }else{
        console.log('Elemento não existe');
    }   
    
}

const listaDeTeclas = document.querySelectorAll('.tecla');


for (let contador = 0;contador < listaDeTeclas.length; contador++){

    const tecla = listaDeTeclas[contador];
    // metodo classlist
    const listaInstrumento = tecla.classList[1];
    //Templete string. metodo para se trabalhar com o codigo via string
    const idAudio = `#som_${listaInstrumento}`;
    //Função anonima, muito util 

    tecla.onclick = function(){
        tocaTecla(idAudio);
        
    }

    tecla.onkeydown = function(event){

        if (event.code === 'Enter' || event.code === 'Space'){   
            console.log(event.code)
        tecla.classList.add('ativa');

        }
    
    }

    tecla.onkeyup = function () {
        tecla.classList.remove('ativa');
    }
   
}
