const prompt = require("prompt-sync")();

//função simples sem parâmetros e retornos.
function saudacoes(){
    console.log('Olá mundo!!');
}

//função com parâmetros e retorno
function soma(num1, num2){
    let soma = num1 + num2;
    return soma;
}

//arrow function
let multiplicacao = (num1, num2) => num1 * num2

//chamando as funções
saudacoes();
let operacao1 = soma(10, 20);
let operacao2 = multiplicacao(20, 10);
console.log('Soma = '+operacao1+'\nMultiplicação = '+operacao2);