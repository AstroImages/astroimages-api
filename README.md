# astroimages-api

REST API for listing processed images

## Docker Image
 - Build: docker build -t astroimages-api:latest .
 - Run: 
    -- docker run -d -p 5000:5000 astroimages-api (Silent)
    -- docker run --rm -ti -p 5000:5000 astroimages-api (With output)
 - Test: ./tests/start-tests-fits.sh


## References

- https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

- https://medium.com/ki-labs-engineering/designing-well-structured-rest-apis-with-flask-restplus-part-1-7e96f2da8850
