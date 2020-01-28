FROM python:3.8

ENV PYTHONPATH /app
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN make dbupgrade

CMD [ "gunicorn", "api.app:get_app()" ]
