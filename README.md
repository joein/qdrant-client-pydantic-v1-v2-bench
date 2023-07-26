## Qdrant-client Pydantic v1 vs v2 comparison

Qdrant-client has recently introduced support for Pydantic v2.

This repo contains code for performance comparison between qdrant-client with Pydantic v1 and Pydantic v2.

### How to run
```bash
chmod +x install.sh
chmod +x run.sh
./install.sh # install dependencies, prepare environment for benchmarking
./run.sh # run benchmarking, build plots
```


### Results
Result of benchmarking is presented in `results` folder.

It contains raw results file `bench.jsonl` and corresponding plot in `bench.png`