"""
This module gives the experiment configs for a given run.
"""
from reward_analyzer.configs.task_configs import TaskConfig

class ExperimentConfig:
    """
    This fully specifies one run of our experiment extracting base and policy models.
    """

    def __init__(
            self, hyperparameters, base_model_name,
            policy_model_name, task_config=TaskConfig.IMDB,
            wandb_project_name=None, device=None,
    ):
        self.hyperparameters = hyperparameters
        self.base_model_name = base_model_name
        self.task_config = task_config
        self.policy_model_name = policy_model_name

        if wandb_project_name:
            self.wandb_project_name = wandb_project_name
        else:
            self.wandb_project_name = f'Autoencoder_training_{self.task_config.name}'
        self.device = device

    def __str__(self):
        printable = self.hyperparameters.copy()
        printable.update({'base_model_name': self.base_model_name, 'task_config': self.task_config.name})
        return str(printable)

hyperparameters_fast = {
    'max_input_length': 128,
    'hidden_size_multiples': [1, 2],
    'l1_coef': 0.001,
    'batch_size': 32,
    'num_epochs': 1,
    'learning_rate': 1e-3,
    'fast': True,
    'split': 'test',
    'num_layers_to_keep': 5,
    'tied_weights': True,
    'divergence_choice': 'highest_divergence'
}


hyperparameters_full = {
    'max_input_length': 256,
    'hidden_size_multiples': [1, 2],
    'l1_coef': 0.001,
    'batch_size': 32,
    'num_epochs': 3,
    'learning_rate': 1e-3,
    'fast': False,
    'split': 'test',
    'num_layers_to_keep': 5,
    'tied_weights': True,
    'divergence_choice': 'highest_divergence'
}

all_models = [
    'eleutherai/pythia-70m', 'eleutherai/pythia-160m', #'eleutherai/pythia-410m',
    'eleutherai/gpt-neo-125m', 'google/gemma-2b-it' #'ybelkada/gpt-j-6b-sharded-bf16'
]

model_specific_parameters = {
  'pythia-70m': {},
  'pythia-160m': {},
  'pythia-410m': {},
  'gemma-2b-it': {},
  'gpt-neo-125m': {'l1_coef': 0.015},
  'gpt-j-6b-sharded-bf16': {'batch_size': 8, 'num_epochs': 1, 'gradient_accumulation_steps': 4}
}

task_specific_parameters = {
    TaskConfig.UNALIGNED: {'split': 'train', 'num_epochs': 1, 'batch_size': 64},
    TaskConfig.HH_RLHF: {'split': 'train', 'num_epochs': 1, 'batch_size': 64},
    TaskConfig.IMDB: {}
}

def generate_experiment_configs(hyperparameters, task_configs=None):
    """
    We generate experiment configs as a cross product of all possible
    model names and tasks, with the given hyperparameters.
    We update some model specific values based on experimentation -
    namely, gpt-neo-125 has a different l1_coef of 0.015 based on our
    experiments.
    """
    all_experiment_configs = {}
    task_configs = task_configs or [TaskConfig.UNALIGNED, TaskConfig.IMDB, TaskConfig.HH_RLHF]
    for model_name in all_models:
        for task_config in task_configs:
            simplified_model_name = model_name.rsplit('/', maxsplit=1)[-1]
            policy_model_name = f'{simplified_model_name}_{task_config.name}'
            hyperparameters_copy = hyperparameters.copy()

            # Update model specific params.
            hyperparameters_copy.update(model_specific_parameters.get(simplified_model_name, {}))

            # Update task specific params.
            hyperparameters_copy.update(task_specific_parameters.get(task_config, {}))
            new_config = ExperimentConfig(
                hyperparameters=hyperparameters_copy, base_model_name=model_name,
                task_config=task_config, policy_model_name=policy_model_name
            )
            experiment_key = (simplified_model_name, task_config.name)
            all_experiment_configs[experiment_key] = new_config
    return all_experiment_configs

fast_grid_experiment_configs = generate_experiment_configs(hyperparameters_fast)
grid_experiment_configs = generate_experiment_configs(hyperparameters_full)
