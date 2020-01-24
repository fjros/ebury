# Currency Exchange Trades

Client/server web application that books and lists foreign exchange trades.


## Architecture

I could choose a full-featured web framework like *Django* to implement the application. However, I'll go for a more decoupled approach comprised of a standalone *REST API* and a *Single Page Application* (SPA). Rationale:

* I find this approach more appealing from a maintainability viewpoint, allowing to evolve both applications in a more independent way.
* I have way more experience with simpler frameworks only meant to implement REST and Websockets APIs.


## Approach

Since I'm a backend developer, and given the time constraint, I'll focus initially on the REST API to have a working solution asap. This should allow me to have some leeway to determine the way to go for the client app. Then, if time permits, I'll iterate on the backend implementation to improve as many aspects as I can.

From the beginning I'll write working and clean code. It will include integration and/or unit tests, code coverage, and PEP8 style checks (including checks for high cyclomatic complexity). However, I might delay (or even neglect) potential architectural improvements depending on their impact on the problem at hand and, more importantly, on my available time.

REST endpoints will be documented using the Swagger (OpenAPI) format. I'll address validation errors as time permits.


## Backend

REST API implemented using [Falcon](https://falcon.readthedocs.io/en/stable/). If I had more time, I could've used [Flask](https://flask.palletsprojects.com/en/1.1.x/) or [FastAPI](https://fastapi.tiangolo.com) instead. 


## Frontend

To be determined.
