# MyPrj2var

MyPrj2var - веб сервис, основное предназначение которого - генерация кода с использованием большой языковой модели Chat-GPT 3.5 turbo.

## Используемые компоненты
```Python 3.12.1```
```Django 5.0```
```g4f 0.1.7.9```
```markdown 3.5.1```


## Установка и запуск

Скачать папку проекта, установить необходимые компоненты. Нажать Shift + ПКМ по корневой папке и отрыть окно PowerShell, далее ввести команду ```python manage.py runserver```. После запуска локального сервера вы увидите адрес, введя который в поисковую строку, вы попадаете на само приложение.


## Использование

Введите ваш запрос в поле для ввода, затем нажмите на кнопку для выбора языка программирования, далее нажать кнопку отправки и дождаться ответа.


## Возможные ошибки при использовании и способы их устранения

* Неправильная подсветка кода/код выдается в одну строку -  повторить запрос еще раз
* "It seems you want to use our service but are not doing so from VoiGPT.com Come over to VoiGPT.com to experience a free in the web voice assistant. VoiGPT has identifed your IP address to be linked with illegal use of our service. If you are using a VPN, please change servers or turn it off to continue use." - Включить впн
