

# https://dmsimard.com/2016/05/21/ara-an-idea-to-store-browse-and-troubleshoot-ansible-playbook-runs/

# http://ara.readthedocs.io/en/latest/






# Required dependencies
apt-get -y install gcc python-dev libffi-dev libssl-dev


# Development or integration testing dependencies
apt-get -y install python-pip libxml2-dev libxslt1-dev
pip install tox



# Installing ARA from trunk source
pip install git+https://git.openstack.org/openstack/ara
  
# Installing ARA from latest release on PyPi
pip install ara








































