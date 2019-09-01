	# Source Image

FROM ubuntu:18.04
# Mainter Name
maintainer Rahul Gupta <rahul.itnetwork@gmail.com>

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get clean all
RUN pip install xlrd
RUN pip install python-multipart
RUN mkdir /app
ADD . /app/
WORKDIR	/app/
# Command to update and install Apache packages
#RUN apt-get update && apt-get install -y software=properties-common && apt-get-repository ppa:ondrej/php && apt-get update
#ARG DEBIAN_FRONTEND=noninteractive
#RUN apt-get update && apt-get install apache2 -y
#to pass all the interactive pop up auto
#ARG DEBIAN_FRONTEND=noninteractive
#Commands to install php5.6 including other modules
#RUN apt-get install -y php5.6 libapache2-mod-php
# Update our TimeZone in php.ini file
#RUN echo "date.timezone = Asia/Kolkata" > /etc/php/5.6/apache2/php.ini
#Create website document root directoy and logs folder
#RUN mkdir /var/www/html/web1/
#RUN mkdir /var/www/html/web1/public/
#RUN mkdir /var/www/html/web1/logs/
# Copy index.html and info.php file to Web document folder
#copy index.html /var/www/html/web1/public
#copy info.php /var/www/html/web1/public
#copy info.php /var/www/html
#Copy apache virual hostconfiguration file and enable it
#copy testamar.conf /etc/apache2/sites-available/
#RUN a2ensite testamar.conf
#Check apache server configuration
#RUN apachectl -t
# open port 
#EXPOSE 80
CMD ["python","sendmail.py"]
# Command to run Apache server in background
#CMD /usr/sbin/apache2ctl -D FOREGROUND
