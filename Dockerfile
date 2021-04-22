FROM python:3.8
RUN set -ex; \
    apt-get update; \
    apt-get install -y ffmpeg wkhtmltopdf tesseract-ocr-ind libleptonica-dev python3.7 libtesseract-dev libwebp6 libwebp-dev libwebpdemux2 libwebpmux3 python-zbar wget unzip iputils-ping python3-pip webp iputils-ping jp2a 
RUN wget --no-check-certificate https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt -y -f install
#ttyd requirements
#RUN set -ex;\ 
#    apt-get update;\
#    apt-get install build-essential cmake git libjson-c-dev libwebsockets-dev fakeroot proot byobu neofetch ffmpeg neofetch vim nano nmap byobu nodejs npm ruby ruby-dev -y
#RUN git clone https://github.com/tsl0922/ttyd.git
#RUN cd ttyd && mkdir build && cd build && cmake .. && make && make install
RUN wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip&& unzip chromedriver_linux64.zip -d /bin
RUN mkdir /mywork
COPY . /mywork
WORKDIR /mywork
ENV TZ=Asia/Jakarta
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN python3 -m pip install -r /mywork/docker_python_requirements.txt
RUN python3 -m pip install luxand flask psutil pydrive lottie cairosvg googletrans==4.0.0-rc1 psutil
ENV TERM=xterm-256color
RUN python3 -m pip install eventlet python-socketio socketio==0.2.1 socketIO-client==0.7.2 pydub rxpy3 pilgram
RUN python3 -m pip install -U setuptools
RUN python3 -m pip install -U openwa pyngrok
#CMD ttyd -p ${PORT} bash session.sh
#CMD python3 main3.py
CMD python3 main3.py
