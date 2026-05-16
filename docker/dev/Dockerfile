FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

ARG USER=dev
ARG UID=1000
ARG GID=1000

RUN apt-get update && \
    apt-get install -y sudo  && \
    groupadd -g ${GID} ${USER} && \
    useradd -m -u ${UID} -g ${GID} -s /bin/bash ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# uvのキャッシュディレクトリの権限設定
RUN mkdir -p /home/${USER}/.cache/uv && \
    chown -R ${USER}:${USER} /home/${USER}/.cache/uv

USER ${USER}
WORKDIR /home/${USER}/python_ws
WORKDIR /home/${USER}

# エントリーポイントの準備
COPY scripts/entrypoint.sh /home/${USER}/entrypoint.sh
RUN sudo chmod +x /home/${USER}/entrypoint.sh && \
    sudo chown ${USER}:${USER} /home/${USER}/entrypoint.sh

ENV UV_CACHE_DIR=/home/${USER}/.cache/uv

ENTRYPOINT ["/home/dev/entrypoint.sh"]
