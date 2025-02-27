from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import json

# Membuat chatbot
chatbot = ChatBot(
    'MyCustomChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
    ],
    database_uri='sqlite:///database.db'
)

# Membuat trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Melatih chatbot dengan corpus bahasa Inggris
trainer.train('chatterbot.corpus.english')

# Melatih chatbot dengan dataset kustom (misalnya file JSON)
def train_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    for entry in data:
        # Anggap format dataset adalah {"input": "question", "output": "answer"}
        chatbot.set_trainer(ChatterBotCorpusTrainer)
        chatbot.train(entry["input"], entry["output"])

# Misalnya, melatih dengan file dataset "data.json"
train_from_json('data.json')

print("Bot has been trained with custom data!")
