package aplicação;

import java.util.ArrayList;
import java.util.Scanner;

import primeiraClasse.CadastroCliente;
public class programa {

	public static void main(String[] args) {

		//Variáveis
		int opcao;
		String nome, email, senha;
		ArrayList <CadastroCliente> ListaClientes = new ArrayList();
		int quantClientes = 0;
		
		//Leitor do teclado
		Scanner leitor = new Scanner(System.in);
		
		//Cadastrar Cliente
		//Cliente insere os dados do cadastro
		
		do {
			System.out.println("Deseja realizar novo cadastro? \n1- SIM\n2- NÃO");
			opcao = leitor.nextInt();
			if(opcao == 1) {
				//Cliente insere seus dados para cadastro
				System.out.println("Cadastro de Clientes");
				System.out.print("Nome: ");
				nome = leitor.next();
				System.out.print("E-mail: ");
				email = leitor.next();
				System.out.print("Senha: ");
				senha = leitor.next();
				CadastroCliente Cliente = new CadastroCliente(nome, email, senha);
				
				ListaClientes.add(Cliente);
				
				quantClientes++;
				
			}else if(opcao == 2) {
				//Sai do looping
				
			}else {
				//Cliente digita opção inválida
				System.out.println("ERROR!Insira uma opção válida!!");
			}

		}while(opcao != 2);
		
		//Imprimindo os clientes cadastrados na tela
		System.out.println("Foram cadastrados "+ quantClientes + " clientes");
		
		for(CadastroCliente cliente:ListaClientes) {
			System.out.println(cliente);
		}

		leitor.close();

	}

}
