class Autor:
    def __init__(self, nome: str, nacionalidade: str):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def __repr__(self):
        return f"Autor(Nome: {self.nome}, Nacionalidade: {self.nacionalidade})"

class Livro:
    def __init__(self, titulo: str, autor: Autor, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f"Livro(Título: '{self.titulo}', Autor: {self.autor.nome}, Páginas: {self.paginas})"

class No:
    def __init__(self, dado: Autor):
        self.dado = dado
        self.proximo = None

class ListaAutores:
    def __init__(self):
        self.head = None

    def adicionar_autor_ordenado(self, novo_autor: Autor):
        novo_no = No(novo_autor)

        if self.head is None or novo_autor.nome < self.head.dado.nome:
            novo_no.proximo = self.head
            self.head = novo_no
            print(f"Autor '{novo_autor.nome}' adicionado com sucesso no início da lista.")
            return

        atual = self.head
        while atual.proximo is not None and atual.proximo.dado.nome < novo_autor.nome:
            atual = atual.proximo

        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        print(f"Autor '{novo_autor.nome}' adicionado com sucesso.")

    def buscar_autor(self, nome_autor: str) -> Autor | None:
        atual = self.head
        while atual is not None:
            if atual.dado.nome.lower() == nome_autor.lower():
                return atual.dado
            atual = atual.proximo
        return None 

    def imprimir(self):
        if self.head is None:
            print("A lista de autores está vazia.")
            return

        print("\n--- Lista de Autores (Ordenada por Nome) ---")
        atual = self.head
        contador = 1
        while atual is not None:
            print(f"{contador}. {atual.dado}")
            atual = atual.proximo
            contador += 1
        print("------------------------------------------")

class PilhaLivros:
    def __init__(self):
        self._itens = []

    def esta_vazia(self) -> bool:
        return not self._itens

    def empilhar(self, livro: Livro):
        self._itens.append(livro)
        print(f"Livro '{livro.titulo}' empilhado com sucesso.")

    def desempilhar(self) -> Livro | None:
        if self.esta_vazia():
            print("A pilha de livros está vazia. Nenhum livro para remover.")
            return None
        livro_removido = self._itens.pop()
        print(f"Livro '{livro_removido.titulo}' desempilhado.")
        return livro_removido

    def imprimir(self):
        if self.esta_vazia():
            print("A pilha de livros está vazia.")
            return

        print("\n--- Pilha de Livros (Topo para Base) ---")
        for i in range(len(self._itens) - 1, -1, -1):
            print(f"- {self._itens[i]}")
        print("----------------------------------------")

def main():
    lista_de_autores = ListaAutores()
    pilha_de_livros = PilhaLivros()

    autor1 = Autor("Thomas Karlsson", "Suéca")
    autor2 = Autor("J.R.R. Tolkien", "Inglesa")
    autor3 = Autor("H.P. Lovecraft", "Americana")
    lista_de_autores.adicionar_autor_ordenado(autor1)
    lista_de_autores.adicionar_autor_ordenado(autor2)
    lista_de_autores.adicionar_autor_ordenado(autor3)

    livro1 = Livro("Qabballah", autor1, 325)
    livro2 = Livro("O Hobbit", autor2, 303)
    livro3 = Livro("O Chamado de Cthulhu", autor3, 118)
    pilha_de_livros.empilhar(livro1)
    pilha_de_livros.empilhar(livro2)
    pilha_de_livros.empilhar(livro3)


    while True:
        print("\n=============== MENU ===============")
        print("1. Adicionar Autor")
        print("2. Adicionar Livro na Pilha")
        print("3. Remover Livro da Pilha")
        print("4. Imprimir Lista de Autores")
        print("5. Imprimir Pilha de Livros")
        print("0. Sair")
        print("====================================")

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            nome = input("Digite o nome do autor: ")
            nacionalidade = input("Digite a nacionalidade do autor: ")
            novo_autor = Autor(nome, nacionalidade)
            lista_de_autores.adicionar_autor_ordenado(novo_autor)

        elif escolha == '2':
            nome_autor = input("Digite o nome do autor do livro: ")
            autor_encontrado = lista_de_autores.buscar_autor(nome_autor)

            if autor_encontrado:
                titulo = input("Digite o título do livro: ")
                try:
                    paginas = int(input("Digite o número de páginas: "))
                    novo_livro = Livro(titulo, autor_encontrado, paginas)
                    pilha_de_livros.empilhar(novo_livro)
                except ValueError:
                    print("Erro: Número de páginas deve ser um inteiro.")
            else:
                print(f"Erro: Autor '{nome_autor}' não encontrado. Adicione o autor primeiro.")

        elif escolha == '3':
            pilha_de_livros.desempilhar()

        elif escolha == '4':
            lista_de_autores.imprimir()

        elif escolha == '5':
            pilha_de_livros.imprimir()

        elif escolha == '0':
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()