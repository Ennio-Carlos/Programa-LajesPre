import gi
import math
from Dimensionamento import Dimensionamento

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from random import randrange
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

class Handler(object):
    def __init__(self):
        self.Stack: Gtk.Stack = Builder.get_object('stack')
        self.calc = Dimensionamento()
        self.usar_estilo()
        #PAVPRE ============================================================================
        #self.combobox_engaste_1 = Builder.get_object('combobox_engaste_1')
        #self.combobox_engaste_1.connect('changed', self.on_combobox_engaste_1_changet)
        self.entry_inter_1 = Builder.get_object('entry_inter_1')
        self.tipo_de_engaste_1 = Builder.get_object('tipo_de_engaste_1')
        self.resultado_momento_pos = Builder.get_object('resultado_momento_pos')
        self.operacao_1 = None
        self.entry_vao_livre_1 = Builder.get_object('entry_vao_livre_1')
        self.entry_revestimento_1 = Builder.get_object('entry_revestimento_1')
        self.combobox_acidental_1 = Builder.get_object('combobox_acidental_1')
        self.combobox_psi2_1 = Builder.get_object('combobox_psi2_1')
        self.entry_nome_laje_1 = Builder.get_object('entry_nome_laje_1')
        #COMBOBOX
        self.combobox_bloco_1 = Builder.get_object('combobox_bloco_1')
        self.combobox_bloco_1.connect('changed', self.on_combobox_bloco_1_changet)
        self.combobox_aco_1 = Builder.get_object('combobox_aco_1')
        #self.combobox_aco_1.connect('changed', self.on_combobox_aco_1_changet)
        self.combobox_fyk_1 = Builder.get_object('combobox_fyk_1')
        #self.combobox_fyk_1.connect('changed', self.on_combobox_fyk_1_changet)
        self.combobox_fyk_trelica_1 = Builder.get_object('combobox_fyk_trelica_1')
        #self.combobox_fyk_trelica_1.connect('changed', self.on_combobox_fyk_trelica_1_changet)
        self.combobox_agressividade_1 = Builder.get_object('combobox_agressividade_1')
        self.combobox_agressividade_1.connect('changed', self.on_combobox_agressividade_1_changet)
        self.combobox_bitola_1 = Builder.get_object('combobox_bitola_1')
        self.combobox_bitola_1.connect('changed', self.on_combobox_bitola_1_changet)
        #SETAR
        self.label_permamente_1 = Builder.get_object('label_permamente_1')
        self.entry_comprimento_1 = Builder.get_object('entry_comprimento_1')
        self.label_ht_1= Builder.get_object('label_ht_1')
        self.label_be_1 = Builder.get_object('label_be_1')
        self.entry_capa_1 = Builder.get_object('entry_capa_1')
        self.entry_cobrimento_1 = Builder.get_object('entry_cobrimento_1')
        self.entry_escoramento_dias_1 = Builder.get_object('entry_escoramento_dias_1')
        self.combobox_fck_1 = Builder.get_object('combobox_fck_1')
        self.fyk_1 = Builder.get_object('fyk_1')
        self.entry_d_1 = Builder.get_object('entry_d_1')
        self.label_resultado_area_total = Builder.get_object('label_resultado_area_total')
        self.label_resultado_area_adicional = Builder.get_object('label_resultado_area_adicional')
        self.entry_bv_1 = Builder.get_object('entry_bv_1')
        self.entry_hv_1 = Builder.get_object('entry_hv_1')
        self.aco_1 = Builder.get_object('aco_1')
        self.Iii_1 = Builder.get_object('Iii_1')
        self.label_flecha_imediata = Builder.get_object('label_flecha_imediata')
        self.label_flecha_tempo = Builder.get_object('label_flecha_tempo')
        self.label_flecha_total = Builder.get_object('label_flecha_total')
        self.imagem_informacao = Builder.get_object('imagem_informacao')
        self.label_quantidade_barras_1 = Builder.get_object('label_quantidade_barras_1')
        self.label_volume = Builder.get_object('label_volume')
        self.label_lajotas = Builder.get_object('label_lajotas')
        self.label_vigotas = Builder.get_object('label_vigotas')
        self.label_aco = Builder.get_object('label_aco')
        #OBJETOS DA TELA DE RESULTADOS
        self.label_vao_livre = Builder.get_object('label_vao_livre')
        self.label_comprimento_vao = Builder.get_object('label_comprimento_vao')
        self.label_peso_proprio = Builder.get_object('label_peso_proprio')
        self.label_revestimento = Builder.get_object('label_revestimento')
        self.label_acidental = Builder.get_object('label_acidental')
        self.label_p_total = Builder.get_object('label_p_total')
        self.label_limite_total = Builder.get_object('label_limite_total')
        self.label_contra_flecha = Builder.get_object('label_contra_flecha')
        self.label_area_minima = Builder.get_object('label_area_minima')
        self.label_cortante = Builder.get_object('label_cortante')
        self.label_bielas = Builder.get_object('label_bielas')
        self.label_fck = Builder.get_object('label_fck')
        self.label_tipo_aco = Builder.get_object('label_tipo_aco')
        self.label_dias_escora = Builder.get_object('label_dias_escora')
        self.label_bloco_escolhido = Builder.get_object('label_bloco_escolhido')
        self.label_aco_esa = Builder.get_object('label_trelica_escolhida')
        self.label_hb = Builder.get_object('label_hb')
        self.label_be = Builder.get_object('label_be')
        self.label_ce = Builder.get_object('label_ce')
        self.label_trelica_escolhida = Builder.get_object('label_trelica_escolhida')

        # OBJETOS DA TELA DE RESULTADOS PARA GERAR PDF

        self.entry_nome_laje = Builder.get_object('entry_nome_laje')




        # LAJOTA CERAMICA ============================================================================
        #self.combobox_engaste_2 = Builder.get_object('combobox_engaste_2')
        #self.combobox_engaste_2.connect('changed', self.on_combobox_engaste_2_changet)
        self.entry_inter_2 = Builder.get_object('entry_inter_2')
        self.tipo_de_engaste_2 = Builder.get_object('tipo_de_engaste_2')
        self.resultado_momento_pos = Builder.get_object('resultado_momento_pos')
        self.operacao_2 = None
        self.entry_vao_livre_2 = Builder.get_object('entry_vao_livre_2')
        self.entry_revestimento_2 = Builder.get_object('entry_revestimento_2')
        self.combobox_acidental_2 = Builder.get_object('combobox_acidental_2')
        self.combobox_psi2_2 = Builder.get_object('combobox_psi2_2')
        self.entry_nome_laje_2 = Builder.get_object('entry_nome_laje_2')
        # COMBOBOX
        self.combobox_bloco_2 = Builder.get_object('combobox_bloco_2')
        self.combobox_bloco_2.connect('changed', self.on_combobox_bloco_2_changet)
        self.combobox_aco_2 = Builder.get_object('combobox_aco_2')
        # self.combobox_aco_1.connect('changed', self.on_combobox_aco_1_changet)
        self.combobox_fyk_2 = Builder.get_object('combobox_fyk_2')
        #self.combobox_fyk_2.connect('changed', self.on_combobox_fyk_2_changet)
        self.combobox_fyk_trelica_2 = Builder.get_object('combobox_fyk_trelica_2')
        # self.combobox_fyk_trelica_1.connect('changed', self.on_combobox_fyk_trelica_1_changet)
        self.combobox_agressividade_2 = Builder.get_object('combobox_agressividade_2')
        self.combobox_agressividade_2.connect('changed', self.on_combobox_agressividade_2_changet)
        #self.combobox_bitola_1 = Builder.get_object('combobox_bitola_1')
        #self.combobox_bitola_1.connect('changed', self.on_combobox_bitola_1_changet)
        # SETAR
        self.check_button1_2 = Builder.get_object('check_button1_2')
        self.check_button1_2.connect('toggled', self.on_button_toggled2)
        self.label_permamente_2 = Builder.get_object('label_permamente_2')
        self.entry_comprimento_2 = Builder.get_object('entry_comprimento_2')
        self.entry_hb_2 = Builder.get_object('entry_hb_2')
        self.entry_be_2 = Builder.get_object('entry_be_2')
        self.entry_ah_2 = Builder.get_object('entry_ah_2')
        self.entry_av_2 = Builder.get_object('entry_av_2')
        self.entry_ce_2 = Builder.get_object('entry_ce_2')
        self.entry_capa_2 = Builder.get_object('entry_capa_2')
        self.entry_cobrimento_2 = Builder.get_object('entry_cobrimento_2')
        self.entry_escoramento_dias_2 = Builder.get_object('entry_escoramento_dias_2')
        self.combobox_fck_2 = Builder.get_object('combobox_fck_2')
        self.fyk_2 = Builder.get_object('fyk_2')
        self.entry_d_2 = Builder.get_object('entry_d_2')
        self.label_resultado_area_total = Builder.get_object('label_resultado_area_total')
        self.label_resultado_area_adicional = Builder.get_object('label_resultado_area_adicional')
        self.entry_bv_2 = Builder.get_object('entry_bv_2')
        self.entry_hv_2 = Builder.get_object('entry_hv_2')
        self.aco_2 = Builder.get_object('aco_2')
        self.Iii_2 = Builder.get_object('Iii_2')
        self.label_flecha_imediata = Builder.get_object('label_flecha_imediata')
        self.label_flecha_tempo = Builder.get_object('label_flecha_tempo')
        self.label_flecha_total = Builder.get_object('label_flecha_total')
        self.imagem_informacao = Builder.get_object('imagem_informacao')
        self.imagem_informacao_pavpre = Builder.get_object('imagem_informacao_pavpre')
        self.label_quantidade_barras_2 = Builder.get_object('label_quantidade_barras_2')
        self.label_volume = Builder.get_object('label_volume')
        self.label_lajotas = Builder.get_object('label_lajotas')
        self.label_vigotas = Builder.get_object('label_vigotas')
        self.label_aco = Builder.get_object('label_aco')





        # LAJOTA ISOPOR ============================================================================
        #self.combobox_engaste_3 = Builder.get_object('combobox_engaste_3')
        #self.combobox_engaste_3.connect('changed', self.on_combobox_engaste_3_changet)
        self.entry_inter_3 = Builder.get_object('entry_inter_3')
        self.tipo_de_engaste_3 = Builder.get_object('tipo_de_engaste_3')
        self.resultado_momento_pos = Builder.get_object('resultado_momento_pos')
        self.operacao_3 = None
        self.entry_vao_livre_3 = Builder.get_object('entry_vao_livre_3')
        self.entry_revestimento_3 = Builder.get_object('entry_revestimento_3')
        self.combobox_acidental_3 = Builder.get_object('combobox_acidental_3')
        self.combobox_psi2_3 = Builder.get_object('combobox_psi2_3')
        self.entry_nome_laje_3 = Builder.get_object('entry_nome_laje_3')
        # COMBOBOX
        self.combobox_bloco_3 = Builder.get_object('combobox_bloco_3')
        self.combobox_bloco_3.connect('changed', self.on_combobox_bloco_3_changet)
        self.combobox_aco_3 = Builder.get_object('combobox_aco_3')
        # self.combobox_aco_1.connect('changed', self.on_combobox_aco_1_changet)
        self.combobox_fyk_3 = Builder.get_object('combobox_fyk_3')
        #self.combobox_fyk_3.connect('changed', self.on_combobox_fyk_3_changet)
        self.combobox_fyk_trelica_3 = Builder.get_object('combobox_fyk_trelica_3')
        # self.combobox_fyk_trelica_1.connect('changed', self.on_combobox_fyk_trelica_1_changet)
        self.combobox_agressividade_3 = Builder.get_object('combobox_agressividade_3')
        self.combobox_agressividade_3.connect('changed', self.on_combobox_agressividade_3_changet)
        # self.combobox_bitola_1 = Builder.get_object('combobox_bitola_1')
        # self.combobox_bitola_1.connect('changed', self.on_combobox_bitola_1_changet)
        # SETAR
        self.check_button1_3 = Builder.get_object('check_button1_3')
        self.check_button1_3.connect('toggled', self.on_button_toggled3)
        self.label_permamente_3 = Builder.get_object('label_permamente_3')
        self.entry_comprimento_3 = Builder.get_object('entry_comprimento_3')
        self.entry_hb_3 = Builder.get_object('entry_hb_3')
        self.entry_be_3 = Builder.get_object('entry_be_3')
        self.entry_ah_3 = Builder.get_object('entry_ah_3')
        self.entry_av_3 = Builder.get_object('entry_av_3')
        self.entry_ce_3 = Builder.get_object('entry_ce_3')
        self.entry_capa_3 = Builder.get_object('entry_capa_3')
        self.entry_cobrimento_3 = Builder.get_object('entry_cobrimento_3')
        self.entry_escoramento_dias_3 = Builder.get_object('entry_escoramento_dias_3')
        self.combobox_fck_3 = Builder.get_object('combobox_fck_3')
        self.fyk_2 = Builder.get_object('fyk_3')
        self.entry_d_3 = Builder.get_object('entry_d_3')
        self.label_resultado_area_total = Builder.get_object('label_resultado_area_total')
        self.label_resultado_area_adicional = Builder.get_object('label_resultado_area_adicional')
        self.entry_bv_3 = Builder.get_object('entry_bv_3')
        self.entry_hv_3 = Builder.get_object('entry_hv_3')
        self.aco_3 = Builder.get_object('aco_3')
        self.Iii_3 = Builder.get_object('Iii_3')
        self.label_flecha_imediata = Builder.get_object('label_flecha_imediata')
        self.label_flecha_tempo = Builder.get_object('label_flecha_tempo')
        self.label_flecha_total = Builder.get_object('label_flecha_total')
        self.imagem_informacao = Builder.get_object('imagem_informacao')
        self.label_quantidade_barras_3 = Builder.get_object('label_quantidade_barras_3')
        self.label_volume = Builder.get_object('label_volume')
        self.label_lajotas = Builder.get_object('label_lajotas')
        self.label_vigotas = Builder.get_object('label_vigotas')
        self.label_aco = Builder.get_object('label_aco')

        # OBJETOS DA TELA DE RESULTADOS
        self.label_vao_livre = Builder.get_object('label_vao_livre')
        self.label_comprimento_vao = Builder.get_object('label_comprimento_vao')
        self.label_peso_proprio = Builder.get_object('label_peso_proprio')
        self.label_revestimento = Builder.get_object('label_revestimento')
        self.label_acidental = Builder.get_object('label_acidental')
        self.label_p_total = Builder.get_object('label_p_total')
        self.label_limite_total = Builder.get_object('label_limite_total')
        self.label_contra_flecha = Builder.get_object('label_contra_flecha')


    def on_main_window_destroy(self, Window):
        Gtk.main_quit()

    def usar_estilo(self):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('static\estilo_botoes_e_texto.css')
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen.get_default(),
                                              css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)



