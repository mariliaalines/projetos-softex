const prompt = require("prompt-sync")();

var nota1, nota2, nota3;
console.log('\nINSIRA SUAS NOTAS')
nota1 = parseFloat(prompt("Digite a 1° nota:"));
nota2 = parseFloat(prompt("Digite a 2° nota:"));

nota3 = 21 - nota1 - nota2;

console.log('\nVocê precisa tirar '+nota3+' na próxima prova para ser aprovado por média.');