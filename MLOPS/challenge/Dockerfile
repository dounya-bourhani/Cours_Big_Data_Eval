FROM python:3.9-slim

COPY requirements.txt /exo/requirements.txt

WORKDIR /exo 
RUN pip install -r requirements.txt

COPY exo.ipynb exo.ipynb 

CMD ["jupyter","lab","--ip=0.0.0.0","--port=8888","--no-browser","--allow-root"]
