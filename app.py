import ollama

with open("music_data.txt", "r") as file:
    music_data = file.read()

print("🎵 Music Assistant is running! Type 'exit' to quit.\n")

while True:
    question = input("Ask a music question: ")

    if question.lower() == "exit":
        break

    response = ollama.chat(
        model="music-assistant",
        messages=[
            {
                "role": "user",
                "content": f"""
You are a music assistant.

Use this music data to answer:

{music_data}

Question: {question}
"""
            }
        ]
    )

    print("\nAnswer:\n")
    print(response["message"]["content"])
    print("\n-----------------\n")