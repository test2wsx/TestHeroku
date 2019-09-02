FROM ubuntu

RUN apt-get update
RUN apt-get install apt-utils -y
RUN apt-get install sudo -y
RUN apt-get install vim -y
RUN apt-get install python -y
RUN apt-get install mysql-server -y
RUN apt-get install python-mysqldb -y
RUN apt-get install nginx -y
RUN apt-get install python-pip -y
RUN apt-get install libmysqlclient-dev -y

CMD service mysql start
CMD service nginx start

RUN mysql -u root -e "CREATE USER 'shiori_admin'@'localhost' IDENTIFIED BY 'blabla';"
RUN mysql -u root -e "CREATE DATABASE shiori_db;"
RUN mysql -u root -e "GRANT ALL PRIVILEGES ON shiori_db . * TO 'shiori_admin'@'localhost';"

USER bob
WORKDIR ../shioriProject

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD flask db init
CMD flask db migrate
CMD flask run

