from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Before
def before_all(context):
    options = Options()
    options.add_experimental_option('detach', True)
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# def before_feature(contex):
#     ...

# def before_scenario(contex):
#     ...

# def before_step(contex):
#     ...

# After
def after_all(context):
    context.driver.quit()

# def after_feature(contex):
#     ...

# def after_scenario(contex):
#     ...

# def after_step(contex):
#     ...