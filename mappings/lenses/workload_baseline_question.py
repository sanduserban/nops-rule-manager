BASELINE_PARTNER_HOSTED_SAAS = [
    # 1.
    {
        "QuestionId": "aws-premium-support-level",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "Support Level",
        "Choices": [
            {
                "ChoiceId": "enable_aws_business_support",
                "Title": "Enable AWS Business Support (or greater) on all production AWS accounts.",
                "Description": "AWS Support provides a mix of tools and technology, people, and programs designed to proactively help you optimize performance, lower costs, and innovate faster. AWS Business Support provides additional benefits including access to AWS Trusted Advisor and AWS Personal Health Dashboard and faster response times. Subscribing to AWS Business Support or greater for all production accounts is a requirement to successfully complete the FTR. Business Support billing calculations are performed on a per-account basis. Monthly charges are based on each month's AWS usage charges, subject to monthly minimum. For latest pricing information see Premium Support Pricing.",
            }
        ],
    },
    # 2.
    {
        "QuestionId": "aws-well-architected-review",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "AWS Well-Architected Review",
        "Choices": [
            {
                "ChoiceId": "conduct_well_architected_rewiew_production_yearly",
                "Title": "Conduct a Well-Architected Review with FTR Lens on the production workload on a periodic basis(minimum once every year).",
                "Description": "The AWS Well-Architected Tool helps you review the state of your workloads and compares them to the latest AWS architectural best practices. The tool is based on the AWS Well-Architected Framework, developed to help cloud architects build secure, high-performing, resilient, and efficient application infrastructure. Well Architected Reviews must be conducted on the production workload on a periodic basis. After conducting the review, you should prioritize the remediation of any identified issues according to your business priorities. It is not a requirement to complete the remediation of any issues identified in the review other than the requirements defined in this checklist.",
            }
        ],
    },
    # 3.
    {
        "QuestionId": "aws-root-account-protection",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "AWS Root Account",
        "Choices": [
            {
                "ChoiceId": "do_not_use_root_routinely",
                "Title": "Use root user is only by exception.",
                "Description": "The root user has unlimited access to your account and its resources, and using it only by exception helps protect your AWS resources. The AWS root user must not be used for everyday tasks, even administrative ones. Instead, adhere to the best practice of using the root user only to create your first AWS Identity and Access Management (IAM) user. Then securely lock away the root user credentials and use them to perform only a few account and service management tasks. To view the tasks that require you to sign in as the root user, see AWS Tasks That Require Root User. To learn more about FTR AWS root account protection and IAM configuration requirements, watch Baseline Bits: 03 AWS Root Account Protection and AWS Identity and Access Management Configuration.",
            },
            {
                "ChoiceId": "no_access_keys_on_root",
                "Title": "Remove access keys for the root user.",
                "Description": "Programmatic access to AWS APIs should never use the root user. It is best not to generate static an access key for the root user. If one already exists, you should transition any processes using that key to use temporary access keys from an AWS Identity and Access Management (IAM) role, or, if necessary, static access keys from an IAM user.",
            },
            {
                "ChoiceId": "enable_mfa_on_all_root_accounts",
                "Title": "Enable multi-factor authentication (MFA) on root user.",
                "Description": "If an account is not managed by AWS Organizations, enabling MFA provides an additional control for account sign-in. Because your root user can perform sensitive operations in your account, adding an additional layer of authentication helps you to better secure your account. Multiple types of MFA are available, including virtual MFA and hardware MFA. To learn more about FTR AWS root account protection and AWS Identity and Access Management configuration requirements, watch Baseline Bits: 03 AWS Root Account Protection and AWS Identity and Access Management Configuration.",
            },
            {
                "ChoiceId": "define_an_incident_response_plan",
                "Title": "Create an incident response (IR) runbook for root account credential misuse.",
                "Description": "A runbook that details an appropriate response to root account credential misuse enables you to promptly act in the event that your root user becomes compromised. In the event your root account credentials are inaccessible, you will need to either change your AWS account root user password, or contact account and billing support through the Unable to Sign in & Submit Billing or Account Request page.",
            },
        ],
    },
    # 4.
    {
        "QuestionId": "aws-accounts",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "AWS accounts",
        "Choices": [
            {
                "ChoiceId": "use_separate_accounts",
                "Title": "Use separate accounts for production and non-production stages.",
                "Description": "Multiple AWS accounts allow you to separate data and resources, and enable the use of Service Control Policies to implement guardrails. For example, users outside of your account do not have access to your resources by default. Similarly, the cost of AWS resources that you consume is allocated to your account. AWS recommends that you use multiple AWS Accounts to separate workloads and workload stages, such as production and non-production.",
            }
        ],
    },
    {
        "QuestionId": "communications-from-aws",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "Communications from AWS",
        "Choices": [
            {
                "ChoiceId": "configure_account_contacts",
                "Title": "Configure AWS account contacts.",
                "Description": "If an account is not managed by AWS Organizations , alternate account contacts help AWS get in contact with the appropriate personnel if needed. Configure the account’s alternate contacts to point to a group rather than an individual. For example, create separate email distribution lists for billing, operations, and security and configure these as Billing, Security, and Operations contacts in each active AWS account. This ensures that multiple people will receive AWS notifications and be able to respond, even if someone is on vacation, changes roles, or leaves the company.",
            },
            {
                "ChoiceId": "set_account_contract_information",
                "Title": "Set account contact information including the root user email address to email addresses and phone numbers owned by your company.",
                "Description": "Using company owned email addresses and phone numbers for contact information enables you to access them even if the individuals whom they belong to are no longer with your organization.",
            },
        ],
    },
    # 5.
    {
        "QuestionId": "audit-and-logging",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "CloudTrail",
        "Choices": [
            {
                "ChoiceId": "enable_aws_cloudtrail",
                "Title": "Configure CloudTrail in all AWS Accounts and in all Regions.",
                "Description": "AWS CloudTrail enables governance, compliance, operational auditing, and risk auditing of your AWS account. To meet FTR requirements, you must have management events enabled for all AWS accounts and aggregate these logs into an Amazon Simple Storage Service (Amazon S3) bucket owned by a separate AWS account. The first copy of management events in each region is delivered free of charge and you only pay for S3 storage cost. Additional copies of management events will incur charges. Should you enable data events, you will incur charges for each copy along with associated S3 storage costs. For latest pricing information see CloudTrail pricing.To learn more about FTR audit and logging requirements, watch Baseline Bits 05: Audit and Logging on AWS Accounts.",
            },
            {
                "ChoiceId": "store_cloudtrail_logs_in_a_separate_domain",
                "Title": "Store logs in a separate administrative domain with limited access (e.g. Separate AWS Account or an equivalent AWS Partner solution).",
                "Description": "Configuring the logs to flow to a central account (i.e. separate AWS Account that is only intended for log storage and limited access ) or an equivalent AWS Partner solution protects the logs from manipulation or deletion. To learn more about FTR audit and logging requirements, watch Baseline Bits 05: Audit and Logging on AWS Accounts.",
            },
            {
                "ChoiceId": "protect_cloudtrail_logs_from_deletion",
                "Title": "Protect log storage from unintended access (e.g. MFA-delete, versioning on S3, object lock or an equivalent solution)",
                "Description": "Protecting log storage locations from unintended access helps with avoiding any unintended changes to log files.",
            },
            {
                "ChoiceId": "enable_cloudtrail_log_validation",
                "Title": "Enable CloudTrail log file integrity validation.",
                "Description": "A validated log file using integrity validation enables you to assert positively that the log file itself has not changed, or that particular user credentials performed specific API activity. The CloudTrail log file integrity validation process also lets you know if a log file has been deleted or changed, or assert positively that no log files were delivered to your account during a given period of time. CloudTrail log file integrity validation uses industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally unfeasible to modify, delete or forge CloudTrail log files without detection. For more information, see Enabling Validation and Validating Files.",
            },
        ],
    },
    # 6.
    {
        "QuestionId": "access-management",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "Identity and Access Management",
        "Choices": [
            {
                "ChoiceId": "enable_mfa_for_all_interactive_iam",
                "Title": "Enable multi-factor authentication for all Human Identities with AWS access.",
                "Description": "You must require any human identities to authenticate using MFA before accessing your AWS accounts. Typically this means enabling MFA within your corporate identity provider. If you have existing legacy IAM users you must enable MFA for console access for those principals as well. Enabling MFA for IAM users provides an additional layer of security. With MFA, users have a device that generates a unique authentication code (a one-time password, or OTP). Users must provide both their normal credentials (user name and password) and the OTP. The MFA device can either be a special piece of hardware, or it can be a virtual device (for example, it can run in an app on a smartphone). To learn more about FTR IAM configuration requirements, watch Baseline Bits: 03 AWS Root Account Protection and AWS Identity and Access Management Configuration. Please note that Machine Identities do not require MFA.",
            },
            {
                "ChoiceId": "rotate_iam_credentials_regularly",
                "Title": "Rotate credentials regularly.",
                "Description": "When you cannot rely on temporary credentials and require long term credentials, rotate the IAM access keys regularly. If an access key is compromised without your knowledge, you limit how long the credentials can be used to access your resources. For information about rotating access keys for IAM users, see Rotating Access Keys. To learn more about FTR IAM configuration requirements, watch Baseline Bits: 03 AWS Root Account Protection and AWS Identity and Access Management Configuration.",
            },
            {
                "ChoiceId": "enforce_strong_password_policy",
                "Title": "Use strong password policy.",
                "Description": "Enforce a strong password policy, and educate users to avoid common or re-used passwords. For IAM users, you can create a password policy for your account on the Account Settings page of the IAM console. You can use the password policy to define password requirements, such as minimum length, whether it requires non-alphabetic characters, and so on. For more information, see Setting an Account Password Policy for IAM Users. To learn more about FTR IAM configuration requirements, watch Baseline Bits: 03 AWS Root Account Protection and AWS Identity and Access Management Configuration.",
            },
            {
                "ChoiceId": "create_unique_iam_user_for_each_individiual",
                "Title": "Create individual identities (no shared credentials) for anyone who needs AWS access.",
                "Description": "By creating individual identities for people accessing your account, you can give each user a unique set of security credentials and permissions. Individual users provide the ability to audit each users activity. To learn more about FTR IAM configuration requirements, watch Baseline Bits: 03 AWS Root Account Protection and AWS Identity and Access Management Configuration.",
            },
            {
                "ChoiceId": "do_not_share_iam_credentials_with_external_parties",
                "Title": "Use IAM roles and its temporary security credentials to provide access to third parties.",
                "Description": "Do not provision IAM users and share those credentials with people outside of your organization. Any external services that need to make AWS API calls against your account (e.g. a monitoring solution that accesses your account's AWS CloudWatch metrics) must use a cross-account role. See documentation on providing access to AWS accounts owned by third parties for more information.",
            },
            {
                "ChoiceId": "scope_iam_policies_down_to_least_privelege",
                "Title": "Grant least privilege access.",
                "Description": "You must follow the standard security advice of granting least privilege. Grant only the access that identities require by allowing access to specific actions on specific AWS resources under specific conditions. Rely on groups and identity attributes to dynamically set permissions at scale, rather than defining permissions for individual users. For example, you can allow a group of developers access to manage only resources for their project. This way, when a developer is removed from the group, access for the developer is revoked everywhere that group was used for access control, without requiring any changes to the access policies. To learn more about FTR IAM configuration requirements, watch Baseline Bits: 03 AWS Root Account Protection and AWS Identity and Access Management Configuration.",
            },
            {
                "ChoiceId": "revoke_unused_credentials",
                "Title": "Manage access based on life cycle.",
                "Description": "Integrate access controls with operator and application lifecycle and your centralized federation provider and IAM. For example, remove a user’s access when they leave the organization or change roles",
            },
            {
                "ChoiceId": "audit_permissions_yearly",
                "Title": "Audit identities quarterly.",
                "Description": "Auditing the identities that are configured in your identity provider and IAM helps ensure that only authorized identities have access to your workload. For example, remove people that leave the organization, and remove cross-account roles that are no longer required. Have a process in place to periodically audit permissions to the services accessed by an IAM entity. This helps you identify the policies you need to modify to remove any unused permissions, see IAM access advisor.",
            },
            {
                "ChoiceId": "do_not_hardcode_credentials",
                "Title": "Do not embed credentials in application code.",
                "Description": "Ensure all credentials used by your applications (e.g. IAM access keys, database passwords, etc.) are never included in your application's source code or committed to source control in any way.",
            },
            {
                "ChoiceId": "encrypt_credentials_at_rest",
                "Title": "Store secrets in specialized service.",
                "Description": "Where you cannot use temporary credentials, such as tokens from AWS Security Token Service, storing your secrets, such as database passwords, using a service like AWS Secrets Manager or an equivalent AWS Partner solution, helps secure your credentials.",
            },
            {
                "ChoiceId": "encrypt_user_credentials_at_rest",
                "Title": "Encrypt all end user/customer credentials and hash passwords at rest.",
                "Description": "If storing end user/customer credentials in a database that you manage, encrypt credentials at rest and hash passwords. As an alternative, AWS recommends using a user identity synchronization service, such as Amazon Cognito or an equivalent AWS Partner solution.",
            },
        ],
    },
    # 7.
    {
        "QuestionId": "backups-and-recovery",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "Backups and Recovery",
        "Choices": [
            {
                "ChoiceId": "regular_backups_and_schedule",
                "Title": "Perform data backup automatically.",
                "Description": "You must perform regular backups to a durable storage service. Backups ensure that you have the ability to recover from administrative, logical, or physical error scenarios. Configure backups to be taken automatically based on a periodic schedule, or by changes in the dataset. RDS instances, EBS volumes, DynamoDB tables, and S3 objects can all be configured for automatic backup. AWS Marketplace solutions or third-party solutions can also be used. To learn more about FTR backup and recovery requirements, watch Baseline Bits 07: Backups and Disaster Recovery.",
            },
            {
                "ChoiceId": "test_recovery_regularly",
                "Title": "Perform periodic recovery of the data to verify backup integrity and processes.",
                "Description": "Validate that your backup process implementation meets your recovery time objectives (RTO) and recovery point objectives (RPO) by performing a recovery test both on a periodic basis and after making significant changes to your cloud environment. AWS provides resources to help you manage backup and restore of your data. To learn more about FTR backup and recovery requirements, watch Baseline Bits 07: Backups and Disaster Recovery.",
            },
        ],
    },
    # 8.
    {
        "QuestionId": "disaster-recovery",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "Disaster Recovery",
        "Choices": [
            {
                "ChoiceId": "define_rpo_and_rto",
                "Title": "Define a Recovery Point Objective (RPO) according to your organizational needs.",
                "Description": "Your data loss tolerance is the basis of your backup strategy and frequency. Recovery Point Objective (RPO) defines your data loss tolerance in-terms of time. Define a Recovery Point Objective (RPO) according to your organizational needs.",
            },
            {
                "ChoiceId": "have_and_rto_of_24_hours",
                "Title": "Establish a Recovery Time Objective (RTO) to meet business needs and expectations. This should be on the order of minutes for all components that are critical for providing service to your customers, but should never exceed 24 hours.",
                "Description": "Recovery Time Objective (RTO) defines your tolerance for downtime. The FTR requirement is for the RTO to be less than 24.",
            },
            {
                "ChoiceId": "test_dr_plan_against_rpo_and_rto",
                "Title": "Test disaster recovery implementation to validate the implementation.",
                "Description": "Test failover to DR to ensure that RTO and RPO are met, both periodically and after major updates. The DR test must include accidental data loss, instance, and Availability Zone (AZ) failures. At least one DR test that passes RTO and RPO requirements must be completed prior to FTR approval.",
            },
        ],
    },
    # 9.
    {
        "QuestionId": "amazon-s3-bucket-access-policies",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "Amazon S3 Bucket Access",
        "Choices": [
            {
                "ChoiceId": "properly_configure_s3_buckets",
                "Title": "Review all Amazon S3 buckets to determine appropriate access levels.",
                "Description": "You must ensure that buckets that require public access have been reviewed to determine if public read or write access is needed, and appropriate controls are in place to control public access. When using AWS, it's best practice to restrict access to your resources to the people that absolutely need it (the principle of least privilege). To learn more about FTR S3 bucket access management requirements, watch Baseline Bits 06: S3 Bucket Access Management and Configuration.",
            },
            {
                "ChoiceId": "scope_s3_buckets_with_public_access",
                "Title": "Restrict access to S3 buckets that should not have public access.",
                "Description": "You must ensure that buckets that should not allow public access are properly configured to prevent public access. By default, all S3 buckets are private, and can only be accessed by users that have been explicitly granted access. Most use cases won't require broad-ranging public access to read files from your S3 buckets, unless you're using S3 to host public assets (for example, to host images for use on a public website), and it's best practice to never open access to the public. To learn more about FTR S3 bucket access management requirements, watch Baseline Bits 06: S3 Bucket Access Management and Configuration.",
            },
            {
                "ChoiceId": "put_monitoring_and_alerting_in_place",
                "Title": "Implement monitoring and alerting to identify when S3 buckets become public.",
                "Description": "You must have monitoring or alerting in place to identify when S3 buckets become public. Trusted Advisor checks for S3 buckets that have open access permissions. Bucket permissions that grant List access to everyone can result in higher than expected charges if objects in the bucket are listed by unintended users at a high frequency. Bucket permissions that grant Upload/Delete access to everyone create potential security vulnerabilities by allowing anyone to add, modify, or remove items in a bucket. The Trusted Advisor check examines explicit bucket permissions and associated bucket policies that might override the bucket permissions. You can also use AWS Config to monitor your S3 buckets for public access. For more information on using AWS Config to monitor S3, please take a look at this blog. To learn more about FTR S3 bucket access management requirements, watch Baseline Bits 06: S3 Bucket Access Management and Configuration.",
            },
        ],
    },
    # 10.
    {
        "QuestionId": "cross-account-access",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "Cross-Account Access",
        "Choices": [
            {
                "ChoiceId": "use_iam_cross_account_roles",
                "Title": "Use cross-account roles to access to a customer accounts.",
                "Description": "Cross-account roles reduce the amount of sensitive information AWS Partners need to store for their customers. To learn more about FTR cross-account access requirements, watch Baseline Bits 04: Using AWS Identity and Access Management Roles for Cross-Account Access.",
            },
            {
                "ChoiceId": "provide_guidance_or_automation",
                "Title": "Provide guidance or an automated setup mechanism (e.g. AWS CloudFormation template) for creating cross-account role with minimum required privileges.",
                "Description": "The policy created for cross-account access in customer accounts must follow the least privilege principle. The partner must provide a role policy document or an automated setup mechanism (e.g. an AWS CloudFormation template) for the customers to use to ensure that the roles are created with minimum required privileges.",
            },
            {
                "ChoiceId": "use_external_id",
                "Title": "Use external ID with cross-account roles to access customer accounts.",
                "Description": "The external ID allows the user that is assuming the role to assert the circumstances in which they are operating. It also provides a way for the account owner to permit the role to be assumed only under specific circumstances. The primary function of the external ID is to address and prevent the confused deputy problem.",
            },
            {
                "ChoiceId": "use_value_you_generate_for_external_id",
                "Title": "Use a value you generate (not something provided by the customer) for the external ID.",
                "Description": "When configuring cross-account access using IAM roles, you must use a value you generate for the external ID, instead of one provided by the customer, to ensure the integrity of the cross account role configuration. A partner-generated external ID ensures that malicious parties cannot impersonate a customer's configuration and enforces uniqueness and format consistency across all customers. If you are not generating an external ID today we recommend implementing a process that ensures a random unique value, such as a Universally Unique Identifier, is generated for the external ID that a customer would use to setup a cross account role.",
            },
            {
                "ChoiceId": "ensure_all_external_ids_are_unique",
                "Title": "Ensure all external IDs are unique.",
                "Description": "The external IDs used must be unique across all customers. Re-using external IDs for different customers does not solve the confused deputy problem and runs the risk of customer A being able to view data of customer B by using the role ARN of customer B along with the external ID of customer B. To resolve this, we recommend implementing a process that ensures a random unique value, such as a Universally Unique Identifier, is generated for the external ID that a customer would use to setup a cross account role.",
            },
            {
                "ChoiceId": "do_not_allow_customers_to_set_or_update_external_id",
                "Title": "Provide read-only access to external ID to customers.",
                "Description": "Customers must not be able to set or influence external IDs. When the external ID is editable, it is possible for one customer to impersonate the configuration of another. When the external ID is editable Customer A can create a cross account role setup using customer B’s role ARN and external id, granting customer A access to customer B’s data. Remediation of this item involves making the external ID a view only field ensuring that the external ID cannot be changed for purposes of impersonating the setup of another customer.",
            },
            {
                "ChoiceId": "deprecate_all_historical_use_of_customer_provided_iam_credentials",
                "Title": "Deprecate any historical use of customer-provided IAM credentials.",
                "Description": "If your application provides legacy support for the use of static IAM credentials for cross-account access, the application's user interface and customer documentation must make it clear that this method is deprecated and the use of a cross-account IAM role is recommended. Existing customers should be encouraged to switch to cross-account role based-access, and collection of credentials should be disabled for new customers. To learn more about FTR cross-account access requirements, watch Baseline Bits 04: Using AWS Identity and Access Management Roles for Cross-Account Access",
            },
        ],
    },
    # 11.
    {
        "QuestionId": "PII-handling",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "Sensitive Data",
        "Choices": [
            {
                "ChoiceId": "identify_sensitive_data",
                "Title": "Identify sensitive data (e.g. Personally Identifiable Information (PII) and Protected Health Information (PHI)).",
                "Description": "Data classification enables you to determine which data needs to be protected and how. Based on the workload and the data it processes, identify the data that is not common public knowledge.",
            },
            {
                "ChoiceId": "ecrypt_pii",
                "Title": "Encrypt all sensitive data at rest.",
                "Description": "Encryption maintains the confidentiality of sensitive data even when it gets stolen or the network through which it is transmitted becomes compromised.",
            },
            {
                "ChoiceId": "use_protocols_with_encryption",
                "Title": "Only use protocols with encryption when transmitting sensitive data.",
                "Description": "Encryption maintains data confidentiality even when the network through which it is transmitted becomes compromised.",
            },
            {
                "ChoiceId": "log_access_to_pii",
                "Title": "Log access to sensitive data comprehensively throughout the system",
                "Description": "Visibility into any unexpected access to sensitive data provides you with the opportunity to perform necessary corrective actions to further protect your data. Scope your systems for components that store sensitive data. Implement application- and resource-level auditing and logging to monitor all access to data and quickly identify unauthorized access.",
            },
        ],
    },
    # 12.
    {
        "QuestionId": "PHI-handling",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "Protected Health Information",
        "Choices": [
            {
                "ChoiceId": "have_baa_in_place",
                "Title": "If the solution handles Protected Health Information (PHI), the partner must have a Business Associate Addendum (BAA) in place with AWS for every AWS account with PHI",
                "Description": "Have a Business Associate Addendum (BAA) in place with AWS for every AWS account with Protected Health Information (PHI).",
            },
            {
                "ChoiceId": "only_use_services_in_the_hipaa_elibile_services",
                "Title": "Only use services in the HIPAA Eligible Services Reference for solutions that handle PHI.",
                "Description": "Solutions handling PHI must use services in the HIPAA Eligible Services Reference.",
            },
        ],
    },
    # 13.
    {
        "QuestionId": "regulatore-compliance-validation-process",
        "PillarId": "PartnerHostedSaaSChecklist",
        "QuestionTitle": "Regulatory Compliance Validation Process",
        "Choices": [
            {
                "ChoiceId": "ensure_compliance_is_met",
                "Title": "Establish a process to ensure that all required compliance standards are met.",
                "Description": "If you advertise that your product meets specific compliance standards, you must have an internal process for ensuring compliance. Examples of compliance standards include PCI DSS, FedRAMP, and HIPAA. Applicable compliance standards are determined by various factors, such as what types of data the solution stores or transmits and which geographic regions the solution supports.",
            }
        ],
    },
]
