FROM python:3.10-slim

WORKDIR /app

COPY app/ app/
COPY tests/ tests/

RUN pip install flask requests pytest

EXPOSE 5000

CMD ["python", "app/main.py"]
