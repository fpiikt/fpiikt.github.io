```sh
php -help

# -S <addr>:<port> Run with built-in web server.
```

Запуск приложения: 

```sh
php -S localhost:4321 -t public public/index.php 

```
В браузере: http://localhost:4321. Маршрут - есть. 

Такого маршрута нет:
```sh
curl -iX GET http://localhost:4321/x

```