import os
import requests
import pytest
import paramiko
from datetime import datetime, timedelta, timezone

@pytest.fixture(scope="session")
def ssh_client():
    host = os.getenv("TARGET_HOST")
    port = int(os.getenv("SSH_PORT"))
    user = os.getenv("SSH_USER")
    password = os.getenv("SSH_PASS")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=user, password=password)
    yield client
    client.close()

def test_apache_running():
    host = os.getenv("TARGET_HOST")
    port = os.getenv("TARGET_PORT")
    url = f"http://{host}:{port}/index.html"
    page = requests.get(url)
    assert page.status_code == 200, f"Apache не запущен или не отвечает. Код {page.status_code}"


def test_no_errors_in_logs(ssh_client):
    interval = int(os.getenv("LOG_INTERVAL"))
    since_time = (datetime.now(timezone.utc) - timedelta(minutes=interval)).strftime("%d/%b/%Y:%H:%M:%S")
    cmd = f'awk \'$4 > "[{since_time}"\' /var/log/apache2/error.log || true'
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    errors = stdout.read().decode().strip()
    assert errors == "", f"Найдены ошибки в логах Apache2:\n{errors}"


def test_index_page_avaliable():
    host = os.getenv("TARGET_HOST")
    port = os.getenv("TARGET_PORT")
    url = f"http://{host}:{port}/index.html"
    page = requests.get(url)
    assert page.status_code == 200, f"Код ответа {page.status_code}, ожидался 200"
    assert page.text.strip(), "Страница /index.html пустая"


def test_nonexistent_page():
    host = os.getenv("TARGET_HOST")
    port = os.getenv("TARGET_PORT")
    url = f"http://{host}:{port}/does_not_exist.html"
    page = requests.get(url)
    assert page.status_code == 404, f"Код ответа {page.status_code}, ожидался 404"
