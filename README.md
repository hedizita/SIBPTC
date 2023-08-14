**1. Introduction**
This documentation provides instructions for generating an XML product feed from a given SQLite database of products, adhering to the Google Merchant product data specifications. 

The implementation uses Python and the SQLite database.

**2. Setup**
  
  *Prerequisites* 
  
Python (recommended version 3.6+)

SQLite database file (download link provided in the task)


*Downloading the Database*
Click on the following link to download the SQLite database: data.sqlite


Save the downloaded file as data.sqlite in the same directory as the script.

**3. Running the code**
Clone or download the project repository from GitHub: https://github.com/hedizita/SIBPTC/tree/main 

**4. Github repository**
You can see several Python files besides the downloaded sqlite file, *README.md* and *.gitignore*. I also created SQL files throughout the process: *data.sqbpro*, *db.mssql*.

The files *nn.py* and *nn2.py* are previous test files for creating the base, you do not need to run these since there will be several errors which I corrected in the *base.py*.

The *base.py* file is the one that creates the *feed.xml* given in the task.
You can see my supporting explanations in my code in this file.

**5. XML file data**
During the creation of the needed *feed.xml* I had some troubles. These are the following:
I could not import the *product_id* (due to many errors) which was needed for creating the *link* and *ID* to each product. Therefore these are not included in the *feed.xml*. 


What I did and got errors for are the following:
```ET.SubElement(prod_el, 'id').text = str(prod_id)```python3
and
```ET.SubElement(prod_el, 'link').text = f'https://butopea.com/p/{prod_id}```python3


For *condition* I defined it as ‘new’: 
This means that regardless of the product’s actual condition it is specified that all products should be treated as new. My assumption is that you only sell new products. 

For the *additional_image_link*: 
I initialized it as an empty string, this means that I saw no data that can be associated with this requirement although it is present at the feed.

After generating the *feed.xml* you can see that the encoding I used is UTF-8 and the fields generated are:
- Title [*title*] 
- Description [*description*] 
- Image link [*image_link*]
- Additional image link [*additional_image_link*]
- Availability [*availability*] 
- Price [*price*] 
- Brand [*brand*] 
- Condition [*condition*]


You can download the *feed.xml* from the repository. 
