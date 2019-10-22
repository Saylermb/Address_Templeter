venv/bin/python3 training/checked_to_xml.py
venv/bin/pip install .
venv/bin/parserator train training/dataset.xml address_templeter
venv/bin/pip uninstall -y address-templeter
venv/bin/pip install .
venv/bin/python3 test.py
rm address_templeter/learned_settings_*