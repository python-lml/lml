virtualenv --no-site-packages /tmp/v2-robot
source /tmp/v2-robot/bin/activate
cd ../../
python setup.py install
cd -
cd robotchef_api
python setup.py install
cd ../robotchef_britishcuisine
python setup.py install
cd ../
cd robotchef_v2
pip install -r tests/requirements.txt
nosetests tests
status=$?
rm -rf /tmp/v2-robot
exit status
