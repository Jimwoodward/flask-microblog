FROM ubuntu:bionic
RUN apt-get update -y -qq
RUN apt-get -qq -y install python-pip python-dev build-essential
WORKDIR /source
COPY microblog.py .
RUN mkdir app/
COPY app/* app/
RUN pip install Flask
ENV FLASK_APP, microblog.py
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["microblog.py"]