#JANELA ENTRADA DE DADOS LAJOTA
#==============================================================
    
#ENTRADA DE DADOS - TRELICA
# ==============================================================









#BOTÕES PAGINA INICIAL
#========================================================================
    def on_button_dimensionar_clicked(self, button):
        self.Stack.set_visible_child_name('view_enchimentos')

    def on_button_pavpre_informacoes_clicked(self, button):
        self.imagem_informacao_pavpre.set_from_file('static/imagens/aaaa.png')
        self.informacao_pavpre('Caro Usuário', '      As cubetas do sistema patenteado PavPré possuem um dispositivo de travas'
                                               ' embutidas que permite a desforma completa da laje, sem a perda de nenhum' 
                                               ' elemento. As fôrmas seguem a modularização de 54 x 61 cm e alturas que variam' 
                                               ' de 21 até 35 cm.' 
                                               '\n        As cubetas do sistema PavPré também contam com o' 
                                               ' Tapa Nervuras, elemento plástico que elimina as nervuras em uma' 
                                               ' direção, constituindo a laje unidirecional.', 'gtk-index')

    def informacao_pavpre(self, param, param1, param2):
        informacao_pavpre: Gtk.MessageDialog = Builder.get_object('informacao_pavpre')
        informacao_pavpre.props.text = param
        informacao_pavpre.props.secondary_text = param1
        informacao_pavpre.props.icon_name = param2
        informacao_pavpre.show_all()
        informacao_pavpre.run()
        informacao_pavpre.hide()

    def on_button_informacoes_clicked(self, button):
        self.informacao('Caro Usuário', ' LAJESPRÉ é o resultado de uma monografia apresentada'
                                               '\n     ao Curso de Engenharia Civil do Centro Universitário'
                                               '\n  Christus como requisito para a obtenção do título de '
                                               '\n                 Bacharel em Engenharia Civil.', 'gtk-index')
    def on_button_creditos_clicked(self, button):
        self.informacao('Resposáveis pelo desenvolvimento deste Sofware: ', 'Orientando: Ennio Carlos Barbosa Silva'
                                                                             '\n  Orientador: Bergson da Silva Matias', 'gtk-index')

    def informacao(self, param, param1, param2):
        informacao: Gtk.MessageDialog = Builder.get_object('informacao')
        informacao.props.text = param
        informacao.props.secondary_text = param1
        informacao.props.icon_name = param2
        informacao.show_all()
        informacao.run()
        informacao.hide()

# BOTÕES PAGINA DE ELEMENTOS
# ========================================================================
# VOLTAR PARA TELA INICIAL
    def on_button_voltar_1_clicked(self, button):
        self.Stack.set_visible_child_name('view_inicial')
#ENTRAR NO DIMENSIONAMENTO DO PAVPRE
    def on_button_pavpre_clicked(self, button):
        self.Stack.set_visible_child_name('view_dimensionamento_1')
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('static\estilo_texto_habilitado.css')
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen.get_default(),
                                              css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    def on_button_voltar_enchimentos1_clicked(self, button):
        self.Stack.set_visible_child_name('view_enchimentos')
    def on_button_voltar_dimensionamento1_clicked(self, button):
        self.Stack.set_visible_child_name('view_enchimentos')
#ENTRAR NO DIMENSIONAMENTO DA LAJOTA
    def on_button_lajota_clicked(self, button):
        self.Stack.set_visible_child_name('view_dimensionamento_2')
        self.entry_hb_2.set_sensitive(False)
        self.entry_ah_2.set_sensitive(False)
        self.entry_av_2.set_sensitive(False)
        self.entry_be_2.set_sensitive(False)
        self.entry_ce_2.set_sensitive(False)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('static\estilo_texto_inabilitado.css')
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen.get_default(),
                                              css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    def on_button_voltar_enchimentos2_clicked(self, button):
        self.Stack.set_visible_child_name('view_enchimentos')
    def on_button_voltar_dimensionamento2_clicked(self, button):
        self.Stack.set_visible_child_name('view_dimensionamento_2')
#ENTRAR DIMENSIONAMENTO ISOPOR
    def on_button_isopor_clicked(self, button):
        self.Stack.set_visible_child_name('view_dimensionamento_3')
        self.entry_hb_3.set_sensitive(False)
        self.entry_ah_3.set_sensitive(False)
        self.entry_av_3.set_sensitive(False)
        self.entry_be_3.set_sensitive(False)
        self.entry_ce_3.set_sensitive(False)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('static\estilo_texto_inabilitado.css')
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen.get_default(),
                                              css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    def on_button_voltar_enchimentos3_clicked(self, button):
        self.Stack.set_visible_child_name('view_enchimentos')
    def on_button_voltar_dimensionamento3_clicked(self, button):
        self.Stack.set_visible_child_name('view_dimensionamento_3')


#INFORMAÇÕES DE ERRO===================
    def informacao_erro_kmd(self, param, param1, param2):
        informacao_erro_kmd: Gtk.MessageDialog = Builder.get_object('informacao_aviso')
        informacao_erro_kmd.props.text = param
        informacao_erro_kmd.props.secondary_text = param1
        informacao_erro_kmd.props.icon_name = param2
        informacao_erro_kmd.show_all()
        informacao_erro_kmd.run()
        informacao_erro_kmd.hide()

#TELA COM ENTRADA DE DADOS E RESULTADOS
#======================================================
#PAVPRE
    def on_combobox_bloco_1_changet(self, changet):
        bloco = self.combobox_bloco_1.get_active_text()
        if bloco is not None:

            if bloco == 'H21 / 54':
                self.label_ht_1.set_text('21')
                self.label_be_1.set_text('54')
            elif bloco == 'H23 / 54':
                self.label_ht_1.set_text('23')
                self.label_be_1.set_text('54')
            elif bloco == 'H26 / 54':
                self.label_ht_1.set_text('26')
                self.label_be_1.set_text('54')
            elif bloco == 'H31 / 54':
                self.label_ht_1.set_text('31')
                self.label_be_1.set_text('54')
            elif bloco == 'H35 / 54':
                self.label_ht_1.set_text('35')
                self.label_be_1.set_text('54')

    def ler_informacao_1(self):
        string = self.entry_inter_1.get_text(), \
                 self.entry_vao_livre_1.get_text(), \
                 self.entry_revestimento_1, \
                 self.combobox_acidental_1.get_text(), \
                 self.label_ht_1.get_text(), \
                 self.label_be_1.get_text(), \
                 self.entry_capa_1.get_text(), \
                 self.entry_bv_1.get_text(), \
                 self.entry_hv_1.get_text()


        try:
            numero = int(string)
        except:
            numero = float(string)
        return numero


    def informacao_tabela(self, param, param1, param2):
        informacao_erro: Gtk.MessageDialog = Builder.get_object('informacao_tabela')
        informacao_erro.props.text = param
        informacao_erro.props.secondary_text = param1
        informacao_erro.props.icon_name = param2
        informacao_erro.show_all()
        informacao_erro.run()
        informacao_erro.hide()
    def informacao_aviso(self, param, param1, param2):
        informacao_erro: Gtk.MessageDialog = Builder.get_object('informacao_aviso')
        informacao_erro.props.text = param
        informacao_erro.props.secondary_text = param1
        informacao_erro.props.icon_name = param2
        informacao_erro.show_all()
        informacao_erro.run()
        informacao_erro.hide()
