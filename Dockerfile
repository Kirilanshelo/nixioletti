FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ARG VERSION=dockerbuild
ENV VERSION ${VERSION}
ENV PYTHONUNBUFFERED 1

# add python deps here
RUN pip install coloredlogs==15.0.1
RUN pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117

WORKDIR /app
COPY app/ /app

# custom code
# COPY src/mylib/ /app/mylib/
