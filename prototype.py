from tkinter import *
import json
from difflib import get_close_matches


def load_knowledge_base(file_path: str):
    """
    Read the knowledge base from a JSON file.

    :param file_path: The path to the JSON file containing the knowledge base.
    :return: A dictionary with the knowledge base data.
    """
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


# Save the updated knowledge base to the JSON file
def save_knowledge_base(file_path: str, data: dict):
    """
    Write the updated knowledge base to a JSON file.

    :param file_path: The path to the JSON file to save the knowledge base.
    :param data: A dictionary with the knowledge base data.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None


def chatbot():

    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input = queryField.get()
        textarea.insert(END,'You: '+user_input+'\n\n')
        queryField.delete(0,END)

        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            # If there is a best match, return the answer from the knowledge base
            answer: str = get_answer_for_question(best_match, knowledge_base)
            textarea.insert(END,"Alpha: "+answer+"\n\n")
        else:
            textarea.insert(END,"Alpha: I don't know the answer. Can you teach me?\n\n")
            new_answer = queryField.get()

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                textarea.insert(END,"Alpha: Thank you! I've learned something new.\n\n")


if __name__ == "__main__":
    chatbot()


root = Tk()

root.geometry('520x590+100+30')

root.title('A.G.D.A.V Public School Assistance Chatbot')

root.config(bg='white')
logoPic = PhotoImage(file='agdavlogo.png')
logoLabel = Label(root,image=logoPic)
logoLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame,height=20,yscrollcommand=scrollbar.set,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

queryField = Entry(root)
queryField.config(bg='light grey')
queryField.pack(pady=15,fill=X)


buttonPic = PhotoImage(file='send.png',height=57,width=67)

button = Button(root, image=buttonPic, command=chatbot)
button.pack()


logoLabel.pack()
root.mainloop()
