FROM mysql:8.0-debian
RUN apt-get update && apt-get install -y wget unzip python3 python3-pip
RUN pip3 install pyarrow==13.0.0
RUN pip3 install SQLAlchemy mysql-connector-python 
RUN pip3 install pandas==2.1.0 jupyterlab==4.0.3 matplotlib
RUN pip3 install torch==2.0.1 --index-url https://download.pytorch.org/whl/cpu 
RUN pip3 install tensorboard==2.14.0
CMD ["python3", "-m", "jupyterlab", "--no-browser", "--ip=0.0.0.0", "--port=5440", "--allow-root", "--NotebookApp.token=''"]

