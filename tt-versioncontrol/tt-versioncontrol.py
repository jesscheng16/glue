  glue = boto3.client(service_name='glue', region_name='us-east-1',
              endpoint_url='https://glue.us-east-1.amazonaws.com')

    response = glue.update_source_control_from_job(
            JobName='tt-versioncontrol',
            Provider='GITHUB',
            RepositoryName='glue',
            RepositoryOwner='jesscheng16',
            BranchName='main',
            AuthStrategy='PERSONAL_ACCESS_TOKEN',
            AuthToken='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'
        )