FROM prestashop/prestashop:1.7.8

# Zmiana uprawnień
RUN chown -R www-data:www-data /var/www/html
Run find /var/www/html -type d -exec chmod 755 {} \;

CMD ["apache2-foreground"]
