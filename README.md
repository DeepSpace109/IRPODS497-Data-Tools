# IRPODS497-Data-Tools

<p>DataTools contains the relevant tools for connecting to the TIF database currently up, an example query, and several specific tools for data preliminary data analysis.</p>

<h2>CONNECTING TO DATABASE</h2>
<p>An example Database connection, and the one used by all relevant tools, is handeled by <i>establishConnection.py</i></p>. 
<p>To use <i>establishConnection.py</i>, you will need to clone this repo, and then provide database credentials.</p>

<h4>Linux:</h4>

```
$ git clone https://github.com/TIFScrapingOrg/DataTools
$ touch awscreds.csv
```

<h4>Windows:</h4>

```
$ git clone https://github.com/TIFScrapingOrg/DataTools
$ start notepad awscreds.csv
```

<p>From here, you will have to enter in the database endpoint and relevant credentials to access the DB. If you do not have these credentials and believe you should, please message me! We are working on a User Provisioning system for public use.</p>
<p>Proceed to open the CSV and fill it out as below:</p>

`tifproject.cruoe42s86b2.us-east-2.rds.amazonaws.com,[YOUR_USERNAME],[YOUR_PASSWORD]`

<p>From here, run <i>establishConnection.py</i></p>

