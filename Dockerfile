FROM python:2

RUN mkdir xblock_development/

COPY requirements.txt xblock_development/

WORKDIR /xblock_development/

RUN pip install -r requirements.txt

ADD . /xblock_development/

RUN apt-get update; apt-get install -y git

RUN git clone https://github.com/edx/xblock-sdk.git

RUN pip install -e .

RUN mkdir ./var; touch ./var/workbench.logcd

RUN python xblock-sdk/manage.py migrate
