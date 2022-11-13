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
        comando = """ Insert into medico (cpf_medico, nome, rua, numero, cep, cidade, estado, telefone, crm, especialidade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        try:



            cpf_medico = int(input("Digite o CPF (obrigatório e somente numeros): "))
            nome = input("Digite o nome: ")
            rua = input(print("Digite a rua: "))
            numero = int(input("Digite o numero: "))
            cep = int(input("Digite o CEP: "))
            cidade = input("Digite o cidade: ")
            estado = input("Digite o estado: ")
            telefone = int(input("Número de telefone: "))
            crm = int(input("CRM: "))
            especialidade = input("Especialidade: ")

            cursor.execute(comando, (cpf_medico, nome, rua, numero, cep, cidade, estado, telefone, crm, especialidade,))
            connection.commit()
            print("\nMédico cadastrado\n ")

        except(Exception):
            print("Caractere inválido, tente novamente ")

    except(Exception, psycopg2.Error) as error:
        print("Erro na conexão", error)

def excluirMedico():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")

        cursor = connection.cursor()

        cpf_medico = int(input("Digite o CPF > "))

        # Apagando uma tupla pelo CPF
        sql_delete_query = """Delete from medico where cpf_medico = %s"""
        cursor.execute(sql_delete_query, (cpf_medico,))
        connection.commit()
        count = cursor.rowcount
        print(count, "medico deletado\n ")

    except (Exception, psycopg2.Error) as error:
        print("Erro na operação deletar", error)



#Menu do sistema
def menuAdministrador():
    print("\n --- SISTEMA MORELIFE ---")
    print("     [Administrador]    ")
    print("Digite oque fazer:  \n 1 - Consultar paciente da lista de espera\n 2 - Cadastrar novo paciente\n 3 - Atualizar dados de um paciente\n 4 - Excluir paciente\n 5 - Cadastratar médico\n 6 - Atualizar dados de um médico\n 7 - Excluir médico\n 8 - Cadastrar consulta """)



