# chat-groups-api

Slack clone API built with Django.

## Requirements

- Python 3.10.5

## Setup

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## API

```
/
/users
/login
/channels
/channels/<int:channel_id>/messages
```
