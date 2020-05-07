from fastapi.testclient import TestClient
from pathlib import Path

test_files_directory = f"{Path.cwd()}/tests/files/"
Path(test_files_directory).mkdir(parents=True, exist_ok=True)
file = Path(test_files_directory) / "access.log"
Path(file).touch()

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.text == "ok"
