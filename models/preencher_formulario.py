from selenium import webdriver


class PreencherFormulario:

    def __init__(self):
        self.browser = None

    def inicializar_navegador(self):
        self.browser = webdriver.Firefox()

    def acessar_site(self):
        self.browser.get(
            "https://www.jotform.com/pt/form-templates/preview/212414140816041/classic&nofs&disableSmartEmbed=1"
        )

    def maximixar_navegador(self):
        self.browser.maximize_window()

    def select_campo(self, tipo_campo, ident_campo):
        self.campo_selecionado = self.browser.find_element(
            f"{tipo_campo}", f"{ident_campo}"
        )

    def selec_varios_campos(self, tipo_campo, ident_campo):
        self.lista_campos = self.browser.find_element(f"{tipo_campo}", f"{ident_campo}")

    def inserir_campos_multiplos(self, busca_campo, info_campo):
        if busca_campo in self.lista_campos.text:
            self.inserir_campo(f"{info_campo}")

    def inserir_campo(self, info_campo):
        self.campo_selecionado.send_keys(f"{info_campo}")

    def centralizar_campo(self):
        campo = self.campo_selecionado
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", campo
        )

    def clicar_campo(self):
        campo = self.campo_selecionado
        campo.click()
