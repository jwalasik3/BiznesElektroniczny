FROM prestashop/prestashop:1.7.8

RUN apt-get update && apt-get install -y openssl

RUN mkdir -p /etc/apache2/private && mkdir -p /etc/apache2/certs

RUN openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /etc/apache2/private/sslkey.key -out /etc/apache2/certs/sslcertificate.crt -subj "/C=PL/ST=pomorskie/L=Gdansk/O=./OU=./CN=localhost"

RUN chown www-data:www-data /etc/apache2/private/sslkey.key /etc/apache2/certs/sslcertificate.crt

COPY ./000-default.conf /etc/apache2/sites-available/000-default.conf

RUN a2enmod ssl && a2ensite 000-default.conf

CMD ["apache2-foreground"]
