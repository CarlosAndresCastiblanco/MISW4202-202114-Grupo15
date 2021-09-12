#!/bin/bash
function executingNodes() {
    ./monitor/run.sh &    
    ./service/run.sh &
    wait
    
}
executingNodes
