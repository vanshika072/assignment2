#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[93]:


pip install Ticker


# In[92]:


pip install yfinance


# In[81]:


import yfinance as yf
import pandas as pd


# In[4]:


tesla=yf.Ticker('TSLA')


# In[6]:


tesla_data=tesla.history(period='max')
tesla_data


# In[69]:


tesla_data.reset_index(inplace=True)
tesla_data.head(5)


# # Question 2

# In[9]:


url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'


# In[96]:


import requests
html_data=requests.get(url).text


# In[11]:


from bs4 import BeautifulSoup


# In[97]:


soup=BeautifulSoup(html_data,'html5lib')


# In[13]:


tesla_revenue=pd.DataFrame(columns=['Date','Revenue'])
tesla_revenue


# In[14]:


for row in soup.find('tbody').find_all('tr'):
    col=row.find_all('td')
    date=col[0].text
    revenue=col[1].text
    tesla_revenue=tesla_revenue.append({'Date':date,'Revenue':revenue},ignore_index=True)
tesla_revenue    


# In[15]:


tesla_revenue['Revenue']=tesla_revenue['Revenue'].str.replace(r'\$|,', '')
tesla_revenue['Revenue']


# In[16]:


tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue


# In[17]:


tesla_revenue.tail(5)


# # Question 3

# In[18]:


gamestock=yf.Ticker('GME')


# In[19]:


gme_data=gamestock.history(period='max')
gme_data


# In[20]:


gme_data.reset_index(inplace=True)


# In[21]:


gme_data.head(5)


# # Question 4

# In[32]:


url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'


# In[33]:


import requests
html_data=requests.get(url).text
html_data


# In[34]:


soup=BeautifulSoup(html_data,'html5lib')
soup


# In[37]:


gme_revenue=pd.DataFrame(columns=['Date','Revenue'])
for row in soup.find('tbody').find_all('tr'):
    col=row.find_all('td')
    date=col[0].text
    revenue=col[1].text
    gme_revenue=gme_revenue.append({'Date':date,'Revenue':revenue},ignore_index=True)
gme_revenue    


# In[38]:


gme_revenue['Revenue']=gme_revenue['Revenue'].str.replace(r'\$|,', '')
gme_revenue['Revenue']


# In[39]:


gme_revenue.tail(5)


# # Question 5

# In[1]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing=0.3)
    
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    fig.update_layout(showlegend=False, height=900, title=stock, xaxis_rangeslider_visible=True)
    fig.show()


tesla_ticker = yf.Ticker("TSLA")
tesla_data = tesla_ticker.history(period="max")
tesla_data.reset_index(inplace=True)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
html_data = response.text
soup = BeautifulSoup(html_data, "html.parser")

tbody = soup.find_all("tbody")[1]
dates = []
revenues = []

for row in tbody.find_all("tr"):
    cols = row.find_all("td")
    date = cols[0].get_text()
    revenue = cols[1].get_text().replace(",", "")  # Remove commas from revenue
    dates.append(date)
    revenues.append(revenue)
    
tesla_revenue = pd.DataFrame({"Date": dates, "Revenue": revenues})
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


make_graph(tesla_data, tesla_revenue, 'Tesla')
    


# # Question 6

# In[2]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing=0.3)
    
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    fig.update_layout(showlegend=False, height=900, title=stock, xaxis_rangeslider_visible=True)
    fig.show()
    
gme_ticker = yf.Ticker("GME")
gme_data = gme_ticker.history(period="max")
gme_data.reset_index(inplace=True)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
response = requests.get(url)
html_data = response.text
soup = BeautifulSoup(html_data, "html.parser")

tbody = soup.find_all("tbody")[1]
dates = []
revenues = []

for row in tbody.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:  # Ensure there are exactly 2 columns in the row
        dates.append(cols[0].text.strip())
        revenues.append(cols[1].text.strip())
    
    gme_revenue = pd.DataFrame({"Date": dates, "Revenue": revenues})
    gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
    gme_revenue.dropna(inplace=True)
    gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

make_graph(gme_data, gme_revenue, 'GameStop')
   

