# URL Shortener #

This django-react app shortens URLs.

To install and run this app, you need to have the following:

- Docker
- Python
- Node

To install: clone the repo, navigate to its root folder. 

The first time you run this app, use the following command in command line to build the services: 

`docker compose build`

Subsequently, use `docker compose up` to run the app. There may be some errors the first time you run it. If url_shortener-django-1 exits, use Ctrl+C to quit the server and once the containers have stopped, run `docker compose up` again until you see the message 
```Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.```

The app will be accessible through a browser at `localhost:8000`. The redirect root URLs will also be through localhost:8000.

### Developer Notes ###

This was the first app I've built in a while, and the first time I've worked with Django and React in almost two years. I needed a quick refresher in all the technologies involved. It took some time, but it also reminded me how much I missed full stack engineering.

In the interest of time, and because I'm not yet familiar with testing in python, I chose not to write any unit tests in `tests.py`, opting to test end-to-end while developing the app. Since the implementation for this app (one model, one post request) is pretty straightforward, and only the MVP was required, I didn't think I lost much by not writing unit tests.

This was my first time ever dockerizing an application. It might be a little rough around the edges (I'm not entirely sure if Python and Node are still required to run this app, or if Docker automatically uses an official image to run any python/npm commands), and it definitely took some debugging, but I'm glad with the end result and it gave me a much better idea about how docker works.