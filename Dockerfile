FROM python:3.7-alpine

# Copy all source files to /app.
WORKDIR /app
COPY . ./

# Install Python dependencies.
RUN export PATH="${PATH}:/root/.local/bin" && \
    pip install --user --no-cache-dir pipenv && \
    pipenv install --system && \
    pip uninstall --yes virtualenv virtualenv-clone pipenv

CMD ["python", "-u", "."]
