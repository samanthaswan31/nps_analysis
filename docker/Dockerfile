# OpenMS tools image = base
FROM ghcr.io/openms/openms-tools:3.1.0

# Set wd inside container
WORKDIR /work

# Install application dependencies
COPY docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY scripts ./scripts

# Set default command to start shell session when container runs
CMD ["bash"]