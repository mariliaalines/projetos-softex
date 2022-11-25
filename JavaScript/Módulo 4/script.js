var banco = {
    conta: '0120365',
    saldo: 5000.50,
    tipo_conta: 'Corrente',
    agencia: '010',

    buscarSaldo: function (){

        return this.saldo;
    },

    deposito: function (depositarValor){
        return this.saldo + depositarValor;

    },

    saque: function (sacarValor){
        return this.saldo - sacarValor;
    },

    getNumConta: function (){
        return this.conta;
    }

}

//valor inicial de saldo
console.log('Saldo Inicial: '+ banco.saldo);

//depositando R$ 500,00
console.log('Saldo após depósito: '+ banco.deposito(500));

//sacando R$ 160,00
console.log('Saldo após saque: '+ banco.saque(160));


