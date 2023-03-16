driverPathChrome = 'driver/chromedriver.exe'
baseUrl = 'https://b2c.passport.rt.ru'

registerFormKeysFirstName = ['A', 'Ab', '!@#$', 'aбвгдеёжзиклмнопрстуфхчшщъыьэюя', 'Юлия']
registerFormKeysLastName = ['A', 'Ab', '!@#$', 'aбвгдеёжзиклмнопрстуфхчшщъыьэюя', 'Юлия']
registerFormKeysAddress = ['A', '!@#$', 'aбвгдеёжзиклмнопрстуфхчшщъыьэюя', '9205555095', 'test@mail.ru']
registerFormPassword = ['а', 'аааааааа', 'abcdefgh', 'abcdefgh1', 'Abcdefgh1']
registerKeysDict = {
    'firstName': registerFormKeysFirstName,
    'lastName': registerFormKeysLastName
}

registerErrorsName = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
registerErrorsAddress = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
registerErrorsPasswordConfirm = 'Пароли не совпадают'
regErPass = 'Длина пароля должна быть не менее 8 символов'

tabButtonsId = ['t-btn-tab-phone', 't-btn-tab-mail', 't-btn-tab-login', 't-btn-tab-ls']
placeholderInputsValue = ['Мобильный телефон', 'Электронная почта', 'Логин', 'Лицевой счёт']
tabTitles = ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']
sendedKeys = ['79102290979', 'test@test.ru', '848624620025', 'someText']
placeValue = ['Мобильный телефон', 'Электронная почта', 'Лицевой счёт', 'Логин']
tabTitlesAuth = ['Телефон', 'Почта', 'Лицевой счёт', 'Логин']
activeTab = 'rt-tab--active'