#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork865-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 
# <h1 align=center><font size = 5>Assignment: SQL Notebook for Peer Assignment</font></h1>
# 
# Estimated time needed: **60** minutes.
# 
# ## Introduction
# Using this Python notebook you will:
# 
# 1.  Understand the Spacex DataSet
# 2.  Load the dataset  into the corresponding table in a Db2 database
# 3.  Execute SQL queries to answer assignment questions 
# 

# ## Overview of the DataSet
# 
# SpaceX has gained worldwide attention for a series of historic milestones. 
# 
# It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010.
# SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage. 
# 
# 
# Therefore if we can determine if the first stage will land, we can determine the cost of a launch. 
# 
# This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.
# 
# This dataset includes a record for each payload carried during a SpaceX mission into outer space.
# 

# ### Download the datasets
# 
# This assignment requires you to load the spacex dataset.
# 
# In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the link below to download and save the dataset (.CSV file):
# 
#  <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv" target="_blank">Spacex DataSet</a>
# 
# 

# In[2]:


get_ipython().system('pip install sqlalchemy==1.3.9')
# These libraries are pre-installed in SN Labs. If running in another environment please uncomment lines below to install them:
get_ipython().system('pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3')
#Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
get_ipython().system('pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24')
get_ipython().system('pip install ipython-sql')


# ### Connect to the database
# 
# Let us first load the SQL extension and establish a connection with the database
# 

# In[3]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[12]:


import csv, sqlite3

con = sqlite3.connect("my_data1.db")
cur = con.cursor()


# In[13]:


get_ipython().system('pip install -q pandas==1.1.5')


# In[14]:


get_ipython().run_line_magic('sql', 'sqlite:///my_data1.db')


# In[18]:


get_ipython().run_line_magic('sql', 'ibm_db_sa://szs06487:Lc6YHVA7zeTqJMX8@764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:32536/szs06487:Lc6YHVA7zeTqJMX8@764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:32536/bludb?authSource=admin&replicaSet=replset?security=SSL')


# In[19]:


import pandas as pd
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv")
df.to_sql("SPACEXTBL", con, if_exists='replace', index=False,method="multi")


# In[61]:


