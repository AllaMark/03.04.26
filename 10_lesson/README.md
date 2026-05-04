# 03.04.26
Тесты в этой папке размечены при помощи Allure. 
Для запуска тестов необходимо в терминале перейти в папку с уроком 10: cd .\10_lesson\
Ввести в терминале команду для запуска теста калькулятора: pytest test_calc.py --alluredir=./allure-results
Ввести в терминале команду для запуска теста магазина: pytest test_shop.py --alluredir=./allure-results
Ввести в терминале команду для просмотра отчета в браузере: allure serve ./allure-results
Ввести в терминале команду для формирования отчета в папке урока: allure generate ./allure-results -o ./allure-report --clean