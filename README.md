# pier2pier: Massive Wiki tools in a docker container

### development journal and notes are [here](/devNotes.md).

2022-02-17: Notes in this README build on instructions and descriptions in this
Medium post: <https://medium.com/swlh/flask-docker-the-basics-66a699aa1e7d>

Once all the scaffolding is done this is one way to run the code and continue
development:

In the terminal type:
```
$ docker-compose up -d
```

This builds an image called ‘flask-docker_mywebservice’, then run a container using this image, bind the ports, and then, most importantly, create a volume mapping the contents of the hosts current working directory to the /usr/src/app folder inside the container.

So at this point you should be able to modify the app.py file, refresh your browser and see those updates reflected immediately.

You can stop the container simply by doing:
```
$ docker-compose down
```

If, in the terminal, you type:
```
$ docker images
```

This will list your images, you should see something like:
```
REPOSITORY                 TAG     IMAGE ID      CREATED
flask-docker_mywebservice  latest  d53b4335a737  About a minute ago
```

Then you can delete the image by typing:
```
$ docker rmi d53 -f
```

Where ‘d53’ in this (example) case is the first few letters of the generated
image ID (yours will be different), and -f forces the delete to happen no matter what.
