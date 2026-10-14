# LintTwin and the linters it compares, at the versions used in the study.
#   docker build -t linttwin https://github.com/sariddangerpowers/linttwin.git
#   docker run --rm linttwin findings
#   docker run --rm -v "$PWD:/src" linttwin check /src
FROM docker.io/library/node:22-bookworm-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
ENV UV_PYTHON_INSTALL_DIR=/opt/python LINTTWIN_HOME=/opt/linttwin PATH=/opt/venv/bin:$PATH
COPY . /tmp/linttwin
RUN uv venv /opt/venv --python 3.12 \
 && uv pip install --python /opt/venv/bin/python /tmp/linttwin \
 && linttwin setup --pinned \
 && rm -rf /tmp/linttwin /root/.cache /root/.npm
WORKDIR /src
ENTRYPOINT ["linttwin"]
CMD ["--help"]
