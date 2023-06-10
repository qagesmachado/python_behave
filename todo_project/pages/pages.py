from todo_project.page_objects import Page
from .elemements import AFazer, Fazendo, Pronto, Todo

class PageTodo(Page):
    a_fazer = AFazer()
    fazendo = Fazendo()
    pronto = Pronto()
    todo = Todo()