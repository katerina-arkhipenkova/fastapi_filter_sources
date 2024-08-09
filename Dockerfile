FROM python:3.11.0

WORKDIR /fastapi_filter_sources

COPY ./requirements.txt /fastapi_filter_sources/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi_filter_sources/requirements.txt

COPY ./app /fastapi_filter_sources/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]