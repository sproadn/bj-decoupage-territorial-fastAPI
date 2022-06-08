FROM python:3.8-alpine3.15
RUN apk add build-base libffi-dev

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . .

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["python", "app.py"]