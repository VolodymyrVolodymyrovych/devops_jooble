У головному файлі app.py містяться декоратори «@app.route», за якими і відбувається вся динаміка переходу прогрми між функціональностями. Кожен з декораторі має методи GET і/або POST. 
	Якщо форма має метод GET, то вертається файл .html сторінки відповідного змісту. 
	Якщо надсилається метод POST, то спершу app.py отримує дані з html сторінки за допомогою методу request.form, записуючи їх в змінні. І потом ці змінні передаються відповідним функціям модулю sqlalchemy, які взаємодіють з базою даних і вертають результат, який далі додається до html файлу і вертається користувачу.
	app.py має 6 декораторів:
	/ (він же '/home') Головна сторінка, яка не має полів для вводу і виводу даних.
	/define-data - інтерфейс для отримання запису по id. Має одне поле для запрошення id у клієнта. Дані записуються у зміну 'id' як <str>. Потім у строці: 
"users = db.session.query(User).get(id_)"
робиться екземпляр класу 'User'. Який у свою чергу, користуючись методами sqlalchemy, знаходить запис в таблиці за id. І, в завершення, користувачу вертається сторінка output-data.html із результатом метода (users=users).
	/users_all - інтерфейс для отримання всіх записів в таблиці. Тут не приймаються ніякі дані від клієнта. Так, само в зміну user присвоюється екземпляр класу User, що використовує методи sqlalchemy. В результаті отримуєтсья весь список записів і виводиться в інтерфейс "users_all.html" із змінною users, і яка містить весь список. 
	/delete-data - інтерфейс для видалення запису по id. Тут аналогічно до декоратора "/define-data" запрошується id в користувача. Запис екземпляру класу User. І через метод модуля sqlalchemy виконується видалення запису. Далі, в рядку:
 db.session.commit()
зберігаються зміни в таблицю. І переходить до інтерфейсу списку всіх записів users_all.html
	/add-data - інтерфейс для додання запису. Тут запрошуються 2 змінних. Це 'first_name' і 'second_name'. Вони записуються у відповідні змінні і через метод модуля sqlalchemy додають новий запис до таблиці, де id генерується автоматично. По завершунню переходить на головний інтерфейс "/".
	/change-data - інтерфейс для редагування існуючого запису за його id. Запрошується 3 змінних: id, first_name, second_name. Передаються методам модуля sqlalchemy, де редагують запис. Та повертають на головний інтерфейс '/'.
	В декораторах, де відбувається запит даних від користувача, приймаються два метода: 'POST'і 'GET'. В методі POST (де передаються, якісь дані програмі з веб-інтерфейса) виконується взаємодія з базою даних.  А в - GET (де не передаються ніякі дані) повертається та ж сама сторінка html.