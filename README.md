Instruções para teste da aplicação:

1. Após git clone ou download da aplicação pelo GitHub, abra o diretório em seu terminal.
2. A aplicação foi desenvolvida em Python. É necessária a instalação prévia do Python no dispositivo.
Os seguintes componentes devem ser instalados para que a aplicação seja executada no ambiente:

pip install django-braces
pip install django-crispy-forms
pip install crispy_bootstrap5

3. Após a instalação dos componentes acima, execute o seguinte comando pelo terminal:
   python3 manage.py runserver
   ou
   python manage.py runserver
   O comando depende da versão Python instalada no dispositivo.

4. Uma mensagem similar ao modelo abaixo deve ser apresentada no terminal após a instalação correta dos componentes informados:
   System check identified no issues (0 silenced).
  May 14, 2024 - 22:48:46
  Django version 5.0.4, using settings 'poeu.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.

5. Abrar seu navegador Web e use o endereço: http://127.0.0.1:8000/


