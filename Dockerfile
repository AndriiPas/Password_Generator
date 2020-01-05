FROM python
LABEL maintainer="https://github.com/AndriiPas/Password_Generator"
EXPOSE 8080
COPY . /app
RUN pip install -r /app/requirements.txt
CMD python /app/generator.py