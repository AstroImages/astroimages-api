AstroImages API (astroimages-api)
=================================

REST API for listing processed images

Usage
-----

Clone the repo:

    git clone https://github.com/AstroImages/astroimages-api/
    cd astroimages-api

Create virtualenv:

    virtualenv env
    source env/bin/activate
    pip3 install -r requirements.txt

Run the server via CLI

    ./start-server.sh
    
Or run the docker image

    # build: 
    docker build -t astroimages-api:latest .
    # run silent
    docker run -d -p 5000:5000 astroimages-api
    # run with output
    docker run --rm -ti -p 5000:5000 astroimages-api

Try the endpoints:

    ./tests/start-tests-fits.sh

Swagger docs would be available at `http://localhost:5000/api/spec.html`

## References

- https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

- https://medium.com/ki-labs-engineering/designing-well-structured-rest-apis-with-flask-restplus-part-1-7e96f2da8850


License
-------

MIT, see LICENSE file