# TELA DE DIMENSIONAMENTO
    #====================================================================================================
    #INFORMAÇÕES COM IMAGENS
    def on_button_informacao_acidental_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/cargas_verticais.jpg')
        self.informacao_tabela('Cargas Verticais (NBR 6120/2019)', '', 'dialog-warning-symbolic')
    def on_button_informacao_psi_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/acoes_acidentais.jpg')
        self.informacao_tabela('Coeficiente de ponderação ELU (NBR 6118/2014)', '', 'dialog-warning-symbolic')
    def on_button_informacao_trelica_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/tabela_trelica.jpg')
        self.informacao_tabela('Treliças Padronizadas','','dialog-warning-symbolic')
    def on_button_informacao_agressividade_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/tabela_agressividade.jpg')
        self.informacao_tabela('Classe de agressividade Ambiental (NBR 6118/2014)','', 'dialog-warning-symbolic')
    #SETAR CLASSE DE AGRESSIVIDADE
    #=====================================================================================================
    def on_combobox_agressividade_1_changet(self, changet):
        agressividade = self.combobox_agressividade_1.get_active_text()
        if agressividade is not None:

            if agressividade == 'I - Fraca':
                self.entry_cobrimento_1.set_text('2')
            elif agressividade == 'II - Moderada':
                self.entry_cobrimento_1.set_text('2.5')
            elif agressividade == 'III - Forte':
                self.entry_cobrimento_1.set_text('3.5')
            elif agressividade == 'IV - Muito Forte':
                self.entry_cobrimento_1.set_text('4.5')
    def on_button_realizar_dimensionamento_1_clicked(self, button):
    #MENSAGENS DE AVISO!!!!
    #==============================================================================================
        agressividade = self.combobox_agressividade_1.get_active_text()
        cobrimento = self.entry_cobrimento_1.get_text()

        if agressividade == 'I - Fraca' and cobrimento < str(2):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')
        elif agressividade == 'II - Moderada' and cobrimento < str(2.5):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')
        elif agressividade == 'III - Forte' and cobrimento < str(3.5):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')
        elif agressividade == 'IV - Muito Forte' and cobrimento < str(4.5):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')



    #AREA DE AÇO
        #MOMENTO POSITIVO
        r = self.entry_revestimento_1.get_text()
        self.label_revestimento.set_text(str(r))
        q = self.combobox_acidental_1.get_active_text()
        l = self.entry_vao_livre_1.get_text()
        ht = self.label_ht_1.get_text()
        self.label_hb.set_text(str(ht))
        be = self.label_be_1.get_text()
        self.label_be.set_text(str(be))
        capa = self.entry_capa_1.get_text()
        bv = self.entry_bv_1.get_text()
        hv = self.entry_hv_1.get_text()
        c = self.entry_comprimento_1.get_text()
        self.label_ce.set_text("66")
        if c=="":
            c = 0
        else:
            c = self.entry_comprimento_1.get_text()

        if r == '' \
                or l == '' \
                or ht == '' \
                or be == '' \
                or hv == '' \
                or bv == '' \
                or cobrimento == '' \
                or capa == '':
            self.informacao_aviso('Caro Usuário',
                                  'Preencha todos os campos!',
                                  'dialog-warning-symbolic')


        else:
            acidental = self.calc.funcoes['acidental'](float(q))
            self.label_acidental.set_text(str("%.2f" % acidental))
            vao_livre = self.calc.funcoes['vao_livre'](float(l))
            self.label_vao_livre.set_text(str("%.2f" % vao_livre))
            vao_comprimento = self.calc.funcoes['vao_comprimento'](float(c))
            self.label_comprimento_vao.set_text(str("%.2f" % vao_comprimento))
            bf = self.calc.funcoes['bf'](float(be),
                                             float(0),
                                             float(bv))

            bw = self.calc.funcoes['bw'](float(bv),
                                         float(0))

            pp_c = self.calc.funcoes['pp_c'](float(capa),
                                             float(bf),
                                             float(ht),
                                             float(bw),
                                             float(0),
                                             float(3),
                                             float(0),
                                             float(0))
            pp_c1 = pp_c/(bf/100)
            self.label_peso_proprio.set_text(str("%.2f" % pp_c1))
            p_total = self.calc.funcoes['p_total'](float(pp_c),
                                                   float(r),
                                                   float(q),
                                                   float(bf))
            p_total1 = p_total/(bf/100)
            self.label_p_total.set_text(str("%.2f" % p_total1))

            mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
            md_pos = mk_pos*1.4
            md_pos1 = md_pos/(bf/100)
            self.resultado_momento_pos.set_text(str("%.2f" % md_pos1))

            self.calculo_1()

    def calculo_1 (self):#Bi_apoiado
        #ÁREA DE AÇO POSITIVA
        global d0, phi_trelica, fyk_trelica, yii, fyk
        r = self.entry_revestimento_1.get_text()
        q = self.combobox_acidental_1.get_active_text()
        l = self.entry_vao_livre_1.get_text()
        c = self.entry_comprimento_1.get_text()
        if c=="":
            c = 0
        else:
            c = self.entry_comprimento_1.get_text()
        ht = self.label_ht_1.get_text()
        capa = self.entry_capa_1.get_text()
        bv = self.entry_bv_1.get_text()
        be = self.label_be_1.get_text()
        hv = self.entry_hv_1.get_text()
        escoramento = self.entry_escoramento_dias_1.get_text()
        self.label_dias_escora.set_text(escoramento)
        alpha_c = 5 / 384
        fyk_adicional = self.combobox_fyk_1.get_active_text()
        if fyk_adicional == 'CA 50':
            fyk = 500
        elif fyk_adicional == 'CA 60':
            fyk = 600
        self.label_tipo_aco.set_text(fyk_adicional)
        fyk_da_trelica = self.combobox_fyk_trelica_1.get_active_text()
        if fyk_da_trelica == 'CA 50':
            fyk_trelica = 500
        elif fyk_da_trelica == 'CA 60':
            fyk_trelica = 600

        bw = self.calc.funcoes['bw'](float(bv),
                                     float(0))
        bf = self.calc.funcoes['bf'](float(be),
                                     float(0),
                                     float(bv))
        pp_c = self.calc.funcoes['pp_c'](float(capa),
                                         float(bf),
                                         float(ht),
                                         float(bw),
                                         float(0),
                                         float(3),
                                         float(be),
                                         float(0))
        p_total = self.calc.funcoes['p_total'](float(pp_c),
                                               float(r),
                                               float(q),
                                               float(bf))

        cobrimento = self.entry_cobrimento_1.get_text()
        aco = self.combobox_aco_1.get_active_text()
        self.label_trelica_escolhida.set_text(aco)
        if aco == 'TR 8644':
            phi_trelica = '4.2'
        elif aco == 'TR 8645':
            phi_trelica = '5'
        elif aco == 'TR 12645':
            phi_trelica = '5'
        elif aco == 'TR 12646':
            phi_trelica = '6'
        elif aco == 'TR 16745':
            phi_trelica = '5'
        elif aco == 'TR 16746':
            phi_trelica = '6'
        elif aco == 'TR 20745':
            phi_trelica = '5'
        elif aco == 'TR 20756':
            phi_trelica = '6'
        elif aco == 'TR 25856':
            phi_trelica = '6'
        elif aco == 'TR 25858':
            phi_trelica = '8'
        elif aco == 'TR 30856':
            phi_trelica = '6'
        elif aco == 'TR 30858':
            phi_trelica = '8'

        d = self.calc.funcoes['d'](float(ht),
                                   float(3),
                                   float(capa),
                                   float(hv),
                                   float(cobrimento),
                                   float(phi_trelica))

        mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
        fck = self.combobox_fck_1.get_active_text()
        self.label_fck.set_text(fck)
        d0 = self.calc.funcoes['d0'](float(mk_pos),
                                     float(fck),
                                     float(bf),
                                     float(capa))


        d = float(d)
        if d >= d0:
            mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
            kmd = self.calc.funcoes['kmd'](float(mk_pos),
                                           float(bf),
                                           float(fck),
                                           float(d))
            if kmd > 0.251:
                self.informacao_erro_kmd('Caro Usuário', 'Linha neutra fora dos domínios de deformação', 'emblem-default')

            else:
                kx = self.calc.funcoes['kx'](float(kmd))

                as_total = self.calc.funcoes['as_total'](float(mk_pos),
                                                         float(d),
                                                         float(kx),
                                                         float(fyk_trelica))
                self.label_resultado_area_total.set_text(str("%.2f" % as_total))
                as_adicional = self.calc.funcoes['as_adicional'](float(as_total),
                                                                 float(phi_trelica),
                                                                 float(fyk),
                                                                 float(fyk_trelica))
                if as_adicional < 0:
                    self.label_resultado_area_adicional.set_text(str(0.00))
                else:
                    self.label_resultado_area_adicional.set_text(str("%.2f" % as_adicional))


                # AS MÍNIMA E CORTANTE==========================================================
                pmin = self.calc.funcoes['pmin'](float(fck),
                                                 float(fyk_trelica))
                as_min = self.calc.funcoes['as_min'](float(pmin),
                                                     float(capa),
                                                     float(bf),
                                                     float(ht),
                                                     float(bw))
                self.label_area_minima.set_text(str("%.2f" % as_min))

                Vk = self.calc.funcoes['Vk'](float(p_total),
                                             float(l))
                trd = self.calc.funcoes['trd'](float(fck))
                k = self.calc.funcoes['k'](float(d))
                p1 = self.calc.funcoes['p1'](float(as_total),
                                             float(bw),
                                             float(d))
                Vrd1 = self.calc.funcoes['Vrd1'](float(trd),
                                                 float(k),
                                                 float(p1),
                                                 float(bw),
                                                 float(d))
                alpha_v1 = self.calc.funcoes['alpha_v1'](float(fck))
                if alpha_v1 > 0.5:
                    av1 = 0.5
                else:
                    av1 = alpha_v1
                Vrd2 = self.calc.funcoes['Vrd2'](float(av1),
                                                 float(fck),
                                                 float(bw),
                                                 float(d))
                print(bf, bw, pp_c, p_total, mk_pos, d0, d, kmd, kx, as_total, as_adicional)
                print(fyk, fyk_trelica)
                Vd = Vk*1.4
                if Vd < Vrd1:
                    self.label_cortante.set_text("Não é necessário")
                else:
                    self.label_cortante.set_text("Redimensionar")
                if Vd < Vrd2:
                    self.label_bielas.set_text("Não")
                else:
                    self.label_bielas.set_text("Sim")
                print ("d=",d,"BW=",bw, Vd, Vrd1, av1, Vrd2)
                self.Stack.set_visible_child_name('view_resultado')
        elif d < d0: # Dimensionamento linha neutra na alma
            mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
            M1 = self.calc.funcoes['M1'](float(fck),
                                         float(capa),
                                         float(bf),
                                         float(bw),
                                         float(d))
            M2 = self.calc.funcoes['M2'](float(mk_pos),
                                         float(M1))

            kmd2 = self.calc.funcoes['kmd2'](float(M2),
                                             float(d),
                                             float(fck),
                                             float(bw))
            print('M1, m2, kmd2', M1, M2, kmd2)
            if kmd2 > 0.251:
                self.informacao_erro_kmd('Caro Usuário', 'Linha neutra fora dos domínios de deformação',
                                         'emblem-default')

            else:
                kx2 = self.calc.funcoes['kx2'](float(kmd2))
                As_1 = self.calc.funcoes['As_1'](float(M1),
                                                 float(d),
                                                 float(capa),
                                                 float(fyk_trelica))
                As_2 = self.calc.funcoes['As_2'](float(M2),
                                                 float(kx2),
                                                 float(d),
                                                 float(fyk_trelica))
                as_total2 = self.calc.funcoes['as_total2'](float(As_1),
                                                           float(As_2))
                as_adicional2 = self.calc.funcoes['as_adicional2'](float(as_total2),
                                                                   float(phi_trelica),
                                                                   float(fyk),
                                                                   float(fyk_trelica))
                self.label_resultado_area_total.set_text(str("%.2f" % as_total2))
                self.label_resultado_area_adicional.set_text(str("%.2f" % as_adicional2))
                # AS MÍNIMA E CORTANTE==========================================================
                pmin = self.calc.funcoes['pmin'](float(fck),
                                                 float(fyk))
                as_min = self.calc.funcoes['as_min'](float(pmin),
                                                     float(capa),
                                                     float(bf),
                                                     float(hb),
                                                     float(bw))
                self.label_area_minima.set_text(str("%.2f" % as_min))

                Vk = self.calc.funcoes['Vk'](float(p_total),
                                             float(l))
                trd = self.calc.funcoes['trd'](float(fck))
                k = self.calc.funcoes['k'](float(d))
                p1 = self.calc.funcoes['p1'](float(as_total2),
                                             float(bw),
                                             float(d))
                Vrd1 = self.calc.funcoes['Vrd1'](float(trd),
                                                 float(k),
                                                 float(p1),
                                                 float(bw),
                                                 float(d))
                alpha_v1 = self.calc.funcoes['alpha_v1'](float(fck))
                if alpha_v1 > 0.5:
                    av1 = 0.5
                else:
                    av1 = alpha_v1
                Vrd2 = self.calc.funcoes['Vrd2'](float(av1),
                                                 float(fck),
                                                 float(bw),
                                                 float(d))
                print(bf, bw, pp_c, p_total, mk_pos, d0, d, kmd, kx, as_total, as_adicional)
                print(fyk, fyk_trelica)
                Vd = Vk*1.4
                if Vd < Vrd1:
                    self.label_cortante.set_text("Não é necessário")
                else:
                    self.label_cortante.set_text("Redimensionar")
                if Vd < Vrd2:
                    self.label_bielas.set_text("Não")
                else:
                    self.label_bielas.set_text("Sim")
                print ("d=",d,"BW=",bw, Vd, Vrd1, av1, Vrd2)
                self.Stack.set_visible_child_name('view_resultado')




        #DEFORMAÇÕES
        as_total = self.label_resultado_area_total.get_text()
        psi2 = self.combobox_psi2_1.get_active_text()
        p_total_els = self.calc.funcoes['p_total_els'](float(pp_c),
                                                       float(r),
                                                       float(q),
                                                       float(bf),
                                                       float(psi2))
        mk_els = self.calc.funcoes['mk_els'](float(p_total_els), float(l))
        Ecs = self.calc.funcoes['Ecs'](float(fck))
        fctm = self.calc.funcoes['fctm'](float(fck))
        ag = self.calc.funcoes['ag'](float(bf),
                                     float(bw),
                                     float(capa),
                                     float(ht),
                                     float(3),
                                     float(hv))
        ycg = self.calc.funcoes['ycg'](float(capa),
                                       float(bf),
                                       float(bw),
                                       float(ht),
                                       float(hv),
                                       float(3),
                                       float(ag))
        Ic = self.calc.funcoes['Ic'](float(bf),
                                     float(bw),
                                     float(capa),
                                     float(ht),
                                     float(hv),
                                     float(ycg),
                                     float(3))

        Mr = self.calc.funcoes['Mr'](float(fctm),
                                     float(Ic),
                                     float(ht),
                                     float(hv),
                                     float(ycg),
                                     float(3),
                                     float(capa))
        if d >= d0:
            a1 = self.calc.funcoes['a1'](float(bf))
            a2 = self.calc.funcoes['a2'](float(capa),
                                         float(bf),
                                         float(bf),
                                         float(Ecs),
                                         float(as_total))
            a3 = self.calc.funcoes['a3'](float(d),
                                         float(Ecs),
                                         float(as_total),
                                         float(capa),
                                         float(bf),
                                         float(bf),)
            yii = self.calc.funcoes['yii'](float(a1),
                                           float(a2),
                                           float(a3))
            Iii_mesa = self.calc.funcoes['Iii_mesa'](float(bf),
                                                     float(yii),
                                                     float(Ecs),
                                                     float(as_total),
                                                     float(d))
            self.Iii_1.set_text(str("%.2f" % Iii_mesa))
        elif d < d0: # Dimensionamento linha neutra na alma
            a1 = self.calc.funcoes['a1'](float(bw))
            a2 = self.calc.funcoes['a2'](float(capa),
                                         float(bf),
                                         float(bw),
                                         float(Ecs),
                                         float(as_total))
            a3 = self.calc.funcoes['a3'](float(d),
                                         float(Ecs),
                                         float(as_total),
                                         float(capa),
                                         float(bf),
                                         float(bw),)
            yii = self.calc.funcoes['yii'](float(a1),
                                           float(a2),
                                           float(a3))
            Iii_alma = self.calc.funcoes['Iii_alma'](float(bf),
                                                     float(bw),
                                                     float(capa),
                                                     float(yii),
                                                     float(Ecs),
                                                     float(as_total),
                                                     float(d))
            self.Iii_1.set_text(str("%.2f" % Iii_alma))
        Iii = self.Iii_1.get_text()
        EI_eq = self.calc.funcoes['EI_eq'](float(Ecs),
                                           float(Mr),
                                           float(mk_els),
                                           float(Ic),
                                           float(Iii))
        w0 = self.calc.funcoes['w0'](float(alpha_c),
                                     float(p_total_els),
                                     float(l),
                                     float(EI_eq))
        t0 = self.calc.funcoes['t0'](float(escoramento))
        ksi_t0 = self.calc.funcoes['ksi_t0'](float(t0))
        alpha_f = self.calc.funcoes['alpha_f'](float(ksi_t0))
        flecha_diferida = alpha_f*w0
        flecha_total = self.calc.funcoes['flecha_total'](float(w0),
                                                        float(alpha_f))
        self.label_flecha_imediata.set_text(str("%.2f" % w0))
        self.label_flecha_tempo.set_text(str("%.2f" % flecha_diferida))
        self.label_flecha_total.set_text(str("%.2f" % flecha_total))
        flecha_lim = self.calc.funcoes['flecha_lim'](float(l))
        contra_flecha = self.calc.funcoes['contra_flecha'](float(flecha_total),
                                                           float(l))
        self.label_limite_total.set_text(str("%.2f" % flecha_lim))
        cf_lim = float(l)/350
        if contra_flecha > 0 and contra_flecha < cf_lim:
            self.label_contra_flecha.set_text(str("%.2f" % contra_flecha))
        elif contra_flecha > cf_lim:
            self.label_contra_flecha.set_text("Limite atingido (L/350)")
        elif contra_flecha <= 0:
            self.label_contra_flecha.set_text("Não é necessário")

        print('deformação', yii, bf, bw, capa, ht, ag, ycg, Ic, Ecs, Mr, mk_els, Ic, yii, Iii, EI_eq)

        # QUANTITATIVO
        por_enchimento = self.calc.funcoes['por_enchimento'](float(be),
                                                             float(0),
                                                             float(ht),
                                                             float(capa),
                                                             float(bv))
        volume = self.calc.funcoes['volume'](float(c),
                                             float(l),
                                             float(por_enchimento),
                                             float(ht),
                                             float(capa))
        self.label_volume.set_text(str("%.2f" % volume))
        vigota = self.calc.funcoes['vigota'](float(bv),
                                             float(be),
                                             float(0),
                                             float(c))
        self.label_vigotas.set_text(str("%.2f" % vigota))
        lajota_1 = self.calc.funcoes['lajota_1'](float(bv),
                                                 float(be),
                                                 float(0),
                                                 float(c))
        lajota_2 = self.calc.funcoes['lajota_2'](float(l),
                                                 float(66))
        quantidade_lajota = self.calc.funcoes['quantidade_lajota'](float(lajota_1),
                                                                   float(lajota_2))
        self.label_lajotas.set_text(str("%.2f" % quantidade_lajota))
        vao_livre = self.entry_vao_livre_1.get_text()
        self.label_vao_livre.set_text(str(vao_livre))
        comprimento_vao = self.entry_comprimento_1.get_text()
        self.label_comprimento_vao.set_text(str(comprimento_vao))



