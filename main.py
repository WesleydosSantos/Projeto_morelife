#############################
#                           #
#   * sistema morelife *    #
#    Autores:               #
#       Wesley              #
#       Luana               #
#       Jeverton            #
#                           #
#############################





#Biblioteca para realizar a conexão com o Postgres
import psycopg2





#Menu do sistema
def menu():
    print(" --- SEJA BEM VINDO AO SISTEMA MORELIFE ---")
    print("Digite oque fazer:  \n1 - Cadastrar novo cliente\n2 - Consultar cliente na lista de espera\n3 - Excluir cliente ")



#inserção de um novo usuário
def inserirUsuario ():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")

        cursor = connection.cursor()
        comando = """ Insert into listadeespera (cpf_espera, nome, rua, numero, cep, cidade, estado, telefone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        cpf = int(input(print("Digite o cpf: ")))
        nome = input(print("Digite o nome: "))
        rua = input(print("Digite a rua: "))
        numero = int(input(print("Digite o numero: ")))
        cep = int(input(print("Digite o CEP: ")))
        cidade = input(print("Digite o cidade: "))
        estado = input(print("Digite o estado: "))
        telefone = int(input(print("Número de telefone: ")))
        cursor.execute(comando, (cpf, nome, rua, numero, cep, cidade, estado, telefone,))
        connection.commit()
        print("\nUsuário cadastrado\n ")

    except (Exception, psycopg2.Error) as error:
        print("Erro ao inserir usuário ", error)



#ver clientes da fila de espera
def verFila():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")
        cursor = connection.cursor()


        cursor.execute(" SELECT * FROM listaDeEspera");
        print("     CPF      NOME     RUA   NUMERO   CEP    CIDADE   ESTADO  TELEFONE")
        consulta = cursor.fetchall()
        print(consulta)

    except (Exception, psycopg2.Error) as error:
        print("Erro ao ver usuário da fila de espera ", error)




#função deletar cliente através do CPF
def deletarCliente(cpf):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")

        cursor = connection.cursor()

        # Apagando uma tupla pelo CPF
        sql_delete_query = """Delete from cliente where cpf = %s"""
        cursor.execute(sql_delete_query, (cpf,))
        connection.commit()
        count = cursor.rowcount
        print(count, "cliente deletado ")

    except (Exception, psycopg2.Error) as error:
        print("Erro na operação deletar", error)



# validando a entrada do CPF que será excluido e excluindo se ele for validado
def validarExcluir():
    try:
        digite = int(input("Digite o CPF a ser excluído (apenas números)\nExemplo XXXXXXXXXXX: "))
        deletarCliente(digite)

    except (Exception):

        print("Erro na operação. Caractere inválido ")


                                                        ###opcao do usuario###
opcao = 0
while opcao != 1:
    menu()
    escolha = int(input("--> "))


    #aqui um novo usuário é inserido
    if escolha == 1:
        inserirUsuario()


    #visualizar a fila de espera
    elif escolha == 2:
        ## tira de uma tabela e joga na outra --> INSERT INTO cliente SELECT * FROM listaDeEspera;
        verFila()
        input("\nPressione ENTER para sair ")

    #excluir um cliente
    elif escolha == 3:
        validarExcluir()

    #caso o usuário insira uma opção inválida
    else:
        print("Ops opção inválida. ")

    #variável que armazena a escolha do usuário
    opcao = int(input("1-sair\n2-voltar ao menu inicial\n"))















