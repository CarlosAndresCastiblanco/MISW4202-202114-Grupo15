#!/bin/bash
function runServer() {
    cd monitor/
    rm -r venv
    echo "[####] Creating VENV"
    python3.8 -m venv venv
    sleep 5s
    pwd
    source venv/bin/activate
    echo "[####] INSTALLING REQUIREMENTS"
    #pip install --no-warn-script-location -r requirements.txt
    pip install  -r requirements.txt
    echo "[####] CHECK PIP"
    pip list    
    flask run
}
runServer