get_ipython().run_cell_magic('sql', '', "CREATE TABLE spacex(\n   Date             DATE  NOT NULL PRIMARY KEY\n  ,Time_UTC         VARCHAR(8) NOT NULL\n  ,Booster_Version  VARCHAR(14) NOT NULL\n  ,Launch_Site      VARCHAR(12) NOT NULL\n  ,Payload          VARCHAR(61) NOT NULL\n  ,PAYLOAD_MASS_KG_ INTEGER  NOT NULL\n  ,Orbit            VARCHAR(11) NOT NULL\n  ,Customer         VARCHAR(57) NOT NULL\n  ,Mission_Outcome  VARCHAR(32) NOT NULL\n  ,Landing_Outcome  VARCHAR(22) NOT NULL\n);\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2010-06-04','18:45:00','F9 v1.0  B0003','CCAFS LC-40','Dragon Spacecraft Qualification Unit',0,'LEO','SpaceX','Success','Failure (parachute)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2010-12-08','15:43:00','F9 v1.0  B0004','CCAFS LC-40','Dragon demo flight C1, two CubeSats, barrel of Brouere cheese',0,'LEO (ISS)','NASA (COTS) NRO','Success','Failure (parachute)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2012-05-22','7:44:00','F9 v1.0  B0005','CCAFS LC-40','Dragon demo flight C2',525,'LEO (ISS)','NASA (COTS)','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2012-10-08','0:35:00','F9 v1.0  B0006','CCAFS LC-40','SpaceX CRS-1',500,'LEO (ISS)','NASA (CRS)','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2013-03-01','15:10:00','F9 v1.0  B0007','CCAFS LC-40','SpaceX CRS-2',677,'LEO (ISS)','NASA (CRS)','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2013-09-29','16:00:00','F9 v1.1  B1003','VAFB SLC-4E','CASSIOPE',500,'Polar LEO','MDA','Success','Uncontrolled (ocean)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2013-12-03','22:41:00','F9 v1.1','CCAFS LC-40','SES-8',3170,'GTO','SES','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2014-01-06','22:06:00','F9 v1.1','CCAFS LC-40','Thaicom 6',3325,'GTO','Thaicom','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2014-04-18','19:25:00','F9 v1.1','CCAFS LC-40','SpaceX CRS-3',2296,'LEO (ISS)','NASA (CRS)','Success','Controlled (ocean)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2014-07-14','15:15:00','F9 v1.1','CCAFS LC-40','OG2 Mission 1  6 Orbcomm-OG2 satellites',1316,'LEO','Orbcomm','Success','Controlled (ocean)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2014-08-05','8:00:00','F9 v1.1','CCAFS LC-40','AsiaSat 8',4535,'GTO','AsiaSat','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2014-09-07','5:00:00','F9 v1.1 B1011','CCAFS LC-40','AsiaSat 6',4428,'GTO','AsiaSat','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2014-09-21','5:52:00','F9 v1.1 B1010','CCAFS LC-40','SpaceX CRS-4',2216,'LEO (ISS)','NASA (CRS)','Success','Uncontrolled (ocean)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2015-01-10','9:47:00','F9 v1.1 B1012','CCAFS LC-40','SpaceX CRS-5',2395,'LEO (ISS)','NASA (CRS)','Success','Failure (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2015-02-11','23:03:00','F9 v1.1 B1013','CCAFS LC-40','DSCOVR',570,'HEO','U.S. Air Force NASA NOAA','Success','Controlled (ocean)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2015-03-02','3:50:00','F9 v1.1 B1014','CCAFS LC-40','ABS-3A Eutelsat 115 West B',4159,'GTO','ABS Eutelsat','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2015-04-14','20:10:00','F9 v1.1 B1015','CCAFS LC-40','SpaceX CRS-6',1898,'LEO (ISS)','NASA (CRS)','Success','Failure (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2015-04-27','23:03:00','F9 v1.1 B1016','CCAFS LC-40','Turkmen 52 / MonacoSAT',4707,'GTO','Turkmenistan National Space Agency','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2015-06-28','14:21:00','F9 v1.1 B1018','CCAFS LC-40','SpaceX CRS-7',1952,'LEO (ISS)','NASA (CRS)','Failure (in flight)','Precluded (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2015-12-22','1:29:00','F9 FT B1019','CCAFS LC-40','OG2 Mission 2  11 Orbcomm-OG2 satellites',2034,'LEO','Orbcomm','Success','Success (ground pad)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2016-01-17','18:42:00','F9 v1.1 B1017','VAFB SLC-4E','Jason-3',553,'LEO','NASA (LSP) NOAA CNES','Success','Failure (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2016-03-04','23:35:00','F9 FT B1020','CCAFS LC-40','SES-9',5271,'GTO','SES','Success','Failure (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2016-04-08','20:43:00','F9 FT B1021.1','CCAFS LC-40','SpaceX CRS-8',3136,'LEO (ISS)','NASA (CRS)','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2016-05-06','5:21:00','F9 FT B1022','CCAFS LC-40','JCSAT-14',4696,'GTO','SKY Perfect JSAT Group','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2016-05-27','21:39:00','F9 FT B1023.1','CCAFS LC-40','Thaicom 8',3100,'GTO','Thaicom','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2016-06-15','14:29:00','F9 FT B1024','CCAFS LC-40','ABS-2A Eutelsat 117 West B',3600,'GTO','ABS Eutelsat','Success','Failure (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2016-07-18','4:45:00','F9 FT B1025.1','CCAFS LC-40','SpaceX CRS-9',2257,'LEO (ISS)','NASA (CRS)','Success','Success (ground pad)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2016-08-14','5:26:00','F9 FT B1026','CCAFS LC-40','JCSAT-16',4600,'GTO','SKY Perfect JSAT Group','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-01-14','17:54:00','F9 FT B1029.1','VAFB SLC-4E','Iridium NEXT 1',9600,'Polar LEO','Iridium Communications','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-02-19','14:39:00','F9 FT B1031.1','KSC LC-39A','SpaceX CRS-10',2490,'LEO (ISS)','NASA (CRS)','Success','Success (ground pad)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-03-16','6:00:00','F9 FT B1030','KSC LC-39A','EchoStar 23',5600,'GTO','EchoStar','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-03-30','22:27:00','F9 FT  B1021.2','KSC LC-39A','SES-10',5300,'GTO','SES','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-05-01','11:15:00','F9 FT B1032.1','KSC LC-39A','NROL-76',5300,'LEO','NRO','Success','Success (ground pad)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-05-15','23:21:00','F9 FT B1034','KSC LC-39A','Inmarsat-5 F4',6070,'GTO','Inmarsat','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-06-03','21:07:00','F9 FT B1035.1','KSC LC-39A','SpaceX CRS-11',2708,'LEO (ISS)','NASA (CRS)','Success','Success (ground pad)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-06-23','19:10:00','F9 FT  B1029.2','KSC LC-39A','BulgariaSat-1',3669,'GTO','Bulsatcom','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-06-25','20:25:00','F9 FT B1036.1','VAFB SLC-4E','Iridium NEXT 2',9600,'LEO','Iridium Communications','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-07-05','23:38:00','F9 FT B1037','KSC LC-39A','Intelsat 35e',6761,'GTO','Intelsat','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-08-14','16:31:00','F9 B4 B1039.1','KSC LC-39A','SpaceX CRS-12',3310,'LEO (ISS)','NASA (CRS)','Success','Success (ground pad)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-08-24','18:51:00','F9 FT B1038.1','VAFB SLC-4E','Formosat-5',475,'SSO','NSPO','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-09-07','14:00:00','F9 B4 B1040.1','KSC LC-39A','Boeing X-37B OTV-5',4990,'LEO','U.S. Air Force','Success','Success (ground pad)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-10-09','12:37:00','F9 B4 B1041.1','VAFB SLC-4E','Iridium NEXT 3',9600,'Polar LEO','Iridium Communications','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-10-11','22:53:00','F9 FT  B1031.2','KSC LC-39A','SES-11 / EchoStar 105',5200,'GTO','SES EchoStar','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-10-30','19:34:00','F9 B4 B1042.1','KSC LC-39A','Koreasat 5A',3500,'GTO','KT Corporation','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-12-15','15:36:00','F9 FT  B1035.2','CCAFS SLC-40','SpaceX CRS-13',2205,'LEO (ISS)','NASA (CRS)','Success','Success (ground pad)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2017-12-23','1:27:00','F9 FT  B1036.2','VAFB SLC-4E','Iridium NEXT 4',9600,'Polar LEO','Iridium Communications','Success','Controlled (ocean)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-01-08','1:00:00','F9 B4 B1043.1','CCAFS SLC-40','Zuma',5000,'LEO','Northrop Grumman','Success (payload status unclear)','Success (ground pad)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-01-31','21:25:00','F9 FT  B1032.2','CCAFS SLC-40','GovSat-1 / SES-16',4230,'GTO','SES','Success','Controlled (ocean)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-02-22','14:17:00','F9 FT  B1038.2','VAFB SLC-4E','Paz  Tintin A & B',2150,'SSO','Hisdesat exactEarth SpaceX','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-03-06','5:33:00','F9 B4 B1044','CCAFS SLC-40','Hispasat 30W-6  PODSat',6092,'GTO','Hispasat  NovaWurks','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-03-30','14:14:00','F9 B4  B1041.2','VAFB SLC-4E','Iridium NEXT 5',9600,'Polar LEO','Iridium Communications','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-04-02','20:30:00','F9 B4  B1039.2','CCAFS SLC-40','SpaceX CRS-14',2647,'LEO (ISS)','NASA (CRS)','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-04-18','22:51:00','F9 B4 B1045.1','CCAFS SLC-40','Transiting Exoplanet Survey Satellite (TESS)',362,'HEO','NASA (LSP)','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-05-11','20:14:00','F9 B5  B1046.1','KSC LC-39A','Bangabandhu-1',3600,'GTO','Thales-Alenia/BTRC','Success','Success (drone ship)');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-05-22','19:47:58','F9 B4  B1043.2','VAFB SLC-4E','Iridium NEXT 6   GRACE-FO 1, 2',6460,'Polar LEO','Iridium Communications GFZ ‚ NASA','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-06-04','4:45:00','F9 B4  B1040.2','CCAFS SLC-40','SES-12',5384,'GTO','SES','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-06-29','9:42:00','F9 B4 B1045.2','CCAFS SLC-40','SpaceX CRS-15',2697,'LEO (ISS)','NASA (CRS)','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-07-22','5:50:00','F9 B5B1047.1','CCAFS SLC-40','Telstar 19V',7075,'GTO','Telesat','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-07-25','11:39:00','F9 B5B1048.1','VAFB SLC-4E','Iridium NEXT-7',9600,'Polar LEO','Iridium Communications','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-08-07','5:18:00','F9 B5 B1046.2','CCAFS SLC-40','Merah Putih',5800,'GTO','Telkom Indonesia','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-09-10','4:45:00','F9 B5B1049.1','CCAFS SLC-40','Telstar 18V / Apstar-5C',7060,'GTO','Telesat','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-10-08','2:22:00','F9 B5 B1048.2','VAFB SLC-4E','SAOCOM 1A',3000,'SSO','CONAE','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-11-15','20:46:00','F9 B5 B1047.2','KSC LC-39A','Es hail 2',5300,'GTO','Es hailSat','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-12-03','18:34:05','F9 B5 B1046.3','VAFB SLC-4E','SSO-A',4000,'SSO','Spaceflight Industries','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-12-05','18:16:00','F9 B5B1050','CCAFS SLC-40','SpaceX CRS-16',2500,'LEO (ISS)','NASA (CRS)','Success','Failure');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2018-12-23','13:51:00','F9 B5B1054','CCAFS SLC-40','GPS III-01',4400,'MEO','USAF','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-01-11','15:31:00','F9 B5 B1049.2','VAFB SLC-4E','Iridium NEXT-8',9600,'Polar LEO','Iridium Communications','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-02-22','1:45:00','F9 B5 B1048.3','CCAFS SLC-40','Nusantara Satu, Beresheet Moon lander, S5',4850,'GTO','PSN, SpaceIL / IAI','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-03-02','7:49:00','F9 B5B1051.1','KSC LC-39A','Crew Dragon Demo-1, SpaceX CRS-17',12055,'LEO (ISS)','NASA (CCD)','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-05-04','6:48:00','F9 B5B1056.1','CCAFS SLC-40','SpaceX CRS-17, Starlink v0.9',2495,'LEO (ISS)','NASA (CRS)','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-05-24','2:30:00','F9 B5 B1049.3','CCAFS SLC-40','Starlink v0.9, RADARSAT Constellation',13620,'LEO','SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-06-12','14:17:00','F9 B5 B1051.2','VAFB SLC-4E','RADARSAT Constellation, SpaceX CRS-18',4200,'SSO','Canadian Space Agency (CSA)','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-07-25','22:01:00','F9 B5 B1056.2','CCAFS SLC-40','SpaceX CRS-18, AMOS-17',2268,'LEO (ISS)','NASA (CRS)','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-08-06','23:23:00','F9 B5 B1047.3','CCAFS SLC-40','AMOS-17, Starlink 1 v1.0',6500,'GTO','Spacecom','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-11-11','14:56:00','F9 B5 B1048.4','CCAFS SLC-40','Starlink 1 v1.0, SpaceX CRS-19',15600,'LEO','SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-12-05','17:29:00','F9 B5B1059.1','CCAFS SLC-40','SpaceX CRS-19, JCSat-18 / Kacific 1',2617,'LEO (ISS)','NASA (CRS), Kacific 1','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2019-12-17','0:10:00','F9 B5 B1056.3','CCAFS SLC-40','JCSat-18 / Kacific 1, Starlink 2 v1.0',6956,'GTO','Sky Perfect JSAT, Kacific 1','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-01-07','2:33:00','F9 B5 B1049.4','CCAFS SLC-40','Starlink 2 v1.0, Crew Dragon in-flight abort test',15600,'LEO','SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-01-19','15:30:00','F9 B5 B1046.4','KSC LC-39A','Crew Dragon in-flight abort test, Starlink 3 v1.0',12050,'Sub-orbital','NASA (CTS)','Success','No attempt');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-01-29','14:07:00','F9 B5 B1051.3','CCAFS SLC-40','Starlink 3 v1.0, Starlink 4 v1.0',15600,'LEO','SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-02-17','15:05:00','F9 B5 B1056.4','CCAFS SLC-40','Starlink 4 v1.0, SpaceX CRS-20',15600,'LEO','SpaceX','Success','Failure');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-03-07','4:50:00','F9 B5 B1059.2','CCAFS SLC-40','SpaceX CRS-20, Starlink 5 v1.0',1977,'LEO (ISS)','NASA (CRS)','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-03-18','12:16:00','F9 B5 B1048.5','KSC LC-39A','Starlink 5 v1.0, Starlink 6 v1.0',15600,'LEO','SpaceX','Success','Failure');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-04-22','19:30:00','F9 B5 B1051.4','KSC LC-39A','Starlink 6 v1.0, Crew Dragon Demo-2',15600,'LEO','SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-05-30','19:22:00','F9 B5B1058.1','KSC LC-39A','Crew Dragon Demo-2, Starlink 7 v1.0',12530,'LEO (ISS)','NASA (CCDev)','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-06-04','1:25:00','F9 B5 B1049.5','CCAFS SLC-40','Starlink 7 v1.0, Starlink 8 v1.0',15600,'LEO','SpaceX, Planet Labs','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-06-13','9:21:00','F9 B5 B1059.3','CCAFS SLC-40','Starlink 8 v1.0, SkySats-16, -17, -18, GPS III-03',15410,'LEO','SpaceX, Planet Labs','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-06-30','20:10:46','F9 B5B1060.1','CCAFS SLC-40','GPS III-03, ANASIS-II',4311,'MEO','U.S. Space Force','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-07-20','21:30:00','F9 B5 B1058.2','CCAFS SLC-40','ANASIS-II, Starlink 9 v1.0',5500,'GTO','Republic of Korea Army, Spaceflight Industries (BlackSky)','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-08-07','5:12:00','F9 B5 B1051.5','KSC LC-39A','Starlink 9 v1.0, SXRS-1, Starlink 10 v1.0',14932,'LEO','SpaceX, Spaceflight Industries (BlackSky), Planet Labs','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-08-18','14:31:00','F9 B5 B1049.6','CCAFS SLC-40','Starlink 10 v1.0, SkySat-19, -20, -21, SAOCOM 1B',15440,'LEO','SpaceX, Planet Labs, PlanetIQ','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-08-30','23:18:00','F9 B5 B1059.4','CCAFS SLC-40','SAOCOM 1B, GNOMES 1, Tyvak-0172',3130,'SSO','CONAE, PlanetIQ, SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-09-03','12:46:14','F9 B5 B1060.2','KSC LC-39A','Starlink 11 v1.0, Starlink 12 v1.0',15600,'LEO','SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-10-06','11:29:34','F9 B5 B1058.3','KSC LC-39A','Starlink 12 v1.0, Starlink 13 v1.0',15600,'LEO','SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-10-18','12:25:57','F9 B5 B1051.6','KSC LC-39A','Starlink 13 v1.0, Starlink 14 v1.0',15600,'LEO','SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-10-24','15:31:34','F9 B5 B1060.3','CCAFS SLC-40','Starlink 14 v1.0, GPS III-04',15600,'LEO','SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-11-05','23:24:23','F9 B5B1062.1','CCAFS SLC-40','GPS III-04 , Crew-1',4311,'MEO','USSF','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-11-16','0:27:00','F9 B5B1061.1','KSC LC-39A','Crew-1, Sentinel-6 Michael Freilich',12500,'LEO (ISS)','NASA (CCP)','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-11-21','17:17:08','F9 B5B1063.1','VAFB SLC-4E','Sentinel-6 Michael Freilich, Starlink 15 v1.0',1192,'LEO','NASA / NOAA / ESA / EUMETSAT','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-11-25','2:13:00','F9 B5 B1049.7','CCAFS SLC-40','Starlink 15 v1.0, SpaceX CRS-21',15600,'LEO','SpaceX','Success','Success');\nINSERT INTO spacex(Date,Time_UTC,Booster_Version,Launch_Site,Payload,PAYLOAD_MASS_KG_,Orbit,Customer,Mission_Outcome,Landing_Outcome) VALUES ('2020-12-06','16:17:08','F9 B5 B1058.4','KSC LC-39A','SpaceX CRS-21',2972,'LEO (ISS)','NASA (CRS)','Success','Success');")


