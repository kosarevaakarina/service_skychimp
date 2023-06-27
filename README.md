Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд:

python -m venv venv 
source venv/bin/activate 
pip install -r requirement.txt

Для запуска celery-beat: 
celery -A config beat --loglevel=info

Для запуска redis: 
redis-cli

Для заполнения моделей данными необходимо выполнить следующую команду: 
python3 manage.py fill

Для запуска приложения: 
python3 manage.py runserver

Для отправки рассылки из командной строки: 
python3 manage.py sendmessage N, где N - это pk рассылки

Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample
