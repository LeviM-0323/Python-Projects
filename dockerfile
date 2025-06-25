FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    xvfb \
    x11-utils \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libsm6 \
    libxext6 \
    libxrender-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/LeviM-0323/Python-Projects.git || \
    (cd Python-Projects && git pull)

# RUN pip3 install -r requirements.txt
RUN pip3 install pygame numpy

COPY SnakeAI ./SnakeAI

WORKDIR /app/SnakeAI

CMD ["xvfb-run", "-a", "python", "snake.py"]