# Currency Exchange Trades

Client/server web application that books and lists foreign exchange trades.


## Architecture

The web application is comprised of a standalone *REST API* and a *Single Page Application* (SPA).


## Usage

### Running

In order to build and run the application, just run the following commands (substitute `<your-access-key>` for your
actual [Fixer](https://fixer.io/) key).

```
cd ebury/
echo "FIXER_ACCESS_KEY=<your-access-key>" > .api.env 
docker-compose up --build -d
```

This will build and run the two containers of the application. Once it's done, open
[http://localhost:8080/](http://localhost:8080/) in your browser. 

In case you need the web server to listen on a different port, set the env var `EBURY_HOST_PORT` to the appropriate
value. E.g.:

```
EBURY_HOST_PORT=80 docker-compose up --build -d
```

### Tests

The API features the following test suites:

```
make pep8      # check for code style and cyclomatic complexity
make test      # run unit and integration tests
make coverage  # coverage results saved in htmlcov/index.html
make all       # pep8 && coverage
```

You can also run them within the container (but note that this would remove the database content). E.g.:

```
docker exec -ti ebury_api_1 make test
```


## Design

### Back-end

The back-end of the application is a REST API that uses the
[Falcon framework](https://falcon.readthedocs.io/en/stable/). I could've used
[Flask](https://flask.palletsprojects.com/en/1.1.x/) or [FastAPI](https://fastapi.tiangolo.com) instead, but given the
time constraints of the project I chose the framework I'm more familiar with. By the way, I discarded
[Django](https://www.djangoproject.com/) because I find it a too-big dependency for a simple REST API.

The code loosely follows a
[clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html). A simple project
like this one could've been implemented in a more straightforward way. However, I've wanted to show some design
decisions that could help improve the maintainability of the project in the hypothetical case it kept growing.

The `adapter` package contains the interface adapters of the web application. I.e. the endpoint
controllers, network adapters, and persistence implementations that interconnect external entities (e.g. API requests
or databases) with the core of our application.

The business logic of our application lies within the `core` package. I've also included there the
*application services* that implement the use cases of the API. Following the *dependency rule*, the classes of the
core know nothing about the interface adapters. They work based on abstract classes of the core whose implementations
(adapters) are provided via the `binding` package. The latter is kind of a simple and straightforward dependency
injector.

The former guidelines lead to loosely-coupled software components. By following the single-responsibility principle of
object-oriented design, we also achive high cohesion. The resulting software can be more easily maintained and reused.

Regarding re-usability, here you can find an example. If we were to implement a background service that creates trades
after receiving a certain event, it could leverage the corresponding application service like this:

```
# e is the event with the data for the trade
session = session_manager.open()
service = TradeService(session)
try:
  trade = service.create_trade(e.sell_ccy, e.sell_amount, e.buy_ccy, e.buy_amount, e.rate)
finally:
  session_manager.close()
```

I've used the Test-Driven Development (TDD) methodology in this project (test coverage reaches 100%). Most of the tests
are integration tests, but I've written a few unit tests to show the case (however, in a real-world project we'd likely
have more unit tests).

Finally, the REST API follow common practices in terms of HTTP status codes, headers, or error responses. You can paste
the content of file `swagger.json` in any [Swagger editor](https://editor.swagger.io/) to check the details of the API.


### Front-end

I've developed a SPA in [Vue.js](https://vuejs.org/). In addition to the main application component, it consists of:

* A component that shows the trades already booked.
* A component that creates new trades.
* A router that binds paths to components.

This is the first time I use Vue, so I'm sure the code could be improved in lots of ways. 


## Potential improvements

* The API should allocate unique codes for each error type so that clients can disambiguate easily and internationalize
their messages easily. Such codes should be documented in the API spec.

* Build a smaller Docker image of the REST API for the production environment.

* Improve the UX of web front-end.

* Refactor the fron-end code for better maintainability and reusability.


## Additional notes

* In order to help you test the application, the API container runs database migrations as part of the Docker build. In
a real-world project (in which a full-featured database like MySQL or PostgreSQL would be used - instead of SQLite),
that would be part of the deployment pipeline.

* If you're on the Free Plan of Fixer.io, you'll only be able to retrieve the exchange rates of EUR as the base (sell)
currency.
