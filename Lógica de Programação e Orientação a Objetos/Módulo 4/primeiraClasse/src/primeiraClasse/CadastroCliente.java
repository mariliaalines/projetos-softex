package primeiraClasse;

public class CadastroCliente {
	
	//atributos da classe
	private String nome;
	private String email;
	private String senha;
	private int id = 0;
	private static int nClientes = 0;
	
	public CadastroCliente() {
		
	}
	public CadastroCliente(String nome, String email, String senha) {
		this.nome = nome;
		this.email = email;
		this.senha = senha;
		this.id = nClientes++;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getSenha() {
		return senha;
	}
	public void setSenha(String senha) {
		this.senha = senha;
	}	
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.senha = nome;
	}

	public int getId() {
		return id;
	}
	@Override
	public String toString() {
		return "Nome: " + nome + ", E-mail: " + email + ", Senha: " + senha + ", ID: " + id + "";
	}
	

}