# QUANTIDADES DE BARRAS
    def on_combobox_bitola_1_changet(self, changet):
        aco_adicional = self.label_resultado_area_adicional.get_text()
        l = self.entry_vao_livre_1.get_text()
        bitola = self.combobox_bitola_1.get_active_text()
        if bitola is not None:
            if bitola == 'Ø 6.3':
                area_bitola = self.calc.funcoes['area_bitola'](float(6.3))
                quantidade_barras = self.calc.funcoes['quantidade_barras'](float(aco_adicional),
                                                                           float(area_bitola))
                self.label_quantidade_barras_1.set_text(str("%.2f" % quantidade_barras))

            elif bitola == 'Ø 8':
                area_bitola = self.calc.funcoes['area_bitola'](float(8))
                quantidade_barras = self.calc.funcoes['quantidade_barras'](float(aco_adicional),
                                                                           float(area_bitola))
                self.label_quantidade_barras_1.set_text(str("%.2f" % quantidade_barras))

            elif bitola == 'Ø 10':
                area_bitola = self.calc.funcoes['area_bitola'](float(10))
                quantidade_barras = self.calc.funcoes['quantidade_barras'](float(aco_adicional),
                                                                           float(area_bitola))
                self.label_quantidade_barras_1.set_text(str("%.2f" % quantidade_barras))

            elif bitola == 'Ø 12.5':
                area_bitola = self.calc.funcoes['area_bitola'](float(12.5))
                quantidade_barras = self.calc.funcoes['quantidade_barras'](float(aco_adicional),
                                                                           float(area_bitola))
                self.label_quantidade_barras_1.set_text(str("%.2f" % quantidade_barras))
            elif bitola == 'Ø 16':
                area_bitola = self.calc.funcoes['area_bitola'](float(16))
                quantidade_barras = self.calc.funcoes['quantidade_barras'](float(aco_adicional),
                                                                           float(area_bitola))
                self.label_quantidade_barras_1.set_text(str("%.2f" % quantidade_barras))


    #==============================================================================================

