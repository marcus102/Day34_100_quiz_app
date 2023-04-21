from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain
    self.window= Tk()
    self.window.title('Quizzler!')
    self.window.config(bg=THEME_COLOR, padx=20,pady=20)
    
    self.check= PhotoImage(file="images/true.png")
    self.cross= PhotoImage(file="images/false.png")
    
    self.canvas= Canvas(width=300, height=250, bg='#ffffff', highlightthickness=0)
    self.quetion= self.canvas.create_text(150, 125, text='Test', fill= THEME_COLOR,font=('arial', 20, 'italic'), width=280)
    self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
    
    self.score= Label(text='Score: 0', font=('arial', 15, 'bold'),bg= THEME_COLOR, highlightthickness=0, fg='#ffffff')
    self.score.grid(column=1, row=0)
    
    self.true = Button(image= self.check, highlightthickness=0, command= self.true_pressed)
    self.true.grid(column=0, row=2)
    
    self.false = Button(image= self.cross, highlightthickness=0, command= self.false_pressed)
    self.false.grid(column=1, row=2)
    
    self.get_next_question()
    
    self.window.mainloop()
    
  def get_next_question(self):
    self.canvas.config(bg='#ffffff')
    if self.quiz.still_has_questions():
      self.score.config(text=f'Score: {self.quiz.score}')
      question_text= self.quiz.next_question()
      self.canvas.itemconfig(self.quetion, text= question_text)
    else:
      self.canvas.itemconfig(self.quetion, text="That's the end of the quiz!")
      self.true.config(state='disabled')
      self.false.config(state='disabled')
    
  def true_pressed(self):
    self.give_feedback(self.quiz.check_answer('True'))
    
  def false_pressed(self):
    self.give_feedback(self.quiz.check_answer('False'))
    
  def give_feedback(self, is_right):
    if is_right:
      self.canvas.config(bg='green')
    else:
      self.canvas.config(bg='red')
      
    self.window.after(1000, self.get_next_question)

