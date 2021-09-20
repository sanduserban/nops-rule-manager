CUSTOM_RULE_MAPPINGS = {
    "aws": {
        "ec2_low_network_utilization": {
            "title": "EC2 Low Network Traffic details",
            "name": "EC2 low network traffic details",
            "breadcrumbTitle": "EC2 low network traffic",
            "description": "Some description",
            "service": "ec2",
            "pillar": "Cost",
            "compliance": ["FTR", "WAFR"],
            "tags": [
                "AWS",
                "WAFR"
            ]
        },
        "check_ec2_autoscaling": {
            "title": "Resources are part of autoscaling groups",
            "name": "Autoscaling disabled for EC2 instances\"",
            "breadcrumbTitle": "EC2 Autoscaling",
            "description": "Consider leveraging autoscaling for high availability and lower cost",
            "service": "ec2",
            "pillar": "Reliability",
            "compliance": ["FTR", "WAFR"],
            "tags": [
                "AWS",
                "FTR",
                "WAFR"
            ]
        },
        "rds_instances_without_multiaz": {
            "title": "Resources are part of autoscaling groups",
            "name": "Enable Multi-AZ for RDS",
            "breadcrumbTitle": "EC2 Autoscaling",
            "description": "RDS instances are enabled for Multi-AZ. "
                           "It provides high availability to quickly and "
                           "automatically recover from infrastructure failures.",
            "service": "rds",
            "pillar": "Reliability",
            "compliance": ["FTR", "HIPAA"],
            "tags": [
                "AWS",
                "FTR",
            ]
        },
        "s3_bucket_versioning_disabled": {
            "title": "S3 buckets without versioning enabled",
            "name": "S3 versioning enabled",
            "breadcrumbTitle": "S3 versioning not enabled",
            "description":
                "S3 bucket versioning allows you to easily recover from unintended user actions and application failures",
            "service": "s3",
            "pillar": "Reliability",
            "compliance": ["WAFR", "PCI"],
            "tags": [
                "AWS",
                "WAFR",
                "PCI"
            ]
        }
    },
    "gcp": {
        "some_gcp_rule": {
            "title": "GCP Title",
            "name": "gcp",
            "breadcrumbTitle": "gcp breadcrump",
            "description": "gcp description",
            "service": "gcp_service",
            "pillar": "Reliability",
            "compliance": ["PCI"],
            "tags": [
                "GCP"
            ]
        }
    }
}

AWS_CONFIG_RULE_MAPPINGS = {
    "s3_bucket_public_write_prohibited": {
        "title": "S3 buckets with public write unprohibited",
        "name": "S3 Bucket public write prohibited",
        "breadcrumbTitle": "S3 versioning not enabled",
        "description":
            "Checks that your Amazon S3 buckets do not allow public write access. "
            "The rule checks the Block Public Access settings, "
            "the bucket policy, and the bucket access control list (ACL).",
        "service": "s3",
        "pillar": "Security",
        "compliance": ["WAFR", "PCI"],
        "tags": [
            "AWS",
            "WAFR",
            "PCI",
            "AWS Config",
        ]
    },
    "cloud_trail_cloudwatch_logs_enabled": {
        "title": "CloudTrail CloudWatch logs enabled",
        "name": "CloudTrail CloudWatch logs enabled",
        "breadcrumbTitle": "S3 versioning not enabled",
        "description":
            "Checks whether AWS CloudTrail trails are configured to send logs to Amazon CloudWatch logs. "
            "The trail is non-compliant if the CloudWatchLogsLogGroupArn property of the trail is empty.",
        "service": "ct_trail",
        "pillar": "Security",
        "compliance": ["FTR"],
        "tags": [
            "AWS",
            "FTR",
            "AWS Config",
        ]
    }
}
