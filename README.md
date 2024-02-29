## Тестовое задание для в RLT (ООО Надежные Лояльные Технологии)

### Использование на Linux

1. Получите токен для вашего телеграм бота  через BotFhather
2. Клонируйте репозиторий
   
   ```sh
   git clone https://github.com/alexeisanko/rlt_task.git
   ```
4. Войдите в виртуальное окружение и установите необходимые библиотеки
   ```sh
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
5. Создайте переменную окружения для токена телеграм бота
   ```sh
   export TG_TOKEN="YOUR TOKEN"
   ```
6. Запустите скрипт
   ```sh
   python main.py
   ```
