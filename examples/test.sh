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
nosetests tests
