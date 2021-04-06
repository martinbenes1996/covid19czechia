
# remove previous releases
rm -rf build/ dist/ covid19czechia.egg-info/ __pycache__/ covid19czechia/data/*.csv
# compile
python setup.py sdist bdist_wheel
# publish
python -m twine upload dist/*