# Shortest-URL-REST-API

### Technologies

- Python 3.9+
- Poetry
- Fast API
- Uvicorn
- Websockets
- Pytest

### Interactive UI

It is possible to encode an URL not only by the /encode endpoint but with the interactive UI at `http://127.0.0.1:8000`, or `http://localhost:8000` if using the application is running inside a Docker container

### Local Development

1. Clone repository and `cd` into repository directory
2. Check Python version `python -V`. Check recommended Python version in Technologies section
3. [Install Poetry](https://python-poetry.org/docs/#installation) (recommended) or skip this step for an isolated installation of Poetry
4. Create a virtual enviroment `python -m venv venv`
5. Install Poetry inside the virtual enviroment `pip install poetry`. Skip this step if Poetry is already available globally (as explained in step 3)
6. Install dependencies `poetry install`
7. Run the local server `poetry run uvicorn app.main:app --reload` or `uvicorn app.main:app --reload`
8. Swagger UI available at `http://127.0.0.1:8000/docs`

### Automated tests during Local Development

1. Simply execute `pytest` standing on the root folder of the project

### Local Deployment for Windows Users

1. [Install Docker](https://docs.docker.com/desktop/windows/install/) with WSL2 backend
2. Check WSL version installed `wsl -l -v`. The listed version must be 2
3. Execute in Windows Console `docker run hello-world` to check if Docker is working correctly
4. [Install GIT Bash](https://gitforwindows.org/) and execute `bash create_container.sh`, OR...
5. Execute in Windows Console manually the two commands in `create_container.sh`
6. Swagger UI will be available at `http://localhost:8000/docs`

### Local Deployment for Linux/Mac Users

1. [Install Docker](https://www.docker.com/products/docker-desktop)
2. Execute in Terminal `make build` followed by `make run`
3. Swagger UI will be available at `http://localhost:8000/docs`

### Data Schemas

- URL
  - original_url: str
  - shortened_url: str

### API Design

**/encode**

- POST: Encodes a URL to a shortened URL

**/decode**

- POST: Decodes a shortened URL to its original URL

**/**

- GET: Interactive UI for encoding an URL

### Considerations regarding memory usage and time complexity

Storing two dictionaries in memory holding exactly the same information, but with the keys being the queries in the second one, might not be the best approach regarding memory usage.

It will work for small applications but for larger applications I would opt to use a local database, or a distributed one for even larger applications.

Nevertheless, it is the best approach in terms of time complexity, since a dictionary search takes O(n)=1, and for this application I need to search by original_url and by index.
