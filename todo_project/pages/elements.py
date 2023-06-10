from abc import ABC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from todo_project.page_objects import PageElement

class Todo(PageElement):
    name = (By.ID, "todo-name")
    description = (By.ID, "todo-desc")
    urgent = (By.ID, "todo-next")
    submit = (By.ID, "todo-submit")

    def create_todo(self, name, description, urgent=False):
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.description).send_keys(description)
        if urgent:
            self.driver.find_element(*self.urgent).send_keys(urgent)
        self.driver.find_element(*self.submit).click()