# ## Tasks
# 
# Now write and execute SQL queries to solve the assignment tasks.
# 
# **Note: If the column names are in mixed case enclose it in double quotes
#    For Example "Landing_Outcome"**
# 
# ### Task 1
# 
# 
# 
# 
# ##### Display the names of the unique launch sites  in the space mission
# 

# In[80]:


get_ipython().run_line_magic('sql', 'Select Distinct(Launch_site) from SPACEX')


# 
# ### Task 2
# 
# 
# #####  Display 5 records where launch sites begin with the string 'CCA' 
# 

# In[64]:


get_ipython().run_line_magic('sql', "Select * from SPACEX where Launch_site like 'CCA%' limit 5")


# ### Task 3
# 
# 
# 
# 
# ##### Display the total payload mass carried by boosters launched by NASA (CRS)
# 

# In[66]:


get_ipython().run_line_magic('sql', "Select sum(PAYLOAD_MASS_KG_) from SPACEX where customer like 'NASA (CRS)'")


# ### Task 4
# 
# 
# 
# 
# ##### Display average payload mass carried by booster version F9 v1.1
# 

# In[67]:


get_ipython().run_line_magic('sql', "Select avg(PAYLOAD_MASS_KG_) from SPACEX where booster_version like 'F9 v1.1'")


