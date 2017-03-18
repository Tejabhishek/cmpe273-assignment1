FROM python:2.7.13
MAINTAINER Tejabhishek “tejabhishek@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["https://github.com/Tejabhishek/cmpe273-assignment1”]
