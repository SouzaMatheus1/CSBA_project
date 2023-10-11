from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout

class PedidoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10)
        
        # NOME PIZZARIA
        self.nome_estabelecimento = Label(text='Pizza do Papa')
        self.layout.add_widget(self.nome_estabelecimento)
        
        # NOME CCLIENTE
        self.nome_usuario = TextInput(hint_text='Digite seu nome', multiline=False)
        self.layout.add_widget(self.nome_usuario)
        
        # SABOR PIZZA
        self.opcoes_sabores = Spinner(text='Escolha um sabor',
                                              values=('Quatro queijos', 'Mussarela', 'Portuguesa', 'Calabresa', 'Frango catupiry', 'Crocante'))
        self.layout.add_widget(self.opcoes_sabores)
        self.pizzas_tradicionais    = ['Quatro queijos', 'Mussarela', 'Calabresa']
        self.pizzas_especiais       = ['Portuguesa', 'Frango catupiry', 'Crocante']

        # TAMANHO PIZZA
        self.opcoes_tamanhos = Spinner(text='Escolha o tamanho',
                                      values=('Broto', 'Média', 'Grande', 'Gigante'))
        self.layout.add_widget(self.opcoes_tamanhos)
        self.pizzas_tamanhos = ['Broto', 'Média', 'Grande', 'Gigante']
        
        # QUANTIDADE PIZZAS
        self.quantidade_label = Label(text='Digite a quantidade')
        self.layout.add_widget(self.quantidade_label)
        self.quantidade = TextInput(hint_text='Quantidade', multiline=False, input_type='number')
        self.layout.add_widget(self.quantidade)
        
        # GRID DE PAGAMENTOS
        self.pagamento_layout = GridLayout(cols=4, padding=12)
        
        self.pagamento_a_vista_esp = CheckBox(group='pagamento', active=False)
        self.pagamento_label_esp = Label(text='À vista (espécie)')
        self.pagamento_layout.add_widget(self.pagamento_a_vista_esp)
        self.pagamento_layout.add_widget(self.pagamento_label_esp)
        
        self.pagamento_a_vista_pix = CheckBox(group='pagamento', active=False)
        self.pagamento_label_pix = Label(text='À vista (pix)')
        self.pagamento_layout.add_widget(self.pagamento_a_vista_pix)
        self.pagamento_layout.add_widget(self.pagamento_label_pix)
        
        self.pagamento_a_vista_cartao = CheckBox(group='pagamento', active=False)
        self.pagamento_label_cartao = Label(text='À vista (cartão de crédito)')
        self.pagamento_layout.add_widget(self.pagamento_a_vista_cartao)
        self.pagamento_layout.add_widget(self.pagamento_label_cartao)
        
        self.pagamento_parcelado = CheckBox(group='pagamento', active=False)
        self.pagamento_label_parcelado = Label(text='Parcelado 2x cartão de crédito')
        self.pagamento_layout.add_widget(self.pagamento_parcelado)
        self.pagamento_layout.add_widget(self.pagamento_label_parcelado)

        self.layout.add_widget(self.pagamento_layout)
        
        # CALCULAR CONTA
        self.calcular_button = Button(text='Calcular', size_hint_y=None, height=40)
        self.calcular_button.bind(on_press=self.calcular_total)
        self.layout.add_widget(self.calcular_button)
        
        self.resultado = Label(text='', halign='center')
        self.layout.add_widget(self.resultado)
        
        # LIMPAR CAMPOS
        self.reset_button = Button(text='Limpar Campos', size_hint_y=None, height=40)
        self.reset_button.bind(on_press=self.limpar_campos)
        self.layout.add_widget(self.reset_button)
        
        # SAIR APLICAÇÃO
        self.sair_button = Button(text='Sair', size_hint_y=None, height=40)
        self.sair_button.bind(on_press=self.stop)
        self.layout.add_widget(self.sair_button)
        
        return self.layout
    
    def calcular_total(self, instance):
        valor_total = 0

        try:
            quantidade = int(self.quantidade.text)
        except ValueError:
            self.resultado.text = 'Quantidade inválida, tente novamente!'
            return

        tamanho_selecionado = self.opcoes_tamanhos.text
        sabor_selecionado = self.opcoes_sabores.text

        if tamanho_selecionado == self.pizzas_tamanhos[0]:
            for j in self.pizzas_tradicionais:
                if j == sabor_selecionado:
                    valor_total += 1990
                    break
                else:
                    valor_total += 2490
                    break
        elif tamanho_selecionado == self.pizzas_tamanhos[1]:
            for j in self.pizzas_tradicionais:
                if j == sabor_selecionado:
                    valor_total += 2990
                    break
                else:
                    valor_total += 3490
                    break
        elif tamanho_selecionado == self.pizzas_tamanhos[2]:
            for j in self.pizzas_tradicionais:
                if j == sabor_selecionado:
                    valor_total += 3990
                    break
                else:
                    valor_total += 4490
                    break
        elif tamanho_selecionado == self.pizzas_tamanhos[3]:
            for j in self.pizzas_tradicionais:
                if j == sabor_selecionado:
                    valor_total += 4990
                    break
                else:
                    valor_total += 5490
                    break

        nome_usuario = self.nome_usuario.text
        self.resultado.text = f'O valor da compra de {nome_usuario} totalizou R$ {(valor_total * quantidade)/100:.2f}'
    
    def limpar_campos(self, instance):
        self.nome_usuario.text = ''
        self.opcoes_sabores.text = 'Escolha um sabor'
        self.quantidade.text = ''
        self.tipo_pagamento.text = 'Escolha o tipo de pagamento'
        self.resultado.text = ''

if __name__ == '__main__':
    PedidoApp().run()
