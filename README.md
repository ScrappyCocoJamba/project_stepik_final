# project_stepik_final

Course about autotests on python

https://stepik.org/lesson/187065/

11/23/2020 updated: I've had some troubles with yearly-statistic dashboard. My commits were not shown on this dashboard. I found a problem and solved it. git config user.name and git config user.email were wrong for my git account. Although I use IDE PyCharm by JetBrains and I've been connected from UI my wrong credentials have been used.

12/5/2020 updated: To create/update a file with actual packages and plugins you should run in terminal: pip freeze > requirements.txt after in the new env run: pip install -r requirements.txt

To create env, in the created dir:

python -m venv "name"
env_name\Scripts\activate.bat

30/12/2020 upd: 
base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

Файл test_main_page.py - тут мы выполняем сами тесты. Тут вызванные функции будут запускаться.

Здесь мы будем создавать функции, которым:

1. выдаём нужный для проверки линк
1. созаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
1. следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
1. добавляем проверки, которые создавали методами в main_page.py