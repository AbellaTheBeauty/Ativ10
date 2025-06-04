from abc import ABC, abstractmethod

class Pessoa(ABC):
    
    def __init__(self, id: int, nome: str, cpf: str):
        self.id: int = id
        self.nome: str = nome
        self._cpf: str = cpf  

    @abstractmethod
    def marcar_presenca(self) -> None:
        
        pass

    def matricular(self) -> None:
       
        print(f"{self.nome} está realizando uma matrícula genérica.")

class Aluno(Pessoa):
    
    def __init__(self, id: int, nome: str, cpf: str, matricula: str):
        super().__init__(id, nome, cpf)
        self.__matricula: str = matricula  

    def marcar_presenca(self) -> None:
        print(f"Aluno {self.nome} (matrícula: {self.__matricula}) marcou presença.")

    def matricular(self) -> None:
        print(f"Aluno {self.nome} (CPF: {self._cpf}) está sendo matriculado com a matrícula {self.__matricula}.")

    def get_matricula(self) -> str:
        return self.__matricula

    def set_matricula(self, nova_matricula: str) -> None:
        if isinstance(nova_matricula, str) and len(nova_matricula) > 0:
            self.__matricula = nova_matricula
            print(f"Matrícula do aluno {self.nome} alterada para {self.__matricula}.")
        else:
            print("Matrícula inválida.")