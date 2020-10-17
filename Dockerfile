FROM python

RUN apt update -y
RUN apt-get install -y graphviz libgraphviz-dev pkg-config
RUN mkdir /usr/bin/src
WORKDIR /usr/bin/src

COPY ./src .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
