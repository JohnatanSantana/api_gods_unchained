FROM python:3.8

WORKDIR /code/
COPY . .

EXPOSE 8000

RUN pip install --no-cache-dir  -r requirements.txt
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.app:app"]
