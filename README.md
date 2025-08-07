# Meu Blog Final - Projeto Django

Este é um projeto de blog simples desenvolvido com Django, ideal para quem está começando no framework e deseja aprender sobre criação de apps, rotas, templates e administração de conteúdo.

## 🚀 Funcionalidades

- Cadastro, edição e exclusão de postagens via painel administrativo
- Exibição de posts na página inicial, com título, conteúdo, data e imagem
- Visual moderno com tema sombrio inspirado em jogos de terror
- Upload e exibição de imagens para cada post

## 🛠️ Como rodar o projeto

1. **Clone o repositório**
   ```sh
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. **Crie e ative o ambiente virtual**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
   ```
   > Se não existir o arquivo, instale manualmente:
   > ```sh
   > pip install django pillow
   > ```

4. **Realize as migrações**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário**
   ```sh
   python manage.py createsuperuser
   ```

6. **Inicie o servidor**
   ```sh
   python manage.py runserver
   ```

7. **Acesse no navegador**
   - Página do blog: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📁 Estrutura do Projeto

```
meu_blog_final/
├── meu_blog_final/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── posts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── posts/
│   │       └── post_list.html
│   └── ...
├── media/
│   └── post_images/
├── manage.py
└── ...
```

## 📸 Imagens

As imagens dos posts são salvas na pasta `media/post_images/` e exibidas automaticamente na página inicial.

## 📝 Personalização

- Para mudar o tema, edite o arquivo `post_list.html` em `posts/templates/posts/`.
- Para adicionar novos campos aos posts, edite o modelo em `models.py` e faça novas migrações.

## 📚 Licença

Este projeto é livre para fins de estudo e aprendizado.

---

Desenvolvido com 💻 por Matheus Rodrigues
