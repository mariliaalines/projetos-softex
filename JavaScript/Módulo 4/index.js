const Sequelize = require('sequelize');

//realizando a conexão com o BD
const sequelize = new Sequelize('locadora', 'root', 'root12345678', {
    host: 'localhost',
    dialect: 'mysql'
  });

//Verificando se a conexão com o banco de dados foi realizada com sucesso
sequelize.authenticate().then(function(){
	console.log('Conexão realizada com suecsso!!');
}).catch(function(err){
	console.log('Erro ao realizar a conexão com o Banco de dados: ' + err);
});
