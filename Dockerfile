FROM prestashop/prestashop:1.7.8

# Zmiana uprawnień
RUN chown -R www-data:www-data /var/www/html
RUN find /var/www/html -type d -exec chmod 755 {} \;
RUN find /var/www/html -type f -exec chmod 644 {} \;
CMD ["apache2-foreground"]
