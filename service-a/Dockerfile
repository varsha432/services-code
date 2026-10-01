FROM python:3.12-slim

WORKDIR /app

COPY --chown=10001:10001 app.py .

USER 10001

ENV SERVICE_NAME=service-a
ENV PORT=8081

EXPOSE 8081

CMD ["python", "app.py"]