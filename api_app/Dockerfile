FROM python:3.6-alpine
ENV TZ=UTC
COPY requirements.txt /tmp/

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
 && echo $TZ > /etc/timezone \
 && mkdir /flask_app \
 && mkdir /flask_app/configs \
 && pip install -Ur /tmp/requirements.txt

COPY ./ /flask_app
CMD sh -c "python /flask_app/run.py"