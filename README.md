# Dome9-Discord-Intagration
By:      
-David Zehner  
-Matthew Busby

**Solution Overview**

Proper log management and notifications are paramount to keep your environment secure and compliant. With Dome9’s SNS integration, customers are able to push events into a SIEM or log management tool of their choice. We can also take these notifications and push them to Discord to provide updates in real time. 





**Workflow**


![Build](https://github.com/MatthBusby/Dome9-Discord-Intagration/blob/main/Drawing2.png)


**How To**

**Step 1 – Create Discord Webhook**

  1.	Open Discord, and either:        
    a.	Create a new channel
    
          - Click the Add a Server (+) button in the left-hand pane
          - Click Create My Own, enter a Server Name, and click Create         
   
   b.	Or select the channel you wish to receive event notifications
  
  2.	From the channel menu, select Edit channel
  3.	Click on Webhooks menu item
  4.	Click the Create Webhook button and fill in the name of the bot that will post the messages
  5.	Note the URL from the WEBHOOK URL field
  6.	Click the Save butto

**Step 2 - Deploying AWS enviroment**

  1. Download this repo.
  2. Create an S3 bucket
  3. Upload Package.zip to S3 bucket
  4. Run CloudFormation template
  5. Copy the SNS Topic ARN
  
  *Sample Commands*
  
   $ aws s3 mb s3://discord-d9 
   
   $ aws s3 cp ./package.zip s3://discord-d9 --acl public-read
   
   $ aws cloudformation deploy --template-file C:\GitHub\d9\sample.yml --stack-name test --parameter-overrides Bucket=discord-d9 webhook="WEBHOOK" --capabilities CAPABILITY_IAM

**Step 3 – Enable Dome9 SNS Integration**

  1.	In the Dome9 Console, navigate to Settings > Integrations
  2.	Under SNS, click ENABLE
  3.	Enter the ARN for the SNS created in Step 2
  4.	Click SAVE

Done!
