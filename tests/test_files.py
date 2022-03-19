import os

def test_file_exists_databases():
     assert os.path.isfile('src/databases/mongodb.py')

def test_file_exists_mongodb_dml():
     assert os.path.isfile('src/databases/mongodb_dml.py')

def test_file_exists_scoring():
     assert os.path.isfile('src/ml/predictor.py')

def test_file_exists_schemas():
     assert os.path.isfile('src/schemas/schema_request.py')

def test_file_exists_config():
     assert os.path.isfile('src/utils/config.py')

def test_file_exists_model():
     assert os.path.isfile('model/model.pkl')

def test_file_exists_gitignore():
    assert os.path.isfile('.gitignore')

def test_file_exists_requirements():
    assert os.path.isfile('requirements.txt')

def test_file_exists_dockerfile_api():
    assert os.path.isfile('docker/api/Dockerfile')

def test_file_exists_dockerfile_mongo():
    assert os.path.isfile('docker/data_to_mongo/Dockerfile')
    
def test_file_exists_data():
    assert os.path.isfile('data/challenge_data.csv')
