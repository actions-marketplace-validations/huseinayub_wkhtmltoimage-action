FROM surnet/alpine-python-wkhtmltopdf:3.9.5-0.12.6-full

COPY . /

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "screenshotter.py"]
