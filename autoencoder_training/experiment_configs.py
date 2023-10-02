# Will increment hyperparameter sets as we try different ones.

class ExperimentConfig:

    def __init__(self, hyperparameters, base_model_name, policy_model_name, device=None):
        self.hyperparameters = hyperparameters
        self.base_model_name = base_model_name
        self.policy_model_name = policy_model_name
        self.device = device

    def __str__(self):
        printable = self.hyperparameters.copy()
        printable.update({'base_model_name': self.base_model_name, 'policy_model_name': self.policy_model_name})
        return str(printable)

hyperparameters_1 = {
    'hidden_size_multiples': [1, 2],
    'l1_coef': 0.001,
    'batch_size': 32,
    'num_epochs': 3,
    'learning_rate': 1e-3,
    'fast': True,
    'split': 'test',
    'num_layers_to_keep': 5
}


hyperparameters_2 = {
    'max_input_length': 256,
    'hidden_size_multiples': [1, 2],
    'l1_coef': 0.001,
    'batch_size': 32,
    'num_epochs': 3,
    'learning_rate': 1e-3,
    'fast': False,
    'split': 'test',
    'num_layers_to_keep': 5,
    'tied_weights': True
}

all_models = ['eleutherai/pythia-70m', 'eleutherai/pythia-160m', 'eleutherai/pythia-410m']
all_reward_functions = ['sentiment_reward', 'utility_reward']

def generate_experiment_configs(hyperparameters):
    all_experiment_configs = []
    device = 4
    for model_name in all_models:
        for reward_function in all_reward_functions:
            simplified_model_name = model_name.split('/')[-1]
            policy_model_name = f'amirabdullah19852020/{simplified_model_name}_{reward_function}'
            new_config = ExperimentConfig(hyperparameters=hyperparameters, base_model_name=model_name, policy_model_name=policy_model_name, device=device)
            all_experiment_configs.append(new_config)
    return all_experiment_configs

all_experiment_configs = generate_experiment_configs(hyperparameters_2)

experiment_config_A = ExperimentConfig(
    hyperparameters=hyperparameters_2,  base_model_name="eleutherai/pythia-70m",
    policy_model_name="amirabdullah19852020/pythia-70m_sentiment_reward"
)

experiment_config_B = ExperimentConfig(
    hyperparameters=hyperparameters_2,  base_model_name="eleutherai/pythia-70m",
    policy_model_name="amirabdullah19852020/pythia-70m_utility_reward"
)

experiment_config_C = ExperimentConfig(
    hyperparameters=hyperparameters_2,  base_model_name="eleutherai/pythia-160m",
    policy_model_name="amirabdullah19852020/pythia-160m_sentiment_reward"
)

experiment_config_D = ExperimentConfig(
    hyperparameters=hyperparameters_2,  base_model_name="eleutherai/pythia-160m",
    policy_model_name="amirabdullah19852020/pythia-160m_utility_reward"
)

experiment_config_E = ExperimentConfig(
    hyperparameters=hyperparameters_2,  base_model_name="eleutherai/pythia-410m",
    policy_model_name="amirabdullah19852020/pythia-410m_sentiment_reward"
)

experiment_config_F = ExperimentConfig(
    hyperparameters=hyperparameters_2,  base_model_name="eleutherai/pythia-410m",
    policy_model_name="amirabdullah19852020/pythia-410m_utility_reward"
)