# LAJOTA
    def on_combobox_bloco_2_changet(self, changet):
        bloco = self.combobox_bloco_2.get_active_text()
        if bloco is not None:

            if bloco == 'H7.5 / 34 / 18':
                self.entry_hb_2.set_text('7.5')
                self.entry_be_2.set_text('34')
                self.entry_ah_2.set_text('1.5')
                self.entry_av_2.set_text('3.0')
                self.entry_ce_2.set_text('18')
            elif bloco == 'H8 / 25 / 20':
                self.entry_hb_2.set_text('8')
                self.entry_be_2.set_text('25')
                self.entry_ah_2.set_text('1.5')
                self.entry_av_2.set_text('3.0')
                self.entry_ce_2.set_text('20')
            elif bloco == 'H8 / 30 / 20':
                self.entry_hb_2.set_text('8')
                self.entry_be_2.set_text('30')
                self.entry_ah_2.set_text('1.5')
                self.entry_av_2.set_text('3.0')
                self.entry_ce_2.set_text('20')
            elif bloco == 'H10 / 40 / 19':
                self.entry_hb_2.set_text('10')
                self.entry_be_2.set_text('40')
                self.entry_ah_2.set_text('1.5')
                self.entry_av_2.set_text('3.0')
                self.entry_ce_2.set_text('19')
            elif bloco == 'H12 / 34 / 19':
                self.entry_hb_2.set_text('12')
                self.entry_be_2.set_text('34')
                self.entry_ah_2.set_text('1.5')
                self.entry_av_2.set_text('3.0')
                self.entry_ce_2.set_text('19')
            elif bloco == 'H13 / 40 / 19':
                self.entry_hb_2.set_text('13')
                self.entry_be_2.set_text('40')
                self.entry_ah_2.set_text('1.5')
                self.entry_av_2.set_text('3.0')
                self.entry_ce_2.set_text('19')
            elif bloco == 'H16 / 40 / 19':
                self.entry_hb_2.set_text('16')
                self.entry_be_2.set_text('40')
                self.entry_ah_2.set_text('1.5')
                self.entry_av_2.set_text('3.0')
                self.entry_ce_2.set_text('19')
            elif bloco == 'H19 / 36 / 19':
                self.entry_hb_2.set_text('19')
                self.entry_be_2.set_text('36')
                self.entry_ah_2.set_text('1.5')
                self.entry_av_2.set_text('3.0')
                self.entry_ce_2.set_text('19')
            elif bloco == 'H20 / 40 / 19':
                self.entry_hb_2.set_text('20')
                self.entry_be_2.set_text('40')
                self.entry_ah_2.set_text('1.5')
                self.entry_av_2.set_text('3.0')
                self.entry_ce_2.set_text('19')

    def on_combobox_fyk_2_changet(self, changet):
        fyk = self.combobox_fyk_2.get_active_text()
        if fyk is not None:

            if fyk == 'CA 50':
                self.entry_fyk_2.set_text('500')
            elif fyk == 'CA 60':
                self.entry_fyk_2.set_text('600')

    def on_button_toggled2(self, button):
        self.entry_hb_2.set_sensitive(False)
        self.entry_ah_2.set_sensitive(False)
        self.entry_av_2.set_sensitive(False)
        self.entry_be_2.set_sensitive(False)
        self.entry_ce_2.set_sensitive(False)
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('static\estilo_texto_inabilitado.css')
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen.get_default(),
                                              css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        if self.check_button1_2.get_active():
            self.entry_hb_2.set_sensitive(True)
            self.entry_ah_2.set_sensitive(True)
            self.entry_av_2.set_sensitive(True)
            self.entry_be_2.set_sensitive(True)
            self.entry_ce_2.set_sensitive(True)
            css_provider = Gtk.CssProvider()
            css_provider.load_from_path('static\estilo_texto_habilitado.css')
            screen = Gdk.Screen()
            style_context = Gtk.StyleContext()
            style_context.add_provider_for_screen(screen.get_default(),
                                                  css_provider,
                                                  Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def on_button_trelica_informacao_2_clicked(self, button):
        self.informacao_trelica('Caro Usuário', 'O PavPré é um \nsistema blá blá blá...', 'emblem-default')

    def informacao_trelica(self, param, param1, param2):
        informacao_trelica: Gtk.MessageDialog = Builder.get_object('informacao_trelica')
        # informacao_trelica.props.text = param
        # informacao_trelica.props.secondary_text = param1
        # informacao_trelica.props.icon_name = param2
        informacao_trelica.show_all()
        informacao_trelica.run()
        informacao_trelica.hide()

    def ler_informacao_2(self):
        string = self.entry_inter_2.get_text(), \
                 self.entry_vao_livre_2.get_text(), \
                 self.entry_revestimento_2, \
                 self.combobox_acidental_2.get_text(), \
                 self.entry_hb_2.get_text(), \
                 self.entry_be_2.get_text(), \
                 self.entry_ah_2.get_text(), \
                 self.entry_av_2.get_text(), \
                 self.entry_ce_2.get_text(), \
                 self.entry_capa_2.get_text(), \
                 self.entry_bv_2.get_text(), \
                 self.entry_be_2.get_text(), \
                 self.entry_hv_2.get_text()

        try:
            numero = int(string)
        except:
            numero = float(string)
        return numero
    # TELA DE DIMENSIONAMENTO
    # ====================================================================================================
    # INFORMAÇÕES COM IMAGENS
    def on_button_informacao_acidental_2_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/apoiado_e_engastado.png')
        self.informacao_tabela('Caro Usuário', 'O PavPré é um \nsistema blá blá blá...', 'image-x-generic')

    def on_button_informacao_psi_2_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/apoiado_e_engastado.png')
        self.informacao_tabela('Caro Usuário', 'O PavPré é um \nsistema blá blá blá...', 'image-x-generic')

    def on_button_informacao_trelica_2_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/tabela_trelica.png')
        self.informacao_tabela('Caro Usuário', 'O PavPré é um \nsistema blá blá blá...', 'image-x-generic')

    def on_button_informacao_agressividade_2_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/tabela_agressividade.png')
        self.informacao_tabela('Tabela 6.1 - Classe de agressividade Ambiental (NBR 6118/2014)', '',
                               'image-x-generic')

    # SETAR CLASSE DE AGRESSIVIDADE
    # =====================================================================================================
    def on_combobox_agressividade_2_changet(self, changet):
        agressividade = self.combobox_agressividade_2.get_active_text()
        if agressividade is not None:

            if agressividade == 'I - Fraca':
                self.entry_cobrimento_2.set_text('2')
            elif agressividade == 'II - Moderada':
                self.entry_cobrimento_2.set_text('2.5')
            elif agressividade == 'III - Forte':
                self.entry_cobrimento_2.set_text('3.5')
            elif agressividade == 'IV - Muito Forte':
                self.entry_cobrimento_2.set_text('4.5')

    def on_button_realizar_dimensionamento_2_clicked(self, button):
        # MENSAGENS DE AVISO!!!!
        # ==============================================================================================
        agressividade = self.combobox_agressividade_2.get_active_text()
        cobrimento = self.entry_cobrimento_2.get_text()

        if agressividade == 'I - Fraca' and cobrimento < str(2):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')
        elif agressividade == 'II - Moderada' and cobrimento < str(2.5):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')
        elif agressividade == 'III - Forte' and cobrimento < str(3.5):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')
        elif agressividade == 'IV - Muito Forte' and cobrimento < str(4.5):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')

        # AREA DE AÇO
        # MOMENTO POSITIVO
        r = self.entry_revestimento_2.get_text()
        self.label_revestimento.set_text(str(r))
        q = self.combobox_acidental_2.get_active_text()
        b = 1300  # kgf/m³
        l = self.entry_vao_livre_2.get_text()
        hb = self.entry_hb_2.get_text()
        self.label_hb.set_text(str(hb))
        ah = self.entry_ah_2.get_text()
        av = self.entry_av_2.get_text()
        capa = self.entry_capa_2.get_text()
        bv = self.entry_bv_2.get_text()
        be = self.entry_be_2.get_text()
        self.label_be.set_text(str(be))
        hv = self.entry_hv_2.get_text()
        ce = self.entry_ce_2.get_text()
        self.label_ce.set_text(str(ce))
        c = self.entry_comprimento_2.get_text()
        if c=="":
            c = 0
        else:
            c = self.entry_comprimento_2.get_text()

        # self.label_acidental.set_active_text(str("%.2f" % r))
        if r == '' \
                or l == '' \
                or hb == '' \
                or be == '' \
                or ah == '' \
                or av == '' \
                or ce == '' \
                or hv == '' \
                or bv == '' \
                or cobrimento == '' \
                or capa == '':
            self.informacao_aviso('Caro Usuário',
                                  'Preencha todos os campos!',
                                  'dialog-warning-symbolic')


        else:
            acidental = self.calc.funcoes['acidental'](float(q))
            self.label_acidental.set_text(str("%.2f" % acidental))
            vao_livre = self.calc.funcoes['vao_livre'](float(l))
            self.label_vao_livre.set_text(str("%.2f" % vao_livre))
            vao_comprimento = self.calc.funcoes['vao_comprimento'](float(c))
            self.label_comprimento_vao.set_text(str("%.2f" % vao_comprimento))
            bf = self.calc.funcoes['bf'](float(be),
                                         float(ah),
                                         float(bv))

            bw = self.calc.funcoes['bw'](float(bv),
                                         float(ah))

            pp_c = self.calc.funcoes['pp_c'](float(capa),
                                             float(bf),
                                             float(hb),
                                             float(bw),
                                             float(ah),
                                             float(av),
                                             float(be),
                                             float(b))
            pp_c1 = pp_c / (bf / 100)
            self.label_peso_proprio.set_text(str("%.2f" % pp_c1))
            p_total = self.calc.funcoes['p_total'](float(pp_c),
                                                   float(r),
                                                   float(q),
                                                   float(bf))
            p_total1 = p_total / (bf / 100)
            self.label_p_total.set_text(str("%.2f" % p_total1))

            mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
            md_pos = mk_pos * 1.4
            md_pos1 = md_pos / (bf / 100)
            self.resultado_momento_pos.set_text(str("%.2f" % md_pos1))
            self.calculo_2()

    def calculo_2(self):
        # ÁREA DE AÇO
        global d0, phi_trelica, fyk_trelica, yii, fyk
        r = self.entry_revestimento_2.get_text()
        q = self.combobox_acidental_2.get_active_text()
        b = 1300
        l = self.entry_vao_livre_2.get_text()
        c = self.entry_comprimento_2.get_text()
        if c=="":
            c = 0
        else:
            c = self.entry_comprimento_2.get_text()
        hb = self.entry_hb_2.get_text()
        ah = self.entry_ah_2.get_text()
        av = self.entry_av_2.get_text()
        capa = self.entry_capa_2.get_text()
        bv = self.entry_bv_2.get_text()
        be = self.entry_be_2.get_text()
        ce = self.entry_ce_2.get_text()
        hv = self.entry_hv_2.get_text()
        escoramento = self.entry_escoramento_dias_2.get_text()
        self.label_dias_escora.set_text(escoramento)
        alpha_c = 5 / 384
        fyk_adicional = self.combobox_fyk_2.get_active_text()
        if fyk_adicional == 'CA 50':
            fyk = 500
        elif fyk_adicional == 'CA 60':
            fyk = 600
        self.label_tipo_aco.set_text(fyk_adicional)
        fyk_da_trelica = self.combobox_fyk_trelica_2.get_active_text()
        if fyk_da_trelica == 'CA 50':
            fyk_trelica = 500
        elif fyk_da_trelica == 'CA 60':
            fyk_trelica = 600
        bw = self.calc.funcoes['bw'](float(bv),
                                     float(ah))
        bf = self.calc.funcoes['bf'](float(be),
                                     float(ah),
                                     float(bv))
        pp_c = self.calc.funcoes['pp_c'](float(capa),
                                         float(bf),
                                         float(hb),
                                         float(bw),
                                         float(ah),
                                         float(av),
                                         float(be),
                                         float(b))
        p_total = self.calc.funcoes['p_total'](float(pp_c),
                                               float(r),
                                               float(q),
                                               float(bf))

        cobrimento = self.entry_cobrimento_2.get_text()
        aco = self.combobox_aco_2.get_active_text()
        self.label_trelica_escolhida.set_text(aco)
        if aco == 'TR 8644':
            phi_trelica = '4.2'
            p_trelica = 0.735
        elif aco == 'TR 8645':
            phi_trelica = '5'
        elif aco == 'TR 12645':
            phi_trelica = '5'
        elif aco == 'TR 12646':
            phi_trelica = '6'
        elif aco == 'TR 16745':
            phi_trelica = '5'
        elif aco == 'TR 16746':
            phi_trelica = '6'
        elif aco == 'TR 20745':
            phi_trelica = '5'
        elif aco == 'TR 20756':
            phi_trelica = '6'
        elif aco == 'TR 25856':
            phi_trelica = '6'
        elif aco == 'TR 25858':
            phi_trelica = '8'
        elif aco == 'TR 30856':
            phi_trelica = '6'
        elif aco == 'TR 30858':
            phi_trelica = '8'

        d = self.calc.funcoes['d'](float(hb),
                                   float(av),
                                   float(capa),
                                   float(hv),
                                   float(cobrimento),
                                   float(phi_trelica))

        mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
        fck = self.combobox_fck_2.get_active_text()
        self.label_fck.set_text(fck)
        d0 = self.calc.funcoes['d0'](float(mk_pos),
                                     float(fck),
                                     float(bf),
                                     float(capa))

        d = float(d)
        if d >= d0:
            mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
            kmd = self.calc.funcoes['kmd'](float(mk_pos),
                                           float(bf),
                                           float(fck),
                                           float(d))
            if kmd > 0.251:
                self.informacao_erro_kmd('Caro Usuário', 'Linha neutra fora dos domínios de deformação', 'emblem-default')

            else:
                kx = self.calc.funcoes['kx'](float(kmd))

                as_total = self.calc.funcoes['as_total'](float(mk_pos),
                                                         float(d),
                                                         float(kx),
                                                         float(fyk_trelica))
                self.label_resultado_area_total.set_text(str("%.2f" % as_total))
                as_adicional = self.calc.funcoes['as_adicional'](float(as_total),
                                                                 float(phi_trelica),
                                                                 float(fyk),
                                                                 float(fyk_trelica))
                if as_adicional < 0:
                    self.label_resultado_area_adicional.set_text(str(0.00))
                else:
                    self.label_resultado_area_adicional.set_text(str("%.2f" % as_adicional))



                # AS MÍNIMA E CORTANTE==========================================================
                pmin = self.calc.funcoes['pmin'](float(fck),
                                                 float(fyk))
                as_min = self.calc.funcoes['as_min'](float(pmin),
                                                     float(capa),
                                                     float(bf),
                                                     float(hb),
                                                     float(bw))
                self.label_area_minima.set_text(str("%.2f" % as_min))

                Vk = self.calc.funcoes['Vk'](float(p_total),
                                             float(l))
                trd = self.calc.funcoes['trd'](float(fck))
                k = self.calc.funcoes['k'](float(d))
                p1 = self.calc.funcoes['p1'](float(as_total),
                                             float(bw),
                                             float(d))
                Vrd1 = self.calc.funcoes['Vrd1'](float(trd),
                                                 float(k),
                                                 float(p1),
                                                 float(bw),
                                                 float(d))
                alpha_v1 = self.calc.funcoes['alpha_v1'](float(fck))
                if alpha_v1 > 0.5:
                    av1 = 0.5
                else:
                    av1 = alpha_v1
                Vrd2 = self.calc.funcoes['Vrd2'](float(av1),
                                                 float(fck),
                                                 float(bw),
                                                 float(d))

                Vd = Vk*1.4
                if Vd < Vrd1:
                    self.label_cortante.set_text("Não é necessário")
                else:
                    self.label_cortante.set_text("Redimensionar")
                if Vd < Vrd2:
                    self.label_bielas.set_text("Não")
                else:
                    self.label_bielas.set_text("Sim")
                print ("d=",d,"BW=",bw, Vd, Vrd1, av1, Vrd2)
                self.Stack.set_visible_child_name('view_resultado')
        elif d < d0:  # Dimensionamento linha neutra na alma
            mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
            M1 = self.calc.funcoes['M1'](float(fck),
                                         float(capa),
                                         float(bf),
                                         float(bw),
                                         float(d))
            M2 = self.calc.funcoes['M2'](float(mk_pos),
                                         float(M1))
            print('M1 e M2= ', M1, M2)
            kmd2 = self.calc.funcoes['kmd2'](float(M2),
                                             float(d),
                                             float(fck),
                                             float(bw))
            print('M1, m2, kmd2', M1, M2, kmd2)
            if kmd2 > 0.251:
                self.informacao_erro_kmd('Caro Usuário', 'Linha neutra fora dos domínios de deformação', 'emblem-default')

            else:
                kx2 = self.calc.funcoes['kx2'](float(kmd2))
                As_1 = self.calc.funcoes['As_1'](float(M1),
                                                 float(d),
                                                 float(capa),
                                                 float(fyk_trelica))
                As_2 = self.calc.funcoes['As_2'](float(M2),
                                                 float(kx2),
                                                 float(d),
                                                 float(fyk_trelica))
                as_total2 = self.calc.funcoes['as_total2'](float(As_1),
                                                           float(As_2))
                as_adicional2 = self.calc.funcoes['as_adicional2'](float(as_total2),
                                                                   float(phi_trelica),
                                                                   float(fyk),
                                                                   float(fyk_trelica))
                self.label_resultado_area_total.set_text(str("%.2f" % as_total2))
                self.label_resultado_area_adicional.set_text(str("%.2f" % as_adicional2))
                # AS MÍNIMA E CORTANTE==========================================================
                pmin = self.calc.funcoes['pmin'](float(fck),
                                                 float(fyk))
                as_min = self.calc.funcoes['as_min'](float(pmin),
                                                     float(capa),
                                                     float(bf),
                                                     float(hb),
                                                     float(bw))
                self.label_area_minima.set_text(str("%.2f" % as_min))

                Vk = self.calc.funcoes['Vk'](float(p_total),
                                             float(l))
                trd = self.calc.funcoes['trd'](float(fck))
                k = self.calc.funcoes['k'](float(d))
                p1 = self.calc.funcoes['p1'](float(as_total2),
                                             float(bw),
                                             float(d))
                Vrd1 = self.calc.funcoes['Vrd1'](float(trd),
                                                 float(k),
                                                 float(p1),
                                                 float(bw),
                                                 float(d))
                alpha_v1 = self.calc.funcoes['alpha_v1'](float(fck))
                if alpha_v1 > 0.5:
                    av1 = 0.5
                else:
                    av1 = alpha_v1
                Vrd2 = self.calc.funcoes['Vrd2'](float(av1),
                                                 float(fck),
                                                 float(bw),
                                                 float(d))

                Vd = Vk*1.4
                if Vd < Vrd1:
                    self.label_cortante.set_text("Não é necessário")
                else:
                    self.label_cortante.set_text("Redimensionar")
                if Vd < Vrd2:
                    self.label_bielas.set_text("Não")
                else:
                    self.label_bielas.set_text("Sim")
                print ("d=",d,"BW=",bw, Vd, Vrd1, av1, Vrd2)
                self.Stack.set_visible_child_name('view_resultado')

        # DEFORMAÇÕES
        as_total = self.label_resultado_area_total.get_text()
        psi2 = self.combobox_psi2_2.get_active_text()
        p_total_els = self.calc.funcoes['p_total_els'](float(pp_c),
                                                       float(r),
                                                       float(q),
                                                       float(bf),
                                                       float(psi2))
        mk_els = self.calc.funcoes['mk_els'](float(p_total_els), float(l))
        Ecs = self.calc.funcoes['Ecs'](float(fck))
        fctm = self.calc.funcoes['fctm'](float(fck))
        ag = self.calc.funcoes['ag'](float(bf),
                                     float(bw),
                                     float(capa),
                                     float(hb),
                                     float(av),
                                     float(hv))
        ycg = self.calc.funcoes['ycg'](float(capa),
                                       float(bf),
                                       float(bw),
                                       float(hb),
                                       float(hv),
                                       float(av),
                                       float(ag))
        Ic = self.calc.funcoes['Ic'](float(bf),
                                     float(bw),
                                     float(capa),
                                     float(hb),
                                     float(hv),
                                     float(ycg),
                                     float(av))

        Mr = self.calc.funcoes['Mr'](float(fctm),
                                     float(Ic),
                                     float(hb),
                                     float(hv),
                                     float(ycg),
                                     float(av),
                                     float(capa))
        if d >= d0:
            a1 = self.calc.funcoes['a1'](float(bf))
            a2 = self.calc.funcoes['a2'](float(capa),
                                         float(bf),
                                         float(bf),
                                         float(Ecs),
                                         float(as_total))
            a3 = self.calc.funcoes['a3'](float(d),
                                         float(Ecs),
                                         float(as_total),
                                         float(capa),
                                         float(bf),
                                         float(bf), )
            yii = self.calc.funcoes['yii'](float(a1),
                                           float(a2),
                                           float(a3))
            Iii_mesa = self.calc.funcoes['Iii_mesa'](float(bf),
                                                     float(yii),
                                                     float(Ecs),
                                                     float(as_total),
                                                     float(d))
            self.Iii_1.set_text(str("%.2f" % Iii_mesa))
        elif d < d0:  # Dimensionamento linha neutra na alma
            a1 = self.calc.funcoes['a1'](float(bw))
            a2 = self.calc.funcoes['a2'](float(capa),
                                         float(bf),
                                         float(bw),
                                         float(Ecs),
                                         float(as_total))
            a3 = self.calc.funcoes['a3'](float(d),
                                         float(Ecs),
                                         float(as_total),
                                         float(capa),
                                         float(bf),
                                         float(bw), )
            yii = self.calc.funcoes['yii'](float(a1),
                                           float(a2),
                                           float(a3))
            Iii_alma = self.calc.funcoes['Iii_alma'](float(bf),
                                                     float(bw),
                                                     float(capa),
                                                     float(yii),
                                                     float(Ecs),
                                                     float(as_total),
                                                     float(d))
            self.Iii_1.set_text(str("%.2f" % Iii_alma))
        Iii = self.Iii_1.get_text()
        EI_eq = self.calc.funcoes['EI_eq'](float(Ecs),
                                           float(Mr),
                                           float(mk_els),
                                           float(Ic),
                                           float(Iii))
        w0 = self.calc.funcoes['w0'](float(alpha_c),
                                     float(p_total_els),
                                     float(l),
                                     float(EI_eq))
        t0 = self.calc.funcoes['t0'](float(escoramento))
        ksi_t0 = self.calc.funcoes['ksi_t0'](float(t0))
        alpha_f = self.calc.funcoes['alpha_f'](float(ksi_t0))
        flecha_diferida = alpha_f * w0
        flecha_total = self.calc.funcoes['flecha_total'](float(w0),
                                                         float(alpha_f))
        self.label_flecha_imediata.set_text(str("%.2f" % w0))
        self.label_flecha_tempo.set_text(str("%.2f" % flecha_diferida))
        self.label_flecha_total.set_text(str("%.2f" % flecha_total))
        flecha_lim = self.calc.funcoes['flecha_lim'](float(l))
        contra_flecha = self.calc.funcoes['contra_flecha'](float(flecha_total),
                                                           float(l))
        self.label_limite_total.set_text(str("%.2f" % flecha_lim))
        cf_lim = float(l)/350
        if contra_flecha > 0 and contra_flecha < cf_lim:
            self.label_contra_flecha.set_text(str("%.2f" % contra_flecha))
        elif contra_flecha > cf_lim:
            self.label_contra_flecha.set_text("Limite atingido (L/350)")
        elif contra_flecha <= 0:
            self.label_contra_flecha.set_text("Não é necessário")

        print('deformação', Ecs, ycg, Ic, Mr, fctm, p_total_els, mk_els, yii, Iii, EI_eq)

        # QUANTITATIVO
        por_enchimento = self.calc.funcoes['por_enchimento'](float(be),
                                                             float(ah),
                                                             float(hb),
                                                             float(capa),
                                                             float(bv))
        volume = self.calc.funcoes['volume'](float(c),
                                             float(l),
                                             float(por_enchimento),
                                             float(hb),
                                             float(capa))
        self.label_volume.set_text(str("%.2f" % volume))
        vigota = self.calc.funcoes['vigota'](float(bv),
                                             float(be),
                                             float(ah),
                                             float(c))
        self.label_vigotas.set_text(str("%.2f" % vigota))
        lajota_1 = self.calc.funcoes['lajota_1'](float(bv),
                                                 float(be),
                                                 float(ah),
                                                 float(c))
        lajota_2 = self.calc.funcoes['lajota_2'](float(l),
                                                 float(ce))
        quantidade_lajota = self.calc.funcoes['quantidade_lajota'](float(lajota_1),
                                                                   float(lajota_2))
        self.label_lajotas.set_text(str("%.2f" % quantidade_lajota))
        vao_livre = self.entry_vao_livre_2.get_text()
        self.label_vao_livre.set_text(str(vao_livre))
        comprimento_vao = self.entry_comprimento_2.get_text()
        self.label_comprimento_vao.set_text(str(comprimento_vao))

        # ==============================================================================================


    # ISOPOR
    def on_combobox_bloco_3_changet(self, changet):
        bloco = self.combobox_bloco_3.get_active_text()
        if bloco is not None:

            if bloco == 'H8 / 30 / 100':
                self.entry_hb_3.set_text('8')
                self.entry_be_3.set_text('30')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')
            elif bloco == 'H8 / 40 / 100':
                self.entry_hb_3.set_text('8')
                self.entry_be_3.set_text('40')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')
            elif bloco == 'H10 / 30 / 100':
                self.entry_hb_3.set_text('10')
                self.entry_be_3.set_text('30')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')
            elif bloco == 'H10 / 40 / 100':
                self.entry_hb_3.set_text('10')
                self.entry_be_3.set_text('40')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')
            elif bloco == 'H12 / 30 / 100':
                self.entry_hb_3.set_text('12')
                self.entry_be_3.set_text('30')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')
            elif bloco == 'H12 / 40 / 100':
                self.entry_hb_3.set_text('12')
                self.entry_be_3.set_text('40')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')
            elif bloco == 'H16 / 30 / 100':
                self.entry_hb_3.set_text('16')
                self.entry_be_3.set_text('30')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')
            elif bloco == 'H16 / 40 / 100':
                self.entry_hb_3.set_text('16')
                self.entry_be_3.set_text('40')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')
            elif bloco == 'H20 / 30 / 100':
                self.entry_hb_3.set_text('20')
                self.entry_be_3.set_text('30')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')
            elif bloco == 'H25 / 30 / 100':
                self.entry_hb_3.set_text('25')
                self.entry_be_3.set_text('30')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')
            elif bloco == 'H30 / 30 / 100':
                self.entry_hb_3.set_text('30')
                self.entry_be_3.set_text('30')
                self.entry_ah_3.set_text('1.5')
                self.entry_av_3.set_text('3.0')
                self.entry_ce_3.set_text('100')

    def on_button_toggled3(self, button):
        self.entry_hb_3.set_sensitive(False)
        self.entry_ah_3.set_sensitive(False)
        self.entry_av_3.set_sensitive(False)
        self.entry_be_3.set_sensitive(False)
        self.entry_ce_3.set_sensitive(False)
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('static\estilo_texto_inabilitado.css')
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen.get_default(),
                                              css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        if self.check_button1_3.get_active():
            self.entry_hb_3.set_sensitive(True)
            self.entry_ah_3.set_sensitive(True)
            self.entry_av_3.set_sensitive(True)
            self.entry_be_3.set_sensitive(True)
            self.entry_ce_3.set_sensitive(True)
            css_provider = Gtk.CssProvider()
            css_provider.load_from_path('static\estilo_texto_habilitado.css')
            screen = Gdk.Screen()
            style_context = Gtk.StyleContext()
            style_context.add_provider_for_screen(screen.get_default(),
                                                  css_provider,
                                                  Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def on_button_trelica_informacao_3_clicked(self, button):
        self.informacao_trelica('Caro Usuário', 'O PavPré é um \nsistema blá blá blá...', 'emblem-default')

    def ler_informacao_3(self):
        string = self.entry_inter_3.get_text(), \
                 self.entry_vao_livre_3.get_text(), \
                 self.entry_revestimento_3, \
                 self.combobox_acidental_3.get_text(), \
                 self.entry_hb_3.get_text(), \
                 self.entry_be_3.get_text(), \
                 self.entry_ah_3.get_text(), \
                 self.entry_av_3.get_text(), \
                 self.entry_ce_3.get_text(), \
                 self.entry_capa_3.get_text(), \
                 self.entry_bv_3.get_text(), \
                 self.entry_be_3.get_text(), \
                 self.entry_hv_3.get_text()

        try:
            numero = int(string)
        except:
            numero = float(string)
        return numero

    # TELA DE DIMENSIONAMENTO
    # ====================================================================================================
    # INFORMAÇÕES COM IMAGENS
    def on_button_informacao_acidental_3_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/apoiado_e_engastado.png')
        self.informacao_tabela('Caro Usuário', 'O PavPré é um \nsistema blá blá blá...', 'dialog-warning-symbolic')

    def on_button_informacao_psi_3_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/apoiado_e_engastado.png')
        self.informacao_tabela('Caro Usuário', 'O PavPré é um \nsistema blá blá blá...', 'dialog-warning-symbolic')

    def on_button_informacao_trelica_3_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/tabela_trelica.png')
        self.informacao_tabela('Caro Usuário', 'O PavPré é um \nsistema blá blá blá...', 'dialog-warning-symbolic')

    def on_button_informacao_agressividade_3_clicked(self, button):
        self.imagem_informacao.set_from_file('static/imagens/tabela_agressividade.png')
        self.informacao_tabela('Tabela 6.1 - Classe de agressividade Ambiental (NBR 6118/2014)', '',
                               'dialog-warning-symbolic')

    # SETAR CLASSE DE AGRESSIVIDADE
    # =====================================================================================================
    def on_combobox_agressividade_3_changet(self, changet):
        agressividade = self.combobox_agressividade_3.get_active_text()
        if agressividade is not None:

            if agressividade == 'I - Fraca':
                self.entry_cobrimento_3.set_text('2')
            elif agressividade == 'II - Moderada':
                self.entry_cobrimento_3.set_text('2.5')
            elif agressividade == 'III - Forte':
                self.entry_cobrimento_3.set_text('3.5')
            elif agressividade == 'IV - Muito Forte':
                self.entry_cobrimento_3.set_text('4.5')

    def on_button_realizar_dimensionamento_3_clicked(self, button):
        # MENSAGENS DE AVISO!!!!
        # ==============================================================================================
        agressividade = self.combobox_agressividade_3.get_active_text()
        cobrimento = self.entry_cobrimento_3.get_text()

        if agressividade == 'I - Fraca' and cobrimento < str(2):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')
        elif agressividade == 'II - Moderada' and cobrimento < str(2.5):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')
        elif agressividade == 'III - Forte' and cobrimento < str(3.5):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')
        elif agressividade == 'IV - Muito Forte' and cobrimento < str(4.5):
            self.informacao_aviso('Caro Usuário', 'O cobrimento inserido é menor que o recomendado pela norma!',
                                  'dialog-warning-symbolic')

        # AREA DE AÇO
        # MOMENTO POSITIVO
        r = self.entry_revestimento_3.get_text()
        self.label_revestimento.set_text(str(r))
        q = self.combobox_acidental_3.get_active_text()
        b = 20 # kgf/m³
        l = self.entry_vao_livre_3.get_text()
        hb = self.entry_hb_3.get_text()
        self.label_hb.set_text(str(hb))
        ah = self.entry_ah_3.get_text()
        av = self.entry_av_3.get_text()
        capa = self.entry_capa_3.get_text()
        bv = self.entry_bv_3.get_text()
        be = self.entry_be_3.get_text()
        self.label_be.set_text(str(be))
        hv = self.entry_hv_3.get_text()
        ce = self.entry_ce_3.get_text()
        self.label_ce.set_text(str(ce))
        c = self.entry_comprimento_3.get_text()
        if c=="":
            c = 0
        else:
            c = self.entry_comprimento_3.get_text()
        # self.label_acidental.set_active_text(str("%.2f" % r))
        if r == '' \
                or l == '' \
                or hb == '' \
                or be == '' \
                or ah == '' \
                or av == '' \
                or ce == '' \
                or hv == '' \
                or bv == '' \
                or cobrimento == '' \
                or capa == '':
            self.informacao_aviso('Caro Usuário',
                                  'Preencha todos os campos!',
                                  'dialog-warning-symbolic')


        else:
            acidental = self.calc.funcoes['acidental'](float(q))
            self.label_acidental.set_text(str("%.2f" % acidental))
            vao_livre = self.calc.funcoes['vao_livre'](float(l))
            self.label_vao_livre.set_text(str("%.2f" % vao_livre))
            vao_comprimento = self.calc.funcoes['vao_comprimento'](float(c))
            self.label_comprimento_vao.set_text(str("%.2f" % vao_comprimento))
            bf = self.calc.funcoes['bf'](float(be),
                                         float(ah),
                                         float(bv))

            bw = self.calc.funcoes['bw'](float(bv),
                                         float(ah))

            pp_c = self.calc.funcoes['pp_c'](float(capa),
                                             float(bf),
                                             float(hb),
                                             float(bw),
                                             float(ah),
                                             float(av),
                                             float(be),
                                             float(b))
            pp_c1 = pp_c / (bf / 100)
            self.label_peso_proprio.set_text(str("%.2f" % pp_c1))
            p_total = self.calc.funcoes['p_total'](float(pp_c),
                                                   float(r),
                                                   float(q),
                                                   float(bf))
            p_total1 = p_total / (bf / 100)
            self.label_p_total.set_text(str("%.2f" % p_total1))

            mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
            md_pos = mk_pos * 1.4
            md_pos1 = md_pos / (bf / 100)
            self.resultado_momento_pos.set_text(str("%.2f" % md_pos1))
            self.calculo_3()

    def calculo_3(self):
        # ÁREA DE AÇO
        global d0, phi_trelica, fyk_trelica, yii, fyk
        r = self.entry_revestimento_3.get_text()
        q = self.combobox_acidental_3.get_active_text()
        b = 20
        l = self.entry_vao_livre_3.get_text()
        c = self.entry_comprimento_3.get_text()
        if c=="":
            c = 0
        else:
            c = self.entry_comprimento_3.get_text()
        hb = self.entry_hb_3.get_text()
        ah = self.entry_ah_3.get_text()
        av = self.entry_av_3.get_text()
        capa = self.entry_capa_3.get_text()
        bv = self.entry_bv_3.get_text()
        be = self.entry_be_3.get_text()
        ce = self.entry_ce_3.get_text()
        hv = self.entry_hv_3.get_text()
        escoramento = self.entry_escoramento_dias_3.get_text()
        self.label_dias_escora.set_text(escoramento)
        alpha_c = 5 / 384
        fyk_adicional = self.combobox_fyk_3.get_active_text()
        if fyk_adicional == 'CA 50':
            fyk = 500
        elif fyk_adicional == 'CA 60':
            fyk = 600
        self.label_tipo_aco.set_text(fyk_adicional)
        fyk_da_trelica = self.combobox_fyk_trelica_3.get_active_text()
        if fyk_da_trelica == 'CA 50':
            fyk_trelica = 500
        elif fyk_da_trelica == 'CA 60':
            fyk_trelica = 600
        bw = self.calc.funcoes['bw'](float(bv),
                                     float(ah))
        bf = self.calc.funcoes['bf'](float(be),
                                     float(ah),
                                     float(bv))
        pp_c = self.calc.funcoes['pp_c'](float(capa),
                                         float(bf),
                                         float(hb),
                                         float(bw),
                                         float(ah),
                                         float(av),
                                         float(be),
                                         float(b))
        p_total = self.calc.funcoes['p_total'](float(pp_c),
                                               float(r),
                                               float(q),
                                               float(bf))

        cobrimento = self.entry_cobrimento_3.get_text()
        aco = self.combobox_aco_3.get_active_text()
        self.label_trelica_escolhida.set_text(aco)
        if aco == 'TR 8644':
            phi_trelica = '4.2'
        elif aco == 'TR 8645':
            phi_trelica = '5'
        elif aco == 'TR 12645':
            phi_trelica = '5'
        elif aco == 'TR 12646':
            phi_trelica = '6'
        elif aco == 'TR 16745':
            phi_trelica = '5'
        elif aco == 'TR 16746':
            phi_trelica = '6'
        elif aco == 'TR 20745':
            phi_trelica = '5'
        elif aco == 'TR 20756':
            phi_trelica = '6'
        elif aco == 'TR 25856':
            phi_trelica = '6'
        elif aco == 'TR 25858':
            phi_trelica = '8'
        elif aco == 'TR 30856':
            phi_trelica = '6'
        elif aco == 'TR 30858':
            phi_trelica = '8'

        d = self.calc.funcoes['d'](float(hb),
                                   float(av),
                                   float(capa),
                                   float(hv),
                                   float(cobrimento),
                                   float(phi_trelica))

        mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
        fck = self.combobox_fck_3.get_active_text()
        self.label_fck.set_text(fck)
        d0 = self.calc.funcoes['d0'](float(mk_pos),
                                     float(fck),
                                     float(bf),
                                     float(capa))

        d = float(d)
        if d >= d0:
            mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
            kmd = self.calc.funcoes['kmd'](float(mk_pos),
                                           float(bf),
                                           float(fck),
                                           float(d))
            if kmd > 0.251:
                self.informacao_erro_kmd('Caro Usuário', 'Linha neutra fora dos domínios de deformação', 'emblem-default')

            else:
                kx = self.calc.funcoes['kx'](float(kmd))

                as_total = self.calc.funcoes['as_total'](float(mk_pos),
                                                         float(d),
                                                         float(kx),
                                                         float(fyk_trelica))
                self.label_resultado_area_total.set_text(str("%.2f" % as_total))
                as_adicional = self.calc.funcoes['as_adicional'](float(as_total),
                                                                 float(phi_trelica),
                                                                 float(fyk),
                                                                 float(fyk_trelica))
                if as_adicional < 0:
                    self.label_resultado_area_adicional.set_text(str(0.00))
                else:
                    self.label_resultado_area_adicional.set_text(str("%.2f" % as_adicional))

                # AS MÍNIMA E CORTANTE==========================================================
                pmin = self.calc.funcoes['pmin'](float(fck),
                                                 float(fyk))
                as_min = self.calc.funcoes['as_min'](float(pmin),
                                                     float(capa),
                                                     float(bf),
                                                     float(hb),
                                                     float(bw))
                self.label_area_minima.set_text(str("%.2f" % as_min))

                Vk = self.calc.funcoes['Vk'](float(p_total),
                                             float(l))
                trd = self.calc.funcoes['trd'](float(fck))
                k = self.calc.funcoes['k'](float(d))
                p1 = self.calc.funcoes['p1'](float(as_total),
                                             float(bw),
                                             float(d))
                Vrd1 = self.calc.funcoes['Vrd1'](float(trd),
                                                 float(k),
                                                 float(p1),
                                                 float(bw),
                                                 float(d))
                alpha_v1 = self.calc.funcoes['alpha_v1'](float(fck))
                if alpha_v1 > 0.5:
                    av1 = 0.5
                else:
                    av1 = alpha_v1
                Vrd2 = self.calc.funcoes['Vrd2'](float(av1),
                                                 float(fck),
                                                 float(bw),
                                                 float(d))
                print(bf, bw, pp_c, p_total, mk_pos, d0, d, kmd, kx, as_total, as_adicional)
                print(fyk, fyk_trelica)
                Vd = Vk*1.4
                if Vd < Vrd1:
                    self.label_cortante.set_text("Não é necessário")
                else:
                    self.label_cortante.set_text("Redimensionar")
                if Vd < Vrd2:
                    self.label_bielas.set_text("Não")
                else:
                    self.label_bielas.set_text("Sim")
                print ("d=",d,"BW=",bw, Vd, Vrd1, av1, Vrd2)
                self.Stack.set_visible_child_name('view_resultado')
        elif d < d0:  # Dimensionamento linha neutra na alma
            mk_pos = self.calc.funcoes['momento_pos_biapoiado'](float(p_total), float(l))
            M1 = self.calc.funcoes['M1'](float(fck),
                                         float(capa),
                                         float(bf),
                                         float(bw),
                                         float(d))
            M2 = self.calc.funcoes['M2'](float(mk_pos),
                                         float(M1))

            kmd2 = self.calc.funcoes['kmd2'](float(M2),
                                             float(d),
                                             float(fck),
                                             float(bw))
            print('M1, m2, kmd2', M1, M2, kmd2)
            if kmd2 > 0.251:
                self.informacao_erro_kmd('Caro Usuário', 'Linha neutra fora dos domínios de deformação', 'emblem-default')

            else:
                kx2 = self.calc.funcoes['kx2'](float(kmd2))
                As_1 = self.calc.funcoes['As_1'](float(M1),
                                                 float(d),
                                                 float(capa),
                                                 float(fyk_trelica))
                As_2 = self.calc.funcoes['As_2'](float(M2),
                                                 float(kx2),
                                                 float(d),
                                                 float(fyk_trelica))
                as_total2 = self.calc.funcoes['as_total2'](float(As_1),
                                                           float(As_2))
                as_adicional2 = self.calc.funcoes['as_adicional2'](float(as_total2),
                                                                   float(phi_trelica),
                                                                   float(fyk),
                                                                   float(fyk_trelica))
                self.label_resultado_area_total.set_text(str("%.2f" % as_total2))
                self.label_resultado_area_adicional.set_text(str("%.2f" % as_adicional2))
                # AS MÍNIMA E CORTANTE==========================================================
                pmin = self.calc.funcoes['pmin'](float(fck),
                                                 float(fyk))
                as_min = self.calc.funcoes['as_min'](float(pmin),
                                                     float(capa),
                                                     float(bf),
                                                     float(hb),
                                                     float(bw))
                self.label_area_minima.set_text(str("%.2f" % as_min))

                Vk = self.calc.funcoes['Vk'](float(p_total),
                                             float(l))
                trd = self.calc.funcoes['trd'](float(fck))
                k = self.calc.funcoes['k'](float(d))
                p1 = self.calc.funcoes['p1'](float(as_total2),
                                             float(bw),
                                             float(d))
                Vrd1 = self.calc.funcoes['Vrd1'](float(trd),
                                                 float(k),
                                                 float(p1),
                                                 float(bw),
                                                 float(d))
                alpha_v1 = self.calc.funcoes['alpha_v1'](float(fck))
                if alpha_v1 > 0.5:
                    av1 = 0.5
                else:
                    av1 = alpha_v1
                Vrd2 = self.calc.funcoes['Vrd2'](float(av1),
                                                 float(fck),
                                                 float(bw),
                                                 float(d))
                print(bf, bw, pp_c, p_total, mk_pos, d0, d, kmd, kx, as_total, as_adicional)
                print(fyk, fyk_trelica)
                Vd = Vk*1.4
                if Vd < Vrd1:
                    self.label_cortante.set_text("Não é necessário")
                else:
                    self.label_cortante.set_text("Redimensionar")
                if Vd < Vrd2:
                    self.label_bielas.set_text("Não")
                else:
                    self.label_bielas.set_text("Sim")
                print ("d=",d,"BW=",bw, Vd, Vrd1, av1, Vrd2)
                self.Stack.set_visible_child_name('view_resultado')

        # DEFORMAÇÕES
        as_total = self.label_resultado_area_total.get_text()
        psi2 = self.combobox_psi2_3.get_active_text()
        p_total_els = self.calc.funcoes['p_total_els'](float(pp_c),
                                                       float(r),
                                                       float(q),
                                                       float(bf),
                                                       float(psi2))
        mk_els = self.calc.funcoes['mk_els'](float(p_total_els), float(l))
        Ecs = self.calc.funcoes['Ecs'](float(fck))
        fctm = self.calc.funcoes['fctm'](float(fck))
        ag = self.calc.funcoes['ag'](float(bf),
                                     float(bw),
                                     float(capa),
                                     float(hb),
                                     float(av),
                                     float(hv))
        ycg = self.calc.funcoes['ycg'](float(capa),
                                       float(bf),
                                       float(bw),
                                       float(hb),
                                       float(hv),
                                       float(av),
                                       float(ag))
        Ic = self.calc.funcoes['Ic'](float(bf),
                                     float(bw),
                                     float(capa),
                                     float(hb),
                                     float(hv),
                                     float(ycg),
                                     float(av))

        Mr = self.calc.funcoes['Mr'](float(fctm),
                                     float(Ic),
                                     float(hb),
                                     float(hv),
                                     float(ycg),
                                     float(av),
                                     float(capa))
        if d >= d0:
            a1 = self.calc.funcoes['a1'](float(bf))
            a2 = self.calc.funcoes['a2'](float(capa),
                                         float(bf),
                                         float(bf),
                                         float(Ecs),
                                         float(as_total))
            a3 = self.calc.funcoes['a3'](float(d),
                                         float(Ecs),
                                         float(as_total),
                                         float(capa),
                                         float(bf),
                                         float(bf), )
            yii = self.calc.funcoes['yii'](float(a1),
                                           float(a2),
                                           float(a3))
            Iii_mesa = self.calc.funcoes['Iii_mesa'](float(bf),
                                                     float(yii),
                                                     float(Ecs),
                                                     float(as_total),
                                                     float(d))
            self.Iii_1.set_text(str("%.2f" % Iii_mesa))
        elif d < d0:  # Dimensionamento linha neutra na alma
            a1 = self.calc.funcoes['a1'](float(bw))
            a2 = self.calc.funcoes['a2'](float(capa),
                                         float(bf),
                                         float(bw),
                                         float(Ecs),
                                         float(as_total))
            a3 = self.calc.funcoes['a3'](float(d),
                                         float(Ecs),
                                         float(as_total),
                                         float(capa),
                                         float(bf),
                                         float(bw), )
            yii = self.calc.funcoes['yii'](float(a1),
                                           float(a2),
                                           float(a3))
            Iii_alma = self.calc.funcoes['Iii_alma'](float(bf),
                                                     float(bw),
                                                     float(capa),
                                                     float(yii),
                                                     float(Ecs),
                                                     float(as_total),
                                                     float(d))
            self.Iii_1.set_text(str("%.2f" % Iii_alma))
        Iii = self.Iii_1.get_text()
        EI_eq = self.calc.funcoes['EI_eq'](float(Ecs),
                                           float(Mr),
                                           float(mk_els),
                                           float(Ic),
                                           float(Iii))
        w0 = self.calc.funcoes['w0'](float(alpha_c),
                                     float(p_total_els),
                                     float(l),
                                     float(EI_eq))
        t0 = self.calc.funcoes['t0'](float(escoramento))
        ksi_t0 = self.calc.funcoes['ksi_t0'](float(t0))
        alpha_f = self.calc.funcoes['alpha_f'](float(ksi_t0))
        flecha_diferida = alpha_f * w0
        flecha_total = self.calc.funcoes['flecha_total'](float(w0),
                                                         float(alpha_f))
        self.label_flecha_imediata.set_text(str("%.2f" % w0))
        self.label_flecha_tempo.set_text(str("%.2f" % flecha_diferida))
        self.label_flecha_total.set_text(str("%.2f" % flecha_total))
        flecha_lim = self.calc.funcoes['flecha_lim'](float(l))
        contra_flecha = self.calc.funcoes['contra_flecha'](float(flecha_total),
                                                           float(l))
        self.label_limite_total.set_text(str("%.2f" % flecha_lim))
        cf_lim = float(l)/350
        if contra_flecha > 0 and contra_flecha < cf_lim:
            self.label_contra_flecha.set_text(str("%.2f" % contra_flecha))
        elif contra_flecha > cf_lim:
            self.label_contra_flecha.set_text("Limite atingido (L/350)")
        elif contra_flecha <= 0:
            self.label_contra_flecha.set_text("Não é necessário")

        print('deformação', yii, bf, bw, capa, hb, ag, ycg, av, Ic, Ecs, Mr, mk_els, Ic, yii, Iii, EI_eq)

        # QUANTITATIVO
        por_enchimento = self.calc.funcoes['por_enchimento'](float(be),
                                                             float(ah),
                                                             float(hb),
                                                             float(capa),
                                                             float(bv))
        volume = self.calc.funcoes['volume'](float(c),
                                             float(l),
                                             float(por_enchimento),
                                             float(hb),
                                             float(capa))
        self.label_volume.set_text(str("%.2f" % volume))
        vigota = self.calc.funcoes['vigota'](float(bv),
                                             float(be),
                                             float(ah),
                                             float(c))
        self.label_vigotas.set_text(str("%.2f" % vigota))
        lajota_1 = self.calc.funcoes['lajota_1'](float(bv),
                                                 float(be),
                                                 float(ah),
                                                 float(c))
        lajota_2 = self.calc.funcoes['lajota_2'](float(l),
                                                 float(ce))
        quantidade_lajota = self.calc.funcoes['quantidade_lajota'](float(lajota_1),
                                                                   float(lajota_2))
        self.label_lajotas.set_text(str("%.2f" % quantidade_lajota))
        vao_livre = self.entry_vao_livre_3.get_text()
        self.label_vao_livre.set_text(str(vao_livre))
        comprimento_vao = self.entry_comprimento_3.get_text()
        self.label_comprimento_vao.set_text(str(comprimento_vao))
#TELA DE RESULTADO - GERAÇÃO DE PDF
# ======================================================
    #def printCliente(self):
        #laje = self.entry_nome_laje.get_text()
        #webbrowser.open('Resultado Simplificado de Cálculo - ' + laje)

    def geraRelatCliente(self):
        laje = self.entry_nome_laje.get_text()
        dialog = Gtk.FileChooserDialog(
            title="Selecione um local para salvar o arquivo", parent=Window, action=Gtk.FileChooserAction.SAVE
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE,
            Gtk.ResponseType.OK,
        )
        dialog.set_default_size(800, 400)

        # Confirmação de sobrescrita, caso o arquivo já exista
        dialog.set_do_overwrite_confirmation(True)

        # Nome inicial
        dialog.set_current_name('Resultado Simplificado de Cálculo - ' + laje)

        # filtro de formato
        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.caminho = dialog.get_filename()

        self.laje = canvas.Canvas(self.caminho + '.pdf')

        self.momento = self.resultado_momento_pos.get_text()
        self.vao = self.label_vao_livre.get_text()
        self.comprimento = self.label_comprimento_vao.get_text()
        self.fck = self.label_fck.get_text()
        self.aco_ad = self.label_tipo_aco.get_text()
        self.dias_escora = self.label_dias_escora.get_text()

        self.laje.setFont("Helvetica-Bold", 14)
        self.laje.drawString(190, 756.85, 'Resultado Simplificado de Cálculo')

        self.laje.setFont("Helvetica-Bold", 12)
        self.laje.drawString(250, 730, 'Parâmetros Gerais')
        self.laje.drawString(60, 700, 'Nome da Laje: ')
        self.laje.drawString(60, 680, 'Vão Efetivo (cm): ')
        self.laje.drawString(60, 660, 'Comprimento do Vão (cm): ')
        self.laje.drawString(350, 700, 'fck (MPa): ')
        self.laje.drawString(350, 680, 'Aço Adicional: ')
        self.laje.drawString(350, 660, 'Dias de Escoramento: ')

        self.laje.setFont("Helvetica", 12)
        self.laje.drawString(155, 700, laje)
        self.laje.drawString(170, 680, self.vao)
        self.laje.drawString(220, 660, self.comprimento)
        self.laje.drawString(410, 700, self.fck)
        self.laje.drawString(440, 680, self.aco_ad)
        self.laje.drawString(480, 660, self.dias_escora)
        self.laje.rect(50, 645, 497, 83, fill=False, stroke=True)

        self.peso = self.label_peso_proprio.get_text()
        self.carga_rev = self.label_revestimento.get_text()
        self.carga_ac = self.label_acidental.get_text()
        self.carga_total = self.label_p_total.get_text()
        self.momento = self.resultado_momento_pos.get_text()

        self.laje.setFont("Helvetica-Bold", 12)
        self.laje.drawString(150, 610, 'Cargas')
        self.laje.drawString(60, 580, 'Peso Próprio (kgf/m²): ')
        self.laje.drawString(60, 555, 'Revestimento (kgf/m²): ')
        self.laje.drawString(60, 530, 'Adicional (kgf/m²): ')
        self.laje.drawString(60, 505, 'Carga Total (kgf/m²):')
        self.laje.drawString(60, 480, 'Momento - Md (kgf.m/m): ')

        self.laje.setFont("Helvetica", 12)
        self.laje.drawString(195, 580, self.peso)
        self.laje.drawString(200, 555, self.carga_rev)
        self.laje.drawString(175, 530, self.carga_ac)
        self.laje.drawString(185, 505, self.carga_total)
        self.laje.drawString(210, 480, self.momento)
        self.laje.rect(50, 465, 230, 140, fill=False, stroke=True)

        self.hb = self.label_hb.get_text()
        self.be = self.label_be.get_text()
        self.ce = self.label_ce.get_text()
        self.trelica = self.label_trelica_escolhida.get_text()
        self.area_min = self.label_area_minima.get_text()
        self.area_total = self.label_resultado_area_total.get_text()
        self.area_ad = self.label_resultado_area_adicional.get_text()
        self.diamentro = self.combobox_bitola_1.get_active_text()
        self.quantidade = self.label_quantidade_barras_1.get_text()
        self.arm_transversal = self.label_cortante.get_text()
        self.bielas = self.label_bielas.get_text()


        self.laje.setFont("Helvetica-Bold", 12)
        self.laje.drawString(365, 610, 'Enchimento e Aço')
        self.laje.drawString(300, 580, 'Enchimento Escolhido: ')
        self.laje.drawString(300, 550, 'Treliça Escolhida: ')
        self.laje.drawString(300, 520, 'Area de aço mínima (cm²/N): ')
        self.laje.drawString(300, 490, 'Área de Aço Total (cm²/N):')
        self.laje.drawString(300, 460, 'Área de Aço Adicional (cm²/N): ')
        self.laje.drawString(300, 430, 'Diâmetro de Aço Adicional: ')
        self.laje.drawString(300, 400, 'Quantidade de barras p/ nerv.: ')
        self.laje.drawString(300, 370, 'Armadura Transversal:')
        self.laje.drawString(300, 340, 'Esmagamento das bielas?')

        self.laje.setFont("Helvetica", 12)
        self.laje.drawString(445, 580, 'H')
        self.laje.drawString(470, 580, '/')
        self.laje.drawString(490, 580, '/')
        self.laje.drawString(455, 580, self.hb)
        self.laje.drawString(475, 580, self.be)
        self.laje.drawString(495, 580, self.ce)

        self.laje.drawString(410, 550, self.trelica)
        self.laje.drawString(470, 520, self.area_min)
        self.laje.drawString(465, 490, self.area_total)
        self.laje.drawString(480, 460, self.area_ad)
        self.laje.drawString(465, 430, self.diamentro)
        self.laje.drawString(480, 400, self.quantidade)
        self.laje.drawString(440, 370, self.arm_transversal)
        self.laje.drawString(460, 340, self.bielas)

        self.laje.rect(290, 315, 257, 290, fill=False, stroke=True)

        self.concreto = self.label_volume.get_text()
        self.bloco = self.label_lajotas.get_text()
        self.vigota = self.label_vigotas.get_text()

        self.laje.setFont("Helvetica-Bold", 12)
        self.laje.drawString(95, 440, 'Quantitativo Aproximado')
        self.laje.drawString(60, 410, 'Concreto (m³): ')
        self.laje.drawString(60, 390, 'Bloco de Enchimento (un): ')
        self.laje.drawString(60, 370, 'Vigota Treliçada (un): ')

        self.laje.setFont("Helvetica", 12)
        self.laje.drawString(155, 410, self.concreto)
        self.laje.drawString(220, 390, self.bloco)
        self.laje.drawString(190, 370, self.vigota)
        self.laje.rect(50, 315, 230, 120, fill=False, stroke=True)

        self.imediata = self.label_flecha_imediata.get_text()
        self.diferida = self.label_flecha_tempo.get_text()
        self.f_total = self.label_flecha_total.get_text()
        self.f_limite = self.label_limite_total.get_text()
        self.contra_f = self.label_contra_flecha.get_text()

        self.laje.setFont("Helvetica-Bold", 14)
        self.laje.drawString(190, 756.85, 'Resultado Simplificado de Cálculo')

        self.laje.setFont("Helvetica-Bold", 12)
        self.laje.drawString(260, 290, 'Deformação')
        self.laje.drawString(60, 265, 'Flecha Imediata (cm): ')
        self.laje.drawString(60, 240, 'Flecha Diferida no Tempo (cm):')
        self.laje.drawString(60, 210, 'Flecha Total (cm):')
        self.laje.drawString(290, 265, 'Flecha Limite - L/250 (cm):')
        self.laje.drawString(290, 240, 'Contra Flecha (cm):')

        self.laje.setFont("Helvetica", 12)
        self.laje.drawString(190, 265, self.imediata)
        self.laje.drawString(245, 240, self.diferida)
        self.laje.drawString(175, 210, self.f_total)
        self.laje.drawString(450, 265, self.f_limite)
        self.laje.drawString(420, 240, self.contra_f)
        self.laje.rect(50, 195, 497, 90, fill=False, stroke=True)

        self.laje.showPage()
        self.laje.save()
        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("PDF")
        filter_text.add_mime_type("application/pdf")
        dialog.add_filter(filter_text)

    def on_button_salvar_pdf_clicked(self, button):
        diametro = self.combobox_bitola_1.get_active_text()
        if diametro == '...':
            self.informacao_aviso('Caro Usuário', 'Escolha um diâmetro para armadura adicional!', 'dialog-warning-symbolic')
        else:
            self.geraRelatCliente()
        #self.printCliente()









Builder = Gtk.Builder()
Builder.add_from_file('user_interface.glade')
Builder.connect_signals(Handler())
Window: Gtk.Window = Builder.get_object('main_window')
Window.show_all()
Gtk.main()