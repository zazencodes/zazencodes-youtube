const functions = require('@google-cloud/functions-framework');
const { Storage } = require('@google-cloud/storage');
const sgMail = require('@sendgrid/mail');

const SENDGRID_API_KEY = process.env.SENDGRID_API_KEY;
const fromEmail = process.env.FROM_EMAIL;
const userEmail = process.env.TO_EMAIL;

// Set your SendGrid sender email
sgMail.setApiKey(SENDGRID_API_KEY);

// Register a CloudEvent callback with the Functions Framework that will
// be triggered by Cloud Storage.
functions.cloudEvent('sendNewCloudStorageCsvAsEmail', async cloudEvent => {
  console.log(`Event ID: ${cloudEvent.id}`);
  console.log(`Event Type: ${cloudEvent.type}`);

  const file = cloudEvent.data;
  console.log(`Bucket: ${file.bucket}`);
  console.log(`File: ${file.name}`);
  console.log(`Metageneration: ${file.metageneration}`);
  console.log(`Created: ${file.timeCreated}`);
  console.log(`Updated: ${file.updated}`);

  const bucketName = file.bucket;
  const fileName = file.name;

  const storage = new Storage();
  const bucket = storage.bucket(bucketName);
  const fileObject = bucket.file(fileName);
  const [fileContent] = await fileObject.download();
  const fileContentString = fileContent.toString('base64');

  const msg = {
    to: userEmail,
    from: fromEmail,
    subject: 'File Uploaded to Google Cloud Storage',
    text: `File "${fileName}" has been uploaded to Google Cloud Storage bucket "${bucketName}".`,
    attachments: [
        {
          content: fileContentString,
          filename: fileName,
          type: fileObject.metadata.contentType,
          disposition: 'attachment',
        },
      ],
  };

  try {
    // Send email using SendGrid
    await sgMail.send(msg);

    console.log(`Email sent successfully for file: ${fileName}`);
  } catch (error) {
    console.error(`Error sending email: ${error}`);
  }

});


