FROM python:3.9-alpine

COPY ./ /app/
COPY ./requirements.txt /app/requirements.txt
# "-p" - create all chain with parent dirs, if any
RUN mkdir -p /cache
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:12801", "app:app"]
