#!/bin/bash
# Matar procesos VNC/SSH previos (desde tu repo)
pkill Xvnc || true
pkill sshd || true
rm -rf /tmp/.X1-lock /tmp/.X11-unix/X1

# Configurar permisos
chown -R developer:developer /home/developer

# Iniciar SSH (como en tu repo)
mkdir -p /run/sshd
/usr/sbin/sshd -D &

# Iniciar VNC (desde tu repo)
su - developer -c "vncserver :1 -geometry 1280x800 -depth 24 -localhost no"

# Mantener contenedor activo
tail -f /dev/null
