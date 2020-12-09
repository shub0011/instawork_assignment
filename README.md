# instawork_assignment


---

## Setting up

You’ll start by editing this README file to learn how to edit a file in Bitbucket.

1. Install docker and docker-compose
2. make sure all the folders have appropriate permissions
3. `docker-compose build` to pull images, install and run the dependencies
4. `docker-compose up db` to start the db and start taking in connections(required only for first time)
5. `docker-compose up` to start the migrate and start the server
6. hit the url as follows `http://localhost:8000/userbase/users`


---

## Working and Other urls

1. `http://localhost:8000/userbase/users`
2. On clicking the resource urls in the list, you can go and edit a particular resource
3. For editing, you need to click/hit the url like this 
	`http://localhost:8000/userbase/users/4`

4. Consequently for deleting them 
	`http://localhost:8000/userbase/users/4`
	press on DELETE
5. Use curl to POST like this 
	curl -H "Content-Type: application/json" -d '{
    "first_name": "asma",
    "last_name": "kumari",
    "phone_number": "785764837",
    "email": "rehan@balwan.com",
    "role": "A"
}' -X POST  http://localhost:8000/userbase/users
---

## More Additions that could have been done

1. Pagination , as controlled by user
2. More options like date/ pg filter

## What are used

1. Django Rest Framework
2. Postresql
3. Docker