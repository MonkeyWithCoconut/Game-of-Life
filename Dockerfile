FROM python:latest

WORKDIR /Game-of-Life

COPY . .

RUN pip install pyinstaller

RUN pyinstaller --onefile main.py Game_of_life.py

RUN python3 -m pip install pytest
