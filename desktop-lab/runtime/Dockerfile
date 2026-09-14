FROM debian:bookworm-slim@sha256:88200866dfff7ea7f5cbcb6ec7c8a701889efe6fe859fe64d6990e4b07ea4171
ARG KUBERNETES_VERSION
RUN apt-get update && apt-get install -y --no-install-recommends bash ca-certificates curl jq vim-tiny nano && rm -rf /var/lib/apt/lists/*
RUN curl --http1.1 --retry 3 --retry-all-errors --connect-timeout 20 --max-time 180 -fsSLo /usr/local/bin/kubectl "https://dl.k8s.io/release/${KUBERNETES_VERSION}/bin/linux/arm64/kubectl" \
    && curl --http1.1 --retry 3 --retry-all-errors --connect-timeout 20 --max-time 180 -fsSLo /tmp/kubectl.sha256 "https://dl.k8s.io/release/${KUBERNETES_VERSION}/bin/linux/arm64/kubectl.sha256" \
    && echo "$(cat /tmp/kubectl.sha256)  /usr/local/bin/kubectl" | sha256sum --check \
    && chmod +x /usr/local/bin/kubectl && rm /tmp/kubectl.sha256
ENV TERM=xterm-256color
WORKDIR /workspace
