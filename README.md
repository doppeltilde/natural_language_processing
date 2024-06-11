# Natural Language Processing.

## Stack:
- [FastAPI](https://fastapi.tiangolo.com)
- [Python](https://www.python.org)
- [Docker](https://docker.com)

## Installation

- For ease of use it's recommended to use the provided [docker-compose.yml](https://github.com/doppeltilde/natural_language_processing/blob/main/docker-compose.yml).

**CPU Support:** Use the `latest` tag.
```yml
services:
  natural_language_processing:
    image: ghcr.io/doppeltilde/natural_language_processing:latest
    ports:
      - "8000:8000"
    volumes:
      - models:/root/.cache/huggingface/hub:rw
    environment:
      - DEFAULT_SUMMARIZATION_MODEL_NAME
      - DEFAULT_TRANSLATION_MODEL_NAME
      - ACCESS_TOKEN
      - USE_API_KEYS
      - API_KEYS
    restart: unless-stopped

volumes:
  models:
```

**NVIDIA GPU Support:** Use the `latest-cuda` tag.
```yml
services:
  natural_language_processing_cuda:
    image: ghcr.io/doppeltilde/natural_language_processing:latest-cuda
    ports:
      - "8000:8000"
    volumes:
      - models:/root/.cache/huggingface/hub:rw
    environment:
      - DEFAULT_SUMMARIZATION_MODEL_NAME
      - DEFAULT_TRANSLATION_MODEL_NAME
      - ACCESS_TOKEN
      - DEFAULT_SCORE
      - USE_API_KEYS
      - API_KEYS
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [ gpu ]

volumes:
  models:
```

---

### Environment Variables

- Create a `.env` file and set the preferred values.
```sh
DEFAULT_SUMMARIZATION_MODEL_NAME=Falconsai/text_summarization
DEFAULT_TRANSLATION_MODEL_NAME=google-t5/t5-base
ACCESS_TOKEN=

# False == Public Access
# True == Access Only with API Key
USE_API_KEYS=False

# Comma seperated api keys
API_KEYS=abc,123,xyz
```

## Supported NLP tasks
- [x] [Summarization](https://huggingface.co/tasks/summarization)
- [x] [Translation](https://huggingface.co/tasks/translation)

## Models
Any model designed for above tasks and compatible with huggingface transformers should work.

## Usage

> [!NOTE]
> Please be aware that the initial process may require some time, as the model is being downloaded.

> [!TIP]
> Interactive API documentation can be found at: http://localhost:8000/docs

---

_Notice:_ _This project was initally created to be used in-house, as such the
development is first and foremost aligned with the internal requirements._