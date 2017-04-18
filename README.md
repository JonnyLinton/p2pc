# p2pc
Peer-to-Peer Chat Application Based on UDP

## Installation
While in the directory of the repo: `pip3 install -e .`

## Usage
`$ p2pc`

## Docker Stuff
While in the directory of the repo, with a docker daemon running:
`docker build -t p2pc .` To first build the application
`docker run -ti p2pc` to run p2pc inside docker.

For testing, we recommend using `docker run -ti p2pc` in separate terminal tabs.
