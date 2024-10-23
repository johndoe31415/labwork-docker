# labwork-docker
This is a thin shim of code around a submission system. It starts Docker
containers for each student's submission in an isolated container, build and
runs them.

## Installation of the Docker container
If you want to use the Docker container as it is built by the CI system, you can simply:

```
docker pull ghcr.io/johndoe31415/labwork-docker:master
```

Then you can tag it as 'labwork' so it's automatically found by the binary:

```
docker tag ghcr.io/johndoe31415/labwork-docker:master labwork
```

## Building the Docker container
To build the Docker container yourself:

```
docker build docker -t labwork
```

To verify that the build was successful:

```
docker image ls labwork
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
labwork      latest    6e10dc886c2f   2 months ago   1.22GB
```

## Testing inside the container
When you have built the docker container, you can start the virutal environment
and gain a shell there:

```
docker run -it labwork /bin/bash
root@5218562b4ad8:/#
```

As you can see, the current run has been given the container ID 5218562b4ad8
for this run. This ID will vary every time you start the Docker container. You
can now copy your solution inside the container, for example as a .tar.gz
archive:

```
docker cp my_amazing_solution.tar.gz 5218562b4ad8:/
```

And then, inside the Docker environment, have this file available to be able to
decompress it and/or run your tests with the environment (this test suite is
all part of your implementation):

```
root@5218562b4ad8:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  my_amazing_solution.tar.gz  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

## Testing with a proper CI/CD pipeline
The ideal way to build the artifact you need to hand in as your labwork is to
have a custom pipeline that builds it automatically for every change in the
code. This way, you can ensure that you're meeting all formal criteria (e.g.,
permissions inside your submission directory). I can highly recommend you take
a look at this. 

## License
GNU GPL-3.
