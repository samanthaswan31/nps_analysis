# Use Miniconda as a base image
FROM continuumio/miniconda3:latest

# Set working directory inside the container
WORKDIR /nps_analysis

# Copy repository into the container
COPY . /nps_analysis

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libboost-all-dev \
    libxerces-c-dev \
    libz-dev \
    libbz2-dev \
    libhdf5-dev \
    libpng-dev \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Conda environment from environment.yml (without pyOpenMS)
RUN conda update -n base -c defaults conda && \
    conda env create -f envs/nps_base.yml && \
    conda clean --all -y

# Set shell to activate Conda environment
SHELL ["conda", "run", "-n", "nps_base", "/bin/bash", "-c"]

# Set PATH to include Conda environment binaries
ENV PATH="/opt/conda/envs/nps_base/bin:$PATH"

# Default command to keep the container running and interactive
CMD ["/bin/bash"]