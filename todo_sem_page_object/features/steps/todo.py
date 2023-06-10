from json import loads
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from time import sleep


@given('Que eu esteja na página')
def go_to_page(context):
    context.driver.get("https://selenium.dunossauro.live/todo_list.html")
    
@when('criar um todo')
def create_todo(context):
    texto_do_step = loads(context.text)
    context.driver.find_element(By.ID, "todo-name").send_keys(texto_do_step['nome'])
    context.driver.find_element(By.ID, "todo-desc").send_keys(texto_do_step['descricao'])
    context.driver.find_element(By.ID, "todo-submit").send_keys(Keys.ENTER)
    

@then('o todo dever estar na planilha "{pilha}"')
def check_todo(context, pilha):
    assert 'Dormir' in context.driver.find_element(By.CLASS_NAME, "body_a").text
