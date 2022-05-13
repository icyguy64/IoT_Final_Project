# reading from s3
import boto3
import json
import pandas as pd    
import time
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Real-Time Dashboard",
    page_icon="✅",
    layout="wide",
)

# dashboard title
st.title("Real-Time Live Dashboard")

# creating a single-element container.
placeholder = st.empty()

with placeholder.container():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('iot-project-ylchua2')

    # Iterates through all the objects, doing the pagination for you. Each obj
    # is an ObjectSummary, so it doesn't contain the body. You'll need to call
    # get to get the whole body.
    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()

        #df = pd.read_json(body.decode("utf-8"))
        df = pd.read_csv('scenario_1.csv')
    
    st.dataframe(df.groupby(['devices']).last())
    
    # The dashboard will update every 60 secs
    time.sleep(60)
