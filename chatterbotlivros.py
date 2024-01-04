Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from chatterbot import ChatBot
... from chatterbot.trainers import ChatterBotCorpusTrainer
... from chatterbot.conversation import Statement
... 
... # Criação do ChatBot
... chatbot = ChatBot('LivroBot')
... 
... # Treinamento com o corpus de dados em inglês
... trainer = ChatterBotCorpusTrainer(chatbot)
... trainer.train('chatterbot.corpus.english')
... 
... # Dados fictícios de livros para simular recomendações
... livros = {
...     'ficcao_cientifica': ['Neuromancer', 'Duna', 'Snow Crash'],
...     'fantasia': ['O Senhor dos Anéis', 'Harry Potter', 'As Crônicas de Nárnia'],
...     'romance': ['Orgulho e Preconceito', 'Amor nos Tempos do Cólera', 'Cem Anos de Solidão']
... }
... 
... # Função para recomendar livros com base na preferência do usuário
... def recomendar_livro(preferencia):
...     if preferencia in livros:
...         return livros[preferencia]
...     else:
...         return ['Desculpe, não temos recomendações para essa preferência.']
... 
... # Função principal para interagir com o chatbot
... def main():
...     print("Olá! Sou o LivroBot. Posso recomendar livros para você.")
...     
...     while True:
...         try:
...             # Obter entrada do usuário
...             usuario_input = input("Você gosta de livros de ficção científica, fantasia ou romance? Digite 'sair' para encerrar: ")
... 
...             # Verificar se o usuário deseja sair
            if usuario_input.lower() == 'sair':
                print("Até logo!")
                break

            # Obter recomendação do chatbot
            resposta = chatbot.get_response(usuario_input)

            # Apresentar resposta do chatbot
            print(f"LivroBot: {resposta}")

            # Se a resposta for uma recomendação, apresentar os livros recomendados
            if 'recomendar_livro' in resposta.text.lower():
                preferencia_usuario = resposta.text.split(':')[1].strip().lower()
                recomendacoes = recomendar_livro(preferencia_usuario)
                print(f"Livros Recomendados: {', '.join(recomendacoes)}")

        except (KeyboardInterrupt, EOFError):
            print("\nAté logo!")
            break

if __name__ == "__main__":
    main()
