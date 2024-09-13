FROM python:3.11

WORKDIR /code

COPY src/samdul01food/main.py /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/hamsunwoo/samdul01food.git@0.1.1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
