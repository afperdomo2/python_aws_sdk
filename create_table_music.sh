aws dynamodb create-table --table-name 'Music' \
  --attribute-definitions \
    'AttributeName=Artist,AttributeType=S' \
    'AttributeName=SongTitle,AttributeType=S' \
     'AttributeName=AlbumTitle,AttributeType=S' \
  --key-schema \
    'AttributeName=Artist,KeyType=HASH' \
    'AttributeName=SongTitle,KeyType=RANGE' \
  --provisioned-throughput \
     'ReadCapacityUnits=10,WriteCapacityUnits=5' \
  --local-secondary-indexes \
        "[{\"IndexName\": \"AlbumTitleIndex\", \"KeySchema\": [{\"AttributeName\": \"Artist\", \"KeyType\": \"HASH\"}, {\"AttributeName\": \"AlbumTitle\", \"KeyType\": \"RANGE\"}], \"Projection\": {\"ProjectionType\":\"INCLUDE\",\"NonKeyAttributes\":[\"Gender\",\"Year\"]}}]"