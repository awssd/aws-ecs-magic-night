1. Create ECR repo
2. Build docker image, tag, push

3. Create EC2 roles:
       ecsInstanceRole
            AmazonEC2ContainerServiceforEC2Role
                Edit Trust Relationship:
```
{
  "Version": "2008-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
] }
```

        ecsServiceRole
            AmazonEC2ContainerServiceRole
                Edit Trust Relationship:
```
{
     "Version": "2008-10-17",
     "Statement": [
       {
         "Sid": "",
         "Effect": "Allow",
         "Principal": {
           "Service": "ecs.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
￼￼￼} ]
}
```

        ecsAutoscaleRole
            AmazonEC2ContainerServiceAutoscaleRole
            Edit Trust Relationship:
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "application-autoscaling.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
] }
```

4. Create Container Instances on EC2 based off the ecs-optimized AMI
   Use the ecsInstanceRole role.
   Use Auto-Scaling
   Create proper Security Group.
          Enable TCP:{YOUR_PORT_OF_CHOICE} from the places you want to allow
   Put this on the User Data:
   ```
       #!/bin/bash
       echo ECS_CLUSTER={CLUSTER_NAME} >> /etc/ecs/ecs.config
   ```
5. Create ECS Task Definition based on ECR image

6. Run an ECS Task from the previously created Task Definition.

7. Hit your end-point and confirm it responds with the proper value.

Extra Points:

8.  Create an ECS Service from your ECS Task
9. Configure AWS ELB for it.
10. Configure Auto-Scaling for your service by specifying your CloudWatch metric of choice.
