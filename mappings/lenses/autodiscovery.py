AUTODISCOVER_RULES_TO_ANSWERS_MAP = {
    "backups-and-recovery": {
        "regular_backups_and_schedule": [
            {"name": "rds_backup_policy", "should_exist": False, "resources": ["rds"]},
        ]
    },
    # Security
    "identities": {
        "sec_identities_enforce_mechanisms": [
            {"name": "no_mfa_users", "should_exist": False, "resources": ["iam"]},
            {"name": "check_root_user_mfa", "should_exist": False, "resources": ["iam"]},
        ]
    },
    "permissions": {
        "sec_permissions_continuous_reduction": [
            {"name": "inactive_keys", "should_exist": False, "resources": ["iam"]},
        ],
        "sec_permissions_lifecycle": [
            {"name": "inactive_keys", "should_exist": False, "resources": ["iam"]},
        ]
    },
    "backing-up-data": {
        "rel_backing_up_data_automated_backups_data": [
            {"name": "ebs_snapshot", "should_exist": False, "resources": ["ebs"]},
        ]
    },
    "protect-data-rest": {
        "sec_protect_data_rest_encrypt": [
            {"name": "check_resource_encryption", "should_exist": False, "resources": ["ebs", "rds", "s3"]},
        ],
        "sec_protect_data_rest_access_control": [
            {"name": "s3_bucket_security", "should_exist": False, "resources": ["s3"]},
            {"name": "public_ebs_snapshot", "should_exist": False, "resources": ["ebs_snapshot"]},
        ]
    },
    # Cost
    "decomissioning-resources": {
        "cost_decomissioning_resources_decommission": [
            {"name": "underutilized_resources", "should_exist": False, "resources": ["ec2"]},
            {"name": "unused_resources", "should_exist": False, "resources": ["ebs", "elb", "nat"]},
        ]
    },
    "type-size-number-resources": {
        "cost_type_size_number_resources_metrics": [
            {"name": "instance_recommendation_rightsizing", "should_exist": False, "resources": ["ec2"]},
            {"name": "s3_recommendation_rightsizing", "should_exist": False, "resources": ["s3"]},
            {"name": "instance_recommendation", "should_exist": False, "resources": ["rds"]},
        ]
    },
    "aws-root-account-protection": {
        "do_not_use_root_routinely": [
            {"name": "root_account_usage", "should_exist": False, "resources": ["iam"]},
        ],
        "enable_mfa_on_all_root_accounts": [
            {"name": "check_root_user_mfa", "should_exist": False, "resources": ["iam"]},
        ],
        "no_access_keys_on_root": [
            {"name": "root_access_keys", "should_exist": False, "resources": ["iam"]},
        ],
    },
    "network-protection": {
        "sec_network_protection_inspection": [
            {"name": "check_waf_used", "should_exist": False, "resources": ["iam"]},
            {"name": "check_guardduty_enabled", "should_exist": False, "resources": ["iam"]},
        ]
    },
    "securely-operate": {
        "sec_securely_operate_updated_recommendations": [
            {"name": "check_guardduty_enabled", "should_exist": False, "resources": ["iam"]},
        ],
        "sec_securely_operate_aws_account": [
            {"name": "check_root_user_mfa", "should_exist": False, "resources": ["iam"]},
        ],
    },
    "protect-compute": {
        "sec_protect_compute_vulnerability_management": [
            {"name": "check_aws_inspector", "should_exist": False, "resources": ["iam"]},
        ]
    },
    "detect-investigate-events": {
        "sec_detect_investigate_events_auto_response": [
            {"name": "check_aws_inspector", "should_exist": False, "resources": ["iam"]},
        ]
    },
    "access-management": {
        "enable_mfa_for_all_interactive_iam": [
            {"name": "no_mfa_users", "should_exist": False, "resources": ["iam"]},
        ],
        "enforce_strong_password_policy": [
            {"name": "strong_password_policy", "should_exist": False, "resources": ["iam"]},
        ],
        "revoke_unused_credentials": [
            {"name": "inactive_keys", "should_exist": False, "resources": ["iam"]},
        ],
        "encrypt_user_credentials_at_rest": [
            {"name": "check_resource_encryption", "should_exist": False, "resources": ["rds"]},
        ],
        "audit_permissions_yearly": [
            {"name": "inactive_keys", "should_exist": False, "resources": ["iam"]},
        ]
    },
    "amazon-s3-bucket-access-policies": {
        "properly_configure_s3_buckets": [
            {"name": "s3_bucket_security", "should_exist": False, "resources": ["s3"]},
        ],
        "scope_s3_buckets_with_public_access": [
            {"name": "s3_bucket_security", "should_exist": False, "resources": ["s3"]}
        ]
    },
    "PII-handling": {
        "ecrypt_pii": [
            {"name": "check_resource_encryption", "should_exist": False, "resources": ["ebs", "rds", "s3"]},
        ],
    },
    "audit-and-logging": {
        "enable_cloudtrail_log_validation": [
            {"name": "cloudtrail_log_validation_enabled", "should_exist": False, "resources": ["ct_trail"]},
        ],
        "enable_aws_cloudtrail": [
            {"name": "cloudtrail_log_validation_enabled", "should_exist": False, "resources": ["ct_trail"]},
        ],
        "protect_cloudtrail_logs_from_deletion": [
            {"name": "cloudtrail_s3_protection", "should_exist": False, "resources": ["s3"]},
        ]
    },
    "aws-premium-support-level": {
        "enable_aws_business_support": [
            {"name": "check_aws_enterprise_support", "should_exist": False, "resources": ["iam"]},
        ]
    },
    # AWS FTR
    "sec_q8": {
        # Encrypt all sensitive data at rest
        "sec_sec_q8_a2": [
            {"name": "check_resource_encryption", "should_exist": False, "resources": ["ebs", "rds", "s3"]},
        ],
        # Review permissions of all Amazon S3 buckets
        "sec_sec_q8_a5": [
            {"name": "s3_bucket_security", "should_exist": False, "resources": ["s3"]},
        ],
        # Enable default encryption for Amazon S3 Buckets
        "sec_sec_q8_a6": [
            {"name": "check_resource_encryption", "should_exist": False, "resources": ["s3"]},
        ],
        # Enable default encryption for Amazon EBS volumes
        "sec_sec_q8_a7": [
            {"name": "check_resource_encryption", "should_exist": False, "resources": ["ebs"]},
        ],
    },
}
