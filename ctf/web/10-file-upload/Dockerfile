FROM php:8.0-apache

# Включаем отображение ошибок для обучения
RUN echo "display_errors = On" >> /usr/local/etc/php/php.ini

# Создаем директорию для загрузок
RUN mkdir -p /var/www/html/uploads && \
    chmod 777 /var/www/html/uploads

# Копируем флаг
RUN echo "TATARHACK{f1l3_upl04d_1s_d4ng3r0us}" > /flag.txt

# Копируем приложение
COPY index.php /var/www/html/

EXPOSE 80

CMD ["apache2-foreground"]
