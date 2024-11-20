FROM nginx:alpine

# Copia os arquivos do front-end para o diretório padrão do Nginx
COPY index.html /usr/share/nginx/html/index.html
COPY script.js /usr/share/nginx/html/script.js
COPY style.css /usr/share/nginx/html/style.css
COPY nginx.conf /etc/nginx/nginx.conf

# Expor a porta do Nginx
EXPOSE 80
