import argparse


def main():
    parser = argparse.ArgumentParser(description='OpenAI API Cheat Sheet')
    
    parser.add_argument('--completions', action='store_true', help='Information about the Completions API')
    parser.add_argument('--chat', action='store_true', help='Information about the Chat API')
    parser.add_argument('--fine-tuning', action='store_true', help='Information about the Fine-tuning API')

    args = parser.parse_args()

    if args.completions:
        print("The Completions API allows you to generate text completions based on a given prompt.")
    elif args.chat:
        print("The Chat API allows you to have a conversation with the model by sending a series of messages.")
    elif args.fine_tuning:
        print("The Fine-tuning API allows you to train a model on your own data to improve its performance on specific tasks.")

if __name__ == '__main__':
    main()
