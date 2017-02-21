#

#
/usr/lib/python2.7/site-packages/ara
/usr/local/lib/python2.7/dist-packages/ara
$VIRTUAL_ENV/lib/python2.7/site-packages/ara


#
python -c "import os,ara; print(os.path.dirname(ara.__file__))"





# Using ansible.cfg
#------------------------------------------------------------------------------------------------

export ara_location=$(python -c "import os,ara; print(os.path.dirname(ara.__file__))")

cat > ansible.cfg <<EOF
[defaults]
# callback_plugins configuration is required for the ARA callback
callback_plugins = $ara_location/plugins/callbacks

# action_plugins and library configuration is required for the ara_record and ara_read modules
action_plugins = $ara_location/plugins/actions
library = $ara_location/plugins/modules
EOF




# Using environment variables
#------------------------------------------------------------------------------------------------

export ara_location=$(python -c "import os,ara; print(os.path.dirname(ara.__file__))")
export ANSIBLE_CALLBACK_PLUGINS=$ara_location/plugins/callbacks
export ANSIBLE_ACTION_PLUGINS=$ara_location/plugins/actions
export ANSIBLE_LIBRARY=$ara_location/plugins/modules






# ARA
#------------------------------------------------------------------------------------------------

# The order of priority is the following:
-   environment variables
-   ./ansible.cfg                 # In the current working directory
-   ~/.ansible.cfg                # In the home directory
-   /etc/ansible/ansible.cfg



# When using the ansible.cfg file, the configuration options must be set under the ara namespace, as follows:
[ara]
variable = value


























