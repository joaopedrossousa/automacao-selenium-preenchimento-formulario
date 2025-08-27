# 📝 Automação de Formulário com Selenium

Este projeto demonstra o uso do **Selenium WebDriver** para automatizar o preenchimento de formulários em páginas web.  
Ele abre o navegador, navega até o site desejado e insere informações em campos de formulário automaticamente.

---

## 🚀 Tecnologias Utilizadas
- [Python 3.11+](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [GeckoDriver](https://github.com/mozilla/geckodriver) (para Firefox)

---

## 📂 Estrutura do Projeto
```
autSeleniumFormulario/
│── main.py                        # Script principal
│── models/
│   ├── preencher_formulario.py     # Funções para preencher formulários
│   └── __init__.py
```

---

## ⚙️ Como Executar

1. **Clone este repositório ou baixe o projeto.**

2. **Crie um ambiente virtual (opcional, mas recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install selenium
   ```

4. **Baixe o GeckoDriver** (necessário para Firefox)  
   👉 [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)

   - Linux/Mac: coloque o `geckodriver` no `/usr/local/bin`  
   - Windows: coloque o `geckodriver.exe` no mesmo diretório do script ou adicione ao PATH  

5. **Execute o projeto**
   ```bash
   python main.py
   ```

---

## 📖 Funcionalidades
- Abre o navegador Firefox.  
- Acessa uma página web.  
- Preenche automaticamente os campos de formulário (nome, e-mail, telefone, etc.).  
- Pode ser expandido para outros sites e formulários.  

---

## 🔮 Melhorias Futuras
- Tornar os dados de entrada dinâmicos (ler de `.csv` ou `.json`).  
- Suporte a múltiplos navegadores (Chrome, Edge).  
- Adicionar tratamento de erros e logs.  

---

## 👨‍💻 Autor
Automação desenvolvida por **João Pedro Sousa** 🖥️
