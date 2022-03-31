import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(30,0), key='nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(30,0), key='idade')],
            [sg.Text('Qual será o provedor de Email?')],
            [sg.Checkbox('Gmail', key= 'gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('sim', 'cartao', key='aceita'), sg.Radio('não', 'cartao', key=('naoAceita'))],
            [sg.Button('Enviar')],
            #Criar um output na tela, imprimindo as informações.
            [sg.Output(size=(40,10))]
        ]
        #janela
        janela = sg.Window("Dados do usuário").layout(layout)
        #extrair
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        #Se quiser que o tela não feche e continue executando
        #Deve-se criar um while True () e colocar a linha da extração dentro e colocar um self. antes de janela (o window)
        
        #Transformando em variável para exibição?
        nome = self.values['nome']
        idade = self.values ['idade']
        gmail = self.values ['gmail']
        outlook = self.values ['outlook']
        yahoo = self.values ['yahoo']
        aceitaCartao = self.values ['aceita']
        naoAceitaCartao = self.values ['naoAceita']
        #Como será exibido
        print(f'nome: {nome}')
        print(f'idade: {idade}')
        print(f'gmail: {gmail}')
        print(f'outlook: {outlook}')
        print(f'yahoo: {yahoo}')
        print(f'Aceita o cartão: {aceitaCartao}')
        print(f'Não aceita o cartão: {naoAceitaCartao}')

tela = TelaPython()
tela.Iniciar()