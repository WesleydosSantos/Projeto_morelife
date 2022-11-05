#############################
#                           #
#   * sistema morelife *    #
#    Autores:               #
#       Wesley              #
#       Luana               #
#       Jeverton            #
#                           #
#############################
import datetime

#Biblioteca para realizar a conexão com o Postgres
import psycopg2
from datetime import time





#definir login
def loginAdministrador():

    input("CPF: ")
    input("Senha: ")




##inserção de um medico
def cadastrarMedico():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")

        cursor = connection.cursor()
        comando = """ Insert into medico (cpf, nome, rua, numero, cep, cidade, estado, telefone, crm, especialidade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        try:
            cpf = int(input(print("Digite o CPF (obrigatório e somente numeros): ")))
            nome = input(print("Digite o nome: "))
            rua = input(print("Digite a rua: "))
            numero = int(input(print("Digite o numero: ")))
            cep = int(input(print("Digite o CEP: ")))
            cidade = input(print("Digite o cidade: "))
            estado = input(print("Digite o estado: "))
            telefone = int(input(print("Número de telefone: ")))
            crm = int(input(print("CRM: ")))
            especialidade = input(print("Especialidade: "))

            cursor.execute(comando, (cpf, nome, rua, numero, cep, cidade, estado, telefone,crm, especialidade,))
            connection.commit()
            print("\nMédico cadastrado\n ")

        except(Exception):
            print("Caractere inválido, tente novamente ")

    except(Exception, psycopg2.Error) as error:
        print("Erro na inserir usuário", error)

def excluirMedico():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")

        cursor = connection.cursor()

        cpf = int(input("Digite o CPF > "))

        # Apagando uma tupla pelo CPF
        sql_delete_query = """Delete from medico where cpf = %s"""
        cursor.execute(sql_delete_query, (cpf,))
        connection.commit()
        count = cursor.rowcount
        print(count, "medico deletado\n ")

    except (Exception, psycopg2.Error) as error:
        print("Erro na operação deletar", error)



#Menu do sistema
def menuAdministrador():
    print("\n --- SISTEMA MORELIFE ---")
    print("     [Administrador]    ")
    print("Digite oque fazer:  \n 1 - Cadastrar novo paciente\n 2 - Consultar pacientes da lista de espera\n 3 - Excluir paciente\n 4 - Cadastratar médico\n 5 - Excluir médico\n 6 - Cadastrar consulta "
          "")



#inserção de um novo usuário
def inserirUsuario ():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgres",
                                          host="LocalHost",
                                          database="postgres")

            cursor = connection.cursor()
            comando = """ Insert into paciente (cpf, nome, rua, numero, cep, cidade, estado, telefone,status_gravidade,status_tempo_espera) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            try:
                cpf = int(input(print("Digite o CPF (obrigatório e somente numeros): ")))
                nome = input(print("Digite o nome: "))
                rua = input(print("Digite a rua: "))
                numero = int(input(print("Digite o numero: ")))
                cep = int(input(print("Digite o CEP: ")))
                cidade = input(print("Digite o cidade: "))
                estado = input(print("Digite o estado: "))
                telefone = int(input(print("Número de telefone: ")))
                status_gravidade = input("Estatus de gravidade: ")

                print("Status tempo de espera: ")
                hora = int(input("Hora: "))
                minuto = int(input("Minutos: "))
                status_tempo_espera = datetime.time(hora,minuto)

                cursor.execute(comando, (cpf, nome, rua, numero, cep, cidade, estado, telefone,status_gravidade,status_tempo_espera,))
                connection.commit()
                print("\nPaciente cadastrado\n ")

            except(Exception, psycopg2.Error) as error:
                print("Erro na inserir paciente", error)

        except(Exception, psycopg2.Error) as error:
            print("Erro na inserir paciente", error)








#ver clientes da fila de espera
def verFila():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")
        cursor = connection.cursor()


        cursor.execute(" SELECT * FROM listaDeEspera");
        print("     CPF                    NOME                           RUA                NUMERO    CEP    CIDADE   ESTADO   TELEFONE")
        consulta = cursor.fetchall()
        print(consulta)

    except (Exception, psycopg2.Error) as error:
        print("Erro ao ver paciente da fila de espera ", error)




#função deletar cliente através do CPF
def deletarCliente(cpf):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")

        cursor = connection.cursor()

        # Apagando uma tupla pelo CPF
        sql_delete_query = """Delete from paciente where cpf = %s"""
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

def cadastrarConsulta():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")

        cursor = connection.cursor()
        comando = """ Insert into consulta (data,hora, cpf_medico, cpf_paciente, descricao) VALUES (%s,%s,%s,%s,%s)"""

        try:
            print("Digite a data no formato YYYY-MM-DD ")

            ano = int(input("Ano: "))
            mes = int(input("Mês: "))
            dia = int(input("Dia: "))

            data = datetime.date(ano, mes, dia)


            horaGrande = int(input("Digite a hora: "))
            minuto = int(input("Digite os minutos: "))
            hora = datetime.time(horaGrande, minuto)

            cpf_medico = int(input(print("CPF do medico: ")))
            cpf_paciente = int(input(print("Digite o CPF do paciente: ")))
            descricao = input(print("Descrição da : "))

            cursor.execute(comando, (data, hora, cpf_medico, cpf_paciente, descricao,))
            connection.commit()
            print("\nConsulta cadastrada\n ")

        except(Exception, psycopg2.Error) as error:
            print("Erro ", error)

    except(Exception, psycopg2.Error) as error:
        print("Erro ", error)

def menuUsuario():
    print("\n --- SISTEMA MORELIFE ---")
    print("       [Funcionário]    ")
    print(" 1 - Consultar lista de espera\n 2 - Cadastrar consulta\n 2 - Gerar receita\n 4 - Fazer prontuário ")

def menuMedico():
    print("\n --- SISTEMA MORELIFE ---")
    print("         [Médico]    ")
    print(" 1 - Consultar lista de espera\n 2 - Cadastrar consulta\n 2 - Gerar receita\n 4 - Fazer prontuário ")


                                                       ###opcao do usuario###

print("*****************************************")
print("*                                       *")
print("*   1 - Fazer login como funcionário    *")
print("*   2 - Fazer login como médico         *")
print("*   3 - Fazer login como administrador  *")
print("*                                       *")
print("*****************************************")

alternativa = int(input(">> "))


if alternativa == 2:
    int(input("CRM: "))
    input("Senha: ")


if alternativa == 3:

    loginAdministrador()

    opcao = 0
    while opcao != 2:
        menuAdministrador()
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

        #cadastra medico
        elif escolha ==4:
            cadastrarMedico()

        elif escolha ==5:
            excluirMedico()

        elif escolha ==6:
            cadastrarConsulta()

        #caso o usuário insira uma opção inválida
        else:
            print("Ops opção inválida. ")

        #variável que armazena a escolha do usuário
        opcao = int(input("1- voltar ao menu inicial\n2 - sair\n>> "))

elif alternativa == 1:

    escolhaUsuario = 0

    while escolhaUsuario != 2:
        menuUsuario()
        escolha = int(input(">> "))

        if escolha == 1:
            verFila()
        elif escolha == 2:
            cadastrarConsulta()

        escolhaUsuario = int(input("\n1 - Voltar ao menu inicial\n2 - Sair\n>> "))

elif alternativa == 2:
    menuMedico()












