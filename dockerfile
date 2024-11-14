ARG PYTHON_BASE=3.12-slim
# build stage
FROM python:$PYTHON_BASE AS builder

# install PDM
RUN pip install -U pdm
# disable update check
ENV PDM_CHECK_UPDATE=false
# copy files
COPY pyproject.toml pdm.lock README.md /project/

# install dependencies and project into the local packages directory
WORKDIR /project
RUN pdm install --check --prod --no-editable

COPY src/ /project/src

# run stage
FROM python:$PYTHON_BASE

RUN apt-get update && apt-get install -y ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# retrieve packages from build stage
COPY --from=builder /project/.venv/ /project/.venv
ENV PATH="/project/.venv/bin:$PATH"
ENV PATH "/project/scripts:${PATH}"
COPY src /project/src
COPY scripts /procject/scripts


WORKDIR /project
RUN chmod +x scripts/*
ENTRYPOINT ["docker-entrypoint.sh"]