# ### Task 5
# 
# ##### List the date when the first succesful landing outcome in ground pad was acheived.
# 
# 
# _Hint:Use min function_ 
# 

# In[68]:


get_ipython().run_line_magic('sql', "Select min(Date) from SPACEX where Landing_Outcome like 'Success (ground pad)'")


# ### Task 6
# 
# ##### List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000
# 

# In[82]:


get_ipython().run_line_magic('sql', "Select Distinct(BOOSTER_VERSION) from SPACEX where Landing_Outcome like 'Success (drone ship)' and PAYLOAD_MASS_KG_ between 4000 and 6000")


# ### Task 7
# 
# 
# 
# 
# ##### List the total number of successful and failure mission outcomes
# 

# In[83]:


get_ipython().run_line_magic('sql', 'Select Distinct(Mission_Outcome) , count(Mission_Outcome) from Spacex Group By Mission_Outcome')


# ### Task 8
# 
# 
# 
# ##### List the   names of the booster_versions which have carried the maximum payload mass. Use a subquery
# 

# In[75]:


get_ipython().run_line_magic('sql', 'Select BOOSTER_VERSION from spacex where PAYLOAD_MASS_KG_=(Select Max(PAYLOAD_MASS_KG_) from spacex)')


# ### Task 9
# 
# 
# ##### List the records which will display the month names, failure landing_outcomes in drone ship ,booster versions, launch_site for the months in year 2015.
# 
# **Note: SQLLite does not support monthnames. So you need to use  substr(Date, 4, 2) as month to get the months and substr(Date,7,4)='2015' for year.**
# 

