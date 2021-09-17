FTR_AUTODISCOVERY = {
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
