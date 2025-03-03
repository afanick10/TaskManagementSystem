FROM python:3.9

RUN mkdir /tmsapp
WORKDIR /tmsapp

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt /tmsapp/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /tmsapp/

EXPOSE 8000

CMD [ "python", "TaskManagementSystem/manage.py", "runserver", "0.0.0.0:8000" ]