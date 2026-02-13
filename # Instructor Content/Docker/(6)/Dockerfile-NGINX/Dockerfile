FROM nginx:1.27.0

RUN apt-get update
RUN apt-get install vim -y 

# /usr/share/nginx/html is the default root directory for nginx
COPY ./index.html /usr/share/nginx/html

# Maybe only in windows, in linux it is not needed
RUN chown nginx:nginx /usr/share/nginx/html/index.html