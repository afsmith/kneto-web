#!/usr/bin/env bash 
apt-get update -y
apt-get install -y sudo build-essential libjpeg-dev python-dev git-core 
apt-get install -y postgresql libpq-dev memcached
apt-get install -y python-setuptools  python-pip
ln -fs /vagrant /opt/kneto-web
pip install virtualenv virtualenvwrapper
echo "export WORKON_HOME=\$HOME/.virtualenvs" >> /etc/skel/.bashrc
echo "export PROJECT_HOME=/opt/cc" >> /etc/skel/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> /etc/skel/.bashrc

echo "export WORKON_HOME=\$HOME/.virtualenvs" >> /home/vagrant/.bashrc
echo "export PROJECT_HOME=/opt/cc" >> /home/vagrant/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.bashrc
 
