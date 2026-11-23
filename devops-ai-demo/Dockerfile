FROM python:3.12-slim

WORKDIR /app

COPY app.py ./app.py
COPY run.sh ./run.sh

RUN pip install --no-cache-dir flask \
    && chmod +x ./run.sh

# TODO pour le demo : ce port ne correspond pas au port utilisé dans app.py.
EXPOSE 8000

CMD ["./run.sh"]
