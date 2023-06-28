import mysql.connector
import pandas as pd
#import psycopg2
import streamlit as st
import PIL
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd

import requests

# connect to the database
import mysql.connector
#establishing the connection
conn = mysql.connector.connect(user='root', password='Karthik29@', host='127.0.0.1', database="youtube")

# create a cursor object
cursor = conn.cursor()
SELECT = option_menu(
    menu_title = None,
    options = ["Home","Query","Contact","About"],
    icons =["bar-chart","house","toggles","at"],
    default_index=2,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}})

if SELECT == "Query":
    st.title("SQL Basic Query")
    st.write("----")
    st.subheader("Let's know some basic query about the data")
    options = ["--select--",
               "1.What are the names of all the videos and their corresponding channels?",
               "2.Which channels have the most number of videos, and how many videos do they have",
               "3.What are the top 10 most viewed videos and their respective channels?",
               "4.How many comments were made on each video, and what are their corresponding video names?",
               "5.Which videos have the highest number of likes, and what are their corresponding channel names?",
               "6.What is the total number of likes and dislikes for each video,and what are their corresponding video names?",
               "7.What is the total number of views for each channel, and what are their corresponding channel names?",
               "8.What are the names of all the channels that have published videos in the year 2022?"
               "9.What is the average duration of all videos in each channel, and what are their corresponding channel names?",
               "10.Which videos have the highest number of comments, and what are their corresponding channel names?"]

    # 1

    select = st.selectbox("Select the option", options)
    if select == "Top 10 states based on year and amount of transaction":
        cursor.execute(
            "SELECT DISTINCT States, Transaction_Year, SUM(Transaction_Amount) AS Total_Transaction_Amount FROM top_tran GROUP BY States, Transaction_Year ORDER BY Total_Transaction_Amount DESC LIMIT 10");

        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Transaction_Year', 'Transaction_Amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states and amount of transaction")
            st.bar_chart(data=df, x="Transaction_Amount", y="States")

