# drf-hf-hub

[![Ruff Lint](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/ruff.yml)
[![Black Format](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/black.yml)
[![Django CI](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/django.yml/badge.svg)](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/django.yml)
[![Docker](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/docker-publish.yml)
[![Docker Image CI](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/docker-image.yml/badge.svg)](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/docker-image.yml)

Django REST Framework micro service for common AI tasks using HuggingFace Hub

## Supported tasks

Here is a list of supported tasks in the API:

- Chat Completion
- Feature Extraction
- Fill Mask
- Question Answering
- Sentence Similarity
- Summarization
- Text Classification
- Text Generation
- Text To Image
- Text To Speech
- Token Classification
- Translation
- Zero Shot Classification

## Get started

Clone the repo:

```bash
git clone https://github.com/youzarsiph/drf-hf-hub
```

Install `poetry`, a Python tool for building and publishing packages:

```bash
python -m pip install poetry
```

Install dependencies:

```bash
python -m poetry install
```

Activate virtual environment

```bash
python -m poetry env use python
```

Create a new Django project:

```bash
python -m django startproject project
```

Copy `drf_hf_hub` to `project`:

```bash
cp -r drf_hf_hub project/drf_hf_hub
```

Configure project settings, open `project/settings.py`:

```python
...

# Application definition
INSTALLED_APPS = [
    # Add the following lines
    "drf_hf_hub",
    "drf_redesign",
    "rest_framework",
    ...
]

...
```

Then open `project/urls.py`:

```python
...
from django.urls import include, path

urlpatterns = [
    ...
    # Add the following lines
    path("", include("drf_hf_hub.urls")),
    path("", include("rest_framework.urls")),
]

```

Run `check`:

```bash
python manage.py check
```

Create a `.env` file that contains your HuggingFace access token, you may need to create an account on [HuggingFace](https://huggingface.co/):

```env
# Your HF access token
HF_TOKEN=hf_**********************************

```

Or you can export `HF_TOKEN` env variable.

Now you are ready to go.
