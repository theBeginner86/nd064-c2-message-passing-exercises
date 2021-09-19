FROM python:3.7-slim
RUN mkdir customers_api
WORKDIR customers_api
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . .
