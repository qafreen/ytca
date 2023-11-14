# How to setup

- Clone this repo
- Make it a python virtual environment by running in the directory the repo was cloned
```console
python -m venv ytca
```
- Activate the virtual environment by running 
```console
.\Scripts\activate
```
- Create file named .env 
- Add YouTube developer key in the .env file as
DEVELOPER_KEY = "your_api_key"
- Run 
```console 
pip install -r requirements.txt
```
- Fire up the API by running 
```console
uvicorn ytc:app --reload
```
