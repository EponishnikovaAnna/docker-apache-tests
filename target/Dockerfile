FROM debian:bookworm-slim

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        apache2 \
        openssh-server \
        passwd \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd && \
    useradd -m -s /bin/bash testuser && \
    echo 'testuser:testpass' | chpasswd


COPY ./html/index.html /var/www/html/index.html

RUN mkdir -p /var/log/apache2 && touch /var/log/apache2/error.log

EXPOSE 80 22

CMD ["bash", "-c", "service ssh start && apache2ctl -D FOREGROUND"]
