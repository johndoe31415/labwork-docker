# labwork-docker
This is a thin shim of code around a submission system. It starts Docker
containers for each student's submission in an isolated container, build and
runs them.

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

## License
GNU GPL-3.
