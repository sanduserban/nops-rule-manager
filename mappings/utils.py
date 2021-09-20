from .rules import CUSTOM_RULE_MAPPINGS, AWS_CONFIG_RULE_MAPPINGS


def get_full_mappings():
    aws_mappings = {**CUSTOM_RULE_MAPPINGS.get("aws"), **AWS_CONFIG_RULE_MAPPINGS}
    return {**CUSTOM_RULE_MAPPINGS, **{"aws": aws_mappings}}
