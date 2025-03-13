FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias (desde tu repositorio)
RUN apt-get update && apt-get install -y \
    xfce4 \
    xfce4-goodies \
    tightvncserver \
    dbus-x11 \
    xfonts-base \
    libgl1-mesa-dri \
    x11-xkb-utils \
    openssh-server \
    wget \
    sudo \
    nano \
    net-tools \
    git \
    python3 \
    python3-pip \
    --no-install-recommends

# Configurar usuario developer (como en tu repo)
RUN useradd -m -s /bin/bash developer \
    && echo "developer:developer" | chpasswd \
    && usermod -aG sudo developer \
    && echo "developer ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Configurar VNC (desde tu repo)
USER developer
RUN mkdir -p /home/developer/.vnc \
    && echo "password" | vncpasswd -f > /home/developer/.vnc/passwd \
    && chmod 600 /home/developer/.vnc/passwd \
    && echo '#!/bin/sh\nunset SESSION_MANAGER\nunset DBUS_SESSION_BUS_ADDRESS\nexec startxfce4' > /home/developer/.vnc/xstartup \
    && chmod +x /home/developer/.vnc/xstartup

# Script de inicio (adaptado para Compose)
USER root
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

CMD ["/startup.sh"]
