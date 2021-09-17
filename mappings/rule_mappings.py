RULE_MAPPINGS = {
    "aws": {
        "ec2": {
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
        },
        "rds": {
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
            }
        },
        "s3": {
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
        }
    },
    "gcp": {
        "gcp_service": {
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
}
