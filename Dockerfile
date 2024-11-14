FROM python:3.12-alphine
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080
ENV HOST=0.0.0.0
EXPOSE 8080

CMD ["python","app.py"]