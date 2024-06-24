# drf-hf-hub

[![Ruff Lint](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/ruff.yml)
[![Black Format](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/black.yml)
[![Django CI](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/django.yml/badge.svg)](https://github.com/youzarsiph/drf-hf-hub/actions/workflows/django.yml)

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

```console
git clone https://github.com/youzarsiph/drf-hf-hub
```

Install `poetry`, a Python tool for building and publishing packages:

```console
python -m pip install poetry
```

Install dependencies:

```console
python -m poetry install
```

Activate virtual environment

```console
python -m poetry env use python
```

Create a new Django project:

```console
python -m django startproject mysite
```

Copy `drf_hf_hub` to `mysite`:

```console
cp -r drf_hf_hub mysite/drf_hf_hub
```

Configure project settings, open `mysite/settings.py`:

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

Then open `mysite/urls.py`:

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

```console
python manage.py check
```

Create a `.env` file that contains your HuggingFace access token, you may need to create an account on [HuggingFace](https://huggingface.co/):

```bash
# Your HF access token
HF_TOKEN=hf_**********************************

```

Or you can export `HF_TOKEN` env variable.

Now you are ready to go.
