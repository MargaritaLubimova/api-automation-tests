pytest --alluredir=./tests/allure/result/ ./tests/API_tests.py 
/usr/local/lib/node_modules/allure-commandline/bin/allure generate -c -o ./tests/allure/report ./tests/allure/result
