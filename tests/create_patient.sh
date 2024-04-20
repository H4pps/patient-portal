#!/bin/bash

request_payload_path="payloads/create_patients4.json"

payload=$(cat "$request_payload_path")

curl -X POST -H "Content-Type: application/json" -d "$payload" "127.0.0.1:5000/patients"