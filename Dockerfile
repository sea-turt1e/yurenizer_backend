# プラットフォームを明示的に指定
FROM --platform=linux/amd64 python:3.11.6 as builder
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y build-essential

RUN pip install --upgrade pip
RUN pip install poetry
COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --output requirements.txt

FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.11 as executor

WORKDIR ${LAMBDA_TASK_ROOT}

RUN yum install -y gcc rust cargo

COPY ./app ${LAMBDA_TASK_ROOT}

COPY --from=builder /usr/src/app/requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["main.handler"]