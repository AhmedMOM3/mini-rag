# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.8 or later

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install)
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag-app python=3.8
```

3) Activate the environment using the following command:
```bash
$ conda activate mini-rag-app
```

### (Optional) Setup you command line interface for better readability

```shell
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packeges

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set you environment variables in the `.env` file, like `OPENAI_API_KEY` value

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Download the POSTMAN collection from [here](/assets/mini-rag-app.postman_collection.json)
