import subprocess


subprocess.run('alembic revision --autogenerate -m "update"')
subprocess.run("alembic upgrade head")