from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😠"
    else:
        return "Neutral 😐"

def main():
    print("=== Sentiment Analysis Tool ===")
    print("Type your sentence (or type 'exit' to quit):")

    while True:
        user_input = input("\nEnter text: ")

        if user_input.lower() == 'exit':
            print("Exiting the tool. Goodbye!")
            break

        sentiment = get_sentiment(user_input)
        print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()