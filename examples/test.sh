virtualenv --no-site-packages /tmp/v1-robot
source /tmp/v1-robot/bin/activate
cd ..
python setup.py install
cd -
cd robotchef_britishcuisine
python setup.py install
cd ../robotchef_chinesecuisine
python setup.py install
cd ../robotchef_cook
python setup.py install
cd ../robotchef
pip install -r tests/requirements.txt
nosetests tests
status=$?
rm -rf /tmp/v1-robot
exit status
