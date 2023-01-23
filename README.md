# Signup application for course setup and teardown

In order to organise 10 day residential courses, volunteers are needed at rented course sites for setup and teardown. This webapp enables people to sign up for these activities.

## User roles
### Admin
Admins can add and modify course data
### Basic user
Basic users can sign up for course setup and teardown and modify their own signup information

## Pages

### Courses page 

- displays list of courses to sign up to
- by clicking a course, an Information page and an Edit signup page for that course opens
- will be added before 5.2.

### Edit signup page (for each course)
- contains options to sign up for setup or teardown for this specific course and modify this information
- Input fields:
    - time of arrival, days spent and time of leaving
    - name and contact information
    - car or no car
    - will be added before 5.2.

### Information page (for each course)
- shows how many people have signed up and for what times
- shows user's own signup information for this course
- Admins only: shows names of people that signed up
- will be added before 5.2., except Admin parts later

### Login page
- After login basic user can view and modify one's signup information
- After login admin can modify course information and view names and contact information of people who signed up
- will be added before 5.2.

### Register page
- Register to be a basic user, get rights to login
- will be added before 5.2.

### Add course page
- Admin only! 
- Add new course
- will be added before 19.2.

### Register admin page
- Register to be admin, get admin rights
- Will be added only if enough time


## Run application locally

Clone this repository. Go to the local project repository's root folder `signup-app`. Create `.env` file in root folder. Add following contents to `.env`:


    DATABASE_URL=<local-address-of-database>
    SECRET_KEY=<secret-key-you-made-up>

Create virtual environment and activate it:

    $ python3 -m venv venv
    $ source venv/bin/activate

Install requirements:

    $ pip install -r ./requirements.txt

Start database in separate terminal window:

    $ start-pg.sh

Define database schema:

    $ psql < schema.sql

Run application locally

    $ flask run


