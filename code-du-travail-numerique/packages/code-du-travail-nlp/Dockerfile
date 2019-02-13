FROM python:3.7.2-stretch

ENV APP_DIR /app
ENV FLASK_APP ./api/app

WORKDIR ${APP_DIR}

COPY requirements.txt .

RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt

COPY . .

ENV PACK_DIR ./quest2keys
WORKDIR ${PACK_DIR}
RUN pip install .
RUN python -m spacy download fr_core_news_md