from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Nazk')
bot = ChatBot(
    'Nazk',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )
bot = ChatBot(
    'Nazk',  
    logic_adapters=[
        'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'],
)
    
conversa = ChatterBotCorpusTrainer(bot)
conversa.train(
    'chatterbot.corpus.portuguese',
    'chatterbot.corpus.portuguese.greetings',
    'chatterbot.corpus.portuguese.conversations',
    'chatterbot.corpus.portuguese.compliment',
    'chatterbot.corpus.portuguese.linguistic_knowledge',
    'chatterbot.corpus.portuguese.proverbs',
    'chatterbot.corpus.portuguese.suggestions',
    'chatterbot.corpus.portuguese.unilab',
    'chatterbot.corpus.portuguese.trivia'
 )
 
while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Nazk: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
