WELLARCHITECTED = [
    {
        "QuestionId": "cloud-financial-management",
        "PillarId": "costOptimization",
        "QuestionTitle": "How do you implement cloud financial management?",
        "Choices": [
            {
                "ChoiceId": "cost_cloud_financial_management_function",
                "Title": "Establish a cost optimization function",
                "Description": "Create a team that is responsible for establishing and\n                 maintaining cost awareness across your organization. The team requires people from finance,\n                 technology, and business roles across the organization.\n\t\t      ",
            },
            {
                "ChoiceId": "cost_cloud_financial_management_partnership",
                "Title": "Establish a partnership between finance and technology",
                "Description": "Involve finance and technology teams in cost\n                    and usage discussions at all stages of your cloud journey. Teams regularly meet and discuss topics such\n                    as organizational goals and targets, current state of cost and usage, and financial and accounting\n                    practices.\n                ",
            },
            {
                "ChoiceId": "cost_cloud_financial_management_budget_forecast",
                "Title": "Establish cloud budgets and forecasts",
                "Description": "Adjust existing organizational budgeting and forecasting\n                    processes to be compatible with the highly variable nature of cloud costs and usage. Processes must be\n                    dynamic using trend based or business driver-based algorithms, or a combination.\n                ",
            },
            {
                "ChoiceId": "cost_cloud_financial_management_cost_awareness",
                "Title": "Implement cost awareness in your organizational processes",
                "Description": "Implement cost awareness into new or\n                    existing processes that impact usage, and leverage existing processes for cost awareness. Implement\n                    cost awareness into employee training.\n                ",
            },
            {
                "ChoiceId": "cost_cloud_financial_management_usage_report",
                "Title": "Report and notify on cost optimization",
                "Description": "Configure AWS Budgets to provide notifications on cost and\n                    usage against targets. Have regular meetings to analyze this workload's cost efficiency and to promote\n                    cost aware culture.",
            },
            {
                "ChoiceId": "cost_cloud_financial_management_proactive_process",
                "Title": "Monitor cost proactively",
                "Description": "Implement tooling and dashboards to monitor cost proactively for the\n                    workload. Do not just look at costs and categories when you receive notifications. This helps to identify\n                    positive trends and promote them throughout your organization.",
            },
            {
                "ChoiceId": "cost_cloud_financial_management_scheduled",
                "Title": "Keep up to date with new service releases",
                "Description": "Consult regularly with experts or APN Partners to consider\n                    which services and features provide lower cost. Review AWS blogs and other information sources.\n                ",
            },
            {
                "ChoiceId": "cost_cloud_financial_management_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "govern-usage",
        "PillarId": "costOptimization",
        "QuestionTitle": "How do you govern usage?",
        "Choices": [
            {
                "ChoiceId": "cost_govern_usage_policies",
                "Title": "Develop policies based on your organization requirements",
                "Description": "Develop policies that define how resources\n               are managed by your organization. Policies should cover cost aspects of resources and workloads,\n               including creation, modification and decommission over the resource lifetime.\n\t\t\t   ",
            },
            {
                "ChoiceId": "cost_govern_usage_goal_target",
                "Title": "Implement goals and targets",
                "Description": "Implement both cost and usage goals for your workload. Goals provide\n               direction to your organization on cost and usage, and targets provide measurable outcomes for your\n               workloads.\n            ",
            },
            {
                "ChoiceId": "cost_govern_usage_account_structure",
                "Title": "Implement an account structure",
                "Description": "Implement a structure of accounts that maps to your organization. This assists in allocating and\n\t\t\t\tmanaging costs throughout your organization.",
            },
            {
                "ChoiceId": "cost_govern_usage_groups_roles",
                "Title": "Implement groups and roles",
                "Description": "Implement groups and roles that align to your policies and control who\n               can create, modify, or decommission instances and resources in each group. For example, implement\n               development, test, and production groups. This applies to AWS services and third-party solutions.",
            },
            {
                "ChoiceId": "cost_govern_usage_controls",
                "Title": "Implement cost controls",
                "Description": "Implement controls based on organization policies and defined groups and\n               roles. These ensure that costs are only incurred as defined by organization requirements: for example,\n               control access to regions or resource types with IAM policies.",
            },
            {
                "ChoiceId": "cost_govern_usage_track_lifecycle",
                "Title": "Track project lifecycle",
                "Description": "Track, measure, and audit the lifecycle of projects, teams, and environments to\n               avoid using and paying for unnecessary resources.",
            },
            {
                "ChoiceId": "cost_govern_usage_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "monitor-usage",
        "PillarId": "costOptimization",
        "QuestionTitle": "How do you monitor usage and cost?",
        "Choices": [
            {
                "ChoiceId": "cost_monitor_usage_detailed_source",
                "Title": "Configure detailed information sources",
                "Description": "Configure the AWS Cost and Usage Report, and Cost Explorer\n               hourly granularity, to provide detailed cost and usage information. Configure your workload to have log\n               entries for every delivered business outcome.",
            },
            {
                "ChoiceId": "cost_monitor_usage_define_attribution",
                "Title": "Identify cost attribution categories",
                "Description": "Identify organization categories that could be used to allocate cost\n               within your organization.",
            },
            {
                "ChoiceId": "cost_monitor_usage_define_kpi",
                "Title": "Establish organization metrics",
                "Description": "Establish the organization metrics that are required for this workload.\n               Example metrics of a workload are customer reports produced or web pages served to customers.",
            },
            {
                "ChoiceId": "cost_monitor_usage_config_tools",
                "Title": "Configure billing and cost management tools",
                "Description": "Configure AWS Cost Explorer and AWS Budgets inline\n               with your organization policies.",
            },
            {
                "ChoiceId": "cost_monitor_usage_org_information",
                "Title": "Add organization information to cost and usage",
                "Description": "Define a tagging schema based on organization, and\n               workload attributes, and cost allocation categories. Implement tagging across all resources. Use Cost\n               Categories to group costs and usage according to organization attributes.",
            },
            {
                "ChoiceId": "cost_monitor_usage_allocate_outcome",
                "Title": "Allocate costs based on workload metrics",
                "Description": "Allocate the workload's costs by metrics or business\n               outcomes to measure workload cost efficiency. Implement a process to analyze the AWS Cost and Usage\n               Report with Amazon Athena, which can provide insight and charge back capability.",
            },
            {
                "ChoiceId": "cost_monitor_usage_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "decomissioning-resources",
        "PillarId": "costOptimization",
        "QuestionTitle": "How do you decommission resources?",
        "Choices": [
            {
                "ChoiceId": "cost_decomissioning_resources_track",
                "Title": "Track resources over their life time",
                "Description": "Define and implement a method to track resources and their\n               associations with systems over their life time. You can use tagging to identify the workload or function\n               of the resource.",
            },
            {
                "ChoiceId": "cost_decomissioning_resources_implement_process",
                "Title": "Implement a decommissioning process",
                "Description": "Implement a process to identify and decommission orphaned\n               resources.",
            },
            {
                "ChoiceId": "cost_decomissioning_resources_decommission",
                "Title": "Decommission resources",
                "Description": "Decommission resources triggered by events such as periodic audits, or\n               changes in usage. Decommissioning is typically performed periodically, and is manual or automated.",
            },
            {
                "ChoiceId": "cost_decomissioning_resources_decomm_automated",
                "Title": "Decommission resources automatically",
                "Description": "Design your workload to gracefully handle resource\n               termination as you identify and decommission non-critical resources, resources that are not required, or\n               resources with low utilization.",
            },
            {
                "ChoiceId": "cost_decomissioning_resources_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "select-service",
        "PillarId": "costOptimization",
        "QuestionTitle": "How do you evaluate cost when you select services?",
        "Choices": [
            {
                "ChoiceId": "cost_select_service_requirements",
                "Title": "Identify organization requirements for cost",
                "Description": "Work with team members to define the balance between\n               cost optimization and other pillars, such as performance and reliability, for this workload.",
            },
            {
                "ChoiceId": "cost_select_service_analyze_all",
                "Title": "Analyze all components of this workload",
                "Description": "Ensure every workload component is analyzed, regardless of\n               current size or current costs. Review effort should reflect potential benefit, such as current and\n               projected costs.",
            },
            {
                "ChoiceId": "cost_select_service_thorough_analysis",
                "Title": "Perform a thorough analysis of each component",
                "Description": "Look at overall cost to the organization of each\n               component. Look at total cost of ownership by factoring in cost of operations and management,\n               especially when using managed services. Review effort should reflect potential benefit: for example,\n               time spent analyzing is proportional to component cost.\n\t\t\t\t",
            },
            {
                "ChoiceId": "cost_select_service_licensing",
                "Title": "Select software with cost effective licensing",
                "Description": "Open source software will eliminate software licensing\n               costs, which can contribute significant costs to workloads. Where licensed software is required, avoid\n               licenses bound to arbitrary attributes such as CPUs, look for licenses that are bound to output or\n               outcomes. The cost of these licenses scales more closely to the benefit they provide.\n            ",
            },
            {
                "ChoiceId": "cost_select_service_select_for_cost",
                "Title": "Select components of this workload to optimize cost in line with organization priorities",
                "Description": "Factor in cost\n               when selecting all components. This includes using application level and managed services, such as\n               Amazon RDS, Amazon DynamoDB, Amazon SNS, and Amazon SES to reduce overall organization cost.\n               Use serverless and containers for compute, such as AWS Lambda, Amazon S3 for static websites, and\n               Amazon ECS. Minimize license costs by using open source software, or software that does not have\n               license fees: for example, Amazon Linux for compute workloads or migrate databases to Amazon\n               Aurora.",
            },
            {
                "ChoiceId": "cost_select_service_analyze_over_time",
                "Title": "Perform cost analysis for different usage over time",
                "Description": "Workloads can change over time. Some services or\n               features are more cost effective at different usage levels. By performing the analysis on each\n               component over time and at projected usage, you ensure the workload remains cost effective over its\n               lifetime..",
            },
            {
                "ChoiceId": "cost_select_service_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "type-size-number-resources",
        "PillarId": "costOptimization",
        "QuestionTitle": "How do you meet cost targets when you select resource type, size and number?",
        "Choices": [
            {
                "ChoiceId": "cost_type_size_number_resources_cost_modeling",
                "Title": "Perform cost modeling",
                "Description": "Identify organization requirements and perform cost modeling of the workload\n               and each of its components. Perform benchmark activities for the workload under different predicted\n               loads and compare the costs. The modeling effort should reflect potential benefit: for example, time\n               spent is proportional to component cost.\n\t\t\t\t",
            },
            {
                "ChoiceId": "cost_type_size_number_resources_data",
                "Title": "Select resource type and size based on data",
                "Description": "Select resource size or type based on data about the\n               workload and resource characteristics: for example, compute, memory, throughput, or write intensive.\n               This selection is typically made using a previous version of the workload (such as an on-premises\n               version), using documentation, or using other sources of information about the workload.",
            },
            {
                "ChoiceId": "cost_type_size_number_resources_metrics",
                "Title": "Select resource type and size automatically based on metrics",
                "Description": "Use metrics from the currently running\n               workload to select the right size and type to optimize for cost. Appropriately provision throughput,\n               sizing, and storage for services such as Amazon EC2, Amazon DynamoDB, Amazon EBS (PIOPS), Amazon\n               RDS, Amazon EMR, and networking. This can be done with a feedback loop such as automatic scaling or\n               by custom code in the workload.",
            },
            {
                "ChoiceId": "cost_type_size_number_resources_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "pricing-model",
        "PillarId": "costOptimization",
        "QuestionTitle": "How do you use pricing models to reduce cost?",
        "Choices": [
            {
                "ChoiceId": "cost_pricing_model_analysis",
                "Title": "Perform pricing model analysis",
                "Description": "Analyze each component of the workload. Determine if the component\n               and resources will be running for extended periods (for commitment discounts), or dynamic and short\n               running (for spot or on-demand). Perform an analysis on the workload using the Recommendations\n               feature in AWS Cost Explorer.",
            },
            {
                "ChoiceId": "cost_pricing_model_region_cost",
                "Title": "Implement regions based on cost",
                "Description": "Resource pricing can be different in each region. Factoring in region\n               cost ensures you pay the lowest overall price for this workload",
            },
            {
                "ChoiceId": "cost_pricing_model_third_party",
                "Title": "Select third party agreements with cost efficient terms",
                "Description": "Cost efficient agreements and terms ensure the\n               cost of these services scales with the benefits they provide. Select agreements and pricing that scale\n               when they provide additional benefits to your organization.\n            ",
            },
            {
                "ChoiceId": "cost_pricing_model_implement_models",
                "Title": "Implement pricing models for all components of this workload",
                "Description": "Permanently running resources should\n               utilize reserved capacity such as Savings Plans or reserved Instances. Short term capacity is configured to\n               use Spot Instances, or Spot Fleet. On demand is only used for short-term workloads that cannot be\n               interrupted and do not run long enough for reserved capacity, between 25% to 75% of the period,\n               depending on the resource type.\n\t\t\t\t",
            },
            {
                "ChoiceId": "cost_pricing_model_master_analysis",
                "Title": "Perform pricing model analysis at the master account level",
                "Description": "Use Cost Explorer Savings Plans and\n               Reserved Instance recommendations to perform regular analysis at the master account level for\n               commitment discounts.\n            ",
            },
            {
                "ChoiceId": "cost_pricing_model_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "data-transfer",
        "PillarId": "costOptimization",
        "QuestionTitle": "How do you plan for data transfer charges?",
        "Choices": [
            {
                "ChoiceId": "cost_data_transfer_modeling",
                "Title": "Perform data transfer modeling",
                "Description": "Gather organization requirements and perform data transfer modeling\n               of the workload and each of its components. This identifies the lowest cost point for its current data\n               transfer requirements.",
            },
            {
                "ChoiceId": "cost_data_transfer_optimized_components",
                "Title": "Select components to optimize data transfer cost",
                "Description": "All components are selected, and architecture is\n               designed to reduce data transfer costs. This includes using components such as WAN optimization and\n               Multi-AZ configurations",
            },
            {
                "ChoiceId": "cost_data_transfer_implement_services",
                "Title": "Implement services to reduce data transfer costs",
                "Description": "Implement services to reduce data transfer: for\n               example, using a CDN such as Amazon CloudFront to deliver content to end users, caching layers using\n               Amazon ElastiCache, or using AWS Direct Connect instead of VPN for connectivity to AWS.",
            },
            {
                "ChoiceId": "cost_data_transfer_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "manage-demand-resources",
        "PillarId": "costOptimization",
        "QuestionTitle": "How do you manage demand, and supply resources?",
        "Choices": [
            {
                "ChoiceId": "cost_manage_demand_resources_cost_analysis",
                "Title": "Perform an analysis on the workload demand",
                "Description": "Analyze the demand of the workload over time. Ensure\n               the analysis covers seasonal trends and accurately represents operating conditions over the full\n               workload lifetime. Analysis effort should reflect potential benefit: for example, time spent is\n               proportional to the workload cost.",
            },
            {
                "ChoiceId": "cost_manage_demand_resources_buffer_throttle",
                "Title": "Implement a buffer or throttle to manage demand",
                "Description": "Buffering and throttling modify the demand on\n               your workload, smoothing out any peaks. Implement throttling when your clients perform retries.\n               Implement buffering to store the request and defer processing until a later time. Ensure your throttles\n               and buffers are designed so clients receive a response in the required time.\n            ",
            },
            {
                "ChoiceId": "cost_manage_demand_resources_dynamic",
                "Title": "Supply resources dynamically",
                "Description": "Resources are provisioned in a planned manner. This can be demand-\n               based, such as through automatic scaling, or time-based, where demand is predictable and resources\n               are provided based on time. These methods result in the least amount of over or under provisioning.",
            },
            {
                "ChoiceId": "cost_manage_demand_resources_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "evaluate-new-services",
        "PillarId": "costOptimization",
        "QuestionTitle": "How do you evaluate new services?",
        "Choices": [
            {
                "ChoiceId": "cost_evaluate_new_services_review_process",
                "Title": "Develop a workload review process",
                "Description": "Develop a process that defines the criteria and process for\n               workload review. The review effort should reflect potential benefit: for example, core workloads or\n               workloads with a value of over 10% of the bill are reviewed quarterly, while workloads below 10% are\n               reviewed annually.",
            },
            {
                "ChoiceId": "cost_evaluate_new_services_review_workload",
                "Title": "Review and analyze this workload regularly",
                "Description": "Existing workloads are regularly reviewed as per defined\n               processes.",
            },
            {
                "ChoiceId": "cost_evaluate_new_services_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "priorities",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How do you determine what your priorities are?",
        "Choices": [
            {
                "ChoiceId": "ops_priorities_ext_cust_needs",
                "Title": "Evaluate external customer needs",
                "Description": "\n               Involve key stakeholders, including business, development, and operations teams, to determine where to focus efforts on external customer needs.\n               This will ensure that you have a thorough understanding of the operations support that is required to achieve your desired business outcomes.\n            ",
            },
            {
                "ChoiceId": "ops_priorities_int_cust_needs",
                "Title": "Evaluate internal customer needs",
                "Description": "\n               Involve key stakeholders, including business, development, and operations teams, when determining where to focus efforts on internal customer needs.\n               This will ensure that you have a thorough understanding of the operations support that is required to achieve business outcomes.\n            ",
            },
            {
                "ChoiceId": "ops_priorities_governance_reqs",
                "Title": "Evaluate governance requirements",
                "Description": "\n               Ensure that you are aware of guidelines or obligations defined by your organization that may mandate or emphasize specific focus. Evaluate internal factors, such as organization policy, standards, and requirements. Validate that you have mechanisms to identify changes to governance. If no governance requirements are identified, ensure that you have applied due diligence to this determination.\n            ",
            },
            {
                "ChoiceId": "ops_priorities_compliance_reqs",
                "Title": "Evaluate compliance requirements",
                "Description": "\n               Evaluate external factors, such as regulatory compliance requirements and industry standards, \n               to ensure that you are aware of guidelines or obligations that may mandate or emphasize specific focus.\n               If no compliance requirements are identified, ensure that you apply due diligence to this determination.\n            ",
            },
            {
                "ChoiceId": "ops_priorities_eval_threat_landscape",
                "Title": "Evaluate threat landscape",
                "Description": "\n               Evaluate threats to the business (for example, competition, business risk and liabilities, operational risks, and information security threats) and maintain current information in a risk registry. Include the impact of risks when determining where to focus efforts.\n            ",
            },
            {
                "ChoiceId": "ops_priorities_eval_tradeoffs",
                "Title": "Evaluate tradeoffs",
                "Description": "\n               Evaluate the impact of tradeoffs between competing interests or alternative approaches, to help make informed decisions when determining where to focus efforts or choosing a course of action. For example, accelerating speed to market for new features may be emphasized over cost optimization, or you may choose a relational database for non-relational data to simplify the effort to migrate a system, rather than migrating to a database optimized for your data type and updating your application.\n            ",
            },
            {
                "ChoiceId": "ops_priorities_manage_risk_benefit",
                "Title": "Manage benefits and risks",
                "Description": "\n               Manage benefits and risks to make informed decisions when determining where to focus efforts. For example, it may be beneficial to deploy a workload with unresolved issues so that significant new features can be made available to customers. It may be possible to mitigate associated risks, or it may become unacceptable to allow a risk to remain, in which case you will take action to address the risk.\n            ",
            },
            {
                "ChoiceId": "ops_priorities_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "ops-model",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How do you structure your organization to support your business outcomes?",
        "Choices": [
            {
                "ChoiceId": "ops_ops_model_def_resource_owners",
                "Title": "Resources have identified owners",
                "Description": "\n               Understand who has ownership of each application, workload, platform, and infrastructure component, what business value is provided by that component, and why that ownership exists. Understanding the business value of these individual components and how they support business outcomes informs the processes and procedures applied against them.\n            ",
            },
            {
                "ChoiceId": "ops_ops_model_def_proc_owners",
                "Title": "Processes and procedures have identified owners",
                "Description": "\n               Understand who has ownership of the definition of individual processes and procedures, why those specific process and procedures are used, and why that ownership exists. Understanding the reasons that specific processes and procedures are used enables identification of improvement opportunities. \n            ",
            },
            {
                "ChoiceId": "ops_ops_model_def_activity_owners",
                "Title": "Operations activities have identified owners responsible for their performance",
                "Description": "\n               Understand who has responsibility to perform specific activities on defined workloads and why that responsibility exists. Understanding who has responsibility to perform activities informs who will conduct the activity, validate the result, and provide feedback to the owner of the activity.\n            ",
            },
            {
                "ChoiceId": "ops_ops_model_know_my_job",
                "Title": "Team members know what they are responsible for",
                "Description": "\n               Understanding the responsibilities of your role and how you contribute to business outcomes informs the prioritization of your tasks and why your role is important. This enables team members to recognize needs and respond appropriately.\n            ",
            },
            {
                "ChoiceId": "ops_ops_model_find_owner",
                "Title": "Mechanisms exist to identify responsibility and ownership",
                "Description": "\n               Where no individual or team is identified, there are defined escalation paths to someone with the authority to assign ownership or plan for that need to be addressed.\n            ",
            },
            {
                "ChoiceId": "ops_ops_model_req_add_chg_exception",
                "Title": "Mechanisms exist to request additions, changes, and exceptions",
                "Description": "\n               You are able to make requests to owners of processes, procedures, and resources. Make informed decisions to approve requests where viable and determined to be appropriate after an evaluation of benefits and risks.\n            ",
            },
            {
                "ChoiceId": "ops_ops_model_def_neg_team_agreements",
                "Title": "Responsibilities between teams are predefined or negotiated",
                "Description": "\n               There are defined or negotiated agreements between teams describing how they work with and support each other (for example, response times, service level objectives, or service level agreements). Understanding the impact of the teams’ work on business outcomes, and the outcomes of other teams and organizations, informs the prioritization of their tasks and enables them to respond appropriately.\n            ",
            },
            {"ChoiceId": "ops_ops_model_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "org-culture",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How does your organizational culture support your business outcomes?",
        "Choices": [
            {
                "ChoiceId": "ops_org_culture_executive_sponsor",
                "Title": "Executive Sponsorship",
                "Description": "\n               Senior leadership clearly sets expectations for the organization and evaluates success. Senior leadership is the sponsor, advocate, and driver for the adoption of best practices and evolution of the organization\n            ",
            },
            {
                "ChoiceId": "ops_org_culture_team_emp_take_action",
                "Title": "Team members are empowered to take action when outcomes are at risk",
                "Description": "\n               The workload owner has defined guidance and scope empowering team members to respond when outcomes are at risk. Escalation mechanisms are used to get direction when events are outside of the defined scope.\n            ",
            },
            {
                "ChoiceId": "ops_org_culture_team_enc_escalation",
                "Title": "Escalation is encouraged",
                "Description": "\n               Team members have mechanisms and are encouraged to escalate concerns to decision makers and stakeholders if they believe outcomes are at risk. Escalation should be performed early and often so that risks can be identified, and prevented from causing incidents.\n            ",
            },
            {
                "ChoiceId": "ops_org_culture_effective_comms",
                "Title": "Communications are timely, clear, and actionable",
                "Description": "\n               Mechanisms exist and are used to provide timely notice to team members of known risks and planned events. Necessary context, details, and time (when possible) are provided to support determining if action is necessary, what action is required, and to take action in a timely manner. For example, providing notice of software vulnerabilities so that patching can be expedited, or providing notice of planned sales promotions so that a change freeze can be implemented to avoid the risk of service disruption.\n            ",
            },
            {
                "ChoiceId": "ops_org_culture_team_enc_experiment",
                "Title": "Experimentation is encouraged",
                "Description": "\n               Experimentation accelerates learning and keeps team members interested and engaged. An undesired result is a successful experiment that has identified a path that will not lead to success. Team members are not punished for successful experiments with undesired results. Experimentation is required for innovation to happen and turn ideas into outcomes.\n            ",
            },
            {
                "ChoiceId": "ops_org_culture_team_enc_learn",
                "Title": "Team members are enabled and encouraged to maintain and grow their skill sets",
                "Description": "\n               Teams must grow their skill sets to adopt new technologies, and to support changes in demand and responsibilities in support of your workloads. Growth of skills in new technologies is frequently a source of team member satisfaction and supports innovation. Support your team members’ pursuit and maintenance of industry certifications that validate and acknowledge their growing skills. Cross train to promote knowledge transfer and reduce the risk of significant impact when you lose skilled and experienced team members with institutional knowledge. Provide dedicated structured time for learning.\n            ",
            },
            {
                "ChoiceId": "ops_org_culture_team_res_appro",
                "Title": "Resource teams appropriately",
                "Description": "\n               Maintain team member capacity, and provide tools and resources, to support your workload needs. Overtasking team members increases the risk of incidents resulting from human error. Investments in tools and resources (for example, providing automation for frequently executed activities) can scale the effectiveness of your team, enabling them to support additional activities.\n            ",
            },
            {
                "ChoiceId": "ops_org_culture_diverse_inc_access",
                "Title": "Diverse opinions are encouraged and sought within and across teams",
                "Description": "\n               Leverage cross-organizational diversity to seek multiple unique perspectives. Use this perspective to increase innovation, challenge your assumptions, and reduce the risk of confirmation bias. Grow inclusion, diversity, and accessibility within your teams to gain beneficial perspectives.\n            ",
            },
            {
                "ChoiceId": "ops_org_culture_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "telemetry",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How do you design your workload so that you can understand its state?",
        "Choices": [
            {
                "ChoiceId": "ops_telemetry_application_telemetry",
                "Title": "Implement application telemetry",
                "Description": "\n               Instrument your application code to emit information about its internal state, status, and achievement of business outcomes. For example, queue depth, error messages, and response times. Use this information to determine when a response is required.\n            ",
            },
            {
                "ChoiceId": "ops_telemetry_workload_telemetry",
                "Title": "Implement and configure workload telemetry",
                "Description": "\n               Design and configure your workload to emit information about its internal state and current status. For example, API call volume, HTTP status codes, and scaling events. Use this information to help determine when a response is required.\n            ",
            },
            {
                "ChoiceId": "ops_telemetry_customer_telemetry",
                "Title": "Implement user activity telemetry",
                "Description": "\n               Instrument your application code to emit information about user activity, for example, click streams, or started, abandoned, and completed transactions. Use this information to help understand how the application is used, patterns of usage, and to determine when a response is required.\n            ",
            },
            {
                "ChoiceId": "ops_telemetry_dependency_telemetry",
                "Title": "Implement dependency telemetry",
                "Description": "\n               Design and configure your workload to emit information about the status (for example, reachability or response time) of resources it depends on. Examples of external dependencies can include, external databases, DNS, and network connectivity. Use this information to determine when a response is required.\n            ",
            },
            {
                "ChoiceId": "ops_telemetry_dist_trace",
                "Title": "Implement transaction traceability",
                "Description": "\n               Implement your application code and configure your workload components to emit information about the flow of transactions across the workload. Use this information to determine when a response is required and to assist you in identifying the factors contributing to an issue.\n            ",
            },
            {"ChoiceId": "ops_telemetry_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "dev-integ",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How do you reduce defects, ease remediation, and improve flow into production?",
        "Choices": [
            {
                "ChoiceId": "ops_dev_integ_version_control",
                "Title": "Use version control",
                "Description": "\n               Use version control to enable tracking of changes and releases.\n            ",
            },
            {
                "ChoiceId": "ops_dev_integ_test_val_chg",
                "Title": "Test and validate changes",
                "Description": "\n               Test and validate changes to help limit and detect errors.\n               Automate testing to reduce errors caused by manual processes, and reduce the level of effort to test.\n            ",
            },
            {
                "ChoiceId": "ops_dev_integ_conf_mgmt_sys",
                "Title": "Use configuration management systems",
                "Description": "\n               Use configuration management systems to make and track configuration changes. \n               These systems reduce errors caused by manual processes and reduce the level of effort to deploy changes. \n            ",
            },
            {
                "ChoiceId": "ops_dev_integ_build_mgmt_sys",
                "Title": "Use build and deployment management systems",
                "Description": "\n               Use build and deployment management systems.\n               These systems reduce errors caused by manual processes and reduce the level of effort to deploy changes. \n            ",
            },
            {
                "ChoiceId": "ops_dev_integ_patch_mgmt",
                "Title": "Perform patch management",
                "Description": "\n               Perform patch management to gain features, address issues, and remain compliant with governance. \n               Automate patch management to reduce errors caused by manual processes, and reduce the level of effort to patch.\n            ",
            },
            {
                "ChoiceId": "ops_dev_integ_share_design_stds",
                "Title": "Share design standards",
                "Description": "\n               Share best practices across teams \n               to increase awareness \n               and maximize the benefits of development efforts.\n            ",
            },
            {
                "ChoiceId": "ops_dev_integ_code_quality",
                "Title": "Implement practices to improve code quality",
                "Description": "\n               Implement practices \n               to improve code quality \n               and minimize defects. \n               For example, test-driven development, code reviews, and standards adoption.\n            ",
            },
            {
                "ChoiceId": "ops_dev_integ_multi_env",
                "Title": "Use multiple environments",
                "Description": "\n               Use multiple environments to experiment, develop, and test your workload. Use increasing levels of controls as environments approach production to gain confidence your workload will operate as intended when deployed.\n            ",
            },
            {
                "ChoiceId": "ops_dev_integ_freq_sm_rev_chg",
                "Title": "Make frequent, small, reversible changes",
                "Description": "\n               Frequent, small, and reversible changes reduce the scope and impact of a change.\n               This eases troubleshooting, enables faster remediation, and provides the option to roll back a change.\n            ",
            },
            {
                "ChoiceId": "ops_dev_integ_auto_integ_deploy",
                "Title": "Fully automate integration and deployment",
                "Description": "\n               Automate build, deployment, and testing of the workload. \n               This reduces errors caused by manual processes and reduces the effort to deploy changes.\n            ",
            },
            {"ChoiceId": "ops_dev_integ_no", "Title": "None of these", "Description": ""},
        ],
    },
    {
        "QuestionId": "mit-deploy-risks",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How do you mitigate deployment risks?",
        "Choices": [
            {
                "ChoiceId": "ops_mit_deploy_risks_plan_for_unsucessful_changes",
                "Title": "Plan for unsuccessful changes",
                "Description": "\n               Plan to revert to a known good state, \n               or remediate in the production environment \n               if a change does not have the desired outcome.\n               This preparation reduces recovery time through faster responses.\n            ",
            },
            {
                "ChoiceId": "ops_mit_deploy_risks_test_val_chg",
                "Title": "Test and validate changes",
                "Description": "\n               Test changes and validate the results at all lifecycle stages to confirm new features and minimize the risk and impact of failed deployments.\n            ",
            },
            {
                "ChoiceId": "ops_mit_deploy_risks_deploy_mgmt_sys",
                "Title": "Use deployment management systems",
                "Description": "\n               Use deployment management systems \n               to track and implement change. \n               This reduces errors cause by manual processes and reduces the effort to deploy changes.\n            ",
            },
            {
                "ChoiceId": "ops_mit_deploy_risks_test_limited_deploy",
                "Title": "Test using limited deployments",
                "Description": "\n               Test with limited deployments alongside existing systems \n               to confirm desired outcomes prior to full scale deployment.\n               For example, use deployment canary testing or one-box deployments.\n            ",
            },
            {
                "ChoiceId": "ops_mit_deploy_risks_deploy_to_parallel_env",
                "Title": "Deploy using parallel environments",
                "Description": "\n               Implement changes onto parallel environments, and then transition over to the new environment. Maintain the prior environment until there is confirmation of successful deployment. Doing so minimizes recovery time by enabling rollback to the previous environment.\n            ",
            },
            {
                "ChoiceId": "ops_mit_deploy_risks_freq_sm_rev_chg",
                "Title": "Deploy frequent, small, reversible changes",
                "Description": "\n               Use frequent, small, and reversible changes to reduce the scope of a change.\n               This results in easier troubleshooting and faster remediation with the option to roll back a change.\n            ",
            },
            {
                "ChoiceId": "ops_mit_deploy_risks_auto_integ_deploy",
                "Title": "Fully automate integration and deployment",
                "Description": "\n               Automate build, deployment, and testing of the workload. \n               This reduces errors cause by manual processes and reduces the effort to deploy changes.\n            ",
            },
            {
                "ChoiceId": "ops_mit_deploy_risks_auto_testing_and_rollback",
                "Title": "Automate testing and rollback",
                "Description": "\n               Automate testing of deployed environments to confirm desired outcomes.\n               Automate rollback to previous known good state when outcomes are not achieved to minimize recovery time and reduce errors caused by manual processes.\n            ",
            },
            {
                "ChoiceId": "ops_mit_deploy_risks_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "ready-to-support",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How do you know that you are ready to support a workload?",
        "Choices": [
            {
                "ChoiceId": "ops_ready_to_support_personnel_capability",
                "Title": "Ensure personnel capability",
                "Description": "\n               Have a mechanism to validate that you have the appropriate number of trained personnel to provide support for operational needs. Train personnel and adjust personnel capacity as necessary to maintain effective support.\n            ",
            },
            {
                "ChoiceId": "ops_ready_to_support_const_orr",
                "Title": "Ensure consistent review of operational readiness",
                "Description": "\n               Ensure you have a consistent review of your readiness to operate a workload. Reviews must include, at a minimum, the operational readiness of the teams and the workload, and security requirements. Implement review activities in code and trigger automated review in response to events where appropriate, to ensure consistency, speed of execution, and reduce errors caused by manual processes.\n            ",
            },
            {
                "ChoiceId": "ops_ready_to_support_use_runbooks",
                "Title": "Use runbooks to perform procedures",
                "Description": "\n               Runbooks are documented procedures to achieve specific outcomes. \n               Enable consistent and prompt responses to well-understood events by documenting procedures in runbooks. \n               Implement runbooks as code and trigger the execution of runbooks in response to events where appropriate,\n               to ensure consistency, speed responses, and reduce errors caused by manual processes.\n            ",
            },
            {
                "ChoiceId": "ops_ready_to_support_use_playbooks",
                "Title": "Use playbooks to investigate issues",
                "Description": "\n               Enable consistent and prompt responses to issues that are not well understood, by documenting the investigation process in playbooks. Playbooks are the predefined steps performed to identify the factors contributing to a failure scenario. The results from any process step are used to determine the next steps to take until the issue is identified or escalated.\n            ",
            },
            {
                "ChoiceId": "ops_ready_to_support_informed_deploy_decisions",
                "Title": "Make informed decisions to deploy systems and changes",
                "Description": "\n               Evaluate the capabilities of the team to support the workload and the workload's compliance with governance.\n               Evaluate these against the benefits of deployment when determining whether to transition a system or change into production.\n               Understand the benefits and risks to make informed decisions.\n            ",
            },
            {
                "ChoiceId": "ops_ready_to_support_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "workload-health",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How do you understand the health of your workload?",
        "Choices": [
            {
                "ChoiceId": "ops_workload_health_define_workload_kpis",
                "Title": "Identify key performance indicators",
                "Description": "\n               Identify key performance indicators (KPIs) based on desired business outcomes (for example, order rate, customer retention rate, and profit versus operating expense) and customer outcomes (for example, customer satisfaction). Evaluate KPIs to determine workload success.\n            ",
            },
            {
                "ChoiceId": "ops_workload_health_design_workload_metrics",
                "Title": "Define workload metrics",
                "Description": "\n               Define workload metrics to measure the achievement of KPIs (for example, abandoned shopping carts, orders placed, cost, price, and allocated workload expense). Define workload metrics to measure the health of the workload (for example, interface response time, error rate, requests made, requests completed, and utilization). Evaluate metrics to determine if the workload is achieving desired outcomes, and to understand the health of the workload.\n            ",
            },
            {
                "ChoiceId": "ops_workload_health_collect_analyze_workload_metrics",
                "Title": "Collect and analyze workload metrics",
                "Description": "\n               Perform regular proactive reviews of metrics\n               to identify trends and determine where appropriate responses are needed.\n            ",
            },
            {
                "ChoiceId": "ops_workload_health_workload_metric_baselines",
                "Title": "Establish workload metrics baselines",
                "Description": "\n               Establish baselines for metrics to provide expected values as the basis for comparison and identification of under and over performing components. Identify thresholds for improvement, investigation, and intervention.\n            ",
            },
            {
                "ChoiceId": "ops_workload_health_learn_workload_usage_patterns",
                "Title": "Learn expected patterns of activity for workload",
                "Description": "\n               Establish patterns of workload activity to identify anomalous behavior so that you can respond appropriately if required.\n            ",
            },
            {
                "ChoiceId": "ops_workload_health_workload_outcome_alerts",
                "Title": "Alert when workload outcomes are at risk",
                "Description": "\n               Raise an alert when workload outcomes are at risk so that you can respond appropriately if necessary.\n            ",
            },
            {
                "ChoiceId": "ops_workload_health_workload_anomaly_alerts",
                "Title": "Alert when workload anomalies are detected",
                "Description": "\n               Raise an alert when workload anomalies are detected so that you can respond appropriately if necessary.\n            ",
            },
            {
                "ChoiceId": "ops_workload_health_biz_level_view_workload",
                "Title": "\n               Validate the achievement of outcomes and the effectiveness of KPIs and metrics\n            ",
                "Description": "\n               Create a business-level view of your workload operations\n               to help you determine if you are satisfying needs and \n               to identify areas that need improvement to reach business goals.\n               Validate the effectiveness of KPIs and metrics \n               and revise them if necessary.\n            ",
            },
            {
                "ChoiceId": "ops_workload_health_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "operations-health",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How do you understand the health of your operations?",
        "Choices": [
            {
                "ChoiceId": "ops_operations_health_define_ops_kpis",
                "Title": "Identify key performance indicators",
                "Description": "\n               Identify key performance indicators (KPIs) based on desired business (for example, new features delivered) and customer outcomes (for example, customer support cases). Evaluate KPIs to determine operations success.\n            ",
            },
            {
                "ChoiceId": "ops_operations_health_design_ops_metrics",
                "Title": "Define operations metrics",
                "Description": "\n               Define operations metrics to measure the achievement of KPIs (for example, successful deployments, and failed deployments). Define operations metrics to measure the health of operations activities (for example, mean time to detect an incident (MTTD), and mean time to recovery (MTTR) from an incident). Evaluate metrics to determine if operations are achieving desired outcomes, and to understand the health of your operations activities.\n            ",
            },
            {
                "ChoiceId": "ops_operations_health_collect_analyze_ops_metrics",
                "Title": "Collect and analyze operations metrics",
                "Description": "\n               Perform regular, proactive reviews of metrics to identify trends and determine where appropriate responses are needed.\n            ",
            },
            {
                "ChoiceId": "ops_operations_health_ops_metric_baselines",
                "Title": "Establish operations metrics baselines",
                "Description": "\n               Establish baselines for metrics to provide expected values as the basis for comparison and identification of under and over performing operations activities.\n            ",
            },
            {
                "ChoiceId": "ops_operations_health_learn_ops_usage_patterns",
                "Title": "Learn the expected patterns of activity for operations",
                "Description": "\n               Establish patterns of operations activities to identify anomalous activity so that you can respond appropriately if necessary.\n            ",
            },
            {
                "ChoiceId": "ops_operations_health_ops_outcome_alerts",
                "Title": "Alert when operations outcomes are at risk",
                "Description": "\n               Raise an alert when operations outcomes are at risk so that you can respond appropriately if necessary.\n            ",
            },
            {
                "ChoiceId": "ops_operations_health_ops_anomaly_alerts",
                "Title": "Alert when operations anomalies are detected",
                "Description": "\n               Raise an alert when operations anomalies are detected so that you can respond appropriately if necessary.\n            ",
            },
            {
                "ChoiceId": "ops_operations_health_biz_level_view_ops",
                "Title": "\n               Validate the achievement of outcomes and the effectiveness of KPIs and metrics\n            ",
                "Description": "\n               Create a business-level view of your operations activities\n               to help you determine if you are satisfying needs and \n               to identify areas that need improvement to reach business goals.\n               Validate the effectiveness of KPIs and metrics \n               and revise them if necessary.\n            ",
            },
            {
                "ChoiceId": "ops_operations_health_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "event-response",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How do you manage workload and operations events?",
        "Choices": [
            {
                "ChoiceId": "ops_event_response_event_incident_problem_process",
                "Title": "Use processes for event, incident, and problem management",
                "Description": "\n               Have processes to address observed events, events that require intervention (incidents), \n               and events that require intervention and either recur or cannot currently be resolved (problems). \n               Use these processes to mitigate the impact of these events on the business and your customers \n               by ensuring timely and appropriate responses.\n            ",
            },
            {
                "ChoiceId": "ops_event_response_process_per_alert",
                "Title": "Have a process per alert",
                "Description": "\n               Have a well-defined response (runbook or playbook), \n               with a specifically identified owner, \n               for any event for which you raise an alert.\n               This ensures effective and prompt responses to operations events \n               and prevents actionable events from being obscured by less valuable notifications.\n            ",
            },
            {
                "ChoiceId": "ops_event_response_prioritize_events",
                "Title": "Prioritize operational events based on business impact",
                "Description": "\n               Ensure that when multiple events require intervention, \n               those that are most significant to the business are addressed first.\n               For example, impacts can include loss of life or injury, financial loss, or damage to reputation or trust.\n            ",
            },
            {
                "ChoiceId": "ops_event_response_define_escalation_paths",
                "Title": "Define escalation paths",
                "Description": "\n               Define escalation paths in your runbooks and playbooks, \n               including what triggers escalation, and\n               procedures for escalation. \n               Specifically identify owners for each action \n               to ensure effective and prompt responses to operations events.\n            ",
            },
            {
                "ChoiceId": "ops_event_response_push_notify",
                "Title": "Enable push notifications",
                "Description": "\n               Communicate directly with your users (for example, with email or SMS) when the services they use are impacted, and again when the services return to normal operating conditions, to enable users to take appropriate action.\n            ",
            },
            {
                "ChoiceId": "ops_event_response_dashboards",
                "Title": "Communicate status through dashboards",
                "Description": "\n               Provide dashboards tailored to their target audiences (for example, internal technical teams, leadership, and customers)\n               to communicate the current operating status of the business and provide metrics of interest. \n            ",
            },
            {
                "ChoiceId": "ops_event_response_auto_event_response",
                "Title": "Automate responses to events",
                "Description": "\n               Automate responses to events to reduce errors caused by manual processes, and to ensure prompt and consistent responses. \n            ",
            },
            {
                "ChoiceId": "ops_event_response_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "evolve-ops",
        "PillarId": "operationalExcellence",
        "QuestionTitle": "How do you evolve operations?",
        "Choices": [
            {
                "ChoiceId": "ops_evolve_ops_process_cont_imp",
                "Title": "Have a process for continuous improvement",
                "Description": "\n               Regularly evaluate and prioritize opportunities for improvement\n               to focus efforts where they can provide the greatest benefits.\n            ",
            },
            {
                "ChoiceId": "ops_evolve_ops_perform_rca_process",
                "Title": "Perform post-incident analysis",
                "Description": "\n               Review customer-impacting events, and identify the contributing factors\n               and preventative actions. Use this information to develop mitigations to limit or prevent recurrence. Develop procedures for prompt and effective responses. Communicate contributing factors and corrective actions as appropriate, tailored to target audiences.\n            ",
            },
            {
                "ChoiceId": "ops_evolve_ops_feedback_loops",
                "Title": "Implement feedback loops",
                "Description": "\n               Include feedback loops in your procedures and workloads\n               to help you identify issues and areas that need improvement.\n            ",
            },
            {
                "ChoiceId": "ops_evolve_ops_knowledge_management",
                "Title": "Perform Knowledge Management",
                "Description": "\n               Mechanisms exist for your team members to discover the information that they are looking for in a timely manner, access it, and identify that it’s current and complete. Mechanisms are present to identify needed content, content in need of refresh, and content that should be archived so that it’s no longer referenced.\n            ",
            },
            {
                "ChoiceId": "ops_evolve_ops_drivers_for_imp",
                "Title": "Define drivers for improvement",
                "Description": "\n               Identify drivers for improvement \n               to help you evaluate and prioritize opportunities.\n            ",
            },
            {
                "ChoiceId": "ops_evolve_ops_validate_insights",
                "Title": "Validate insights",
                "Description": "\n               Review your analysis results and responses with cross-functional teams and business owners. \n               Use these reviews to establish common understanding, identify additional impacts, and determine courses of action. \n               Adjust responses as appropriate.\n            ",
            },
            {
                "ChoiceId": "ops_evolve_ops_metrics_review",
                "Title": "Perform operations metrics reviews",
                "Description": "\n               Regularly perform retrospective analysis of operations metrics with cross-team participants from different areas of the business. \n               Use these reviews to identify opportunities for improvement, potential courses of action, and to share lessons learned.\n            ",
            },
            {
                "ChoiceId": "ops_evolve_ops_share_lessons_learned",
                "Title": "Document and share lessons learned",
                "Description": "\n               Document and share lessons learned from the execution of operations activities \n               so that you can use them internally and across teams.\n            ",
            },
            {
                "ChoiceId": "ops_evolve_ops_allocate_time_for_imp",
                "Title": "Allocate time to make improvements",
                "Description": "\n               Dedicate time and resources within your processes \n               to make continuous incremental improvements possible.\n            ",
            },
            {
                "ChoiceId": "ops_evolve_ops_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "performing-architecture",
        "PillarId": "performance",
        "QuestionTitle": "How do you select the best performing architecture?",
        "Choices": [
            {
                "ChoiceId": "perf_performing_architecture_evaluate_resources",
                "Title": "Understand the available services and resources",
                "Description": "\n               Learn about and understand the wide range of services and resources available in the cloud. Identify the relevant services and configuration options for your workload, and understand how to achieve optimal performance. \n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_performing_architecture_process",
                "Title": "Define a process for architectural choices",
                "Description": "\n               Use internal experience and knowledge of the cloud, or external resources such as published use cases, relevant documentation, or whitepapers to define a process to choose resources and services. You should define a process that encourages experimentation and benchmarking with the services that could be used in your workload. \n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_performing_architecture_cost",
                "Title": "Factor cost requirements into decisions ",
                "Description": "\n               Workloads often have cost requirements for operation. Use internal cost controls to select resource types and sizes based on predicted resource need.",
            },
            {
                "ChoiceId": "perf_performing_architecture_use_policies",
                "Title": "Use policies or reference architectures",
                "Description": "\n               Maximize performance and efficiency by evaluating internal policies and existing reference architectures and using your analysis to select services and configurations for your workload. \n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_performing_architecture_external_guidance",
                "Title": "Use guidance from your cloud provider or an appropriate partner",
                "Description": "\n               Use cloud company resources, such as solutions architects, professional services, or an appropriate partner to guide your decisions. These resources can help review and improve your architecture for optimal performance. \n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_performing_architecture_benchmark",
                "Title": "Benchmark existing workloads",
                "Description": "\n               Benchmark the performance of an existing workload to understand how it performs on the cloud. Use the data collected from benchmarks to drive architectural decisions. \n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_performing_architecture_load_test",
                "Title": "Load test your workload",
                "Description": "\n               Deploy your latest workload architecture on the cloud using different resource types and sizes. Monitor the deployment to capture performance metrics that identify bottlenecks or excess capacity. Use this performance information to design or improve your architecture and resource selection. \n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_performing_architecture_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "select-compute",
        "PillarId": "performance",
        "QuestionTitle": "How do you select your compute solution?",
        "Choices": [
            {
                "ChoiceId": "perf_select_compute_evaluate_options",
                "Title": "Evaluate the available compute options",
                "Description": "Understand the performance characteristics of the compute-related options available to you. Know how instances, containers, and functions work, and what advantages, or disadvantages, they bring to your workload.",
            },
            {
                "ChoiceId": "perf_select_compute_config_options",
                "Title": "Understand the available compute configuration options",
                "Description": "Understand how various options complement your workload, and which configuration options are best for your system. Examples of these options include instance family, sizes, features (GPU, I/O), function sizes, container instances, and single versus multi-tenancy.",
            },
            {
                "ChoiceId": "perf_select_compute_collect_metrics",
                "Title": "Collect compute-related metrics",
                "Description": "One of the best ways to understand how your compute systems are performing is to record and track the true utilization of various resources. This data can be used to make more accurate determinations about resource requirements.",
            },
            {
                "ChoiceId": "perf_select_compute_right_sizing",
                "Title": "Determine the required configuration by right-sizing",
                "Description": "\n              Analyze the various performance characteristics of your workload and how these characteristics relate to memory, network, and CPU usage. Use this data to choose resources that best match your workload's profile. For example, a memory-intensive workload, such as a database, could be served best by the r-family of instances. However, a bursting workload can benefit more from an elastic container system.\n\t\t        ",
            },
            {
                "ChoiceId": "perf_select_compute_elasticity",
                "Title": "Use the available elasticity of resources",
                "Description": "\n              The cloud provides the flexibility to expand or reduce your resources dynamically through a variety of mechanisms to meet changes in demand. Combined with compute-related metrics, a workload can automatically respond to changes and utilize the optimal set of resources to achieve its goal.\n\t\t        ",
            },
            {
                "ChoiceId": "perf_select_compute_use_metrics",
                "Title": "Re-evaluate compute needs based on metrics",
                "Description": "\n              Use system-level metrics to identify the behavior and requirements of your workload over time. Evaluate your workload's needs by comparing the available resources with these requirements and make changes to your compute environment to best match your workload's profile. For example, over time a system might be observed to be more memory-intensive than initially thought, so moving to a different instance family or size could improve both performance and efficiency.\n\t\t        ",
            },
            {
                "ChoiceId": "perf_select_compute_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "right-storage-solution",
        "PillarId": "performance",
        "QuestionTitle": "How do you select your storage solution?",
        "Choices": [
            {
                "ChoiceId": "perf_right_storage_solution_understand_char",
                "Title": "Understand storage characteristics and requirements",
                "Description": "\n              Understand the different characteristics (for example, shareable, file size, cache size, access patterns, latency, throughput, and persistence of data) that are required to select the services that best fit your workload, such as object storage, block storage, file storage, or instance storage.\n            ",
            },
            {
                "ChoiceId": "perf_right_storage_solution_evaluated_options",
                "Title": "Evaluate available configuration options",
                "Description": "\n              Evaluate the various characteristics and configuration options and how they relate to storage. Understand where and how to use provisioned IOPS, SSDs, magnetic storage, object storage, archival storage, or ephemeral storage to optimize storage space and performance for your workload.\n            ",
            },
            {
                "ChoiceId": "perf_right_storage_solution_optimize_patterns",
                "Title": "Make decisions based on access patterns and metrics",
                "Description": "\n              Choose storage systems based on your workload's access patterns and configure them by determining how the workload accesses data. Increase storage efficiency by choosing object storage over block storage. Configure the storage options you choose to match your data access patterns.\n\t\t        ",
            },
            {
                "ChoiceId": "perf_right_storage_solution_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "right-database-solution",
        "PillarId": "performance",
        "QuestionTitle": "How do you select your database solution?",
        "Choices": [
            {
                "ChoiceId": "perf_right_database_solution_understand_char",
                "Title": "Understand data characteristics",
                "Description": "\n              Understand the different characteristics of data in your workload. Determine if the workload requires transactions, how it interacts with data, and what its performance demands are. Use this data to select the best performing database approach for your workload (for example, relational databases, NoSQL Key-value, document, wide column, graph, time series, or in-memory storage).\n            ",
            },
            {
                "ChoiceId": "perf_right_database_solution_evaluate_options",
                "Title": "Evaluate the available options",
                "Description": "\n              Evaluate the services and storage options that are available as part of the selection process for your workload's storage mechanisms. Understand how, and when, to use a given service or system for data storage. Learn about available configuration options that can optimize database performance or efficiency, such as provisioned IOPs, memory and compute resources, and caching.\n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_right_database_solution_collect_metrics",
                "Title": "Collect and record database performance metrics",
                "Description": "\n              Use tools, libraries, and systems that record performance measurements related to database performance. For example, measure transactions per second, slow queries, or system latency introduced when accessing the database. Use this data to understand the performance of your database systems.\n            ",
            },
            {
                "ChoiceId": "perf_right_database_solution_access_patterns",
                "Title": "Choose data storage based on access patterns",
                "Description": "\n              Use the access patterns of the workload to decide which services and technologies to use. For example, utilize a relational database for workloads that require transactions, or a key-value store that provides higher throughput but is eventually consistent where applicable.\n\t\t\t\t\t ",
            },
            {
                "ChoiceId": "perf_right_database_solution_optimize_metrics",
                "Title": "Optimize data storage based on access patterns and metrics",
                "Description": "\n              Use performance characteristics and access patterns that optimize how data is stored or queried to achieve the best possible performance. Measure how optimizations such as indexing, key distribution, data warehouse design, or caching strategies impact system performance or overall efficiency.\n            ",
            },
            {
                "ChoiceId": "perf_right_database_solution_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "select-network",
        "PillarId": "performance",
        "QuestionTitle": "How do you configure your networking solution?",
        "Choices": [
            {
                "ChoiceId": "perf_select_network_understand_impact",
                "Title": "Understand how networking impacts performance",
                "Description": "\n              Analyze and understand how network-related decisions impact workload performance. For example, network latency often impacts the user experience, and using the wrong protocols can starve network capacity through excessive overhead.\n            ",
            },
            {
                "ChoiceId": "perf_select_network_evaluate_features",
                "Title": "Evaluate available networking features",
                "Description": "\n              Evaluate networking features in the cloud that may increase performance. Measure the impact of these features through testing, metrics, and analysis. For example, take advantage of network-level features that are available to reduce latency, network distance, or jitter.\n            ",
            },
            {
                "ChoiceId": "perf_select_network_hybrid",
                "Title": "Choose appropriately sized dedicated connectivity or VPN for hybrid workloads",
                "Description": "\n              When there is a requirement for on-premise communication, ensure that you have adequate bandwidth for workload performance.  Based on bandwidth requirements, a single dedicated connection or a single VPN might not be enough, and you must enable traffic load balancing across multiple connections.\n            ",
            },
            {
                "ChoiceId": "perf_select_network_encryption_offload",
                "Title": "Leverage load-balancing and encryption offloading",
                "Description": "\n              Distribute traffic across multiple resources or services to allow your workload to take advantage of the elasticity that the cloud provides. You can also use load balancing for offloading encryption termination to improve performance and to manage and route traffic effectively.\n            ",
            },
            {
                "ChoiceId": "perf_select_network_protocols",
                "Title": "Choose network protocols to improve performance",
                "Description": "\n              Make decisions about protocols for communication between systems and networks based on the impact to the workload’s performance.\n            ",
            },
            {
                "ChoiceId": "perf_select_network_location",
                "Title": "Choose your workload’s location based on network requirements",
                "Description": "\n              Use the cloud location options available to reduce network latency or improve throughput. Utilize AWS Regions, Availability Zones, placement groups, and edge locations such as Outposts, Local Regions, and Wavelength, to reduce network latency or improve throughput.\n            ",
            },
            {
                "ChoiceId": "perf_select_network_optimize",
                "Title": "Optimize network configuration based on metrics",
                "Description": "\n              Use collected and analyzed data to make informed decisions about optimizing your network configuration. Measure the impact of those changes and use the impact measurements to make future decisions.\n            ",
            },
            {
                "ChoiceId": "perf_select_network_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "continue-having-appropriate-resource-type",
        "PillarId": "performance",
        "QuestionTitle": "How do you evolve your workload to take advantage of new releases?",
        "Choices": [
            {
                "ChoiceId": "perf_continue_having_appropriate_resource_type_keep_up_to_date",
                "Title": "Stay up-to-date on new resources and services",
                "Description": "\n              Evaluate ways to improve performance as new services, design patterns, and product offerings become available. Determine which of these could improve performance or increase the efficiency of the workload through ad-hoc evaluation, internal discussion, or external analysis.\n            ",
            },
            {
                "ChoiceId": "perf_continue_having_appropriate_resource_type_define_process",
                "Title": "Define a process to improve workload performance",
                "Description": "\n              Define a process to evaluate new services, design patterns, resource types, and configurations as they become available. For example, run existing performance tests on new instance offerings to determine their potential to improve your workload.\n\t\t\t\t\t",
            },
            {
                "ChoiceId": "perf_continue_having_appropriate_resource_type_evolve",
                "Title": "Evolve workload performance over time",
                "Description": "\n              As an organization, use the information gathered through the evaluation process to actively drive adoption of new services or resources when they become available.\n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_continue_having_appropriate_resource_type_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "monitor-instances-post-launch",
        "PillarId": "performance",
        "QuestionTitle": "How do you monitor your resources to ensure they are performing?",
        "Choices": [
            {
                "ChoiceId": "perf_monitor_instances_post_launch_record_metrics",
                "Title": "Record performance-related metrics",
                "Description": "\n              Use a monitoring and observability service to record performance-related metrics. For example, record database transactions, slow queries, I/O latency, HTTP request throughput, service latency, or other key data.\n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_monitor_instances_post_launch_review_metrics",
                "Title": "Analyze metrics when events or incidents occur",
                "Description": "\n              In response to (or during) an event or incident, use monitoring dashboards or reports to understand and diagnose the impact. These views provide insight into which portions of the workload are not performing as expected.\n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_monitor_instances_post_launch_establish_kpi",
                "Title": "Establish Key Performance Indicators (KPIs) to measure workload performance",
                "Description": "\n              Identify the KPIs that indicate whether the workload is performing as intended. For example, an API-based workload might use overall response latency as an indication of overall performance, and an e-commerce site might choose to use the number of purchases as its KPI.\n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_monitor_instances_post_launch_generate_alarms",
                "Title": "Use monitoring to generate alarm-based notifications",
                "Description": "\n              Using the performance-related key performance indicators (KPIs) that you defined, use a monitoring system that generates alarms automatically when these measurements are outside expected boundaries.\n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_monitor_instances_post_launch_review_metrics_collected",
                "Title": "Review metrics at regular intervals",
                "Description": "\n              As routine maintenance, or in response to events or incidents, review which metrics are collected. Use these reviews to identify which metrics were key in addressing issues and which additional metrics, if they were being tracked, would help to identify, address, or prevent issues.\n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_monitor_instances_post_launch_proactive",
                "Title": "Monitor and alarm proactively",
                "Description": "\n              Use key performance indicators (KPIs), combined with monitoring and alerting systems, to proactively address performance-related issues. Use alarms to trigger automated actions to remediate issues where possible. Escalate the alarm to those able to respond if automated response is not possible. For example, you may have a system that can predict expected key performance indicators (KPI) values and alarm when they breach certain thresholds, or a tool that can automatically halt or roll back deployments if KPIs are outside of expected values.\n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_monitor_instances_post_launch_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "tradeoffs-performance",
        "PillarId": "performance",
        "QuestionTitle": "How do you use tradeoffs to improve performance?",
        "Choices": [
            {
                "ChoiceId": "perf_tradeoffs_performance_critical_areas",
                "Title": "Understand the areas where performance is most critical",
                "Description": "\n              Understand and identify areas where increasing the performance of your workload will have a positive impact on efficiency or customer experience. For example, a website that has a large amount of customer interaction can benefit from using edge services to move content delivery closer to customers.\n\t\t\t\t",
            },
            {
                "ChoiceId": "perf_tradeoffs_performance_design_patterns",
                "Title": "Learn about design patterns and services",
                "Description": "\n              Research and understand the various design patterns and services that help improve workload performance. As part of the analysis, identify what you could trade to achieve higher performance. For example, using a cache service can help to reduce the load placed on database systems; however, it requires some engineering to implement safe caching or possible introduction of eventual consistency in some areas.\n            ",
            },
            {
                "ChoiceId": "perf_tradeoffs_performance_understand_impact",
                "Title": "Identify how tradeoffs impact customers and efficiency",
                "Description": "\n              When evaluating performance-related improvements, determine which choices will impact your customers and workload efficiency. For example, if using a key-value data store increases system performance, it is important to evaluate how the eventually consistent nature of it will impact customers.\n            ",
            },
            {
                "ChoiceId": "perf_tradeoffs_performance_measure",
                "Title": "Measure the impact of performance improvements",
                "Description": "\n              As changes are made to improve performance, evaluate the collected metrics and data. Use this information to determine impact that the performance improvement had on the workload, the workload’s components, and your customers. This measurement helps you understand the improvements that result from the tradeoff, and helps you determine if any negative side-effects were introduced.\n            ",
            },
            {
                "ChoiceId": "perf_tradeoffs_performance_implement_strategy",
                "Title": "Use various performance-related strategies",
                "Description": "\n              Where applicable, utilize multiple strategies to improve performance. For example, using strategies like caching data to prevent excessive network or database calls, using read-replicas for database engines to improve read rates, sharding or compressing data where possible to reduce data volumes, and buffering and streaming of results as they are available to avoid blocking.\n            ",
            },
            {
                "ChoiceId": "perf_tradeoffs_performance_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "manage-service-limits",
        "PillarId": "reliability",
        "QuestionTitle": "How do you manage service quotas and constraints?",
        "Choices": [
            {
                "ChoiceId": "rel_manage_service_limits_aware_quotas_and_constraints",
                "Title": "Aware of service quotas and constraints",
                "Description": "You are aware of your default quotas and quota increase requests for your workload architecture. You additionally know which resource constraints, such as disk or network, are potentially impactful.",
            },
            {
                "ChoiceId": "rel_manage_service_limits_limits_considered",
                "Title": "Manage service quotas across accounts and regions",
                "Description": "If you are using multiple AWS accounts or AWS Regions, ensure that you request the appropriate quotas in all environments in which your production workloads run.",
            },
            {
                "ChoiceId": "rel_manage_service_limits_aware_fixed_limits",
                "Title": "Accommodate fixed service quotas and constraints through architecture",
                "Description": "Be aware of unchangeable service quotas and physical resources, and architect to prevent these from impacting reliability.",
            },
            {
                "ChoiceId": "rel_manage_service_limits_monitor_manage_limits",
                "Title": "Monitor and manage quotas",
                "Description": "Evaluate your potential usage and increase your quotas appropriately allowing for planned growth in usage.",
            },
            {
                "ChoiceId": "rel_manage_service_limits_automated_monitor_limits",
                "Title": "Automate quota management",
                "Description": "Implement tools to alert you when thresholds are being approached. By using AWS Service Quotas APIs, you can automate quota increase requests.",
            },
            {
                "ChoiceId": "rel_manage_service_limits_suff_buffer_limits",
                "Title": "Ensure that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover",
                "Description": "When a resource fails, it may still be counted against quotas until its successfully terminated. Ensure that your quotas cover the overlap of all failed resources with replacements before the failed resources are terminated. You should consider an Availability Zone failure when calculating this gap.",
            },
            {
                "ChoiceId": "rel_manage_service_limits_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "planning-network-topology",
        "PillarId": "reliability",
        "QuestionTitle": "How do you plan your network topology?",
        "Choices": [
            {
                "ChoiceId": "rel_planning_network_topology_ha_conn_users",
                "Title": "Use highly available network connectivity for your workload public endpoints",
                "Description": "These endpoints and the routing to them must be highly available. To achieve this, use highly available DNS, content delivery networks (CDNs), API Gateway, load balancing, or reverse proxies.",
            },
            {
                "ChoiceId": "rel_planning_network_topology_ha_conn_private_networks",
                "Title": "Provision redundant connectivity between private networks in the cloud and on-premises environments",
                "Description": "Use multiple AWS Direct Connect (DX) connections or VPN tunnels between separately deployed private networks. Use multiple DX locations for high availability. If using multiple AWS Regions, ensure redundancy in at least two of them. You might want to evaluate AWS Marketplace appliances that terminate VPNs. If you use AWS Marketplace appliances, deploy redundant instances for high availability in different Availability Zones.",
            },
            {
                "ChoiceId": "rel_planning_network_topology_ip_subnet_allocation",
                "Title": "Ensure IP subnet allocation accounts for expansion and availability",
                "Description": "Amazon VPC IP address ranges must be large enough to accommodate workload requirements, including factoring in future expansion and allocation of IP addresses to subnets across Availability Zones. This includes load balancers, EC2 instances, and container-based applications.",
            },
            {
                "ChoiceId": "rel_planning_network_topology_prefer_hub_and_spoke",
                "Title": "Prefer hub-and-spoke topologies over many-to-many mesh",
                "Description": "If more than two network address spaces (for example, VPCs and on-premises networks) are connected via VPC peering, AWS Direct Connect, or VPN, then use a hub-and-spoke model, like that provided by AWS Transit Gateway.",
            },
            {
                "ChoiceId": "rel_planning_network_topology_non_overlap_ip",
                "Title": "Enforce non-overlapping private IP address ranges in all private address spaces where they are connected",
                "Description": "The IP address ranges of each of your VPCs must not overlap when peered or connected via VPN. You must similarly avoid IP address conflicts between a VPC and on-premises environments or with other cloud providers that you use. You must also have a way to allocate private IP address ranges when needed.",
            },
            {
                "ChoiceId": "rel_planning_network_topology_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "service-architecture",
        "PillarId": "reliability",
        "QuestionTitle": "How do you design your workload service architecture?",
        "Choices": [
            {
                "ChoiceId": "rel_service_architecture_monolith_soa_microservice",
                "Title": "Choose how to segment your workload",
                "Description": "\n               Monolithic architecture should be avoided. Instead, you should choose between SOA and microservices. When making each choice, balance the benefits against the complexities—what is right for a new product racing to first launch is different than what a workload built to scale from the start needs. The benefits of using smaller segments include greater agility, organizational flexibility, and scalability. Complexities include possible increased latency, more complex debugging, and increased operational burden\n            ",
            },
            {
                "ChoiceId": "rel_service_architecture_business_domains",
                "Title": "Build services focused on specific business domains and functionality",
                "Description": "\n               SOA builds services with well-delineated functions defined by business needs. Microservices use domain models and bounded context to limit this further so that each service does just one thing.  Focusing on specific functionality enables you to differentiate the reliability requirements of different services, and target investments more specifically.  A concise business problem and having a small team associated with each service also enables easier organizational scaling.\n            ",
            },
            {
                "ChoiceId": "rel_service_architecture_api_contracts",
                "Title": "Provide service contracts per API",
                "Description": "\n               Service contracts are documented agreements between teams on service integration and include a machine-readable API definition, rate limits, and performance expectations. A versioning strategy allows clients to continue using the existing API and migrate their applications to the newer API when they are ready. Deployment can happen anytime, as long as the contract is not violated. The service provider team can use the technology stack of their choice to satisfy the API contract. Similarly, the service consumer can use their own technology.",
            },
            {
                "ChoiceId": "rel_service_architecture_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "prevent-interaction-failure",
        "PillarId": "reliability",
        "QuestionTitle": "How do you design interactions in a distributed system to prevent failures?",
        "Choices": [
            {
                "ChoiceId": "rel_prevent_interaction_failure_identify",
                "Title": "Identify which kind of distributed system is required",
                "Description": "\n               Hard real-time distributed systems require responses to be given synchronously and rapidly, while soft real-time systems have a more generous time window of minutes or more for response. Offline systems handle responses through batch or asynchronous processing. Hard real-time distributed systems have the most stringent reliability requirements.\n            ",
            },
            {
                "ChoiceId": "rel_prevent_interaction_failure_loosely_coupled_system",
                "Title": "Implement loosely coupled dependencies",
                "Description": "\n               Dependencies such as queuing systems, streaming systems, workflows, and load balancers are loosely coupled. Loose coupling helps isolate behavior of a component from other components that depend on it, increasing resiliency and agility\n            ",
            },
            {
                "ChoiceId": "rel_prevent_interaction_failure_idempotent",
                "Title": "Make all responses idempotent",
                "Description": "\n               An idempotent service promises that each request is completed exactly once, such that making multiple identical requests has the same effect as making a single request. An idempotent service makes it easier for a client to implement retries without fear that a request will be erroneously processed multiple times. To do this, clients can issue API requests with an idempotency token—the same token is used whenever the request is repeated. An idempotent service API uses the token to return a response identical to the response that was returned the first time that the request was completed.\n            ",
            },
            {
                "ChoiceId": "rel_prevent_interaction_failure_constant_work",
                "Title": "Do constant work",
                "Description": "\n               Systems can fail when there are large, rapid changes in load. For example, a health check system that monitors the health of thousands of servers should send the same size payload (a full snapshot of the current state) each time. Whether no servers are failing, or all of them, the health check system is doing constant work with no large, rapid changes.\n            ",
            },
            {
                "ChoiceId": "rel_prevent_interaction_failure_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "mitigate-interaction-failure",
        "PillarId": "reliability",
        "QuestionTitle": "How do you design interactions in a distributed system to mitigate or withstand failures?",
        "Choices": [
            {
                "ChoiceId": "rel_mitigate_interaction_failure_graceful_degradation",
                "Title": "Implement graceful degradation to transform applicable hard dependencies into soft dependencies",
                "Description": "\n                    When a component's dependencies are unhealthy, the component itself can still function, although in a degraded manner. For example, when a dependency call fails, failover to a predetermined static response.\n                ",
            },
            {
                "ChoiceId": "rel_mitigate_interaction_failure_throttle_requests",
                "Title": "Throttle requests",
                "Description": "\n                    This is a mitigation pattern to respond to an unexpected increase in demand. Some requests are honored but those over a defined limit are rejected and return a message indicating they have been throttled. The expectation on clients is that they will back off and abandon the request or try again at a slower rate.\n                ",
            },
            {
                "ChoiceId": "rel_mitigate_interaction_failure_limit_retries",
                "Title": "Control and limit retry calls",
                "Description": "\n                    Use exponential backoff to retry after progressively longer intervals. Introduce jitter to randomize those retry intervals, and limit the maximum number of retries. \n                ",
            },
            {
                "ChoiceId": "rel_mitigate_interaction_failure_fail_fast",
                "Title": "Fail fast and limit queues",
                "Description": "\n                    If the workload is unable to respond successfully to a request, then fail fast. This allows the releasing of resources associated with a request, and permits the service to recover if it’s running out of resources.  If the workload is able to respond successfully but the rate of requests is too high, then use a queue to buffer requests instead. However, do not allow long queues that can result in serving stale requests that the client has already given up on.\n                ",
            },
            {
                "ChoiceId": "rel_mitigate_interaction_failure_client_timeouts",
                "Title": "Set client timeouts",
                "Description": "\n                    Set timeouts appropriately, verify them systematically, and do not rely on default values as they are generally set too high\n                ",
            },
            {
                "ChoiceId": "rel_mitigate_interaction_failure_stateless",
                "Title": "Make services stateless where possible",
                "Description": "\n                    Services should either not require state, or should offload state such that between different client requests, there is no dependence on locally stored data on disk or in memory. This enables servers to be replaced at will without causing an availability impact. Amazon ElastiCache or Amazon DynamoDB are good destinations for offloaded state.\n                ",
            },
            {
                "ChoiceId": "rel_mitigate_interaction_failure_emergency_levers",
                "Title": "Implement emergency levers",
                "Description": "\n                    These are rapid processes that may mitigate availability impact on your workload. They can be operated in the absence of a root cause. An ideal emergency lever reduces the cognitive burden on the resolvers to zero by providing fully deterministic activation and deactivation criteria. Example levers include blocking all robot traffic or serving a static response. Levers are often manual, but they can also be automated.\n                ",
            },
            {
                "ChoiceId": "rel_mitigate_interaction_failure_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "monitor-aws-resources",
        "PillarId": "reliability",
        "QuestionTitle": "How do you monitor workload resources?",
        "Choices": [
            {
                "ChoiceId": "rel_monitor_aws_resources_monitor_resources",
                "Title": "Monitor all components for the workload (Generation)",
                "Description": "Monitor the components of the workload with Amazon CloudWatch or third-party tools. Monitor AWS services with Personal Health Dashboard",
            },
            {
                "ChoiceId": "rel_monitor_aws_resources_notification_aggregation",
                "Title": "Define and calculate metrics (Aggregation)",
                "Description": "Store log data and apply filters where necessary to calculate metrics, such as counts of a specific log event, or latency calculated from log event timestamps",
            },
            {
                "ChoiceId": "rel_monitor_aws_resources_notification_monitor",
                "Title": "Send notifications (Real-time processing and alarming)",
                "Description": "Organizations that need to know, receive notifications when significant events occur",
            },
            {
                "ChoiceId": "rel_monitor_aws_resources_automate_response_monitor",
                "Title": "Automate responses (Real-time processing and alarming)",
                "Description": "Use automation to take action when an event is detected, for example, to replace failed components",
            },
            {
                "ChoiceId": "rel_monitor_aws_resources_storage_analytics",
                "Title": "Storage and Analytics",
                "Description": "Collect log files and metrics histories and analyze these for broader trends and workload insights",
            },
            {
                "ChoiceId": "rel_monitor_aws_resources_review_monitoring",
                "Title": "Conduct reviews regularly",
                "Description": "Frequently review how workload monitoring is implemented and update it based on significant events and changes",
            },
            {
                "ChoiceId": "rel_monitor_aws_resources_end_to_end",
                "Title": "Monitor end-to-end tracing of requests through your system",
                "Description": "Use AWS X-Ray or third-party tools so that developers can more easily analyze and debug distributed systems to understand how their applications and its underlying services are performing",
            },
            {
                "ChoiceId": "rel_monitor_aws_resources_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "adapt-to-changes",
        "PillarId": "reliability",
        "QuestionTitle": "How do you design your workload to adapt to changes in demand?",
        "Choices": [
            {
                "ChoiceId": "rel_adapt_to_changes_autoscale_adapt",
                "Title": "Use automation when obtaining or scaling resources",
                "Description": "When replacing impaired resources or scaling your workload, automate the process by using managed AWS services, such as Amazon S3 and AWS Auto Scaling. You can also use third-party tools and AWS SDKs to automate scaling. ",
            },
            {
                "ChoiceId": "rel_adapt_to_changes_reactive_adapt_auto",
                "Title": "Obtain resources upon detection of impairment to a workload",
                "Description": "Scale resources reactively when necessary if availability is impacted, to restore workload availability.",
            },
            {
                "ChoiceId": "rel_adapt_to_changes_proactive_adapt_auto",
                "Title": "Obtain resources upon detection that more resources are needed for a workload",
                "Description": "Scale resources proactively to meet demand and avoid availability impact.",
            },
            {
                "ChoiceId": "rel_adapt_to_changes_load_tested_adapt",
                "Title": "Load test your workload",
                "Description": "Adopt a load testing methodology to measure if scaling activity meets workload requirements.",
            },
            {
                "ChoiceId": "rel_adapt_to_changes_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "tracking-change-management",
        "PillarId": "reliability",
        "QuestionTitle": "How do you implement change?",
        "Choices": [
            {
                "ChoiceId": "rel_tracking_change_management_planned_changemgmt",
                "Title": "Use runbooks for standard activities such as deployment",
                "Description": "Runbooks are the predefined steps used to achieve specific outcomes. Use runbooks to perform standard activities, whether done manually or automatically. Examples include deploying a workload, patching it, or making DNS modifications.",
            },
            {
                "ChoiceId": "rel_tracking_change_management_functional_testing",
                "Title": "Integrate functional testing as part of your deployment",
                "Description": "Functional tests are run as part of automated deployment. If success criteria are not met, the pipeline is halted or rolled back.",
            },
            {
                "ChoiceId": "rel_tracking_change_management_resiliency_testing",
                "Title": "Integrate resiliency testing as part of your deployment",
                "Description": "Resiliency tests (as part of chaos engineering) are run as part of the automated deployment pipeline in a pre-prod environment.",
            },
            {
                "ChoiceId": "rel_tracking_change_management_immutable_infrastructure",
                "Title": "Deploy using immutable infrastructure",
                "Description": "This is a model that mandates that no updates, security patches, or configuration changes happen in-place on production workloads. When a change is needed, the architecture is built onto new infrastructure and deployed into production.",
            },
            {
                "ChoiceId": "rel_tracking_change_management_automated_changemgmt",
                "Title": "Deploy changes with automation",
                "Description": "Deployments and patching are automated to eliminate negative impact.",
            },
            {
                "ChoiceId": "rel_tracking_change_management_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "backing-up-data",
        "PillarId": "reliability",
        "QuestionTitle": "How do you back up data?",
        "Choices": [
            {
                "ChoiceId": "rel_backing_up_data_identified_backups_data",
                "Title": "Identify and back up all data that needs to be backed up, or reproduce the data from sources",
                "Description": "Amazon S3 can be used as a backup destination for multiple data sources. AWS services such as Amazon EBS, Amazon RDS, and Amazon DynamoDB have built in capabilities to create backups. Third-party backup software can also be used. Alternatively, if the data can be reproduced from other sources to meet RPO, you might not require a backup",
            },
            {
                "ChoiceId": "rel_backing_up_data_secured_backups_data",
                "Title": "Secure and encrypt backups",
                "Description": "Detect access using authentication and authorization, such as AWS IAM, and detect data integrity compromise by using encryption.",
            },
            {
                "ChoiceId": "rel_backing_up_data_automated_backups_data",
                "Title": "Perform data backup automatically",
                "Description": "Configure backups to be taken automatically based on a periodic schedule, or by changes in the dataset. RDS instances, EBS volumes, DynamoDB tables, and S3 objects can all be configured for automatic backup. AWS Marketplace solutions or third-party solutions can also be used.",
            },
            {
                "ChoiceId": "rel_backing_up_data_periodic_recovery_testing_data",
                "Title": "Perform periodic recovery of the data to verify backup integrity and processes",
                "Description": "Validate that your backup process implementation meets your recovery time objectives (RTO) and recovery point objectives (RPO) by performing a recovery test.",
            },
            {
                "ChoiceId": "rel_backing_up_data_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "fault-isolation",
        "PillarId": "reliability",
        "QuestionTitle": "How do you use fault isolation to protect your workload?",
        "Choices": [
            {
                "ChoiceId": "rel_fault_isolation_multiaz_region_system",
                "Title": "Deploy the workload to multiple locations",
                "Description": "\n               Distribute workload data and resources across multiple Availability Zones or, where necessary, across AWS Regions. These locations can be as diverse as required.\n            ",
            },
            {
                "ChoiceId": "rel_fault_isolation_single_az_system",
                "Title": "Automate recovery for components constrained to a single location",
                "Description": "\n               If components of the workload can only run in a single Availability Zone or on-premises data center, you must implement the capability to do a complete rebuild of the workload within your defined recovery objectives.\n            ",
            },
            {
                "ChoiceId": "rel_fault_isolation_use_bulkhead",
                "Title": "Use bulkhead architectures",
                "Description": "\n               Like the bulkheads on a ship, this pattern ensures that a failure is contained to a small subset of requests/users so the number of impaired requests is limited, and most can continue without error. Bulkheads for data are usually called partitions or shards, while bulkheads for services are known as cells.\n            ",
            },
            {
                "ChoiceId": "rel_fault_isolation_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "withstand-component-failures",
        "PillarId": "reliability",
        "QuestionTitle": "How do you design your workload to withstand component failures?",
        "Choices": [
            {
                "ChoiceId": "rel_withstand_component_failures_monitoring_health",
                "Title": "Monitor all components of the workload to detect failures",
                "Description": "Continuously monitor the health of your workload so that you and your automated systems are aware of degradation or complete failure as soon as they occur. Monitor for key performance indicators (KPIs) based on business value.",
            },
            {
                "ChoiceId": "rel_withstand_component_failures_failover2good",
                "Title": "Fail over to healthy resources",
                "Description": "Ensure that if a resource failure occurs, that healthy resources can continue to serve requests. For location failures (such as Availability Zone or AWS Region) ensure you have systems in place to fail over to healthy resources in unimpaired locations.",
            },
            {
                "ChoiceId": "rel_withstand_component_failures_auto_healing_system",
                "Title": "Automate healing on all layers",
                "Description": "Upon detection of a failure, use automated capabilities to perform actions to remediate.",
            },
            {
                "ChoiceId": "rel_withstand_component_failures_static_stability",
                "Title": "Use static stability to prevent bimodal behavior",
                "Description": "Bimodal behavior is when your workload exhibits different behavior under normal and failure modes, for example, relying on launching new instances if an Availability Zone fails. You should instead build workloads that are statically stable and operate in only one mode. In this case, provision enough instances in each Availability Zone to handle the workload load if one AZ were removed and then use Elastic Load Balancing or Amazon Route 53 health checks to shift load away from the impaired instances.",
            },
            {
                "ChoiceId": "rel_withstand_component_failures_notifications_sent_system",
                "Title": "Send notifications when events impact availability",
                "Description": "Notifications are sent upon the detection of significant events, even if the issue caused by the event was automatically resolved.",
            },
            {
                "ChoiceId": "rel_withstand_component_failures_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "testing-resiliency",
        "PillarId": "reliability",
        "QuestionTitle": "How do you test reliability?",
        "Choices": [
            {
                "ChoiceId": "rel_testing_resiliency_playbook_resiliency",
                "Title": "Use playbooks to investigate failures",
                "Description": "Enable consistent and prompt responses to failure\n               scenarios that are not well understood, by documenting the investigation process in\n               playbooks. Playbooks are the predefined steps performed to identify the factors\n               contributing to a failure scenario. The results from any process step are used to\n               determine the next steps to take until the issue is identified or\n               escalated.",
            },
            {
                "ChoiceId": "rel_testing_resiliency_rca_resiliency",
                "Title": "Perform post-incident analysis",
                "Description": "Review customer-impacting events, and identify the\n               contributing factors and preventative action items. Use this information to develop\n               mitigations to limit or prevent recurrence. Develop procedures for prompt and\n               effective responses. Communicate contributing factors and corrective actions as\n               appropriate, tailored to target audiences. Have a method to communicate these causes\n               to others as needed.",
            },
            {
                "ChoiceId": "rel_testing_resiliency_test_functional",
                "Title": "Test functional requirements",
                "Description": "These include unit tests and integration tests that validate required functionality.",
            },
            {
                "ChoiceId": "rel_testing_resiliency_test_non_functional",
                "Title": "Test scaling and performance requirements",
                "Description": "This includes load testing to validate that the workload meets scaling and performance requirements.",
            },
            {
                "ChoiceId": "rel_testing_resiliency_failure_injection_resiliency",
                "Title": "Test resiliency using chaos engineering",
                "Description": "Run tests that inject failures regularly into pre-production and production environments. Hypothesize how your workload will react to the failure, then compare your hypothesis to the testing results and iterate if they do not match. Ensure that production testing does not impact users.",
            },
            {
                "ChoiceId": "rel_testing_resiliency_game_days_resiliency",
                "Title": "Conduct game days regularly",
                "Description": "Use game days to regularly exercise your failure procedures as close to production as possible (including in production environments) with the people who will be involved in actual failure scenarios. Game days enforce measures to ensure that production testing does not impact users.",
            },
            {
                "ChoiceId": "rel_testing_resiliency_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "planning-for-recovery",
        "PillarId": "reliability",
        "QuestionTitle": "How do you plan for disaster recovery (DR)?",
        "Choices": [
            {
                "ChoiceId": "rel_planning_for_recovery_objective_defined_recovery",
                "Title": "Define recovery objectives for downtime and data loss",
                "Description": "The workload has a recovery time objective (RTO) and recovery point objective (RPO).",
            },
            {
                "ChoiceId": "rel_planning_for_recovery_disaster_recovery",
                "Title": "Use defined recovery strategies to meet the recovery objectives",
                "Description": "A disaster recovery (DR) strategy has been defined to meet objectives.",
            },
            {
                "ChoiceId": "rel_planning_for_recovery_dr_tested",
                "Title": "Test disaster recovery implementation to validate the implementation",
                "Description": "Regularly test failover to DR to ensure that RTO and RPO are met.",
            },
            {
                "ChoiceId": "rel_planning_for_recovery_config_drift",
                "Title": "Manage configuration drift at the DR site or region",
                "Description": "Ensure that the infrastructure, data, and configuration are as needed at the DR site or region.  For example, check that AMIs and service quotas are up to date.",
            },
            {
                "ChoiceId": "rel_planning_for_recovery_auto_recovery",
                "Title": "Automate recovery",
                "Description": "Use AWS or third-party tools to automate system recovery and route traffic to the DR site or region.",
            },
            {
                "ChoiceId": "rel_planning_for_recovery_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "securely-operate",
        "PillarId": "security",
        "QuestionTitle": "How do you securely operate your workload?",
        "Choices": [
            {
                "ChoiceId": "sec_securely_operate_multi_accounts",
                "Title": "Separate workloads using accounts",
                "Description": "Organize workloads in separate accounts and group accounts based on function or a common set of controls rather than mirroring your company’s reporting structure. Start with security and infrastructure in mind to enable your organization to set common guardrails as your workloads grow.",
            },
            {
                "ChoiceId": "sec_securely_operate_aws_account",
                "Title": "Secure AWS account",
                "Description": "Secure access to your accounts, for example by enabling MFA and restrict use of the root user, and configure account contacts.",
            },
            {
                "ChoiceId": "sec_securely_operate_control_objectives",
                "Title": "Identify and validate control objectives",
                "Description": "Based on your compliance requirements and risks identified from your threat model, derive and validate the control objectives and controls that you need to apply to your workload. Ongoing validation of control objectives and controls help you measure the effectiveness of risk mitigation.",
            },
            {
                "ChoiceId": "sec_securely_operate_updated_threats",
                "Title": "Keep up to date with security threats",
                "Description": "Recognize attack vectors by staying up to date with the latest security threats to help you define and implement appropriate controls.",
            },
            {
                "ChoiceId": "sec_securely_operate_updated_recommendations",
                "Title": "Keep up to date with security recommendations",
                "Description": "Stay up to date with both AWS and industry security recommendations to evolve the security posture of your workload. ",
            },
            {
                "ChoiceId": "sec_securely_operate_test_validate_pipeline",
                "Title": "Automate testing and validation of security controls in pipelines",
                "Description": "Establish secure baselines and templates for security mechanisms that are tested and validated as part of your build, pipelines, and processes. Use tools and automation to test and validate all security controls continuously. For example, scan items such as machine images and infrastructure as code templates for security vulnerabilities, irregularities, and drift from an established baseline at each stage.",
            },
            {
                "ChoiceId": "sec_securely_operate_threat_model",
                "Title": "Identify and prioritize risks using a threat model",
                "Description": "Use a threat model to identify and maintain an up-to-date register of potential threats. Prioritize your threats and adapt your security controls to prevent, detect, and respond. Revisit and maintain this in the context of the evolving security landscape.",
            },
            {
                "ChoiceId": "sec_securely_operate_implement_services_features",
                "Title": "Evaluate and implement new security services and features regularly",
                "Description": "AWS and APN Partners constantly release new features and services that allow you to evolve the security posture of your workload.",
            },
            {
                "ChoiceId": "sec_securely_operate_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "identities",
        "PillarId": "security",
        "QuestionTitle": "How do you manage identities for people and machines?",
        "Choices": [
            {
                "ChoiceId": "sec_identities_enforce_mechanisms",
                "Title": "Use strong sign-in mechanisms",
                "Description": "Enforce minimum password length, and educate users to avoid common or re-used passwords. Enforce multi-factor authentication (MFA) with software or hardware mechanisms to provide an additional layer.",
            },
            {
                "ChoiceId": "sec_identities_unique",
                "Title": "Use temporary credentials",
                "Description": "Require identities to dynamically acquire temporary credentials. For workforce identities, use AWS Single Sign-On, or federation with IAM roles to access AWS accounts. For machine identities, require the use of IAM roles instead of long term access keys.",
            },
            {
                "ChoiceId": "sec_identities_secrets",
                "Title": "Store and use secrets securely",
                "Description": "For workforce and machine identities that require secrets such as passwords to third party applications, store them with automatic rotation using the latest industry standards in a specialized service.",
            },
            {
                "ChoiceId": "sec_identities_identity_provider",
                "Title": "Rely on a centralized identity provider",
                "Description": "For workforce identities, rely on an identity provider that enables you to manage identities in a centralized place. This enables you to create, manage, and revoke access from a single location making it easier to manage access. This reduces the requirement for multiple credentials and provides an opportunity to integrate with HR processes.",
            },
            {
                "ChoiceId": "sec_identities_audit",
                "Title": "Audit and rotate credentials periodically",
                "Description": "When you cannot rely on temporary credentials and require long term credentials, audit credentials to ensure that the defined controls (for example, MFA) are enforced, rotated regularly, and have appropriate access level.",
            },
            {
                "ChoiceId": "sec_identities_groups_attributes",
                "Title": "Leverage user groups and attributes",
                "Description": "Place users with common security requirements in groups defined by your identity provider, and put mechanisms in place to ensure that user attributes that may be used for access control (e.g., department or location) are correct and updated. Use these groups and attributes, rather than individual users, to control access. This allows you to manage access centrally by changing a user’s group membership or attributes once, rather than updating many individual policies when a user’s access needs change.",
            },
            {
                "ChoiceId": "sec_identities_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "permissions",
        "PillarId": "security",
        "QuestionTitle": "How do you manage permissions for people and machines?",
        "Choices": [
            {
                "ChoiceId": "sec_permissions_define",
                "Title": "Define access requirements",
                "Description": "Each component or resource of your workload needs to be accessed by administrators, end users, or other components. Have a clear definition of who or what should have access to each component, choose the appropriate identity type and method of authentication and authorization.",
            },
            {
                "ChoiceId": "sec_permissions_least_privileges",
                "Title": "Grant least privilege access",
                "Description": "Grant only the access that identities require by allowing access to specific actions on specific AWS resources under specific conditions. Rely on groups and identity attributes to dynamically set permissions at scale, rather than defining permissions for individual users. For example, you can allow a group of developers access to manage only resources for their project. This way, when a developer is removed from the group, access for the developer is revoked everywhere that group was used for access control, without requiring any changes to the access policies.",
            },
            {
                "ChoiceId": "sec_permissions_emergency_process",
                "Title": "Establish emergency access process",
                "Description": "A process that allows emergency access to your workload in the unlikely event of an automated process or pipeline issue. This will help you rely on least privilege access, but ensure users can obtain the right level of access when they require it. For example, establish a process for administrators to verify and approve their request.",
            },
            {
                "ChoiceId": "sec_permissions_continuous_reduction",
                "Title": "Reduce permissions continuously",
                "Description": "As teams and workloads determine what access they need, remove permissions they no longer use and establish review processes to achieve least privilege permissions. Continuously monitor and reduce unused identities and permissions.",
            },
            {
                "ChoiceId": "sec_permissions_define_guardrails",
                "Title": "Define permission guardrails for your organization",
                "Description": "Establish common controls that restrict access to all identities in your organization. For example, you can restrict access to specific AWS Regions, or prevent your operators from deleting common resources, such as an IAM role used for your central security team.",
            },
            {
                "ChoiceId": "sec_permissions_lifecycle",
                "Title": "Manage access based on life cycle",
                "Description": "Integrate access controls with operator and application life cycle and your centralized federation provider. For example, remove a user’s access when they leave the organization or change roles.",
            },
            {
                "ChoiceId": "sec_permissions_analyze_cross_account",
                "Title": "Analyze public and cross account access",
                "Description": "Continuously monitor findings that highlight public and cross account access. Reduce public access and cross account access to only resources that require this type of access.",
            },
            {
                "ChoiceId": "sec_permissions_share_securely",
                "Title": "Share resources securely",
                "Description": "Govern the consumption of shared resources across accounts or within your AWS Organization. Monitor shared resources and review shared resource access.",
            },
            {
                "ChoiceId": "sec_permissions_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "detect-investigate-events",
        "PillarId": "security",
        "QuestionTitle": "How do you detect and investigate security events?",
        "Choices": [
            {
                "ChoiceId": "sec_detect_investigate_events_app_service_logging",
                "Title": "Configure service and application logging",
                "Description": "Configure logging throughout the workload, including application logs, resource logs, and AWS service logs. For example, ensure that AWS CloudTrail, Amazon CloudWatch Logs, Amazon GuardDuty and AWS Security Hub are enabled for all accounts within your organization.",
            },
            {
                "ChoiceId": "sec_detect_investigate_events_analyze_all",
                "Title": "Analyze logs, findings, and metrics centrally",
                "Description": "All logs, metrics, and telemetry should be collected centrally, and automatically analyzed to detect anomalies and indicators of unauthorized activity. A dashboard can provide you easy to access insight into real-time health. For example, ensure that Amazon GuardDuty and Security Hub logs are sent to a central location for alerting and analysis.",
            },
            {
                "ChoiceId": "sec_detect_investigate_events_auto_response",
                "Title": "Automate response to events",
                "Description": "Using automation to investigate and remediate events reduces human effort and error, and enables you to scale investigation capabilities. Regular reviews will help you tune automation tools, and continuously iterate. For example, automate responses to Amazon GuardDuty events by automating the first investigation step, then iterate to gradually remove human effort.",
            },
            {
                "ChoiceId": "sec_detect_investigate_events_actionable_events",
                "Title": "Implement actionable security events",
                "Description": "Create alerts that are sent to and can be actioned by your team. Ensure that alerts include relevant information for the team to take action. For example, ensure that Amazon GuardDuty and AWS Security Hub alerts are sent to the team to action, or sent to response automation tooling with the team remaining informed by messaging from the automation framework.",
            },
            {
                "ChoiceId": "sec_detect_investigate_events_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "network-protection",
        "PillarId": "security",
        "QuestionTitle": "How do you protect your network resources?",
        "Choices": [
            {
                "ChoiceId": "sec_network_protection_create_layers",
                "Title": "Create network layers",
                "Description": "Group components that share reachability requirements into layers. For example, a database cluster in a VPC with no need for internet access should be placed in subnets with no route to or from the internet. In a serverless workload operating without a VPC, similar layering and segmentation with microservices can achieve the same goal.",
            },
            {
                "ChoiceId": "sec_network_protection_layered",
                "Title": "Control traffic at all layers",
                "Description": "Apply controls with a defense in depth approach for both inbound and outbound traffic. For example, for Amazon Virtual Private Cloud (VPC) this includes security groups, Network ACLs, and subnets. For AWS Lambda, consider running in your private VPC with VPC-based controls.",
            },
            {
                "ChoiceId": "sec_network_protection_auto_protect",
                "Title": "Automate network protection",
                "Description": "Automate protection mechanisms to provide a self-defending network based on threat intelligence and anomaly detection. For example, intrusion detection and prevention tools that can pro-actively adapt to current threats and reduce their impact.",
            },
            {
                "ChoiceId": "sec_network_protection_inspection",
                "Title": "Implement inspection and protection",
                "Description": "Inspect and filter your traffic at each layer. For example, use a web application firewall to help protect against inadvertent access at the application network layer. For Lambda functions, third-party tools can add application-layer firewalling to your runtime environment.",
            },
            {
                "ChoiceId": "sec_network_protection_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "protect-compute",
        "PillarId": "security",
        "QuestionTitle": "How do you protect your compute resources?",
        "Choices": [
            {
                "ChoiceId": "sec_protect_compute_vulnerability_management",
                "Title": "Perform vulnerability management",
                "Description": "Frequently scan and patch for vulnerabilities in your code, dependencies, and in your infrastructure to help protect against new threats.",
            },
            {
                "ChoiceId": "sec_protect_compute_reduce_surface",
                "Title": "Reduce attack surface",
                "Description": "Reduce your attack surface by hardening operating systems, minimizing components, libraries, and externally consumable services in use.",
            },
            {
                "ChoiceId": "sec_protect_compute_implement_managed_services",
                "Title": "Implement managed services",
                "Description": "Implement services that manage resources, such as Amazon RDS, AWS Lambda, and Amazon ECS, to reduce your security maintenance tasks as part of the shared responsibility model.",
            },
            {
                "ChoiceId": "sec_protect_compute_auto_protection",
                "Title": "Automate compute protection",
                "Description": "Automate your protective compute mechanisms including vulnerability management, reduction in attack surface, and management of resources.",
            },
            {
                "ChoiceId": "sec_protect_compute_actions_distance",
                "Title": "Enable people to perform actions at a distance",
                "Description": "Removing the ability for interactive access reduces the risk of human error, and the potential for manual configuration or management. For example, use a change management workflow to deploy EC2 instances using infrastructure as code, then manage EC2 instances using tools instead of allowing direct access or a bastion host.",
            },
            {
                "ChoiceId": "sec_protect_compute_validate_software_integrity",
                "Title": "Validate software integrity",
                "Description": "Implement mechanisms (for example, code signing) to validate that the software, code, and libraries used in the workload are from trusted sources and have not been tampered with.",
            },
            {
                "ChoiceId": "sec_protect_compute_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "data-classification",
        "PillarId": "security",
        "QuestionTitle": "How do you classify your data?",
        "Choices": [
            {
                "ChoiceId": "sec_data_classification_identify_data",
                "Title": "Identify the data within your workload",
                "Description": "This includes the type and classification of data, the associated business processes. data owner, applicable legal and compliance requirements, where it’s stored, and the resulting controls that are needed to be enforced. This may include classifications to indicate if the data is intended to be publicly available, if the data is internal use only such as customer personally identifiable information (PII), or if the data is for more restricted access such as intellectual property, legally privileged or marked sensititve, and more.",
            },
            {
                "ChoiceId": "sec_data_classification_define_protection",
                "Title": "Define data protection controls",
                "Description": "Protect data according to its classification level. For example, secure data classified as public by using relevant recommendations while protecting sensitive data with additional controls.",
            },
            {
                "ChoiceId": "sec_data_classification_auto_classification",
                "Title": "Automate identification and classification",
                "Description": "Automate identification and classification of data to reduce the risk of human error from manual interactions.",
            },
            {
                "ChoiceId": "sec_data_classification_lifecycle_management",
                "Title": "Define data lifecycle management",
                "Description": "Your defined lifecycle strategy should be based on sensitivity level, as well as legal and organization requirements. Aspects including the duration you retain data for, data destruction, data access management, data transformation, and data sharing should be considered.",
            },
            {
                "ChoiceId": "sec_data_classification_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "protect-data-rest",
        "PillarId": "security",
        "QuestionTitle": "How do you protect your data at rest?",
        "Choices": [
            {
                "ChoiceId": "sec_protect_data_rest_key_mgmt",
                "Title": "Implement secure key management",
                "Description": "Encryption keys must be stored securely, with\n               strict access control, for example, by using a key management service such as AWS\n               KMS. Consider using different keys, and access control to the keys, combined with the\n               AWS IAM and resource policies, to align with data classification levels and\n               segregation requirements.",
            },
            {
                "ChoiceId": "sec_protect_data_rest_encrypt",
                "Title": "Enforce encryption at rest",
                "Description": "Enforce your encryption requirements based on the\n               latest standards and recommendations to help protect your data at rest.",
            },
            {
                "ChoiceId": "sec_protect_data_rest_automate_protection",
                "Title": "Automate data at rest protection",
                "Description": "Use automated tools to validate and enforce data at\n               rest protection continuously, for example, verify that there are only encrypted\n               storage resources.",
            },
            {
                "ChoiceId": "sec_protect_data_rest_access_control",
                "Title": "Enforce access control",
                "Description": "Enforce access control with least privileges and\n               mechanisms, including backups, isolation, and versioning, to help protect your data\n               at rest. Prevent operators from granting public access to your data.",
            },
            {
                "ChoiceId": "sec_protect_data_rest_use_people_away",
                "Title": "Use mechanisms to keep people away from data",
                "Description": "Keep all users away from directly accessing\n               sensitive data and systems under normal operational circumstances. For example,\n               provide a dashboard instead of direct access to a data store to run queries. Where\n               CI/CD pipelines are not used, determine which controls and processes are required to\n               adequately provide a normally disabled break-glass access mechanism.",
            },
            {
                "ChoiceId": "sec_protect_data_rest_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "protect-data-transit",
        "PillarId": "security",
        "QuestionTitle": "How do you protect your data in transit?",
        "Choices": [
            {
                "ChoiceId": "sec_protect_data_transit_key_cert_mgmt",
                "Title": "Implement secure key and certificate\n               management",
                "Description": "Store encryption keys and certificates securely and\n               rotate them at appropriate time intervals while applying strict access control; for\n               example, by using a certificate management service, such as AWS Certificate Manager\n               (ACM).",
            },
            {
                "ChoiceId": "sec_protect_data_transit_encrypt",
                "Title": "Enforce encryption in transit",
                "Description": "Enforce your defined encryption requirements based\n               on appropriate standards and recommendations to help you meet your organizational,\n               legal, and compliance requirements.",
            },
            {
                "ChoiceId": "sec_protect_data_transit_auto_unintended_access",
                "Title": "Automate detection of unintended data\n               access",
                "Description": "Use tools such as GuardDuty to automatically detect\n               attempts to move data outside of defined boundaries based on data classification\n               level, for example, to detect a trojan that is copying data to an unknown or\n               untrusted network using the DNS protocol.",
            },
            {
                "ChoiceId": "sec_protect_data_transit_authentication",
                "Title": "Authenticate network communications",
                "Description": "Verify the identity of communications by using\n               protocols that support authentication, such as Transport Layer Security (TLS) or\n               IPsec.",
            },
            {
                "ChoiceId": "sec_protect_data_transit_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
    {
        "QuestionId": "incident-response",
        "PillarId": "security",
        "QuestionTitle": "How do you anticipate, respond to, and recover from incidents?",
        "Choices": [
            {
                "ChoiceId": "sec_incident_response_identify_personnel",
                "Title": "Identify key personnel and external resources",
                "Description": "Identify internal and external personnel, resources, and legal obligations that would help your organization respond to an incident.",
            },
            {
                "ChoiceId": "sec_incident_response_develop_management_plans",
                "Title": "Develop incident management plans",
                "Description": "Create plans to help you respond to, communicate during, and recover from an incident. For example, you can start an incident response plan with the most likely scenarios for your workload and organization. Include how you would communicate and escalate both internally and externally.",
            },
            {
                "ChoiceId": "sec_incident_response_prepare_forensic",
                "Title": "Prepare forensic capabilities",
                "Description": "Identify and prepare forensic investigation capabilities that are suitable, including external specialists, tools, and automation.",
            },
            {
                "ChoiceId": "sec_incident_response_auto_contain",
                "Title": "Automate containment capability",
                "Description": "Automate containment and recovery of an incident to reduce response times and organizational impact.",
            },
            {
                "ChoiceId": "sec_incident_response_pre_provision_access",
                "Title": "Pre-provision access",
                "Description": "Ensure that incident responders have the correct access pre-provisioned into AWS to reduce the time for investigation through to recovery.",
            },
            {
                "ChoiceId": "sec_incident_response_pre_deploy_tools",
                "Title": "Pre-deploy tools",
                "Description": "Ensure that security personnel have the right tools pre-deployed into AWS to reduce the time for investigation through to recovery.",
            },
            {
                "ChoiceId": "sec_incident_response_run_game_days",
                "Title": "Run game days",
                "Description": "Practice incident response game days (simulations) regularly, incorporate lessons learned into your incident management plans, and continuously improve.",
            },
            {
                "ChoiceId": "sec_incident_response_no",
                "Title": "None of these",
                "Description": "",
            },
        ],
    },
]
