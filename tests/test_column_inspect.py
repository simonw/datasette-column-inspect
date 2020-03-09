import datasette
from datasette.app import Datasette
import pytest
import sqlite_utils
import httpx


@pytest.fixture
def db_path(tmpdir):
    path = str(tmpdir / "data.db")
    db = sqlite_utils.Database(path)
    db["creatures"].insert_all(
        [
            {"name": "Cleo", "description": "A medium sized dog"},
            {"name": "Siroco", "description": "A troublesome Kakapo"},
        ]
    )
    return path


@pytest.mark.asyncio
async def test_table_page_has_script_on_it(db_path):
    app = Datasette([db_path]).app()
    async with httpx.AsyncClient(app=app) as client:
        response = await client.get("http://localhost/data/creatures")
    assert 200 == response.status_code
    assert b"wrapper.style.display = 'flex';" in response.content
