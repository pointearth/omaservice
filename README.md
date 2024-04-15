# omaservice
the restful api to visit Oma AI from mobile


# prepare virtual environment, in the location
python3 -m venv .venv # only for the first running
source .venv/bin/activate
which python # show the env (option)
pip3 install -r requirements.txt

# exit the virutal environment
deactivate

# unit tests
python -m unittest tests/*
or 
python -m unittest tests.test_corpus_processor

# debug
uvicorn app.main:app --host 0.0.0.0 --port 80
uvicorn main:app --reload
# deploy to local docker
docker build -t omacluster.azurecr.io/omaservice:pinecone .
docker run -d -p 8080:80 --name omaservice omacluster.azurecr.io/omaservice:pinecone
docker push omacluster.azurecr.io/omaservice:pinecone