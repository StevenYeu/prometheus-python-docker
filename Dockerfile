FROM python:3.9
WORKDIR /app
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
EXPOSE 8000
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src ./src
WORKDIR /app/src
CMD ["gunicorn", "-b", "0.0.0.0", "app:app"]