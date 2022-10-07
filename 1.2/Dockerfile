FROM python:3-alpine

WORKDIR /task

COPY /app /task

RUN pip install -r requirements.txt

CMD [ "python", "./index.py" ]

EXPOSE 5000