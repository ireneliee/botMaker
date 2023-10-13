from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from config import BOT_NAME

def read_file_data():
    file_path = "parse_result.txt"
    result = []
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            result = lines
        
        return result
    except Exception as e:
        print(f"An error occurred: {e}")

read_file_data()

if __name__ == "__main__":
    chatbot = ChatBot(BOT_NAME)
    trainer = ListTrainer(chatbot)
    result = read_file_data()
    trainer.train(result)

    exit_conditions = ("exit")

    while True:
        query = input("> ")
        if query in exit_conditions:
            break
        else:
            print(f"🤖{chatbot.get_response(query)}")


