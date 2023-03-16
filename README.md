В репозитории находится итоговый проект по курсу "Тестировщик-автоматизатор на Python" от SkillFactory. Объект тестирования: страницы Авторизации/Регистрации/Восстановления пароля личного кабинета Росстелеком. Ссылка на ЛК Ростелеком: https://b2c.passport.rt.ru

По заданию тестирования необходимо:

1. Протестировать требования.
2. Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
3. Провести автоматизированное тестирование продукта (не менее 15 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
4. Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)



С тест-кейсами и описанными багами/дефектами/недостатками можно ознакомиться по ссылке: https://docs.google.com/spreadsheets/d/1ckSP5ieUjjKbeOwI3bCsBhD1tj3lwqkY285kyp2PP14/edit?usp=sharing  
Проект выполнен с помощью библиотек Pytest и Selenium 
Все тесты находятся в папке tests, файл test_rostelecom.py 
Так же в папке tests находится файл consts, содержащий тестовые данные и локаторы 
При тестировании применялись такие техники тест-дизайна как: Проверка граничных значений, эквивалентное разделение, предугадывание ошибки, исследовательское тестирование



Сценарии работы автотестов:

1. Несколько тестов проверяют редирект по клику на страницы: Регистрация нового пользователя, Восстановление пароля, Пользователького соглашения, авторизации при помощи VK аккаунта, авторизации при помощи OK аккаунта, авторизации при помощи Mail аккаунта, авторизации при помощи Google аккаунта, авторизации при помощи Yandex аккаунта.
2. Проверка корректного изменения поля ввода логина в соответствии с выбранным табом
3. Корректно проходит валидация типа логина (мобилный телефон, почта, логин, личный счёт) в автоматическом режиме
4. Несколько тестов проверяющих появления ошибок при некорректном вводе данных на странице Регистрации
5. На странице Восстановления пароля так же проверены обновление капчи и работоспособность кнопки Вернуться назад



Для работы автотестов необходимы библиотеки Pytest и Selenium. В проекте присутствует webdriver Selenium для Chrome, что облегчает запуск тестов. Запустить тесты можно через терминал прописав последовательно: "cd FinalProject/tests" и "pytest"/