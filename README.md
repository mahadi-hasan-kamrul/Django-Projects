#CV Generator with Django \
In this project, the user can entry all kinds of information and afterthat a CV will be generated for him. It can look like a static project as the designs are not that good. I have hard coded every thing in this project. It was done to go through the basic things in a proper way. 

-Install the requirements.txt file. \
-**wkhtmltopdf** is used to generate the pdf file in this project.

**###The main focus of this project was to make WKHTMLTOPDF work while building a docker image. 
The DOCKER image of this project is custom coded with the collboration of DeepSeek AI. WKHTMLTOPDF does not go along with Docker because of a lot of dependencies failure.** 

**The project is then containerized with Docker. Then the image of the container was pushed into Github. And with Render deployment it was made live.** \
 ### Live Link: https://cvgene-latest.onrender.com/
