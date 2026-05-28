const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

const VERIFY_TOKEN = "my_secret_token"; // Change this to anything you want

// 1. Webhook verification for Facebook
app.get('/webhook', (req, res) => {
  if (req.query['hub.verify_token'] === VERIFY_TOKEN) {
    res.send(req.query['hub.challenge']);
  } else {
    res.send('Error, wrong token');
  }
});

// 2. Handle all webhook events from Messenger
app.post('/webhook', (req, res) => {
  let body = req.body;

  // Check this is a page subscription
  if (body.object === 'page') {
    body.entry.forEach(function(entry) {

      // 3. This is where we catch message_deliveries
      if (entry.messaging) {
        entry.messaging.forEach(event => {
          if (event.delivery) {
            console.log('Message delivered:', event.delivery);
            // event.delivery.mids = array of message IDs that were delivered
            // event.delivery.watermark = timestamp of last delivered message
          }
        });
      }
    });
    res.status(200).send('EVENT_RECEIVED');
  } else {
    res.sendStatus(404);
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(Server running on port ${PORT}));
