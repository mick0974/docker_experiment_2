# docker_experiment_2

docker build -t andrea .

docker run --name andrea -v $(pwd)/results:/tool/output --rm andrea
