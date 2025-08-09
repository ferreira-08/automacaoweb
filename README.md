# 📬 Automação de Envio de E-mails

Este projeto utiliza a biblioteca **PyAutoGUI** para automatizar o processo de envio de e-mails através do navegador Google Chrome. A automação simula ações humanas como abrir o navegador, acessar a conta, preencher os campos do e-mail e enviá-lo.

## 🧰 Tecnologias Utilizadas

- Python 3.x
- PyAutoGUI
- Time
- Google Chrome

## 📌 Funcionalidades

- Abertura automática do navegador
- Acesso à conta do Chrome
- Navegação até a interface de e-mail
- Preenchimento dos campos:
  - Endereço do destinatário
  - Assunto
  - Corpo do e-mail
- Envio automático da mensagem

## ⚠️ Observações Importantes

- As coordenadas de clique (`pyautogui.click(x, y)`) são específicas da resolução e layout da sua tela. É necessário ajustá-las conforme seu ambiente.
- Durante a execução, **não mova o mouse nem digite nada**, pois isso pode interferir na automação.
- O script não utiliza APIs de e-mail, sendo totalmente baseado em simulação de interface gráfica.

## 📁 Estrutura do Projeto

Automacao-Email/ 
├── email_automacao.py


## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/ferreira-08/Automacao-Email.git
   cd Automacao-Email

   Instale a dependência:

   Ajuste as coordenadas dos cliques conforme sua tela.

Execute o script:

python email_automacao.py

