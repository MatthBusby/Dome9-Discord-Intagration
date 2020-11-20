# Dome9-Discord-Intagration
Step 1 – Create Discord Webhook
  1.	Open Discord, and either:
    a.	Create a new channel
      
      i.	Click the Add a Server (+) button in the left-hand pane
      
      ii.	Click Create My Own, enter a Server Name, and click Create
    
    b.	Or select the channel you wish to receive event notifications
  2.	From the channel menu, select Edit channel
  3.	Click on Webhooks menu item
  4.	Click the Create Webhook button and fill in the name of the bot that will post the messages
  5.	Note the URL from the WEBHOOK URL field
  6.	Click the Save butto

Step 2 - Deploying AWS enviroment
  1. Download this repo.
  2. Create an S3 bucket
  3. Upload Package.zip to S3 bucket
  4. Run CloudFormation template
  5. Copy the SNS Topic ARN

Step 3 – Enable Dome9 SNS Integration

  1.	In the Dome9 Console, navigate to Settings > Integrations
  2.	Under SNS, click ENABLE
  3.	Enter the ARN for the SNS created in Step 2
  4.	Click SAVE

Done!
