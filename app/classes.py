from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class PedidoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.nome_estabelecimento = Label(text='Pizza do Papa')
        self.layout.add_widget(self.nome_estabelecimento)
        
        self.nome_usuario = TextInput(hint_text='Digite seu nome', multiline=False)
        self.layout.add_widget(self.nome_usuario)
        
        self.opcoes_sabores = Spinner(text='Escolha um sabor',
                                              values=('Quatro queijos', 'Mussarela', 'Portuguesa', 'Calabresa', 'Frango catupiry', 'Crocante'))
        self.layout.add_widget(self.opcoes_sabores)
        pizzas_tradicionais    = ['Quatro queijos', 'Mussarela', 'Calabresa']
        pizzas_especiais       = ['Portuguesa', 'Frango catupiry', 'Crocante']

        self.opcoes_tamanho = Spinner(text='Escolha um tamanho',
                                      values=('Broto', 'Média', 'Grande', 'Gigante'))
        self.layout.add_widget(self.opcoes_tamanho)
        pizzas_tamanhos = ['Broto', 'Média', 'Grande', 'Gigante']
        
        self.quantidade_label = Label(text='Digite a quantidade')
        self.layout.add_widget(self.quantidade_label)
        self.quantidade = TextInput(hint_text='Quantidade', multiline=False, input_type='number')
        self.layout.add_widget(self.quantidade)
        
        self.tipo_pagamento = Spinner(text='Escolha o tipo de pagamento',
                                      values=('À vista (espécie)', 'À vista (pix)', 'À vista (cartão de crédito)', 'Parcelado 2x no cartão de crédito'))
        self.layout.add_widget(self.tipo_pagamento)
        
        self.calcular_button = Button(text='Calcular', size_hint_y=None, height=40)
        self.calcular_button.bind(on_press=self.calcular_total)
        self.layout.add_widget(self.calcular_button)
        
        self.resultado = Label(text='', halign='center')
        self.layout.add_widget(self.resultado)
        
        self.reset_button = Button(text='Limpar Campos', size_hint_y=None, height=40)
        self.reset_button.bind(on_press=self.limpar_campos)
        self.layout.add_widget(self.reset_button)
        
        self.sair_button = Button(text='Sair', size_hint_y=None, height=40)
        self.sair_button.bind(on_press=self.stop)
        self.layout.add_widget(self.sair_button)
        
        return self.layout
    
    def calcular_total(self, instance):
        valor_total = 0

        if self.opcoes_tamanhos == self.pizzas_tamanhos[0]:
            for j in self.pizzas_tradicionais:
                if j == self.opcoes_sabores:
                    valor_total =+ 19.90
                else:
                    valor_total =+ 24.90
        if self.opcoes_tamanhos == self.pizzas_tamanhos[1]:
            for j in self.pizzas_tradicionais:
                if j == self.opcoes_sabores:
                    valor_total =+ 29.90
                else:
                    valor_total =+ 34.90
        if self.opcoes_tamanhos == self.pizzas_tamanhos[2]:
            for j in self.pizzas_tradicionais:
                if j == self.opcoes_sabores:
                    valor_total =+ 39.90
                else:
                    valor_total =+ 44.90
        if self.opcoes_tamanhos == self.pizzas_tamanhos[3]:
            for j in self.pizzas_tradicionais:
                if j == self.opcoes_sabores:
                    valor_total =+ 49.90
                else:
                    valor_total =+ 54.90

        nome_usuario = self.nome_usuario.text
        self.resultado.text = f'O valor da compra de {nome_usuario} totalizou R$ {valor_total * self.quantidade}'
    
    def limpar_campos(self, instance):
        self.nome_usuario.text = ''
        self.opcoes_estabelecimento.text = 'Escolha um item'
        self.quantidade.text = ''
        self.tipo_pagamento.text = 'Escolha o tipo de pagamento'
        self.resultado.text = ''

if __name__ == '__main__':
    PedidoApp().run()
