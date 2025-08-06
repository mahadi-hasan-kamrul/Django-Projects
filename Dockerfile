FROM python:3.11

#TO MAKE IT FAST, IT REDUCES STOREGE USAGE
ENV PYTHONDONTWRITEBYTECODE=1

#IT WILL ENSURE THAT OUR PYTHON RESULT WILL GO INTO THE TERMINAL IN NO TIME
ENV PYTHONBUFFERED=1 

#DEFINING WORKING DIRECTORY
WORKDIR /APP

#COPYING THE REQUIREMENMTS FILE
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#COPYING EVERYTHING OF OUR PROJECT FILE
COPY . .

#TO MAKE OUR APP ACCESSIBLE OUTSIDE CONTAINER
EXPOSE 8000

#this is the command we are binding with docker file
# we are calling gunicorn, then we are making our app available in all the networks, then we are defining the app name correctly
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "scrapper.wsgi:application", "--workers=3" ]

#RUN chmod +x ./entrypoint.sh

#ENTRYPOINT ["./entrypoint.sh"]