FROM python:3.10-slim

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

COPY utils/ /home/utils/
COPY .streamlit/ /home/.streamlit/
COPY main.py /home/main.py

WORKDIR /home

CMD ["streamlit", "run", "main.py"]