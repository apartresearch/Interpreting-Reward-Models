## Official Repository for Interpreting Reward Models in RLHF-Tuned Language Models Using Sparse Autoencoders
1. This repo provides scripts to train several LLM model and task combinations under RLHF using PPO.
2. The repository also supports training sparse autoencoders for feature extraction on the MLP layers of _pairs of base and policy models_, and automate feature interpretability between these.

## Repository structure.
This repo is structured so that RLHF models are trained under `rlhf_model_training`
The autoencoder training code is under `sparse_codes_training`.

As such we divide this repository into two major components, `rlhf_model_training` and `sparse_codes_training`.

The structure looks like this:

```
requirements.txt
scripts/
    ppo_training/
        run_experiment.sh
    sparse_codes_training/
        experiment.sh
    setup_environment.sh

src/
    rlhf_model_training
        reward_class.py
        rlhf_model_pipeline.py
        rlhf_training_utils/
    sparse_codes_training
        metrics/
        models/
            sparse_autoencoder.py
	experiment_helpers/
            autoencoder_trainer_and_preparer.py
            experiment_runner.py
            layer_activations_handler.py
        experiment.py
        experiment_configs.py
    utils/
```

`experiment.py` is the main script entrypoint where we parse command line arguments and select/launch autoencoder training. `experiment_runner.py` has most of the actual logic of the paper, where we extract divergent layers, initialize models and train pairs of autoencoders on activations.

`network_helper_functions` carries out necessary primitives of extracting activations from a layer, and calculating divergences between the corresponding layers of two neural nets.


## Getting started.
1. Run `source scripts/setup_environment.sh` to set your python path. Run the script as `source scripts/setup_environment.sh -v` if you also want to create and activate the appropriate virtual environment with all dependencies.
2. The main script for training PPO models is under `scripts/ppo_training/run_experiment.sh`.
3. The script for training autoencoders is under `scripts/sparse_codes_training/experiment.sh`. Modify these two scripts as needed to launch new PPO model or autoencoder training runs.

If you use this work, please cite:

```bibtex
@misc{marks2023interpreting,
      title={Interpreting Reward Models in RLHF-Tuned Language Models Using Sparse Autoencoders}, 
      author={Luke Marks and Amir Abdullah and Luna Mendez and Rauno Arike and Philip Torr and Fazl Barez},
      year={2023},
      eprint={2310.08164},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
