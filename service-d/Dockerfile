FROM python:3.12-slim
WORKDIR /app
COPY app.py .
USER 10001
ENV SERVICE_NAME=service-d
ENV PORT=8084
EXPOSE 8084
CMD ["python","app.py"]
