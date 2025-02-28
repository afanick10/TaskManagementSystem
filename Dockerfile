FROM python

RUN mkdir /testapp
WORKDIR /testapp

RUN pip install --upgrade pip
COPY requirements.txt /testapp/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /testapp/

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]