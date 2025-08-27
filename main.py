from models.preencher_formulario import PreencherFormulario
from time import sleep

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

preencher_formulario.select_campo("id", "input_6_addr_line2")
preencher_formulario.centralizar_campo()
preencher_formulario.inserir_campo("Plano Diretor Sul")

preencher_formulario.select_campo("id", "input_6_city")
preencher_formulario.inserir_campo("Palmas")

preencher_formulario.select_campo("id", "input_6_state")
preencher_formulario.inserir_campo("Tocantins")

preencher_formulario.select_campo("id", "input_6_postal")
preencher_formulario.inserir_campo("77645-000")

preencher_formulario.select_campo("id", "input_7_full")
preencher_formulario.centralizar_campo()
preencher_formulario.inserir_campo("63984216017")

preencher_formulario.select_campo("id", "lite_mode_8")
preencher_formulario.inserir_campo("21092001")

preencher_formulario.select_campo("id", "label_input_9_0")
preencher_formulario.centralizar_campo()
preencher_formulario.clicar_campo()

preencher_formulario.select_campo("id", "label_input_9_2")
preencher_formulario.centralizar_campo()
preencher_formulario.clicar_campo()

preencher_formulario.select_campo("id", "input_2")
preencher_formulario.clicar_campo()
