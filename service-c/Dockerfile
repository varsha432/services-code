FROM python:3.12-slim
WORKDIR /app
COPY app.py .
USER 10001
ENV SERVICE_NAME=service-c
ENV PORT=8083
EXPOSE 8083
CMD ["python","app.py"]
