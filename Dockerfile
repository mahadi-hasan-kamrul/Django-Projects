FROM python:3.11-slim-bookworm


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

RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    xfonts-base \
    xfonts-75dpi \
    fontconfig \
    fonts-liberation \
    fonts-dejavu\
    libfreetype6 \
    libjpeg62-turbo \
    libpng16-16 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    xfonts-base \
    xfonts-75dpi \
    xz-utils \
    libssl3 \
    --no-install-recommends



# Add repository for libssl1.1
RUN echo "deb http://security.debian.org/debian-security bullseye-security main" > /etc/apt/sources.list.d/bullseye-security.list

# Install wkhtmltopdf and its dependencies
RUN apt-get update && \
    apt-get install -y libssl1.1 && \
    curl -L -o wkhtmltopdf.deb "https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.bullseye_amd64.deb" && \
    apt-get install -y --no-install-recommends ./wkhtmltopdf.deb && \
    rm wkhtmltopdf.deb && \
    ln -s /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf

# Clean up
RUN rm /etc/apt/sources.list.d/bullseye-security.list && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Verify installation
RUN wkhtmltopdf --version


#COPYING EVERYTHING OF OUR PROJECT FILE
COPY . .




# Verify installation
RUN wkhtmltopdf --version

#TO MAKE OUR APP ACCESSIBLE OUTSIDE CONTAINER
EXPOSE 8000

#this is the command we are binding with docker file
# we are calling gunicorn, then we are making our app available in all the networks, then we are defining the app name correctly
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "cvgene.wsgi:application", "--workers=3" ]

#RUN chmod +x ./entrypoint.sh

#ENTRYPOINT ["./entrypoint.sh"]