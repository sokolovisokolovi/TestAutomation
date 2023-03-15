# Test_A
Прохождение курса на степике Автоматизация тестирования с помощью Selenium и Python


Пометки:

1. Типы модальных окон в браузере с методами WebDriver для взаимодействия с ним:
    alert может только подтвердить
    confirm подтвердить и отказать
    prompt подтвердить, отказать и принять текст
    
2. Команды для манипуляции выводом тестов PyTest
    py.test test_sample.py --collect-only  #собирает информацию набор тестов
    py.test test_sample.py -v  #выводит подробные сообщения
    py.test -q test_sample.py  #опустить вывод имени файла
    python -m pytest -q test_sample.py  #вызов pytest через python
    py.test --markers  #показать доступные маркеры
    py.test -k "TestClass and not test_one"  #запускайте тесты только с именами, соответствующими "строковому выражению"
    py.test test_server.py::TestClass::test_method  # запускайте только те тесты, которые соответствуют ID
    py.test -x  # остановка после первой неудачи
    py.test --maxfail=2  # остановка после двух неудач
    py.test --showlocals  # показывать локальные переменные в обратных трассировках
    py.test -l  # (shortcut)
    py.test --tb=long  # информативное форматирование обратной трассировки по умолчанию
    py.test --tb=native  # форматирование стандартной библиотеки Python
    py.test --tb=short  # более короткий формат обратной трассировки
    py.test --tb=line  # только одна строка на сбой
    py.test --tb=no  # нет вывода обратной трассировки
    py.test -x --pdb # перейдите в PDB при первом сбое, затем завершите тестовый сеанс
    py.test --durations=10  # список 10 самых медленных по продолжительности тестов.
    py.test --maxfail=2 -rf  # завершите работу после 2 сбоев, сообщите информацию о сбое.
    py.test -n 4  # отправка тестов на несколько процессоров
    py.test -m slowest  # отменить тесты с помощью декоратора @pytest.mark.lowest или slowest медленнее всего = pytest.mark.slowest; @slowest
    py.test --traceconfig  # узнайте, какие плагины py.test активны в вашей среде.
    py.test --instafail  # если установлен pytest-instafail, показывайте ошибки и сбои мгновенно, вместо того, чтобы ждать окончания набора тестов.
    
3. Маркировка тестов.
    @pytest.mark.smoke #запускаем только смок тесты
    @pytest.mark.win10 #запускаем тесты для вин 10
    @pytest.mark.skip  #пропустить тест
    @pytest.mark.xfail #Отметить тест как падающий (xfail можно добавлять параметр reason) Запуск(pytest -rx -v name_file.py)
    @pytest.mark.smoke # Запуска всех тестов, не отмеченных как smoke (pytest -s -v -m "not smoke" name_file.py)
    
    #запуск тестов с разными маркерами
    @pytest.mark.smoke
    @pytest.mark.regression : pytest -s -v -m "smoke or regression" name_file.py

    #Запуск нескольких маркеровок
    @pytest.mark.smoke
    @pytest.mark.win10 : pytest -s -v -m "smoke and win10" name_file.py

    #пропуск некольких тестов
    @pytest.mark.skip : pytest -s -v  name_file.py
    
    #написать тест ожидаемо падающий
    @pytest.mark.xfail : pytest -rx -v name_file.py
    
    #параметны на тест
    @pytest.mark.parametrize()   pytest -s -v  name_file.py

    
    

