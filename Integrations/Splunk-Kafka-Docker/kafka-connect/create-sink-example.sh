export TOKEN="955f31f8-5009-474e-ac0d-0c1f494458b6"

curl http://localhost:8088/services/collector/event -H "Authorization: Splunk $TOKEN" -d '{"event": { "stuff": "value" } }'

curl http://localhost:8088/services/collector/event -H "Authorization: Splunk $TOKEN" -d '{"event": "Hello World!!"}'

# curl http://localhost:8083/connectors/ -X POST -H "Content-Type: application/json" -d '{
#     "name": "kafka-connect-splunk",
#     "config": {
#         "connector.class": "com.splunk.kafka.connect.SplunkSinkConnector",
#         "tasks.max": "3",
#         "splunk.indexes": "splunk_kafka_index",
#         "topics": "splunk_kafka_topic",
#       "splunk.hec.uri": "http://localhost:8088",
#       "splunk.hec.token": "$TOKEN"
#     }
# }'

