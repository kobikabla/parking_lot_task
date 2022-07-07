# validate license plat number entering a parking lot

this project is getting pictures of il license plates and determent if a vehicle can enter the parking lot
and writes all the decision to a liteSQL local file.

## how to use

save the license plate images in to the images folder (you can create your owen folder and use it)
in the dataConfig file in the configuration folder insert your -ocr-API key 
run the createSQLDB file to create the DB file and table
and run the main file
e.g -
python "$(pwd)"/main.py


## pytests for testing the project

run tests -  pytest  "$(pwd)"/tests/test.py"