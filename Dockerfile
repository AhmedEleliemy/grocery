FROM python:3.8.8
RUN mkdir -p /usr/apps/grocery/
WORKDIR /usr/apps/grocery/
COPY . .
RUN pip3 install waitress
RUN pip3 install --no-cache-dir -r /usr/apps/grocery/requirements.txt
CMD ["python3", "run.py"]