AstroImages API (astroimages-api)
=================================

REST API for listing processed images

Usage
-----

Clone the repo:

    git clone https://github.com/AstroImages/astroimages-api/
    cd astroimages-api

Create virtualenv:

    virtualenv -p python3 env
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

## Testing

To run unit tests:

    python -m unittest discover test/unit -v


## References

### General
- https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
- https://medium.com/ki-labs-engineering/designing-well-structured-rest-apis-with-flask-restplus-part-1-7e96f2da8850
- http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
- https://medium.com/free-code-camp/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563

 ### Testing
 - https://realpython.com/python-testing/
 - https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
 - https://pythontesting.net/framework/unittest/unittest-introduction

 ### Github actions
  - https://sourcery.ai/blog/github-actions/

License
-------

MIT, see LICENSE file