#inserção de um novo usuário
def cadastrarPaciente ():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgres",
                                          host="LocalHost",
                                          database="postgres")

            cursor = connection.cursor()
            comando = """ Insert into paciente (cpf, nome, rua, numero, cep, cidade, estado, telefone,status_gravidade,status_tempo_espera) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            try:
                cpf = int(input("Digite o CPF (obrigatório e somente numeros): "))
                nome = input("Digite o nome: ")
                rua = input("Digite a rua: ")
                numero = int(input("Digite o numero: "))
                cep = int(input("Digite o CEP: "))
                cidade = input("Digite o cidade: ")
                estado = input("Digite o estado: ")
                telefone = int(input("Número de telefone: "))
                status_gravidade = input("Estatus de gravidade: ")

                print("Status tempo de espera: ")
                hora = int(input("Hora: "))
                minuto = int(input("Minutos: "))
                status_tempo_espera = datetime.time(hora, minuto)

                cursor.execute(comando, (cpf, nome, rua, numero, cep, cidade, estado, telefone,status_gravidade, status_tempo_espera,))
                connection.commit()
                print("\nPaciente cadastrado\n ")

            except(Exception, psycopg2.Error) as error:
                print("Erro na inserir paciente", error)

        except(Exception, psycopg2.Error) as error:
            print("Erro na conexão", error)








#ver clientes da fila de espera
def verFila():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")
        cursor = connection.cursor()


        cursor.execute(" SELECT * FROM listaDeEspera");

        consulta = cursor.fetchall()

        for row in consulta:
            print("CPF: ", row[0])
            print("Nome: ", row[1])
            print("Rua: ", row[2])
            print("Numero: ", row[3])
            print("CEP: ", row[4])
            print("Cidade: ", row[5])
            print("Estado: ", row[6])
            print("Telefone: ", row[7])
            print("\n")


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

        except(Exception):
            print("Ops, médico e/ou paciente não existe ")

    except(Exception, psycopg2.Error) as error:
        print("Erro ", error)



def menuMedico():
    print("\n --- SISTEMA MORELIFE ---")
    print("         [Médico]    ")
    print(" 1 - Gerar receita\n 2 - Fazer prontuário ")

def gerarReceita():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")

        cursor = connection.cursor()

        comando = """ Insert into receita_paciente ( nome_remedio, cod_remedio, cod_paciente ) VALUES (%s,%s ,%s) """
        codigo_remedio = int(input("Código do medicamento: "))
        nome_remedio = input("Nome: ")
        cod_paciente = int(input("CPF: "))


        cursor.execute(comando, (nome_remedio, codigo_remedio, cod_paciente,))
        connection.commit()

        print("\nReceita gerada com sucesso ")
    except (Exception, psycopg2.Error) as error:
        print("Erro ao gerar receita", error)



def gerarProntuario(cpf):

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")

        cursor = connection.cursor()


        comando = """ select  p.nome, p.rua, p.numero, p.cep, p.cidade, p.estado, p.telefone, p.status_gravidade, rp.cod_remedio, rp.nome_remedio from paciente as p, receita_paciente as rp  where p.cpf = (%s) and rp.cod_paciente = p.cpf """
        cursor.execute(comando, (cpf,))

        result = cursor.fetchall()


        for row in result:
            print("---------------SISTEMA MORELIFE-------------------")
            print("Nome completo:  ", row[0])
            print("Endereço: ")
            print(" Rua: ", row[1])
            print(" Numero: ", row[2])
            print(" CEP: ", row[3])
            print(" Cidade: ", row[4])
            print(" Estado: ", row[5])
            print("Tele fone: ", row[6])
            print("Gravidade: ", row[7])
            print("Código medicamento: ", row[8])
            print("Nome Medicamento: ", row[9])
            print("--------------------------------------------------")
            print("\n")

    except (Exception, psycopg2.Error) as erro:
        print("Deu ao gerar prontuário ", erro)


def atualizarMedico():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="LocalHost",
                                      database="postgres")

        cursor = connection.cursor()

        pensou = int(input("Inform oque deseja atualizar: \n1 - Nome\n2- Rua\n3- Número\n4 - CEP\n5 - Cidade\n6 - Estado\n7 - Telefone\n8 - CRM\n9 - Especialidade\n>> "))

        if pensou == 1:
            comando = """ update medico set nome = %s where cpf_medico = %s """

            cpf_medico = int(input("Informe o CPF do médico a ser atualizado: "))
            nome = input("Novo nome: ")
            cursor.execute(comando, (nome, cpf_medico,))
            connection.commit()
            print("Atualizado com sucesso")

        elif pensou == 2:
            comando = """ update medico set rua = %s where cpf_medico = %s """

            cpf_medico = int(input("Informe o CPF do médico a ser atualizado: "))
            rua = input("Nova rua: ")
            cursor.execute(comando, (rua, cpf_medico,))
            connection.commit()
            print("Atualizado com sucesso")

        elif pensou == 3:
            comando = """ update medico set numero = %s where cpf_medico = %s """

            cpf_medico = int(input("Informe o CPF do médico a ser atualizado: "))
            numero = input("Novo número: ")
            cursor.execute(comando, (numero, cpf_medico,))
            connection.commit()
            print("Atualizado com sucesso")

        elif pensou == 4:
            comando = """ update medico set cep = %s where cpf_medico = %s """

            cpf_medico = int(input("Informe o CPF do médico a ser atualizado: "))
            cep = input("Novo CEP: ")
            cursor.execute(comando, (cep, cpf_medico,))
            connection.commit()
            print("Atualizado com sucesso")

        elif pensou == 5:
            comando = """ update medico set cidade = %s where cpf_medico = %s """

            cpf_medico = int(input("Informe o CPF do médico a ser atualizado: "))
            cidade = input("Nova cidade: ")
            cursor.execute(comando, (cidade, cpf_medico,))
            connection.commit()
            print("Atualizado com sucesso")

        elif pensou == 6:
            comando = """ update medico set estado = %s where cpf_medico = %s """

            cpf_medico = int(input("Informe o CPF do médico a ser atualizado: "))
            estado = input("Novo estado: ")
            cursor.execute(comando, (estado, cpf_medico,))
            connection.commit()
            print("Atualizado com sucesso")

        elif pensou == 7:
            comando = """ update medico set telefone = %s where cpf_medico = %s """

            cpf_medico = int(input("Informe o CPF do médico a ser atualizado: "))
            telefone = input("Novo telefone: ")
            cursor.execute(comando, (telefone, cpf_medico,))
            connection.commit()
            print("Atualizado com sucesso")

        elif pensou == 8:
            comando = """ update medico set crm = %s where cpf_medico = %s """

            cpf_medico = int(input("Informe o CPF do médico a ser atualizado: "))
            crm = input("Novo CRM: ")
            cursor.execute(comando, (crm, cpf_medico,))
            connection.commit()
            print("Atualizado com sucesso")

        elif pensou == 9:
            comando = """ update medico set especialidade = %s where cpf_medico = %s """

            cpf_medico = int(input("Informe o CPF do médico a ser atualizado: "))
            especialidade = input("Nova especialidade: ")
            cursor.execute(comando, (especialidade, cpf_medico,))
            connection.commit()
            print("Atualizado com sucesso")
        else:
            print("Ops opção inválida ")


    except( Exception ):
        print("Erro ao atualizar dados ")

def atualizarPaciente():
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="LocalHost",
                                  database="postgres")

    cursor = connection.cursor()
    pensou = int(input("Informe oque deseja atualizar: \n1 - Nome\n2- Rua\n3- Número\n4 - CEP\n5 - Cidade\n6 - Estado\n7 - Telefone\n8 - Status de gravidade\n9 - Status do tempo de espera\n>> "))

    if pensou == 1:
        comando = """ update paciente set nome = %s where cpf = %s """

        cpf_medico = int(input("Informe o CPF do paciente a ser atualizado: "))
        nome = input("Novo nome: ")
        cursor.execute(comando, (nome, cpf_medico,))
        connection.commit()
        print("Atualizado com sucesso")

    elif pensou == 2:
        comando = """ update paciente set rua = %s where cpf = %s """

        cpf_medico = int(input("Informe o CPF do paciente a ser atualizado: "))
        rua = input("Nova rua: ")
        cursor.execute(comando, (rua, cpf_medico,))
        connection.commit()
        print("Atualizado com sucesso")

    elif pensou == 3:
        comando = """ update paciente set numero = %s where cpf = %s """

        cpf_medico = int(input("Informe o CPF do paciente a ser atualizado: "))
        numero = input("Novo número: ")
        cursor.execute(comando, (numero, cpf_medico,))
        connection.commit()
        print("Atualizado com sucesso")

    elif pensou == 4:
        comando = """ update paciente set cep = %s where cpf = %s """

        cpf_medico = int(input("Informe o CPF do paciente a ser atualizado: "))
        cep = input("Novo CEP: ")
        cursor.execute(comando, (cep, cpf_medico,))
        connection.commit()
        print("Atualizado com sucesso")

    elif pensou == 5:
        comando = """ update paciente set cidade = %s where cpf = %s """

        cpf_medico = int(input("Informe o CPF do paciente a ser atualizado: "))
        cidade = input("Nova cidade: ")
        cursor.execute(comando, (cidade, cpf_medico,))
        connection.commit()
        print("Atualizado com sucesso")

    elif pensou == 6:
        comando = """ update paciente set estado = %s where cpf = %s """

        cpf_medico = int(input("Informe o CPF do paciente a ser atualizado: "))
        estado = input("Novo estado: ")
        cursor.execute(comando, (estado, cpf_medico,))
        connection.commit()
        print("Atualizado com sucesso")

    elif pensou == 7:
        comando = """ update paciente set telefone = %s where cpf = %s """

        cpf_medico = int(input("Informe o CPF do paciente a ser atualizado: "))
        telefone = input("Novo telefone: ")
        cursor.execute(comando, (telefone, cpf_medico,))
        connection.commit()
        print("Atualizado com sucesso")

    elif pensou == 8:
        comando = """ update paciente set status_gravidade = %s where cpf = %s """

        cpf_medico = int(input("Informe o CPF do paciente a ser atualizado: "))
        status_gravidade = input("Novo Status de gravidade: ")
        cursor.execute(comando, (status_gravidade, cpf_medico,))
        connection.commit()
        print("Atualizado com sucesso")

    elif pensou == 9:
        comando = """ update paciente set status_tempo_espera = %s where cpf = %s """

        cpf_medico = int(input("Informe o CPF do paciente a ser atualizado: "))

        horaGrande = int(input("Digite a nova hora: "))
        minuto = int(input("Minuto/s: "))
        status_tempo_espera = datetime.time(horaGrande, minuto)

        cursor.execute(comando, (status_tempo_espera, cpf_medico,))
        connection.commit()
        print("Atualizado com sucesso")
    else:
        print("Ops opção inválida ")














                  ###opcao do usuario###

print("*****************************************")
print("*                                       *")
print("*   1 - Fazer login como médico         *")
print("*   2 - Fazer login como administrador  *")
print("*                                       *")
print("*****************************************")

alternativa = int(input(">> "))





if alternativa == 2:

    loginAdministrador()

    opcao = 0
    while opcao != 2:
        menuAdministrador()
        escolha = int(input("--> "))



        if escolha == 1:
            verFila()
            input("\nPressione ENTER para sair ")


        elif escolha == 2:
            cadastrarPaciente()


        elif escolha == 3:
            atualizarPaciente()


        elif escolha == 4:
            validarExcluir()

        elif escolha == 5:
            cadastrarMedico()

        elif escolha == 6:
            atualizarMedico()

        elif escolha == 7:
            excluirMedico()

        elif escolha == 8:
            cadastrarConsulta()

        #caso o usuário insira uma opção inválida
        else:
            print("Ops opção inválida. ")

        #variável que armazena a escolha do usuário
        opcao = int(input("1 - voltar ao menu inicial\n2 - sair\n>> "))

elif alternativa == 1:
    input("CRM: ")
    input("Senha: ")

    escolhaUsuario = 0

    while escolhaUsuario != 2:
        menuMedico()
        escolha = int(input(">> "))

        if escolha == 1:
            gerarReceita()
        elif escolha == 2:
            cpf = int(input("cpf>> "))
            gerarProntuario(cpf)
        

        escolhaUsuario = int(input("\n1 - Voltar ao menu inicial\n2 - Sair\n>> "))















