# nOps Rules overview web site

#### Local Setup
1. `make deps`
2. `make python-deps`
3. `honcho start`
4. Voila! Your local server should be available at port `2021`: http://localhost:2021/

#### Rule additions

In order to add a new rule or just new mappings you have to manipulate some JSON files in the following way:
1. Locate mappings JSONs found in `mappings.rules`
    - for CUSTOM rules, find CUSTOM_RULE_MAPPINGS dict and under the according Cloud Platform, add the rule details following the exact structure as the above ones
    - for AWS Config rules, find AWS_CONFIG_RULE_MAPPINGS and add the rule details following the exact structure as the above ones
    
2. Map the rule to the appropriate Lens type.
    - `mappings.lenses` directory contains a file for each lens type. 
      - Locate the desired workload file, 
      - Find the question/answer to which your rule applies to
    - Using `mappings.lenses.autodiscovery` insert the `Question -> Answer -> Rule` connection there