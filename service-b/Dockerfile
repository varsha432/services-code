FROM python:3.12-slim
WORKDIR /app
COPY app.py .
USER 10001
ENV SERVICE_NAME=service-b
ENV PORT=8082
EXPOSE 8082
CMD ["python","app.py"]
