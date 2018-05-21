import boto3
import json
import time
import datetime
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

dOM = datetime.datetime.today().day

table = dynamodb.Table('onCallMay2018')

print("The current On-Call Engineers are:")

response = table.query(
    KeyConditionExpression=Key('dayOfMonth').eq(dOM),
)

# print(response)

def lambda_handler(event, context):
    for i in response['Items']:
        		#print("Tier 3:", i['tier3'],'\n', "Tier 4:", i['tier4'])
        		return("Tier 3:", i['tier3']," - " "Tier 4:", i['tier4']," - " "After 6pm EST: Nate")
    		    # FIX THIS onCall = ("Tier 3:", i['tier3'], "Tier 4:", i['tier4'])
# print(onCall)
