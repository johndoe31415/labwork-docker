# labwork-docker
This is a thin shim of code around a submission system. It starts Docker
containers for each student's submission in an isolated container, build and
runs them.

## Installation of the Docker container
If you want to use the Docker container as it is built by the CI system, you can simply:

```
$ docker pull ghcr.io/johndoe31415/labwork-docker:master
```

Then you can tag it as 'labwork' so it's automatically found by the binary:

```
$ docker tag ghcr.io/johndoe31415/labwork-docker:master labwork
```

## Building the Docker container
To build the Docker container yourself:

```
$ docker build docker -t labwork
```

To verify that the build was successful:

```
$ docker image ls labwork
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
labwork      latest    6e10dc886c2f   2 months ago   1.22GB
```

## Submission file
The submission file has the following constraints:
  * It needs to be a .tar.gz archive
  * It needs to contain a "labwork" subdirectory which contains the submission
  * A `build` script may be present for compiling code
  * A `run` script must be present for running code. The `run` script receives
	an API endpoint as its first command line parameters and one or more
	additional command line parameters which are the exercises that it should
    query the labwork server for. The `build` script is called exactly once, the
    `run` script may be called multiple times.
  * The permissions of `build` and `run` need to be set appropriately (chmod +x).

An example `labwork.tar.gz` is included which answers a trivial assignment and
which can be used as a stub for implementing more sophisticated clients.

## Testing locally with network access
The `run-testcases` script is used to validate labwork submission files. It creates a Docker container, copies
the .tar.gz file into it and executes it. When running untrusted code, the network connection is deliberately
severed, but for testing purposes you can simply activate network access and direct your Docker container against
a publicly available solution server.

You'll find an example solution file in `labwork.tar.gz`. To test this out
against a public server at `https://submissions.labserver.com/foobar/`, you can
simply execute:

```
$ ./run-testcases -n -a labwork01 -c 1889d4db-c5cc-4e47-80aa-48b3ff9bac3d -u https://submissions.labserver.com/foobar/ labwork.tar.gz
1 instances finished, 0 timed out. Collecting results.
labwork.tar.gz (064d78b5caa101765c58aad860ed7eef658601b4b50514b1b5a076701474ddd8): exit returncode 0
labwork/
labwork/run
labwork/build
labwork/my_solution.py
No build needed in this case (Python), this file is just an example.

Skipping build step, no 'build' file or not marked executable.
Do not know how to handle type: histogram
Do not know how to handle type: histogram
Do not know how to handle type: histogram
Do not know how to handle type: histogram
Do not know how to handle type: histogram
Do not know how to handle type: histogram
Do not know how to handle type: histogram
Do not know how to handle type: caesar_cipher
Do not know how to handle type: caesar_cipher
Do not know how to handle type: caesar_cipher
Do not know how to handle type: caesar_cipher
Do not know how to handle type: caesar_cipher
Do not know how to handle type: caesar_cipher
Do not know how to handle type: caesar_cipher
4 known assignments, 14 unknown.
Passed: 4. Failed: 0
```

You'll see that we executed the `labwork01` exercise using client ID
`1889d4db-c5cc-4e47-80aa-48b3ff9bac3d` against
`https://submissions.labserver.com/foobar/`. The handler only supports the
simple `strcat` handler, other handlers are not implemented.


## License
GNU GPL-3.
