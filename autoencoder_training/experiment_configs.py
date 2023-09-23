# Will increment hyperparameter sets as we try different ones.

class ExperimentConfig:

    def __init__(self, hyperparameters, base_model_name, policy_model_name):
	self.hyperparameters = hyperparameters
	self.base_model_name = base_model_name
	self.policy_model_name = policy_model_name

hyperparameters_1 = {
    'input_size': 512,
    'hidden_sizes': [512, 1024],
    'sparsity_target': 0.1,
    'sparsity_weight': 1e-2,
    'batch_size': 32,
    'num_epochs': 50,
    'learning_rate': 1e-3
}


hyperparameters_2 = {
    'input_size': 512,
    'hidden_sizes': [512, 1024],
    'sparsity_target': 0.1,
    'sparsity_weight': 1e-1,
    'batch_size': 32,
    'num_epochs': 50,
    'learning_rate': 1e-3
}


experiment_config_A
experiment_config_B