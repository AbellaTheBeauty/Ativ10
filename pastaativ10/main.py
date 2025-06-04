from dadoesc import Aluno

def main():

    print("--- Testando a Classe Aluno ---")

    aluno1 = Aluno(id=1,
                   nome="Lucas Abella",
                   cpf="123.456.789-00",
                   matricula="A2024XYZ")

    aluno1.marcar_presenca()
    aluno1.matricular()

    print("\n--- Testando Assessores e Modificadores ---")

    print(f"Matrícula atual do aluno {aluno1.nome}: {aluno1.get_matricula()}")

    aluno1.set_matricula("B2025ABC")
    print(f"Nova matrícula do aluno {aluno1.nome}: {aluno1.get_matricula()}")

    aluno1.set_matricula("")

    try:
        print(aluno1.__matricula)
    except AttributeError as e:
        print(f"\nTentativa de acesso direto a __matricula: Erro - {e}")
        
    print(f"\nCPF do aluno (acesso ao atributo _cpf): {aluno1._cpf}")
    aluno1._cpf = "999.999.999-99"
    print(f"CPF do aluno modificado: {aluno1._cpf}")


if __name__ == "__main__":
    main()