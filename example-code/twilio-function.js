const client = require('@sendgrid/client');
const Analytics = require('analytics-node');

exports.handler = async function (context, event, callback) {
  const analytics = new Analytics(context.SEGMENT_WRITE_KEY, {
    flushAt: 1,
  });
  const superclassClickedLinkId = context.SENDGRID_LIST_ID;
  client.setApiKey(context.SENDGRID_MARKETING_API_KEY);

  for (const key in event) {
    if (key === 'request') continue;

    const emailEvent = event[key];

    if (emailEvent.event != undefined) {
      console.log(`A ${emailEvent.event} event was received:`);
    } else {
      console.log('A header was received:');
    }
    console.dir(emailEvent);

    // Capture Link Clicks
    if (emailEvent.event === 'click') {
      // Track with Segment Analytics
      analytics.track({
        anonymousId: emailEvent.sg_message_id,
        event: 'Link Clicked',
        properties: {
          email: emailEvent.email,
          timestamp: emailEvent.timestamp,
          url: emailEvent.url,
        },
      });

      // Add to Twilio SendGrid List
      const request = {
        url: '/v3/marketing/contacts',
        method: 'PUT',
        body: {
          list_ids: [superclassClickedLinkId],
          contacts: [{ email: emailEvent.email }],
        },
      };

      const [response, body] = await client.request(request).catch((error) => {
        console.error(error);
        return callback(error);
      });

      // Log something with response or body, or append to some results object?
      // If no logging, just `await client.req...` works just fine to control iteration :)
    }
  }

  return callback('All done!');
};
