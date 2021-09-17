AWS_FTR = [
    {
        "QuestionId": "ops_q1",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How does your organization ensure that contractually obligated compliance standards are met and maintained?",
        "Choices": [
            {
                "ChoiceId": "ops_ops_q1_a1",
                "Title": "Evaluate contractual compliance requirements",
                "Description": "A thorough evaluation of your contractual compliance requirements provides your organization with clarity around risks, challenges, necessary procedures, and deadlines that you need to meet.",
            },
            {
                "ChoiceId": "ops_ops_q1_a2",
                "Title": "Document and share requirements",
                "Description": "Documentation ensures that stakeholders have a common understanding of compliance requirements, how they will be maintained, how they will be evaluated, and what controls they are subject to.",
            },
            {
                "ChoiceId": "ops_ops_q1_a3",
                "Title": "Implement controls",
                "Description": "Executing on necessary procedures based on documented compliance requirements ensures achievement of compliance goals.",
            },
            {
                "ChoiceId": "ops_ops_q1_a4",
                "Title": "Monitor compliance",
                "Description": "Monitoring allows your organization to determine if controls are still in place or if there are needed changes.",
            },
            {
                "ChoiceId": "ops_ops_q1_a5",
                "Title": "Maintain compliance",
                "Description": "Because compliance requirements may change periodically, it is important to stay up to date and implement controls in order to ensure that your organization maintains compliance. ",
            },
            {"ChoiceId": "ops_ops_q1_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "rel_q1",
        "PillarId": "reliability",
        "QuestionTitle": "How do you plan for disaster recovery (DR)?",
        "Choices": [
            {
                "ChoiceId": "rel_rel_q1_a1",
                "Title": "Define a Recovery Point Objective (RPO) according to your organizational needs.",
                "Description": "Your data loss tolerance is the basis of your backup strategy and frequency.",
            },
            {
                "ChoiceId": "rel_rel_q1_a2",
                "Title": "Establish a Recovery Time Objective (RTO) to meet business needs and expectations. This should be on the order of minutes for all components that are critical for providing service to your customers, but should never exceed 24 hours.",
                "Description": "The ability to restore business operations within the first 24 hours of an outage is critical to promote positive customer experiences.",
            },
            {"ChoiceId": "rel_rel_q1_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "sec_q1",
        "PillarId": "security",
        "QuestionTitle": "How do you secure your AWS accounts?",
        "Choices": [
            {
                "ChoiceId": "sec_sec_q1_a3",
                "Title": "Root user is used only by exception",
                "Description": "The root user of an account has full access and must only be used by exception.",
            },
            {
                "ChoiceId": "sec_sec_q1_a4",
                "Title": "Root user has multi-factor authentication (MFA) enabled.",
                "Description": "If an account is not managed by AWS Organizations, enabling MFA provides an additional control for account sign-in.",
            },
            {
                "ChoiceId": "sec_sec_q1_a5",
                "Title": "Root user has no access keys",
                "Description": "Access keys must not be assigned to the root user under any circumstances.",
            },
            {
                "ChoiceId": "sec_sec_q1_a6",
                "Title": "Configure AWS account contacts",
                "Description": "If an account is not managed by AWS Organizations, alternate account contacts help AWS get in contact with the appropriate personnel if needed.",
            },
            {
                "ChoiceId": "sec_sec_q1_a7",
                "Title": "Separate accounts are used for production and non-production stages.",
                "Description": "Multiple AWS accounts allow you to separate workloads and workload stages, such as production and non-production.",
            },
            {
                "ChoiceId": "sec_sec_q1_a8",
                "Title": "Separate accounts are used for critical and shared services",
                "Description": "Multiple AWS accounts allow you to separate data and resources, and enable the use of Service Control Policies to implement guardrails.",
            },
            {
                "ChoiceId": "sec_sec_q1_a1",
                "Title": "Use AWS Organizations to manage your accounts.",
                "Description": "Use AWS Organizations to centrally enforce policy-based management and consolidated billing for multiple AWS accounts.",
            },
            {
                "ChoiceId": "sec_sec_q1_a2",
                "Title": "Restrict access to the AWS Organizations management account",
                "Description": "The AWS Organizations management account is the AWS account that you used to create your organization and has access to all other accounts.",
            },
            {"ChoiceId": "sec_sec_q1_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "sec_q2",
        "PillarId": "security",
        "QuestionTitle": "How do you configure identities for people and machines?",
        "Choices": [
            {
                "ChoiceId": "sec_sec_q2_a2",
                "Title": "Enforce multi-factor authentication (MFA) for all administrators.",
                "Description": "Enforcing multi-factor authentication (MFA) for all administrators provides an additional control for sign-in.",
            },
            {
                "ChoiceId": "sec_sec_q2_a3",
                "Title": "All IAM users have multi-factor authentication (MFA) enabled",
                "Description": "While transitioning from IAM users to a centralized identity provider for workforce identities, or roles for cross-account access, all IAM users must have MFA enabled.",
            },
            {
                "ChoiceId": "sec_sec_q2_a4",
                "Title": "Use roles for cross-account access",
                "Description": "Roles provide a secure method of accessing AWS accounts when implemented with a unique external ID and least privilege permissions.",
            },
            {
                "ChoiceId": "sec_sec_q2_a5",
                "Title": "Use unique external ID for cross-account roles",
                "Description": "Generating a unique external ID for each customer improves the security of cross-account access using roles.",
            },
            {
                "ChoiceId": "sec_sec_q2_a7",
                "Title": "Store secrets in specialized service",
                "Description": "Where you cannot use temporary credentials, such as tokens from AWS Security Token Service (AWS STS), store your secrets (for example, database passwords) using AWS Secrets Manager, which handles encryption, rotation, and access control.",
            },
            {
                "ChoiceId": "sec_sec_q2_a8",
                "Title": "Audit identities quarterly",
                "Description": "Auditing the identities that are configured in your identity provider and IAM helps ensure that only authorized identities have access to your workload. For example, remove people that leave the organization, and remove cross-account roles that are no longer required.",
            },
            {
                "ChoiceId": "sec_sec_q2_a1",
                "Title": "Centralize identities for all administrators",
                "Description": "Centralizing identities using either AWS Single Sign-On or a third-party provider help avoid routinely creating IAM users or using long-term access keys. This approach makes it easier to manage multiple AWS accounts and federated applications.",
            },
            {
                "ChoiceId": "sec_sec_q2_a6",
                "Title": "Use temporary credentials for API and CLI access",
                "Description": "To reduce the risk of unintended access to access keys, require identities, such as administrators, to dynamically acquire temporary credentials.",
            },
            {"ChoiceId": "sec_sec_q2_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "sec_q3",
        "PillarId": "security",
        "QuestionTitle": "How do you control permissions for people and machines?",
        "Choices": [
            {
                "ChoiceId": "sec_sec_q3_a1",
                "Title": "Review IAM policies granting privileged access",
                "Description": "Grant only the access that identities require by allowing access to specific actions on specific AWS resources under specific conditions. Policies should only allow full “*” administrative privileges as an exception.",
            },
            {
                "ChoiceId": "sec_sec_q3_a3",
                "Title": "Configure AWS Organizations Service Control Policies (SCPs)",
                "Description": "Establish common controls that restrict access to all identities in your organization. For example, you can restrict access to specific AWS Regions, or prevent your operators from deleting common resources, such as an IAM role used for your security team.",
            },
            {
                "ChoiceId": "sec_sec_q3_a4",
                "Title": "Use IAM Access Analyzer",
                "Description": "AWS IAM Access Analyzer helps you identify the resources in your organization and accounts, such as Amazon S3 buckets or IAM roles, that are shared with an external entity.",
            },
            {"ChoiceId": "sec_sec_q3_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "sec_q4",
        "PillarId": "security",
        "QuestionTitle": "How are you capturing foundational events?",
        "Choices": [
            {
                "ChoiceId": "sec_sec_q4_a2",
                "Title": "Configure CloudTrail multi-Region",
                "Description": "AWS CloudTrail enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure.",
            },
            {
                "ChoiceId": "sec_sec_q4_a3",
                "Title": "Protect log storage from unintended access",
                "Description": "Protecting log storage locations from unintended access (e.g. versioning and object lock on S3) helps with avoiding any unintended changes to log files.",
            },
            {
                "ChoiceId": "sec_sec_q4_a4",
                "Title": "Enable CloudTrail log file integrity validation",
                "Description": "A validated log file using integrity validation enables you to assert positively that the log file itself has not changed.",
            },
            {
                "ChoiceId": "sec_sec_q4_a5",
                "Title": "Configure centralized threat detection for AWS accounts, workloads, and data",
                "Description": "Configure threat detection, such as Amazon GuardDuty, that monitors for malicious activity and unauthorized behavior to protect your AWS accounts, workloads, and data.",
            },
            {
                "ChoiceId": "sec_sec_q4_a6",
                "Title": "Configure Amazon VPC Flow Logs",
                "Description": "VPC Flow Logs enables you to capture information about the IP traffic going to and from network interfaces in your VPC.",
            },
            {
                "ChoiceId": "sec_sec_q4_a7",
                "Title": "Configure Amazon S3 access logging",
                "Description": "Server access logging provides detailed records for the requests that are made to a bucket.",
            },
            {
                "ChoiceId": "sec_sec_q4_a8",
                "Title": "Configure AWS Config",
                "Description": "AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This view includes how the resources are related to one another and how they were previously configured so that you can see how the configurations and relationships have changed over time.",
            },
            {
                "ChoiceId": "sec_sec_q4_a9",
                "Title": "Store logs in central account with limited access",
                "Description": "Configure logs to flow to a central account, and protect the logs from manipulation or deletion.",
            },
            {
                "ChoiceId": "sec_sec_q4_a1",
                "Title": "Configure AWS Security Hub foundational best practices",
                "Description": "The AWS Foundational Security Best Practices standard is a set of controls that detect when your accounts and resources deviate from security best practices.",
            },
            {"ChoiceId": "sec_sec_q4_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "sec_q5",
        "PillarId": "security",
        "QuestionTitle": "How are you alerting on foundational events?",
        "Choices": [
            {
                "ChoiceId": "sec_sec_q5_a1",
                "Title": "People are notified to take action on critical events",
                "Description": "Ensure that someone with the ability to take action receives notifications from alerts automatically.",
            },
            {
                "ChoiceId": "sec_sec_q5_a2",
                "Title": "Alerts create a ticket or task that is tracked",
                "Description": "Alerts from all sources, such as from GuardDuty, automatically create a ticket or task in your management system that allows for tracking and recording a history of events. Automatically creating trouble tickets is the best way to ensure that GuardDuty findings are integrated with your operational processes.",
            },
            {
                "ChoiceId": "sec_sec_q5_a3",
                "Title": "Events are escalated",
                "Description": "Events must be escalated if the person or team responsible for investigating is unresponsive or unable to resolve the problem.",
            },
            {"ChoiceId": "sec_sec_q5_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "sec_q6",
        "PillarId": "security",
        "QuestionTitle": "How do you manage vulnerabilities?",
        "Choices": [
            {
                "ChoiceId": "sec_sec_q6_a1",
                "Title": "Patch EC2 operating systems automatically",
                "Description": "Use an automated patch management solution, such as AWS Systems Manager Patch Manager, to automate the patching process of all systems and code for which you are responsible, including your operating system, applications, and code dependencies.",
            },
            {
                "ChoiceId": "sec_sec_q6_a2",
                "Title": "Scan source code libraries and dependencies",
                "Description": "Frequently scan and patch for bugs in your code and dependencies to help protect against new security issues.",
            },
            {
                "ChoiceId": "sec_sec_q6_a3",
                "Title": "Scan infrastructure",
                "Description": "Frequently scan your infrastructure for misconfigurations and bugs to help protect against new security issues.",
            },
            {"ChoiceId": "sec_sec_q6_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "sec_q7",
        "PillarId": "security",
        "QuestionTitle": "How do you configure your network protection?",
        "Choices": [
            {
                "ChoiceId": "sec_sec_q7_a1",
                "Title": "Implement distributed denial of service (DDoS) protection",
                "Description": "Protecting your internet facing resources, such as web applications, from a DDoS attempt helps maintain availability to users.",
            },
            {
                "ChoiceId": "sec_sec_q7_a2",
                "Title": "VPC security groups restrict inbound and outbound traffic",
                "Description": "Use security groups for controlling inbound and outbound traffic, and automatically apply rules for both security groups and Web Application Firewall (WAF) using AWS Firewall Manager.",
            },
            {
                "ChoiceId": "sec_sec_q7_a3",
                "Title": "Configure subnets to create layers",
                "Description": "Group components that share reachability requirements into layers. For example, a database cluster in a VPC with no need for internet access should be placed in subnets with no route to or from the internet.",
            },
            {
                "ChoiceId": "sec_sec_q7_a4",
                "Title": "Periodically review unrestricted security groups",
                "Description": "Unrestricted security groups, which allow access from the internet for any network, expose your workload to unnecessary risk. They should only be used when absolutely necessary, for example to allow HTTPS (TCP 443) to an Elastic Load Balancer with AWS WAF enabled.",
            },
            {"ChoiceId": "sec_sec_q7_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "sec_q8",
        "PillarId": "security",
        "QuestionTitle": "How do you protect sensitive data at rest?",
        "Choices": [
            {
                "ChoiceId": "sec_sec_q8_a1",
                "Title": "Identify sensitive data",
                "Description": "Identify sensitive data, such as Personally Identifiable Information (PII), that you are storing in your workload.",
            },
            {
                "ChoiceId": "sec_sec_q8_a2",
                "Title": "Encrypt all sensitive data at rest",
                "Description": "All data that you have identified or classified as sensitive must be encrypted at rest. Encryption maintains the confidentiality of sensitive data even when it gets misplaced. Encryption can be enabled in AWS services, or client-side. ",
            },
            {
                "ChoiceId": "sec_sec_q8_a3",
                "Title": "Log access to sensitive data comprehensively throughout the system",
                "Description": "Visibility into any unexpected access to sensitive data provides you with the opportunity to perform necessary corrective actions to further protect your data.",
            },
            {
                "ChoiceId": "sec_sec_q8_a4",
                "Title": "Manage encryption keys with AWS Key Management Service",
                "Description": "AWS Key Management Service (AWS KMS) should be used to protect data at rest across AWS services and your applications where possible. Use different keys, and access control to the keys, combined with the AWS IAM and resource policies, to align with data classification levels and segregation requirements.",
            },
            {
                "ChoiceId": "sec_sec_q8_a5",
                "Title": "Review permissions of all Amazon S3 buckets",
                "Description": "Review S3 bucket and object permissions:Regularly review the level of access granted in Amazon S3 bucket policies, and grant read or write permissions for those buckets based on least privilege. Use AWS Config to detect buckets that are publicly available and Amazon CloudFront to serve content from Amazon S3.",
            },
            {
                "ChoiceId": "sec_sec_q8_a6",
                "Title": "Enable default encryption for Amazon S3 Buckets",
                "Description": "Amazon S3 bucket encryption helps maintain the confidentiality of your data.",
            },
            {
                "ChoiceId": "sec_sec_q8_a7",
                "Title": "Enable default encryption for Amazon EBS volumes",
                "Description": "Amazon EBS volume encryption helps maintain the confidentiality of your data.",
            },
            {
                "ChoiceId": "sec_sec_q8_a8",
                "Title": "Periodically review shared data",
                "Description": "Assessing shared data periodically allows you to identify and implement necessary changes to data access policies. This minimizes the risk that you are exposing sensitive data to unintended users.",
            },
            {"ChoiceId": "sec_sec_q8_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "sec_q9",
        "PillarId": "security",
        "QuestionTitle": "How are you protecting sensitive data in transit?",
        "Choices": [
            {
                "ChoiceId": "sec_sec_q9_a1",
                "Title": "Manage certificates centrally with Certificate Manager",
                "Description": "AWS Certificate Manager lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services.",
            },
            {
                "ChoiceId": "sec_sec_q9_a2",
                "Title": "Only use protocols with encryption",
                "Description": "Enable encryption for all network traffic, including Transport Layer Security (TLS) for web-based network infrastructure you control.",
            },
            {
                "ChoiceId": "sec_sec_q9_a3",
                "Title": "Block or redirect insecure protocols",
                "Description": "Secure protocols keep your data protected in transit. ",
            },
            {"ChoiceId": "sec_sec_q9_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "sec_q10",
        "PillarId": "security",
        "QuestionTitle": "How have you prepared for a security event?",
        "Choices": [
            {
                "ChoiceId": "sec_sec_q10_a1",
                "Title": "Create an incident response (IR) runbook for root account credential misuse",
                "Description": "Begin your IR planning by building a runbook that will help you if your root account credentials are ever misused.",
            },
            {
                "ChoiceId": "sec_sec_q10_a2",
                "Title": "Practice responding to events",
                "Description": "Simulate and practice incident response by running game days, incorporating the lessons learned into your incident management plans, and continuously improving them.",
            },
            {
                "ChoiceId": "sec_sec_q10_a3",
                "Title": "Create roles for incident responders",
                "Description": "Ensure that incident responders have the correct access pre-provisioned in AWS to reduce the time for investigation through to recovery.",
            },
            {"ChoiceId": "sec_sec_q10_no", "Title": "None of these", "Description": ""},
        ],
    },
]
