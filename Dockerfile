FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./chat_groups_api ./chat_groups_api
COPY manage.py .

CMD [ "python", "manage.py", "runserver" , "0.0.0.0:8000"]
