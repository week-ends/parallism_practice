# parallism_practice

- Install RabbitMQ
```shell
sudo apt-get install rabbitmq-server
```

- Activating the Page Plug-in for managing rabbitmq
```shell
sudo rabbitmq-plugins enable rabbitmq_management
```

- Set user to id:root/pw:1234; Grant administrator tags
```shell
 sudo rabbitmqctl add_user root 1234
 sudo rabbitmqctl set_user_tags root administrator
```

- Setup Celery
```shell
pip install celery
```
