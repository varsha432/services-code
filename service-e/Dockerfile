FROM python:3.12-slim
WORKDIR /app
COPY app.py .
USER 10001
ENV SERVICE_NAME=service-e
ENV PORT=8085
EXPOSE 8085
CMD ["python","app.py"]
