# chat-groups-api

Slack clone API built with Django.

## Requirements

- Python 3.10.5
- PostgreSQL 14.3
- Redis 7.0.2

## Setup

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Start

```sh
python manage.py runserver
```

## Docker

```sh
docker build -t chat-groups-api .
docker-compose up
```

## API

```
/
/users
/login
/channels
/channels/<int:channel_id>/messages
```
