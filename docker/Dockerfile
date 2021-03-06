FROM jupyter/scipy-notebook:python-3.8.8

USER root

# For installation of manim

# Install all OS dependencies for fully functional notebook server
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    build-essential \
    curl \
    vim-tiny \
    git \
    inkscape \
    libsm6 \
    libxext-dev \
    libxrender1 \
    lmodern \
    netcat \
    pandoc \
    pdf2svg \
    # ---- nbconvert dependencies ----
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-plain-generic \
    # ----
    tzdata \
    unzip \
    zip \
    nano-tiny \
    ffmpeg \
    gcc \
    libcairo2-dev \
    libffi-dev \
    libpango1.0-dev \
    pkg-config && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# setup a minimal texlive installation for manim
COPY texlive-profile.txt /tmp/
ENV PATH=/usr/local/texlive/bin/x86_64-linux:$PATH
RUN wget -O /tmp/install-tl-unx.tar.gz http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    mkdir /tmp/install-tl && \
    tar -xzf /tmp/install-tl-unx.tar.gz -C /tmp/install-tl --strip-components=1 && \
    /tmp/install-tl/install-tl --profile=/tmp/texlive-profile.txt \
    && tlmgr install \
        amsmath babel-english cbfonts-fd cm-super caption ctex doublestroke dvisvgm environ eurosym everysel \
        fancyvrb float fontspec frcursive fundus-calligra gnu-freefont jknapltx latex-bin \
        mathastext microtype ms oberdiek parskip physics preview ragged2e relsize rsfs \
        setspace standalone tcolorbox tipa ucs upquote qsymbols wasy wasysym xcolor xetex xkeyval adjustbox collectbox titling booktabs enumitem \
    && fix-permissions /usr/local/texlive

COPY nbgrader_config.py /etc/jupyter/
RUN fix-permissions /etc/jupyter/

ENV TZ=Hongkong
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN curl -fsSL https://code-server.dev/install.sh | sh && \
    rm -rf /home/jovyan/.cache/

# Switch back to jovyan
USER ${NB_UID}

COPY fix-nbextensions /usr/local/bin/fix-nbextensions

# Install Python 3 packages
RUN conda install --quiet --yes \
    'hide_code=0.6.*' \
    'ipydrawio=1.1.*' \
    'ipydrawio-export=1.1.*' \
    'jupyter-server-proxy=3.1.*' \
    'jupyter-vscode-proxy=0.1.*' \
    'jupyter-videochat=0.5.*' \
    'jupyterhub=1.4.1' \
    'jupyterlab-system-monitor=0.8.*' \
    'jupyterlab-git=0.30.*' \
    'jupyterlab-tour=3.1.*' \
    'jupytext=1.11.*' \
    'jupyter_nbextensions_configurator=0.4.*' \
    'jupyter_contrib_nbextensions=0.5.*' \
    'nbgitpuller=0.10.*' \
    'rise=5.7.*' \
    'xeus-python==0.12.*' \
    && \
    fix-nbextensions && \
    jupyter nbextension enable code_prettify/code_prettify --sys-prefix && \
    jupyter nbextension enable init_cell/main --sys-prefix && \
    jupyter nbextension enable scratchpad/main --sys-prefix && \
    jupyter nbextension enable spellchecker/main --sys-prefix && \
    jupyter nbextension enable codefolding/main --sys-prefix && \
    jupyter nbextension enable --section edit codefolding/edit --sys-prefix && \
    pip install --quiet --no-cache-dir \
    'manim==0.7.*' \
    'itikz==0.1.*' \
    'jupyter-www-proxy' \
    'mytutor' \
    'git+https://github.com/jupyter/nbgrader.git@refs/pull/1421/head' &&\
    jupyter nbextension install --symlink --sys-prefix --py nbgrader && \
    jupyter nbextension enable --sys-prefix --py nbgrader && \
    jupyter serverextension enable --sys-prefix --py nbgrader  && \   
    jupyter nbextension disable --sys-prefix formgrader/main --section=tree && \
    jupyter nbextension disable --sys-prefix course_list/main --section=tree && \
    jupyter serverextension disable --sys-prefix nbgrader.server_extensions.course_list && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"


WORKDIR "${HOME}"
