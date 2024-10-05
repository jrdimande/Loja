class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def add_estoque(self, quantidade):
        if quantidade > 0:
            self.estoque += quantidade
            print("Estoque aumentado")
        else:
            print("Quantidade inválida, tente novamente!")

    def remove_estoque(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            print(f"Quantidade reduzida para {self.estoque}")
        else:
            print("Quantidade superior ao estoque disponível")


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.carrinho = []
        self.total_compra = 0

    def add_carrinho(self, produto, quantidade):
        if produto.estoque >= quantidade:
            for _ in range(quantidade):
                self.carrinho.append(produto)
            produto.estoque -= quantidade
            print(f"Adicionou {produto.nome.title()} ao carrinho!")
        else:
            print(f"Restou apenas {produto.estoque} unidades")

    def remove_carrinho(self, produto):
        self.carrinho.remove(produto)
        print("Produto removido")

    def visualizar_Carrinho(self):
        total_preco = 0
        produtos_contagem = {}

        for produto in self.carrinho:
            if produto.nome in produtos_contagem:
                produtos_contagem[produto.nome]["quantidade"] += 1
            else:
                produtos_contagem[produto.nome] = {"preco": produto.preco, "quantidade": 1}

        for nome_produto, info in produtos_contagem.items():
            preco_total = info["preco"] * info["quantidade"]
            print(f"{nome_produto.title()} x {info['quantidade']} = {preco_total} MT")
            total_preco += preco_total

        print(f"Preço total da compra: {total_preco} MT")


class Loja:
    def __init__(self):
        self.produtos = []
        self.usuarios = []

    def add_produto(self, produto):
        if produto not in self.produtos:
            self.produtos.append(produto)
            print(f"{produto.nome.title()} adicionado a loja")
        else:
            print(f"O produto já foi adicionado a loja")

    def add_user(self, user):
        if user not in self.usuarios:
            self.usuarios.append(user)
            print(f"{user.nome.title()} adicionado")
        else:
            print("O usuário já foi adicionado antes")


headphone = Produto("Headphone", 120000000, 2)
tshirt= Produto("T-SHIRT", 1000, 3)
user1 = Usuario("example", "example@gamil.com")
loja = Loja()

loja.add_produto(headphone)
loja.add_produto(tshirt)
loja.add_user(user1)

print(
    "======================================================================================================================================")

user1.add_carrinho(headphone, 2)
user1.add_carrinho(tshirt, 1)

print(
    "======================================================================================================================================")

user1.visualizar_Carrinho()
