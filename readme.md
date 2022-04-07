###Проект №2
В проекте реализованы 3 микросервиса: User, Issue, Book.  
Все микросервисы реализованы в рамках "чистой архитектуры".  
Микросервисы User и Book связаны с микросервисом Issue с помощью брокера сообщений <b>RabbitMQ</b>.  
Для хранение данных используется база данных <b>PostgreSQL</b>.  
Для развертывания приложения используется <b>Docker</b>.
Для запуска проекта перейдите к каталог <b>/components</b>, в командой строке введите команду <b>docker-compose up --build</b>.   
В проекте настроены пайплайны в <b>CI github</b>.