FROM python:3.8
RUN set -ex; \
    apt-get update; \
    apt-get install -y ffmpeg wkhtmltopdf tesseract-ocr-ind libleptonica-dev python3.7 libtesseract-dev libwebp6 libwebp-dev libwebpdemux2 libwebpmux3 python-zbar wget unzip iputils-ping python3-pip webp iputils-ping jp2a 
RUN wget --no-check-certificate https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt -y -f install
RUN wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip&& unzip chromedriver_linux64.zip -d /bin
RUN mkdir /mywork
COPY . /mywork
WORKDIR /mywork
ENV TZ=Asia/Jakarta
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN python3 -m pip install -r /mywork/docker_python_requirements.txt
RUN python3 -m pip install luxand flask psutil pydrive lottie cairosvg googletrans==4.0.0-rc1
ENV TERM=xterm-256color
RUN python3 -m pip install eventlet python-socketio socketio==0.2.1 socketIO-client==0.7.2 pydub rxpy3 pilgram
RUN python3 -m pip install -U setuptools
RUN python3 -m pip install -U openwa pyngrok
#CMD ttyd -p ${PORT} bash session.sh
#CMD python3 main3.py
CMD python3 main3.py