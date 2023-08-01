from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Alpha')
trainer = ListTrainer(bot)

data = open('conversations.yml','r',encoding='utf-8').readline()

trainer.train(data)


def bot_reply():
    question = queryField.get()
    answer = bot.get_response(question)
    textarea.insert(END,'You: '+question+'/n/n')
    textarea.insert(END,'Alpha: '+answer)
    queryField.delete(0,END)


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

button = Button(root, image=buttonPic, command=bot_reply)
button.pack()


logoLabel.pack()
root.mainloop()
