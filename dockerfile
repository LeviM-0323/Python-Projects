FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/LeviM-0323/Python-Projects.git || \
    (cd Python-Projects && git pull)

# RUN pip3 install -r requirements.txt
RUN pip3 install streamlit numpy pandas python-dotenv openai plotly matplotlib

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT [ "streamlit", "run", "Python-Projects/StreamlitTests/Streamlit_Tests.py", "--server.port=8501", "--server.address=0.0.0.0" ]