# In[94]:


get_ipython().run_line_magic('sql', "Select BOOSTER_VERSION,LAUNCH_SITE,LANDING_OUTCOME from spacex where substr(Date)='2015' and LANDING_OUTCOME like 'Failure (drone ship)'")


# ### Task 10
# 
# 
# 
# 
# ##### Rank the  count of  successful landing_outcomes between the date 04-06-2010 and 20-03-2017 in descending order.
# 

# In[93]:


get_ipython().run_line_magic('sql', "Select Count(LANDING_OUTCOME) from Spacex where Date between '04-06-2010' and '20-03-2017'")


# ### Reference Links
# 
# * <a href ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20String%20Patterns%20-%20Sorting%20-%20Grouping/instructional-labs.md.html?origin=www.coursera.org">Hands-on Lab : String Patterns, Sorting and Grouping</a>  
# 
# *  <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Built-in%20functions%20/Hands-on_Lab__Built-in_Functions.md.html?origin=www.coursera.org">Hands-on Lab: Built-in functions</a>
# 
# *  <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sub-queries%20and%20Nested%20SELECTs%20/instructional-labs.md.html?origin=www.coursera.org">Hands-on Lab : Sub-queries and Nested SELECT Statements</a>
# 
# *   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-3-SQLmagic.ipynb">Hands-on Tutorial: Accessing Databases with SQL magic</a>
# 
# *  <a href= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-4-Analyzing.ipynb">Hands-on Lab: Analyzing a real World Data Set</a>
# 
# 
# 

# ## Author(s)
# 
# <h4> Lakshmi Holla </h4>
# 

# ## Other Contributors
# 
# <h4> Rav Ahuja </h4>
# 

# ## Change log
# | Date | Version | Changed by | Change Description |
# |------|--------|--------|---------|
# | 2021-07-09 | 0.2 |Lakshmi Holla | Changes made in magic sql|
# | 2021-05-20 | 0.1 |Lakshmi Holla | Created Initial Version |
# 

# ## <h3 align="center"> © IBM Corporation 2021. All rights reserved. <h3/>
# 