# 2

    elif select == "Which channels have the most number of videos, and how many videos do they have":
        cursor.execute(
            "SELECT DISTINCT States, SUM(Transaction_Count) as Total FROM top_tran GROUP BY States ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Total_Transaction'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Which channels have the most number of videos, and how many videos do they have")
            st.bar_chart(data=df, x="Total_Transaction", y="States")
        # 3

    elif select == "What are the top 10 most viewed videos and their respective channels?":
        cursor.execute(
            "SELECT DISTINCT Transaction_Type, SUM(Transaction_Amount) AS Amount FROM agg_user GROUP BY Transaction_Type ORDER BY Amount DESC LIMIT 5");
        df = pd.DataFrame(cursor.fetchall(), columns=['Transaction_Type', 'Transaction_Amount '])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("What are the top 10 most viewed videos and their respective channels?")
            st.bar_chart(data=df, x="Transaction_Type", y="Amount")

            # 4

    elif select == "How many comments were made on each video, and what are their corresponding video names?":
        cursor.execute(
            "SELECT DISTINCT State, District, SUM(RegisteredUsers) AS Users FROM top_user GROUP BY State, District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'District', 'RegisteredUsers'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("How many comments were made on each video, and what are their corresponding video names?")
            st.bar_chart(data=df, x="State", y="RegisteredUsers")

            # 5

    elif select == "Which videos have the highest number of likes, and what are their corresponding channel names?":
        cursor.execute(
            "SELECT DISTINCT States,District,SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States,District ORDER BY Counts DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'District', 'Transaction_Count'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Which videos have the highest number of likes, and what are their corresponding channel names?")
            st.bar_chart(data=df, x="States", y="Transaction_Count")

            # 6

    elif select == "What is the total number of likes and dislikes for each video,and what are their corresponding video names?":
        cursor.execute(
            "SELECT DISTINCT States,Transaction_year,SUM(Transaction_Amount) AS Amount FROM agg_trans GROUP BY States, Transaction_year ORDER BY Amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Transaction_year', 'Transaction_Amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("What is the total number of likes and dislikes for each video,and what are their corresponding video names?")
            st.bar_chart(data=df, x="States", y="Transaction_Amount")

            # 7

    elif select == "What is the total number of views for each channel, and what are their corresponding channel names?":
        cursor.execute(
            "SELECT DISTINCT States, District, SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States,District ORDER BY Counts ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'District', 'Transaction_Count'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("What is the total number of views for each channel, and what are their corresponding channel names?")
            st.bar_chart(data=df, x="States", y="Transaction_Count")

            # 8

    elif select == "What are the names of all the channels that have published videos in the year 2022?":
        cursor.execute(
            "SELECT DISTINCT States,District, SUM(RegisteredUsers) AS Users FROM map_user GROUP BY States,District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'District', 'RegisteredUsers'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("What are the names of all the channels that have published videos in the year 2022?")
            st.bar_chart(data=df, x="States", y="RegisteredUsers")
    #9
    elif select == "What is the average duration of all videos in each channel, and what are their corresponding channel names?":
        cursor.execute(
            "SELECT DISTINCT States,District, SUM(RegisteredUsers) AS Users FROM map_user GROUP BY States,District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'District', 'RegisteredUsers'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("What is the average duration of all videos in each channel, and what are their corresponding channel names?")
            st.bar_chart(data=df, x="States", y="RegisteredUsers")

    #10
    elif select == "Which videos have the highest number of comments, and what are their corresponding channel names?":
        cursor.execute(
            "SELECT DISTINCT States,District, SUM(RegisteredUsers) AS Users FROM map_user GROUP BY States,District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'District', 'RegisteredUsers'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Which videos have the highest number of comments, and what are their corresponding channel names?")
            st.bar_chart(data=df, x="States", y="RegisteredUsers")

# ----------------Home----------------------#
cursor = conn.cursor()
# execute a SELECT statement
cursor.execute("SELECT * FROM channel")


# fetch all rows
rows = cursor.fetchall()
if SELECT == "Home":
    col1,col2, = st.columns(2)
    col1.image(Image.open("D:/program session/project/Youtube_Data/YouTube.png"),width = 250)
    with col1:
        st.subheader("YouTube Data API, you can add a variety of YouTube features to your application. Use the API to upload videos, manage playlists and subscriptions, update channel settings, and more.")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.apkmirror.com/apk/google-inc/youtube/youtube-18-24-37-release/")
    with col2:
        st.video("D:/program session/project/Youtube_Data/history.mp4")

        df = pd.DataFrame(rows,
                          columns=['','channel_id', 'channel_name', 'description', 'views', 'subscriber',
                                   'published_date'])
# ----------------About-----------------------#

if SELECT == "About":
    col1, col2 = st.columns(2)
    with col1:
        st.video("D:/program session/project/Youtube_Data/about.mp4")
    with col2:
        st.image(Image.open("D:/program session/project/Youtube_Data/YouTube.png"), width=500)
        st.write("---")
        st.subheader("YouTube Data API lets you incorporate functions normally executed on the YouTube website into your own website or application."
                     " The lists below identify the different types of resources that you can retrieve using the API. The API also supports methods to insert, update, or delete many of these resources."
                     " This reference guide explains how to use the API to perform all of these operations. The guide is organized by resource type. A resource represents a type of item that comprises part of the YouTube experience, such as a video, a playlist, or a subscription. For each resource type, the guide lists one or more data representations, and resources are represented as JSON objects. "
                     "The guide also lists one or more supported methods (LIST, POST, DELETE, etc.) for each resource type and explains how to use those methods in your application.")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.title("Youtube Api")
        st.write("---")
        st.subheader("Your API key is available in the Developer Console's API Access pane for your project.")
        st.image(Image.open("D:/program session/project/Youtube_Data/api.png"), width=400)
        with open("D:/program session/project/Youtube_Data/youtube-api.pdf", "rb") as f:
            data = f.read()
        st.download_button("DOWNLOAD REPORT", data, file_name="youtube-api.pdf")
    with col2:
        st.image(Image.open("D:/program session/project/Youtube_Data/report.png"), width=800)

# ----------------------Contact---------------#


if SELECT == "Contact":
    name = "Karthik_Tnj"
    mail = (f'{"Mail :"}  {"krtk613001@gmail.com"}')
    description = "An Aspiring DATA-SCIENTIST..!"
    social_media = {
        "Youtube": "https://www.youtube.com/channel/UC5QsHtuaF2WMMdH7JZk3a4A",
        "GITHUB": "https://github.com/Karthiktnj",
        "LINKEDIN": "https://www.linkedin.com/in/karthik-r-39862a1a0/",
        "INSTAGRAM": "https://www.instagram.com/people_call_me_rowdy/",
        "Facebook": "https://www.facebook.com/rk.karthik.393"}

    col1, col2, col3 = st.columns(3)
    col3.image(Image.open("C:/Users/INFOFIX_COMPUTERS/OneDrive/Desktop/Phonepe/photo/my.jpg"), width=230)
    with col2:
        st.title('YouTube Data Harvesting and Warehousing')
        st.write(
            "The following table shows the most common methods that the API supports. Some resources also support other methods that perform functions more specific to those resources. For example, the videos.rate method associates a user rating with a video, and the thumbnails.set method uploads a video thumbnail image to YouTube and associates it with a video.")
        st.write("---")
        st.subheader(mail)
    st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")
