FROM python:3.12

WORKDIR /srv/shortlink
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install pytest pytest-cov pytest-benchmark
COPY api ./api
