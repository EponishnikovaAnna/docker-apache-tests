FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv openssh-client && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir pytest requests paramiko

RUN useradd -m -d /home/tester -s /bin/bash tester
USER tester
WORKDIR /home/tester

COPY agent/tests/ /home/tester/tests/

CMD ["pytest", "-v", "tests/"]
