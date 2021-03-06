#!/bin/bash

#create logs folder
mkdir logs

#setup environment
set -e
UBUNTU=false
DEBIAN=false
if [ "$(uname)" = "Linux" ]; then
	#LINUX=1
	if type apt-get; then
		OS_ID=$(lsb_release -is)
		if [ "$OS_ID" = "Debian" ] || [ "$OS_ID" = "Kali" ] || "$OS_ID" = "Mint" ; then
			DEBIAN=true
		else
			UBUNTU=true
		fi
	fi
fi

# Manage npm and other install requirements on an OS specific basis
if [ "$(uname)" = "Linux" ]; then
	#LINUX=1
	if [ "$UBUNTU" = "true" ] && [ "$UBUNTU_PRE_2004" = "1" ]; then
		# Ubuntu
		echo "Installing on Ubuntu pre 20.04 LTS."
		sudo apt-get update
		sudo apt-get install -y python3.7-venv python3.7-distutils
	elif [ "$UBUNTU" = "true" ] && [ "$UBUNTU_PRE_2004" = "0" ] && [ "$UBUNTU_2100" = "0" ]; then
		echo "Installing on Ubuntu 20.04 LTS."
		sudo apt-get update
		sudo apt-get install -y python3.8-venv python3-distutils
	elif [ "$UBUNTU" = "true" ] && [ "$UBUNTU_2100" = "1" ]; then
		echo "Installing on Ubuntu 21.04 or newer."
		sudo apt-get update
		sudo apt-get install -y python3.9-venv python3-distutils
	elif [ "$DEBIAN" = "true" ]; then
		echo "Installing on Debian."
		sudo apt-get update
		sudo apt-get install -y python3-venv
	elif type pacman && [ -f "/etc/arch-release" ]; then
		# Arch Linux
		echo "Installing on Arch Linux."
		sudo pacman -S --needed python git
	elif type yum && [ ! -f "/etc/redhat-release" ] && [ ! -f "/etc/centos-release" ] && [ ! -f "/etc/fedora-release" ]; then
		# AMZN 2
		echo "Installing on Amazon Linux 2."
		sudo yum install -y python3 git
	elif type yum && [ -f "/etc/redhat-release" ] || [ -f "/etc/centos-release" ] || [ -f "/etc/fedora-release" ]; then
		# CentOS or Redhat or Fedora
		echo "Installing on CentOS/Redhat/Fedora."
	fi
elif [ "$(uname)" = "Darwin" ] && ! type brew >/dev/null 2>&1; then
	echo "Installation currently requires brew on MacOS - https://brew.sh/"
elif [ "$(uname)" = "OpenBSD" ]; then
	export MAKE=${MAKE:-gmake}
	export BUILD_VDF_CLIENT=${BUILD_VDF_CLIENT:-N}
elif [ "$(uname)" = "FreeBSD" ]; then
	export MAKE=${MAKE:-gmake}
	export BUILD_VDF_CLIENT=${BUILD_VDF_CLIENT:-N}
fi


find_python() {
	set +e
	unset BEST_VERSION
	for V in 39 3.9 38 3.8 37 3.7 3; do
		if which python$V >/dev/null; then
			if [ "$BEST_VERSION" = "" ]; then
				BEST_VERSION=$V
			fi
		fi
	done
	echo $BEST_VERSION
	set -e
}

if [ "$INSTALL_PYTHON_VERSION" = "" ]; then
	INSTALL_PYTHON_VERSION=$(find_python)
fi

INSTALL_PYTHON_PATH=python${INSTALL_PYTHON_VERSION:-3}

echo "Python version is $INSTALL_PYTHON_VERSION"
$INSTALL_PYTHON_PATH -m venv venv
if [ ! -f "activate" ]; then
	ln -s venv/bin/activate .
fi

. ./activate
# pip 20.x+ supports Linux binary wheels
python -m pip install --upgrade pip
python -m pip install wheel

echo ""
echo "install.sh complete."
echo "For further details on the instalation check the README.md"
echo ""
echo "Type '. ./activate' and then 'python setup.py develop' to begin."