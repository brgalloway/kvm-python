# Python code collection

nginx.conf
```
http {
    include       mime.types;
    default_type  application/octet-stream;
    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    sendfile        on;
    keepalive_timeout  65;
    fastcgi_param  REMOTE_USER $remote_user;

  server {
      listen 443 default ssl;
      server_name monitoring.example.com;
      ssl_certificate /etc/ssl/monitoring.crt;
      ssl_certificate_key /etc/ssl/monitoring.key;
      add_header Strict-Transport-Security max-age=2592000;

      location / {
          proxy_pass http://127.0.0.1:4180;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Scheme $scheme;
          proxy_connect_timeout 1;
          proxy_send_timeout 30;
          proxy_read_timeout 30;
      }
   }
```
httpd.conf
`SetEnvIfNoCase ^X-Forwarded-User$ "(.*)" REMOTE_USER=$1`
