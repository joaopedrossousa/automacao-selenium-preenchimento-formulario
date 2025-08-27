from models.preencher_formulario import PreencherFormulario


preencher_formulario = PreencherFormulario()

preencher_formulario.inicializar_navegador()

preencher_formulario.acessar_site()

preencher_formulario.maximixar_navegador()

preencher_formulario.select_campo("id", "first_4")
preencher_formulario.inserir_campo("João Pedro")

preencher_formulario.select_campo("id", "last_4")
preencher_formulario.inserir_campo("Silva Sousa")

preencher_formulario.select_campo("id", "input_5")
preencher_formulario.inserir_campo("jpsousa.ti@gmail.com")

preencher_formulario.select_campo("id", "input_6_addr_line1")
preencher_formulario.centralizar_campo()
preencher_formulario.inserir_campo("504 Sul, Al. 2, LT. 54, Casa 01")
