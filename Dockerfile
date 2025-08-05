FROM python:3.12.1

RUN pip install git+https://github.com/hchiang9/SpoonacularAPI
WORKDIR /OneDrive/Documents/SE2251_Folder/groupproject-team-27
COPY *.py .

CMD python3 app.py